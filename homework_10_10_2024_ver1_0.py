# ******************************************************************
# Ime programa: homework_10_10_2024.py                             *
# Datum: 12. 10. 2024                                              *
# Verzija: 1.0                                                     *
# Avtor: Roman Tušek                                               *
# Opis: Program odpre in prebere vsebino datoteke data.csv,        *
#       loči elemente v vsaki vrstici in elemente vstavi           *
#       v tekst.                                                   *
# ******************************************************************

# Odpremo datoteko data.csv za branje
with open("data.csv", 'r') as data_file:

    # Preberemo posamezno vrstico iz datoteke
    line_1 = data_file.readline()
    line_2 = data_file.readline()
    line_3 = data_file.readline()

    # ločimo elemente, prebrane iz posamezne vrstice
    line_data_1 = line_1.split(",")
    line_data_2 = line_2.split(",")
    line_data_3 = line_3.split(",")

    # Izpišemo elemente skupaj s tekstom
    print(f"{line_data_1[0]} is {line_data_1[1]} years old and {line_data_1[2]}")
    print(f"{line_data_2[0]} is {line_data_2[1]} years old and {line_data_2[2]}")
    print(f"{line_data_3[0]} is {line_data_3[1]} years old and {line_data_3[2]}")
    

    