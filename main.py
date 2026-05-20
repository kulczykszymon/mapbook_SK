from tkinter import *

root = Tk()

root.title("mapbook_nm")
root.geometry("1024x760")


# FRAME
ramka_lista_obiektow = Frame(root)
ramka_formularza = Frame(root)
ramka_szczegoly_obiektu = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularza.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0,columnspan=2)

# RAMKA LISTA OBIEKTOW
label_lista_obiektow = Label(ramka_lista_obiektow, text= 'Lista uzytkownikow: ')
listbox_lista_obiektow = Listbox(ramka_lista_obiektow)

button_pokaz_szczegoly_obiekyu = Button(ramka_lista_obiektow, text='Pokaz szczegoly')
button_usun_obiekt = Button(ramka_lista_obiektow, text='Usun obiekt')
button_edytuj_obiekt = Button(ramka_lista_obiektow, text='Edytuj obiekt')

label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0)
button_pokaz_szczegoly_obiekyu.grid(row=2, column=0)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=2)

# RAMKA FORMULARZ
label_formularz = Label(ramka_formularza, text='Formularz: ')
label_imie = Label(ramka_formularza, text='Imie: ')
label_nazwisko = Label(ramka_formularza, text='Nazwisko: ')
label_liczba_postow = Label(ramka_formularza, text='Liczba postow: ')
label_lokalizacja = Label(ramka_formularza, text='Lokalizacja: ')

label_formularz.grid(row=0, column=0)
label_imie.grid(row=1, column=0)
label_nazwisko.grid(row=2, column=0)
label_liczba_postow.grid(row=3, column=0)
label_lokalizacja.grid(row=4, column=0)


entry_imie = Entry(ramka_formularza)
entry_nazwisko = Entry(ramka_formularza)
entry_liczba_postow = Entry(ramka_formularza)
entry_lokalizacja = Entry(ramka_formularza)

entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_liczba_postow.grid(row=3, column=1)
entry_lokalizacja.grid(row=4, column=1)

button_dodaj_uzytkownika = Button(ramka_formularza, text='Dodaj uzytkownika')
button_dodaj_uzytkownika.grid(row=5, column=0, columnspan=2)


# RAMKA SZCZEGOLY OBIEKTU

label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Szczegoly uzytkownika: ')
label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Imie: ')
label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='... ')
label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Nazwisko: ')
label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='... ')
label_liczba_postow_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Liczba postow: ')
label_liczba_postow_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='... ')
label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Lokalizacja: ')
label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='... ')




label_szczegoly_obiektu.grid(row=0, column=0)
label_imie_szczegoly_obiektu.grid(row=1, column=0)
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)
label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)
label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)
label_liczba_postow_szczegoly_obiektu.grid(row=1, column=4)
label_liczba_postow_szczegoly_obiektu_wartosc.grid(row=1, column=5)
label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6)
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7)












root.mainloop()