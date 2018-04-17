"""
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:

    Write two different functions to do this - one using a loop and
    constructing a list, and another using sets


"""



lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listb = [2, 3, 5, 6, 7, 8, 10]

def remove_dups(a,b):
    new_list = []
    for num in lista:
        if num in listb:
            pass
        else:
            new_list.append(num)
    print(new_list)

remove_dups(lista, listb)

def remove_sets(a,b):
    new_list = set(lista) - set(listb)
    print(new_list)

remove_sets(lista, listb)
    
