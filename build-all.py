import os

def openfile(path):
    file = open(path)
    return file.read()
pass

print("Building All Assemblies...")

os.chdir("engine")
exec(openfile("build_engine.py"))
os.chdir("..")

print("Engine Built Succesfully")

os.chdir("sandbox")
exec(openfile("build_sandbox.py"))
os.chdir("..")

print("All Assemblies built Succesfully!")
