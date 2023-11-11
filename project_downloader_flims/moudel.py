
def delate_part_of_linK(link):
    x = list(link)
    elemnt = "&"
    if elemnt in x:
        num = x.index(elemnt)
        num2 = num + 1
        if x[num2] != "E":
            for i in range(4):
                del x[num2]
    dir_link = ''.join(x)
    return dir_link


#name_film








