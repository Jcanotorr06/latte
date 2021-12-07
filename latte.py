import sys
from latteparser import *

if __name__ == "__main__":
    arguments = len(sys.argv)
    if arguments != 2:
        print("Uso: latte.py <nombre_archivo_entrada> ")
        exit()
    filepath = sys.argv[1]
    mainHW4(filepath)
    