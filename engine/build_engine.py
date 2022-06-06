import os
import sys


buildflags = "-out:..\\bin\\brokkr.dll -build-mode:dll"

print("=== Building Engine... ===")

result = os.system("odin build src " + buildflags)

if result != 0:
    sys.exit("Engine failed to Build!")

# input("Press any key to exit...\n")
