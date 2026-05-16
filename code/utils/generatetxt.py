import os 

files = os.listdir("temp")
# print(len(files))
files = [f.split('.')[0] + ".txt" for f in files]
# print(len(files))
# print(files)

#os.chdir("raw_txt")
for f in files:
    with open(f, mode='a'): pass