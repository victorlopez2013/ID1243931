import csv

name = input()
with open(name, 'r') as myfle:
    rdr = csv.reader(myfle, delimiter=',')
    dictionary = dict()
    for l in rdr:
        for m in l:
            if m in dictionary:
                dictionary[m] = dictionary[m] + 1
            else:
                dictionary[m] = 1
    for n in list(dictionary.keys()):
        print("{} {}".format(n, dictionary[n]))