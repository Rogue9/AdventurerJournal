from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Password Manager",
    options = options,
    version = "1",
    description = 'A program to manage passwords',
    executables = executables
)