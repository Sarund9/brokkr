import os
import sys

buildflags = " -out:..\\bin\\Sandbox.exe -build-mode:exe"

depends = " -collection:engine=../lib"

print("=== Building Sandbox... ===")

result = os.system("odin build src" + buildflags + depends)

if result != 0:
    sys.exit("Sandbox failed to Build!")


# input("Press any key to exit...\n")
