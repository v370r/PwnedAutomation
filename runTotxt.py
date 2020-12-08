import sys
import re
sys.stdout=open("test.txt","w")
a = []
b = ["17","18","19"]
c = [str(x) for x in range(1,45)]
c = [x if len(x)==2 else "0"+x for x in c]
branch = ["me","cs","ce","ch"]

for x in branch:
    for y in b:
        for z in c:
            print(x+y+"btech110"+z+"@iith.ac.in")
