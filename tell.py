f=open("file1.txt",mode='r')
print(f.tell())   #0
f.read(3)
print(f.tell())
f.read()
print(f.tell())
print()
f.close()
