print("Podaj dwie liczby celem ich podzielenia")
try:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    result = a / b
    print("Wynik dzielenia to: ", result)
except ValueError:
    print("Podaj dane liczbowe!")
except ZeroDivisionError:
    result = "Pamiętaj cholero, nie dziel przez zero!"
    print(result)
print(input("Naciśnij dowolny klawisz, aby zkończyć"))