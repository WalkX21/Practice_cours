def average():

    note = input('enter ur marks :(stop to end)')
    nb_note = 0
    sum_note = 0
    while note != 'stop':
        
        nb_note += 1
        sum_note += int(note) # sum_note = sum_note + note
        note = input('enter ur marks :(stop to end)')

    somme = sum_note/ nb_note
    print(somme)

average()


