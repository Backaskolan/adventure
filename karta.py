# coding: utf-8
_karta = {}
startposition = (0, 0)

def ladda_rum():
    #Läser in en fil med rummen utplacerade
    with open('resurser/karta.tsv', 'r') as f:
        rader = f.readlines()

    x_max = len(rader[0].split('\t'))
    for y in range(len(rader)):
        kolumner = rader[y].split('\t')
        for x in range(x_max):
            rumnamn = kolumner[x].replace('\n', '')
            if rumnamn == 'StartRum':
                global startposition
                startposition = (x, y)
            _karta[(x, y)] = None if rumnamn == '' or rumnamn == 'SlutRum' else getattr(__import__('rum'), rumnamn)(x, y)

def rum_finns(x, y):
    return _karta.get((x, y))