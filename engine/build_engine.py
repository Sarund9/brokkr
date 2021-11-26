import os

buildflags = "-out:..\\_bin\\BrokkrEngine.dll -build-mode:dll"

print("Building Engine...")

os.system("odin build src " + buildflags)

# input("Press any key to exit...\n")
