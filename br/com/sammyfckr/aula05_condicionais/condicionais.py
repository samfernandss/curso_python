# if/else/elif

print("Qual sua idade?")
idade = input()
idade = int(idade)

if idade < 18:
    print("Neném")
elif idade == 18:
    print("Tá quase lá")
else:
    print("véio")
