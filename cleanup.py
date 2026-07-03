import os
import subprocess

ROOT_DIR = os.getcwd()  # current folder (./)

AUDIO_EXTS = {".flac", ".wav", ".ogg", ".m4a", ".aac"}

def convert_file(path):
    base, ext = os.path.splitext(path)

    if ext.lower() == ".mp3":
        return

    output = base + ".mp3"

    print(f"Converting: {path}")

    result = subprocess.run([
        "ffmpeg",
        "-y",
        "-i", path,
        "-q:a", "2",
        output
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if result.returncode == 0:
        os.remove(path)
        print(f"✔ Converted + deleted: {path}")
    else:
        print(f"✖ Failed: {path}")

def scan(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            full = os.path.join(root, file)
            ext = os.path.splitext(full)[1].lower()

            if ext in AUDIO_EXTS:
                convert_file(full)

if __name__ == "__main__":
    scan(ROOT_DIR)
    print("Done.")