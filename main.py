import os.path
import mysql.connector
import turtle
import tkinter as tk


#Połączenie, wykonanie zapytania i zapisanie wyniku do pustej listy  oraz styl wyświetlania tekstu

style = ('Courier', 12, 'bold')

connection = mysql.connector.connect(host='localhost', database='online_shop', user='root', password='')
cursor = connection.cursor()
cursor.execute("select database();")
record = cursor.fetchone()
print("You're connected to database: ", record)

list_query = []
query = "SELECT Oi.id, P.Name, O.id, Oi.Amount FROM Order_item Oi, Products P, Orders O WHERE Oi.Product_id = P.id and Oi.Order_id = O.id "
cursor.execute(query)
for row in cursor:
    list_query.append(row)


#definicje funkcji obsługujące program:

#wyswietlanie otrzymanych wyników

def show():
    if list_query is None:
        turtle.write("Nie ma żadnych nowych zamówień", font=style, align='left')
    else:
        i = 0
        y = 400
        while i < len(list_query):
            turtle.penup()
            turtle.goto(-260, y)
            turtle.pendown()
            turtle.write(list_query[i], font=style, align='center')
            i += 1
            y -= 20


#Zapis zamówienia do pliku

def save():
    files = os.path.exists('save.txt')
    if files:
        with open('save.txt', 'w') as open_file:
            for rows in list_query:
                open_file.write(str(rows))
    else:
        file = open("save.txt", "w")
        for chain in list_query:
            file.write(str(chain))
        file.close()


#Odczytanie zamówienia z pliku

def read():
    files = os.path.exists('save.txt')
    if files:
        with open('save.txt', 'r') as open_file:
            lists = open_file.read()
        lists = lists.replace("(", "")
        save_list = lists.split(')')
        turtle.clear()
        i = 0
        y = 400
        while i < len(save_list):
            turtle.penup()
            turtle.goto(-260, y)
            turtle.pendown()
            turtle.write(save_list[i], font=style, align='center')
            i += 1
            y -= 20
    else:
        turtle.clear()
        turtle.penup()
        turtle.goto(-730, 400)
        turtle.pendown()
        turtle.write("Nie ma żadnych nowych zamówień", font=style, align='left')


#Usuwanie zapisanego zamówienia

def delte():
    file = os.path.exists('save.txt')
    if file:
        os.remove("save.txt")
    else:
        turtle.clear()
        turtle.penup()
        turtle.goto(-730, 400)
        turtle.pendown()
        turtle.write("Nie znaleziono pliku", font=style, align="left")



#Zmiana statusu zamówienia - w realizacji

def change():
    ids = turtle.textinput("Zmiana statusu", "Podaj id zamowienia")
    state = turtle.textinput("Zmiana statusu", "Podaj podaj status zamownienia")
    cursor.execute("UPDATE Orders SET Status= '%s' WHERE id= '%s' " % (state, ids))
    connection.commit()
    turtle.clear()
    turtle.penup()
    turtle.goto(-730, 400)
    turtle.pendown()
    turtle.write("Status realizacji zaktualizowany", font=style, align='left')


#wyjście z programu i zamknięcie bazy danych

def exit():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
    quit()


#Tworzenie okna głównego programu za pomocą modułu żółwia

if __name__ == "__main__":
    turtle.title("Panel administratora dostaw")
    turtle.hideturtle()
    turtle.color('white')
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.bgcolor("black")


    #tworzenie przycisków tkinter

    canvas = screen.getcanvas()
    button_show = tk.Button(canvas.master, text="Posdumowanie", command=show)
    canvas.create_window(-720, 300, window=button_show)
    button_add = tk.Button(canvas.master, text="Dodaj status zamowienia", command=change)
    canvas.create_window(-605, 300, window=button_add)
    button_save = tk.Button(canvas.master, text="Zapisz zamówienie", command=save)
    canvas.create_window(-480, 300, window=button_save)
    button_read = tk.Button(canvas.master, text="Wyswietl zapisane zamówienia", command=read)
    canvas.create_window(-340, 300, window=button_read)
    button_del = tk.Button(canvas.master, text="Usun zapisane zamowienie", command=delte)
    canvas.create_window(-180, 300, window=button_del)
    button_exit = tk.Button(canvas.master, text="Wyjscie", command=exit)
    canvas.create_window(730, 300, window=button_exit)

    turtle.done()










