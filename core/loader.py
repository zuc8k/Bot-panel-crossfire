# core/loader.py

import os
import asyncio

async def load_commands(bot):
    for root, dirs, files in os.walk("commands"):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file).replace("\\", ".").replace("/", ".")
                module = path[:-3]

                if file == "__init__.py":
                    continue

                try:
                    await bot.load_extension(module)
                    print(f"✅ Loaded: {module}")
                except Exception as e:
                    print(f"❌ Failed to load {module}: {e}")