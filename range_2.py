import os

dir_name = "range_"
output = "output_2.txt"

text = "id"
r = range(1,3001)
name = "page_"

os.makedirs(dir_name, exist_ok=True)

with open('./' + dir_name + '/' + output, 'w') as f:
    f.write(text + "\n")
#    for i in r:
    for i in reversed(r):
        f.write(name + str(i).zfill(6) + "\n")

# python3 range_2.py
