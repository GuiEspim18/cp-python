import random
import re

wines = [
    "\n_NMR_|_______VINHO_________|____PREÇO____\n"
    "  1  |  Vinho tinto suave  |  R$:100,00  ",
    "  2  |  Vinho tinto seco   |  R$:150,00  ",
    "  3  |  Vinho branco suave |  R$:200,00  ",
    "  4  |  Vinho branco seco  |  R$:250,00  ",
    "  5  |  Vinho espumante    |  R$:300,00  "
]

names = [
    "Vinho tinto suave",
    "Vinho tinto seco",
    "Vinho branco suave",
    "Vinho branco seco",
    "Vinho espumante"
]

order = []

def sortName():
    name = random.randint(1, 3)
    match name:
        case 1: return "Pedro"
        case 2: return "Ricardo"
        case 3: return "Guilherme"

def validate():
    try:
        print(f"\n{client} digite o seu ano de nascimento:")
        year = int(input())
        if len(str(year)) == 4 and year < 2005:
            print(f"\n{client}, digite o seu cep:")
            cep = input()
            if re.search("\d{5}-\d{3}", cep):
               loop() 
            else: 
               print("<ERROR> Cep inválido")
        else:
            print(f"\n{client}, você é menor de idade, não pode comprar vinho!")
    except ValueError:
        print("\n<ERROR> Valores inválidos!")
        

def loop():
    resp = "S"
    while resp == "S":
        for i in wines:
            print(i)
        print("\nDigite o número do vinho que você quer adicionar:")
        wine = int(input())
        print("\nAgora digite a quantidade de garrafas:")
        qtd = int(input())
        appendWine(names[wine-1], qtd, wine)
        print("\nDeseja continuar comprando? (S/N):")
        resp = input().upper()
    final()

def appendWine(wine, qtd, index):
    if (findIntem(wine) != None):
        match index:
            case 1: updateItem(order[findIntem(wine)], 100, qtd, findIntem(wine))
            case 2: updateItem(order[findIntem(wine)], 150, qtd, findIntem(wine))
            case 3: updateItem(order[findIntem(wine)], 200, qtd, findIntem(wine))
            case 4: updateItem(order[findIntem(wine)], 250, qtd, findIntem(wine))
            case 5: updateItem(order[findIntem(wine)], 300, qtd, findIntem(wine))
    else:
        match index:
            case 1: order.append(f"{wine} | R$: {float(100*qtd)}")
            case 2: order.append(f"{wine} | R$: {float(150*qtd)}")
            case 3: order.append(f"{wine} | R$: {float(200*qtd)}")
            case 4: order.append(f"{wine} | R$: {float(250*qtd)}")
            case 5: order.append(f"{wine} | R$: {float(300*qtd)}")

def findIntem(item):
    for i in range(len(order)):
        orderItem = order[i]
        if re.search(item, order[i]) == None:
            return None
        index = re.search(item, order[i]).end()
        if orderItem[:index] == item:
            return i
        
def updateItem(item, price, qtd, index):
    result = re.search("R", item).start() + 4
    lastPrice = float(item[result:])
    currentPrice = float(price*qtd)
    updatedPrice = float(lastPrice + currentPrice)
    item = re.sub(str(lastPrice), str(updatedPrice), item)
    order[index] = item

def getValue(item):
    result = re.search("R", item).start() + 4
    return float(item[result:])
    
def final():
    total = 0
    freight = True
    for i in order:
        total += getValue(i)
    if total < 200:
        total += 15.0
    else:
        freight = False
    print("\nAtendimento finalizado")
    print(f"Cliente: {client}")
    print(f"Atendido por: {name}\n")
    for i in order:
        print(i)
    if freight:
        print("\nFrete: R$:15.0")
    else:
        print("\nFrete: GRATIS!")
    print(f"TOTAL: R$:{total}\n")
    print(f"Obrigado {client} pela preferência!")

       
print("Olá, bem-vindo(a) a Vinheria Agnello!")
print("Digite o seu nome:")
client = input()
name = sortName()
print(f"\nOlá {client}!")
print(f"O atendente {name} irá realizar o seu atendimento.")
validate()
