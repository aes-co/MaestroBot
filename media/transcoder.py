import os
import asyncio
import subprocess
from uuid import uuid4

CONVERTED_DIR = "downloads/converted"
os.makedirs(CONVERTED_DIR, exist_ok=True)

def generate_output_path(chat_id: int) -> str:
    unique = uuid4().hex[:6]
    return os.path.join(CONVERTED_DIR, f"{chat_id}_{unique}.raw")

def ffmpeg_command(input_path: str, output_path: str) -> list:
    return [
        "ffmpeg",
        "-i", input_path,
        "-f", "s16le",
        "-ac", "2",
        "-ar", "48000",
        "-acodec", "pcm_s16le",
        output_path,
        "-y"
    ]

async def transcode_audio(input_path: str, chat_id: int) -> str:
    output_path = generate_output_path(chat_id)
    cmd = ffmpeg_command(input_path, output_path)
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    await proc.communicate()
    return output_path if os.path.exists(output_path) else None

def cleanup_transcoded(chat_id: int):
    for f in os.listdir(CONVERTED_DIR):
        if f.startswith(f"{chat_id}_"):
            try:
                os.remove(os.path.join(CONVERTED_DIR, f))
            except Exception:
                pass

async def get_duration(input_path: str) -> float:
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        input_path
    ]
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL
    )
    stdout, _ = await proc.communicate()
    try:
        return float(stdout.decode().strip())
    except Exception:
        return 0.0
