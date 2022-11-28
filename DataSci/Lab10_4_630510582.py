#StudentID: 630510582
#Name: Tulakorn Sawangmuang
#Lab10_4
import string
import matplotlib.pyplot as plt

def find_stat_data(filename):
    data_ = filename.split("\n")
    list_pokemon = []
    number = []
    pokemon = []
    attack = []
    for i in data_:
        b = i.split(",")
        list_pokemon.append(b)
    print(list_pokemon[0][0] + ' ' + list_pokemon[0][1] + ' ' + 'Type' + ' ' + list_pokemon[0][4] + ' ' + list_pokemon[0][5] + ' ' + list_pokemon[0][6] + ' ' + list_pokemon[0][7])
    for i in range(1, len(list_pokemon)):
        if list_pokemon[i][0] not in number:
            pokemon.append((list_pokemon[i][1]))
            attack.append(int(list_pokemon[i][6]))
            print(list_pokemon[i][0] + ' ' + list_pokemon[i][1] + ' ' + list_pokemon[i][2] + ' ' +list_pokemon[i][4] + ' ' + list_pokemon[i][5] + ' ' + list_pokemon[i][6] + ' ' + list_pokemon[i][7])
            number.append(list_pokemon[i][0])
    plt.bar(number, attack, tick_label = pokemon,
        width = 0.8, color = ['red', 'green', 'purple', 'orange'])
    plt.xlabel('Pokemon Name')
    plt.ylabel('Power')
    plt.title('My Pokemon Power!')
    plt.show()

def read_file(filename,mode="rt"):
    with open(filename) as fin:
        fin = open(filename, mode, encoding='utf-8')
        contents = fin.read()
 
    return contents

def main():
    text_input = read_file("dataset.txt")
    find_stat_data(text_input)

if __name__=="__main__":
    main()