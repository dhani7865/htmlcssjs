import shutil
import os

src = "demo.txt"
dst = "DavesDemo.txt"
shutil.copy(src, dst)

os.rename("DavesDemo.txt", "LeaveMeAlone.txt")

os.remove("DavesDemo.txt")

