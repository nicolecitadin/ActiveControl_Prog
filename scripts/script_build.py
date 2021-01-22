import os


def build():
    cmd = 'pyinstaller "../main.py" '
    # cmd += '-w '
    cmd += '-F '
    cmd += '--clean '
    cmd += '--distpath "../build"'
    os.system(cmd)

    # Optional - Windows OS only
    os.system("rmdir build /S /Q")
    os.system("del main.spec")


if __name__ == "__main__":
    build()
