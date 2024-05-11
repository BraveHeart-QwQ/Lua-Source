import os
import subprocess

DIRECTORY = "Lua"

def FormatAll():
    for root, dirs, files in os.walk(DIRECTORY):
        for file in files:
            if not file.endswith((".c", ".h")): continue
            file_path = os.path.join(root, file)
            print("format: ", file_path)
            subprocess.run(["clang-format", "-i", "-style=file", file_path])
FormatAll()
