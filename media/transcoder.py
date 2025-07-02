import asyncio

async def transcode_audio(input_path: str, output_path: str, codec: str = "opus"):
    """
    Transkoding file audio ke format Opus (atau lain) dengan ffmpeg.
    """
    import subprocess
    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-c:a", codec,
        output_path
    ]
    proc = await asyncio.create_subprocess_exec(*cmd)
    await proc.communicate()
    return output_path