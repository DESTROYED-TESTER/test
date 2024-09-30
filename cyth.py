import os
import shutil
from os import system
try:
    from distutils.core import setup
    from Cython.Build import cythonize
except ModuleNotFoundError:
    system('pip3 install cython')
def logo():
    print(45*"-")
    print("</> ENCCODE BY -SUMON");print(45*"-")
def convert_to_elf(input_file):
    setup_code = f"""
from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize("{input_file}"))
"""
    with open("setup.py", "w") as setup_file:
        setup_file.write(setup_code)
    system("python setup.py build_ext --inplace")
    os.remove("setup.py")
    if os.path.exists("build"):
        shutil.rmtree("build")
    print("\x1b[1;32mTHE OPERATION WAS SUCCESSFUL! \x1b[0m") 
if __name__ == "__main__":
    os.system("clear")
    logo()
    while True:
        file_path = input("\x1b[1;36mENTER YOUR FILE (FINISHED WITH .py): \x1b[0m")
        if os.path.isfile(file_path):
            convert_to_elf(file_path)
            break
        else:
            print("\x1b[1;31mFILE NOT FOUND! \x1b[1;33mVERIFY THAT THE FILE EXISTS AND TRY AGAIN.\x1b[0m")
