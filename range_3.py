output = "output_3.txt"

text = "ヘッダー"
r = range(1,3001)
name = "id_"

with open(output, 'w') as f:
    f.write(text + "\n")
    for i in r:
#    for i in reversed(r):
        f.write(name + str(i).zfill(6) + "\n")

# python3 range_3.py
