def par(n):
    if n % 2 == 0:
        print(f"O número {n} é par.")

def impar(n):
    if n % 2 != 0:
        print(f"O número {n} é ímpar.")

def printnome(nome):
    print(f"Nome: {nome}")

def piramide(a):
    for x in range(a + 1):
        for y in range(x):
            print(x, end = " ")
        print()

def piramide2(a):
    for x in range(a + 1):
        for y in range(1, x):
            print(y, end = " ")
        print()

def vogais(texto):
    text = len(texto)
    cont = 0
    for x in range(text):
        if texto[x] in "aeiouAEIOU":
            cont += 1
    print(cont)

def soma(n1, n2, n3, n4, n5):
    soma = n1 + n2 + n3 + n4+ n5
    print(soma)

def somar(*num):
    len(num)
    soma = 0
    for x in range(len(num)):
        soma += num[x]
    print(soma)
    return soma

def contletras(texto):
    t = len(texto)
    cont = 0
    for y in texto:
        if y not in " ":
            cont += 1
    for x in range(t - 1, -1, -1):
        print(texto[x], end="")
    print()
    print(cont)

def semrepeticao(l):
    l = [10,12,12,31,4,4,5,31,6,7,6,8]
    nlist = []
    for x in l:
        if x not in nlist:
            nlist.append(x)
    print(nlist)

def primo(n):
    if n == 1:
        print("1 não é primo.")
    else:
        if (n / 1 == n) or (n / n == 1):
            print(f"{n} é primo.")