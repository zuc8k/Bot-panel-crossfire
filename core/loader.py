# core/loader.py
import os
import asyncio


async def load_commands(bot) -> None:
    commands_dir = "commands"
    if not os.path.isdir(commands_dir):
        print(f"⚠️ Commands directory '{commands_dir}' not found")
        return

    for root, dirs, files in os.walk(commands_dir):
        for file in files:
            if not file.endswith(".py") or file == "__init__.py":
                continue

            path = os.path.join(root, file).replace("\\", ".").replace("/", ".")
            module = path[:-3]

            try:
                await bot.load_extension(module)
                print(f"✅ Loaded: {module}")
            except Exception as e:
                print(f"❌ Failed to load {module}: {e}")