import os
import subprocess

TARGET_DIRECTORY = "Lua-Source"

def FormatAll():
    for root, dirs, files in os.walk(TARGET_DIRECTORY):
        for file in files:
            if not file.endswith((".c", ".h")): continue
            file_path = os.path.join(root, file)
            print("format: ", file_path)
            subprocess.run(["clang-format", "-i", "-style=file", file_path])
FormatAll()
