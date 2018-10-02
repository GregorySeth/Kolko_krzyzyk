import tkinter as tk
from tkinter import messagebox
import random

'''Zmienne'''
plansza = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
mozliwe_ruchy = [True, True, True, True, True, True, True, True, True]
kolory = ["blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue"]
komputer = "X"
gracz = "O"
remis = "Mamy remis!"
winner = None

'''Funkcje'''


def stworz_buttony():
    global but00, but01, but02, but03, but04, but05, but06, but07, but08
    '''Widżety'''
    but00 = tk.Button(main_window, text=plansza[0], font=("Arial", 20, "bold"), width=5, height=2, command=klik0)
    but01 = tk.Button(main_window, text=plansza[1], font=("Arial", 20, "bold"), width=5, height=2, command=klik1)
    but02 = tk.Button(main_window, text=plansza[2], font=("Arial", 20, "bold"), width=5, height=2, command=klik2)
    but03 = tk.Button(main_window, text=plansza[3], font=("Arial", 20, "bold"), width=5, height=2, command=klik3)
    but04 = tk.Button(main_window, text=plansza[4], font=("Arial", 20, "bold"), width=5, height=2, command=klik4)
    but05 = tk.Button(main_window, text=plansza[5], font=("Arial", 20, "bold"), width=5, height=2, command=klik5)
    but06 = tk.Button(main_window, text=plansza[6], font=("Arial", 20, "bold"), width=5, height=2, command=klik6)
    but07 = tk.Button(main_window, text=plansza[7], font=("Arial", 20, "bold"), width=5, height=2, command=klik7)
    but08 = tk.Button(main_window, text=plansza[8], font=("Arial", 20, "bold"), width=5, height=2, command=klik8)
    '''Geometry'''
    but00.grid(column=0, row=0)
    but01.grid(column=1, row=0)
    but02.grid(column=2, row=0)
    but03.grid(column=0, row=1)
    but04.grid(column=1, row=1)
    but05.grid(column=2, row=1)
    but06.grid(column=0, row=2)
    but07.grid(column=1, row=2)
    but08.grid(column=2, row=2)
    '''Graphic'''
    but00["fg"] = kolory[0]
    but01["fg"] = kolory[1]
    but02["fg"] = kolory[2]
    but03["fg"] = kolory[3]
    but04["fg"] = kolory[4]
    but05["fg"] = kolory[5]
    but06["fg"] = kolory[6]
    but07["fg"] = kolory[7]
    but08["fg"] = kolory[8]


def klik0():
    global plansza, mozliwe_ruchy
    if mozliwe_ruchy[0]:
        plansza[0] = gracz
        but00["text"] = gracz
        kolory[0] = "red"
        mozliwe_ruchy[0] = False
        wygrana(plansza, mozliwe_ruchy)
    if winner is not None:
        messagebox.showinfo("Koniec", "Wygrywa: " + winner)
    else:
        computer_move()


def klik1():
    global plansza, mozliwe_ruchy
    if mozliwe_ruchy[1]:
        plansza[1] = gracz
        but01["text"] = gracz
        kolory[1] = "red"
        mozliwe_ruchy[1] = False
        wygrana(plansza, mozliwe_ruchy)
    if winner is not None:
        messagebox.showinfo("Koniec", "Wygrywa: " + winner)
    else:
        computer_move()


def klik2():
    global plansza, mozliwe_ruchy
    if mozliwe_ruchy[2]:
        plansza[2] = gracz
        but02["text"] = gracz
        kolory[2] = "red"
        mozliwe_ruchy[2] = False
        wygrana(plansza, mozliwe_ruchy)
    if winner is not None:
        messagebox.showinfo("Koniec", "Wygrywa: " + winner)
    else:
        computer_move()


def klik3():
    global plansza, mozliwe_ruchy
    if mozliwe_ruchy[3]:
        plansza[3] = gracz
        but03["text"] = gracz
        kolory[3] = "red"
        mozliwe_ruchy[3] = False
        wygrana(plansza, mozliwe_ruchy)
    if winner is not None:
        messagebox.showinfo("Koniec", "Wygrywa: " + winner)
    else:
        computer_move()


def klik4():
    global plansza, mozliwe_ruchy
    if mozliwe_ruchy[4]:
        plansza[4] = gracz
        but04["text"] = gracz
        kolory[4] = "red"
        mozliwe_ruchy[4] = False
        wygrana(plansza, mozliwe_ruchy)
    if winner is not None:
        messagebox.showinfo("Koniec", "Wygrywa: " + winner)
    else:
        computer_move()


def klik5():
    global plansza, mozliwe_ruchy
    if mozliwe_ruchy[5]:
        plansza[5] = gracz
        but05["text"] = gracz
        kolory[5] = "red"
        mozliwe_ruchy[5] = False
        wygrana(plansza, mozliwe_ruchy)
    if winner is not None:
        messagebox.showinfo("Koniec", "Wygrywa: " + winner)
    else:
        computer_move()


def klik6():
    global plansza, mozliwe_ruchy
    if mozliwe_ruchy[6]:
        plansza[6] = gracz
        but06["text"] = gracz
        kolory[6] = "red"
        mozliwe_ruchy[6] = False
        wygrana(plansza, mozliwe_ruchy)
    if winner is not None:
        messagebox.showinfo("Koniec", "Wygrywa: " + winner)
    else:
        computer_move()


def klik7():
    global plansza, mozliwe_ruchy
    if mozliwe_ruchy[7]:
        plansza[7] = gracz
        but07["text"] = gracz
        kolory[7] = "red"
        mozliwe_ruchy[7] = False
        wygrana(plansza, mozliwe_ruchy)
    if winner is not None:
        messagebox.showinfo("Koniec", "Wygrywa: " + winner)
    else:
        computer_move()


def klik8():
    global plansza, mozliwe_ruchy
    if mozliwe_ruchy[8]:
        plansza[8] = gracz
        but08["text"] = gracz
        kolory[8] = "red"
        mozliwe_ruchy[8] = False
        wygrana(plansza, mozliwe_ruchy)
    if winner is not None:
        messagebox.showinfo("Koniec", "Wygrywa: " + winner)
    else:
        computer_move()


def computer_move():
    global plansza, mozliwe_ruchy
    wybor = random.randint(0, 8)
    while not mozliwe_ruchy[wybor]:
        wybor = random.randint(0, 8)
    plansza[wybor] = komputer
    mozliwe_ruchy[wybor] = False
    wygrana(plansza, mozliwe_ruchy)
    stworz_buttony()
    if winner is not None:
        messagebox.showinfo("Koniec", "Wygrywa: " + winner)


def wygrana(plansza, mozliwe_ruchy):
    global winner
    if mozliwe_ruchy == [False, False, False, False, False, False, False, False, False]:
        if winner is None:
            winner = remis
        elif winner is komputer:
            winner = komputer
        else:
            winner = gracz
    elif mozliwe_ruchy != [False, False, False, False, False, False, False, False, False]:
        if plansza[0] == gracz and plansza[1] == gracz and plansza[2] == gracz:
            winner = gracz
        elif plansza[0] == komputer and plansza[1] == komputer and plansza[2] == komputer:
            winner = komputer
        elif plansza[3] == gracz and plansza[4] == gracz and plansza[5] == gracz:
            winner = gracz
        elif plansza[3] == komputer and plansza[4] == komputer and plansza[5] == komputer:
            winner = komputer
        elif plansza[6] == gracz and plansza[7] == gracz and plansza[8] == gracz:
            winner = gracz
        elif plansza[6] == komputer and plansza[7] == komputer and plansza[8] == komputer:
            winner = komputer
        elif plansza[0] == gracz and plansza[3] == gracz and plansza[6] == gracz:
            winner = gracz
        elif plansza[0] == komputer and plansza[3] == komputer and plansza[6] == komputer:
            winner = komputer
        elif plansza[1] == gracz and plansza[4] == gracz and plansza[7] == gracz:
            winner = gracz
        elif plansza[1] == komputer and plansza[4] == komputer and plansza[7] == komputer:
            winner = komputer
        elif plansza[2] == gracz and  plansza[5] == gracz and plansza[8] == gracz:
            winner = gracz
        elif plansza[2] == komputer and plansza[5] == komputer and plansza[8] == komputer:
            winner = komputer
        elif plansza[0] == gracz and plansza[4] == gracz and plansza[8] == gracz:
            winner = gracz
        elif plansza[0] == komputer and plansza[4] == komputer and plansza[8] == komputer:
            winner = komputer
        elif plansza[2] == gracz and plansza[4] == gracz and plansza[6] == gracz:
            winner = gracz
        elif plansza[2] == komputer and plansza[4] == komputer and plansza[6] == komputer:
            winner = komputer


'''Okno główne'''
main_window = tk.Tk()
main_window.title("OX")

'''Start'''
computer_move()
main_window.mainloop()





