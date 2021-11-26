import os

buildflags = "-out:..\\_bin\\Sandbox.exe -build-mode:exe"

print("Building Sandbox...")

os.system("odin build src " + buildflags)

# input("Press any key to exit...\n")
