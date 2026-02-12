def adiciona_frutas(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity

def verifica(condicao, esperado):
    if condicao == esperado:
        print("Passou")
    else:
        print("Não passou")

def main():
    new_inventory = {}
    adiciona_frutas(new_inventory, 'strawberries', 10)
    verifica('strawberries' in new_inventory, True)
    verifica(new_inventory['strawberries'], 10)
    adiciona_frutas(new_inventory, 'strawberries', 25)
    verifica(new_inventory['strawberries'], 35)

if __name__ == "__main__":
    main()
