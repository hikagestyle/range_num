text = "ヘッダー"
r = range(1,3001)
name = "id_"

print(text)

#for i in r:
for i in reversed(r):
    print(name + str(i).zfill(6))

# python3 range_1.py
# python3 range_1.py > output_1.txt
