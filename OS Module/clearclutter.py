import os

# os.rename("py_learn/OS Module/CS logo.png", "py_learn/OS Module/1.png") for renaming file name


folder = "py_learn/OS Module"
files = [f for f in os.listdir(folder) if f.endswith(".png")]
files.sort()
for i, file in enumerate(files, 1):
    src = os.path.join(folder, file)
    dst = os.path.join(folder, f"{i}.png")
    print(f"Renaming {file} to {i}.png")
    os.rename(src, dst)