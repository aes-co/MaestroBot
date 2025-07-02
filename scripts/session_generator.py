import asyncio
from pyrogram import Client
from pyrogram.enums import ParseMode
from getpass import getpass

API_ID = int(input("Masukkan API_ID: "))
API_HASH = input("Masukkan API_HASH: ")
PHONE = input("Masukkan nomor HP (format internasional, ex: +62xxx): ")

async def main():
    async with Client(
        name="gen",
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=True,
        parse_mode=ParseMode.HTML
    ) as app:
        await app.send_code(PHONE)
        code = input("Masukkan kode OTP: ")
        await app.sign_in(phone_number=PHONE, code=code)
        session_string = await app.export_session_string()
        print("\n✅ String session berhasil dibuat!\n")
        print(f"<SESSION>{session_string}</SESSION>")

if __name__ == "__main__":
    asyncio.run(main())
