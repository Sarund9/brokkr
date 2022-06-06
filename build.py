import os
from shutil import copyfile
# from ntpath import basename;

# Opens file at path as string
def openfile(path:str):
    file = open(path)
    return file.read()

# Creates a Directory if it didn't exist
def assert_dir(dir:str):
    if not os.path.exists(dir):
        os.mkdir(dir)
        print(f"Directory '{dir}' was created")

# Dir Assertions
assert_dir("bin")
assert_dir("lib")

print("Building All Assemblies...")

# Call Build Engine

os.chdir("engine")
exec(openfile("build_engine.py"))
os.chdir("..")

print("Engine Built Succesfully")

# Copying lib files to Sandbox
print("Copying Lib to Sandbox")

for file in os.listdir("bin"):
    if file.endswith(".lib"):
        src = f"bin/{file}"
        dst = f"lib/{file}"
        copyfile(src, dst)

print("Lib files Copied!")

# Call Build Sandbox

os.chdir("sandbox")
exec(openfile("build_sandbox.py"))
os.chdir("..")

print("All Assemblies built Succesfully!")
