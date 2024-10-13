# ******************************************************************
# Ime programa: homework_10_10_2024.py                             *
# Datum: 12. 10. 2024                                              *
# Verzija: 1.1                                                     *
# Avtor: Roman Tušek                                               *
# Opis: Program odpre in prebere vsebino datoteke data.csv,        *
#       loči elemente v vsaki vrstici in elemente vstavi           *
#       v tekst.                                                   *
# ******************************************************************

# Odpremo datoteko data.csv za branje
with open("data.csv", 'r') as data_file:
    
    while True: 
        
        line = str(data_file.readline())    # Preberemo posamezno vrstico iz datoteke
        
        if (line == ""):                    # Če v vrstici ni vsebine, predpostavimo, da je konec datoteke
            #print("file finished")
            break
        else:
            line_data = line.split(",")     # ločimo elemente, prebrane iz posamezne vrstice
            print(f"{line_data[0]} is {line_data[1]} years old and {line_data[2]}")   # Izpišemo elemente skupaj s tekstom


        
       




    