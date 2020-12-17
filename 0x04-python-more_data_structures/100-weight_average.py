#!/usr/bin/python3
def weight_average(my_list=[]):
    somme = 0
    nbr = 0
    for i in range(0, len(my_list)):
        somme += (my_list[i][0] * my_list[i][1])
        nbr += my_list[i][1]
    moyenne = somme / nbr
    return moyenne
