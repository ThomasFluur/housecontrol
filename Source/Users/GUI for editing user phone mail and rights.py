# GUI for homecontrol py 3 version. Try control indicator and threads.
# It should be possible to run with sensor monitoring and control activity in the background.
# Changes in file should cause new user list. Sanity check required

from tkinter import *  # Bad to use * ? from tkinter import *

root = Tk() # Skapar ramen Vettigt namn?
fenster_namn = Label(root, text = "Edit users")
fenster_namn.pack()
# kolumn1 = Label(root, text = "Rättighets nivå")
# kolumn2 = Label(root, text = "Telefon nummer")
# kolumn3 = Label(root, text = "Mail")
# kolumn4 = Label(root, text = "Giltig till datum")  # Gör en transpose för inmatningen.
# Kör med svenska för att inte påskina hur filen är organiserad
# entry1 = Entry(root)
# entry2 = Entry(root)
# entry3 = Entry(root)
# entry4 = Entry(root)

# kolumn1.grid(row = 0)
# kolumn2.grid(row=1)
#kolumn3.grid(row=2)
# kolumn4.grid(row=3)

# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
# entry3.grid(row=2, column=1)
# entry4.grid(row=3, column=1)

toppenram = Frame(root) # frame osynliga ramen
toppenram.pack()
bottenram = Frame(root)
bottenram.pack(side = BOTTOM)
searchknapp = Button(toppenram, text = "Sök", fg= "blue")
knrapp1 = Button(bottenram, text = "Ändra", fg = "purple")
delete_knapp = Button(bottenram, text = "Ta bort", fg ="red")
save_knapp = Button(bottenram, text = "Spara", fg = "green")

searchknapp.pack(side = TOP)
knrapp1.pack(side = LEFT)
knrapp1.pack()
delete_knapp.pack(side = LEFT)
save_knapp.pack( side = LEFT)

root.mainloop()