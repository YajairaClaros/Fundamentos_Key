li = input("Ingresa los números separados por espacio: ")

numdup = []
for x in li.split():
    numdup.append(int(x))

seen = set()
res = []

for dupli in numdup:
    if dupli not in seen:
        res.append(dupli)
        seen.add(dupli)

for i in range(len(res)):
    if i != len(res) - 1:
        print(res[i], end=" ")
    else:
        print(res[i])
