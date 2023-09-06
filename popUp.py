import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import askyesno
import sys
import threadHandle as th
import queryHandle as qh
import time as t
#import wmi

def tryAgain(msg):
    rootWarn = tk.Tk()
    rootWarn.geometry("400x100")
    rootWarn.title("Storek")
    ask = askyesno(title = "Storek", message = msg)
    if ask:
        return True
    else:
        return False
def popUpError(info):
    def closeErr():
        rootErr.destroy()
        
    def closeApp():
        rootErr.destroy()
        th.stopThreads()
        sys.exit()
    rootErr = tk.Tk()
    rootErr.title("Storek")

    rootErr.protocol("WM_DELETE_WINDOW", closeApp)
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
        th.stopThreads()
        sys.exit()
    def closeNoExit():
        rootWarn.destroy()
        return
    rootWarn = tk.Tk()
    rootWarn.geometry("400x100")
    rootWarn.title("Storek")

    rootWarn.protocol("WM_DELETE_WINDOW", closeWarn)
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
            warn = "Baza nie posiada stworzonych tabel"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case 16:
            warn = "Plik konfiguracyjny uszkodzony/niekompletny, uruchom program ponownie"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeWarn)
        case 17:
            warn = "Utracono połączenie z serwerem"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case 18:
            warn = "Nastąpiła zmiana uprawnień, nastąpi wyłączenie"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeWarn)
        case 19:
            warn = "Brak uprawnień do wybranej bazy"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case 20:
            warn = "Niepoprawnie skonfigurowana baza danych"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeNoExit)
        case 21:
            warn = "Błąd połączenia 001"
            warnButton = tk.Button(rootWarn, text = "OK", command = closeWarn)
        case _:
            warn = "That's it, I'am out: Fatal Error"
    warnLabel = tk.Label(rootWarn, text = warn)
    

    
    warnLabel.pack(pady = 10)
    warnButton.pack(pady = 10)
    rootWarn.mainloop()
    return

