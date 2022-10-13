#This program does the calculation of verification of solutions to indicate the ph.#

indice_acid = float(input())

while indice_acid != -1:
    if indice_acid < 7:
        print("ACIDA")
    if indice_acid == 7:
        print("NEUTRA")
    if indice_acid > 7:
        print("BASICA")
    indice_acid = float(input())
