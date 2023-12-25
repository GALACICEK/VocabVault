

print("Hello VocabVault App\n")

print("1- English-Turkish Dictionary\n")
print("2- El Espanol-El Turco El Diccionario\n")

selected_dic = input("Please Choose Dictionary(1 or 2): ") 

while not(selected_dic=="1" or selected_dic=="2"):
    print(f"No Have {selected_dic} Dictionary\n")
    selected_dic = input("Please Choose Dictionary(1 or 2): ") 

