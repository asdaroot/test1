n = int(input())

numerics = []

for _ in range(n):
    number = int(input())
    numerics.append(number)

a = int(input())
b = int(input())

print(sum(numerics[a-1:b]))
