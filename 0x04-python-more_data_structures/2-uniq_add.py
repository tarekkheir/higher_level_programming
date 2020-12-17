#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = [0]
    count = 0
    present = 0
    for i in range(0, len(my_list)):
        for j in range(0, len(new)):
            if my_list[i] == new[j]:
                present += 1
        if present == 0:
            new.append(my_list[i])
        else:
            present = 0
    for i in range(0, len(new)):
        count += new[i]
    return count
