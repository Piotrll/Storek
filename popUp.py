import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import askyesno
import os
import time
#import wmi

def tryAgain():
    rootWarn = tk.Tk()
    rootWarn.geometry("400x100")
    rootWarn.title("Storek")
    ask = askyesno(title = "Ponowić próbe ?", message = "Czy ponowić próbe?")
    if ask:
        return True
    else:
        return False
def popUpError(info):
    def closeErr():
        rootErr.destroy()
        
    def closeApp():
        rootErr.destroy()
        exit()
    rootErr = tk.Tk()
    rootErr.title("Storek")
    errorButton = tk.Button(rootErr, text = "Wyjście", command = closeApp)
    proceedButton = tk.Button(rootErr, text = "Wróć" ,command = closeErr)
    warnLabel = tk.Label(rootErr, text = info, wraplength=300)

    proceedButton.grid(column = 1, row = 1, pady = 10, padx = 5)
    warnLabel.grid(column = 0, row = 0, columnspan = 2, pady = 10)
    errorButton.grid(column = 0, row = 1, pady = 10, padx = 5)
    rootErr.mainloop()

def popUpWarn(case):
    def closeWarn():
        rootWarn.destroy()
        exit()
    def closeNoExit():
        rootWarn.destroy()
        return
    rootWarn = tk.Tk()
    rootWarn.geometry("400x100")
    rootWarn.title("Storek")
    warn = ''
    warnButton = tk.Button(rootWarn, text = "OK")
    match case:
        case 1:
            warn = "Program jest już uruchomiony"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeWarn)
        case 2:
            warn = "Plik konfiguracyjny nie mógł\nzostać utworzony/odczytany, możliwa odmowa dostępu"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeWarn)
        case -1:
            warn = "Nieznany błąd programu, przekaż informacje jak do tego doszło"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeWarn)
        case 4:
            warn = "Błąd połączenia bazy danych"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeWarn)
        case 5:
            warn = "Błąd logowania"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case 6:
            warn = "Serwer bazy danych nie odpowiada"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeWarn)
        case 7:
            if tryAgain():
                return True
            else:
                return False
        case 8:
            warn = "Brak połączenia sieciowego"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeWarn)
        case 9:
            warn = "Błąd tworzenia nowej konfiguracji"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case 10:
            warn = "Brak konfiguracji.\n Wprowadź nowe dane."
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case 11:
            warn = "Dodawanie użytkownika nieudane"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeWarn)
        case 12:
            warn = "Wybrany serwer nie posiada stworzonych baz danych."
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case 13:
            warn = "Błąd konfiguracji wybranej bazy"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case 14:
            warn = "Wystąpił błąd podczass zmiany bazy"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case 15:
            wanr = "Baza nie posiada stworzonych tabel"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case _:
            warn = "That's it am out: Fatal Error"
    warnLabel = tk.Label(rootWarn, text = warn)
    

    
    warnLabel.pack(pady = 10)
    warnButton.pack(pady = 10)
    rootWarn.mainloop()

