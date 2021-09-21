from tkinter import *
import tkinter.font as font

# need make calculator bigger

# GUI for SGB loot splitter
master = Tk()
master.title('SINGAPORE BOLEH LOOT SPLITTER')
master.resizable(0,0)

fontStyle = font.Font(size=12)

#labels for input
Label(master, text='Total Gross Loot: ', font=fontStyle).grid(row=0, sticky=E, padx=2, pady=2)
Label(master, text='Repair Cost: ', font=fontStyle).grid(row=1, sticky=E, padx=2, pady=2)
Label(master, text='To Guild Fund (30%): ', font=fontStyle).grid(row=2, sticky=E, padx=2, pady=2)
Label(master, text='Loot Splitter Bonus: ', font=fontStyle).grid(row=4, sticky=E, padx=2, pady=2)
Label(master, text='Total Net Loot: ', font=fontStyle).grid(row=6, sticky=E, padx=2, pady=2)

Label(master, text='# of Key Weapons (x 1.5)', font=fontStyle).grid(row=8, sticky=E, padx=2, pady=2)
Label(master, text='# of Non Key Weapons (x 1)', font=fontStyle).grid(row=9, sticky=E, padx=2, pady=2)

Label(master, text='Per Key (w/o LS bonus): ', font=fontStyle).grid(row=11, sticky=E, padx=2, pady=2)
Label(master, text='Per Non Key (w/o LS bonus): ', font=fontStyle).grid(row=12, sticky=E, padx=2, pady=2)

# value for the checkbox
ls_var = BooleanVar()
gf_var = BooleanVar()

ls_check = Checkbutton(master, text='LS Bonus On', variable=ls_var).grid(row=13)
gs_check = Checkbutton(master, text='GF Contribution On', variable=gf_var).grid(row=13, column=1)

#entries for the labels
gross_loot = Entry(master, font=fontStyle)
repair_cost = Entry(master, font=fontStyle)
key_weapons = Entry(master, font=fontStyle)
nkey_weapons = Entry(master, font=fontStyle)

gross_loot.grid(row=0, column=1, sticky=W)
repair_cost.grid(row=1, column=1, sticky=W)
key_weapons.grid(row=8, column=1, sticky=W)
nkey_weapons.grid(row=9, column=1, sticky=W)

# variables for the labels
gf_amount = IntVar()
ls_amount = IntVar()
net_loot = IntVar()
key_split = IntVar()
nkey_split = IntVar()

#calculations here
def calculate_loot():
    g_l = int(gross_loot.get())
    r_c = int(repair_cost.get())
    gr_loot = g_l - r_c

    #check that weapons are not empty, if empty then set to 0
    if len(key_weapons.get()) == 0:
        key_num = 0
    else:
        key_num = int(key_weapons.get())

    if len(nkey_weapons.get()) == 0:
        nkey_num = 0
    else:
        nkey_num = int(nkey_weapons.get())

    #for gf_amt
    gf_check = gf_var.get()
    if gf_check is True:
        gf = round((gr_loot) * 0.3)
        gf_amount.set(gf)
    else:
        gf_amount.set(0)

    #for ls_amt
    ls_cb = ls_var.get()
    if ls_cb is True:
        ls = round(((gr_loot) - int(gf_amount.get())) * 0.05)
        ls_amount.set(ls)
    else:
        ls_amount.set(0)

    #for total net loot
    new_net = (gr_loot) - (int(gf_amount.get()) + int(ls_amount.get()))
    net_loot.set(new_net)

    #for the nkey lootsplit
    nkey_loot = round(new_net/((key_num*1.5) + nkey_num))
    key_loot = round((new_net/((key_num*1.5) + nkey_num)) * 1.5)

    key_split.set(key_loot)
    nkey_split.set(nkey_loot)

def reset():
    gross_loot.delete(0, END)
    repair_cost.delete(0, END)
    key_weapons.delete(0, END)
    nkey_weapons.delete(0, END)


#outputs
guild_fund = Label(master, textvariable=gf_amount, bg='white', font=fontStyle)
lootsplit_bonus = Label(master, textvariable=ls_amount, bg='white', font=fontStyle)
key_output = Label(master, textvariable=key_split, bg='white', font=fontStyle)
nkey_output = Label(master, textvariable=nkey_split, bg='white', font=fontStyle)
total_net = Label(master, textvariable=net_loot, bg='white', font=fontStyle)

guild_fund.grid(row=2, column=1, sticky=W, padx=2, pady=2)
lootsplit_bonus.grid(row=4, column=1, sticky=W, padx=2, pady=2)
total_net.grid(row=6, column=1, sticky=W, padx=2, pady=2)
key_output.grid(row=11, column=1, sticky=W, padx=2, pady=2)
nkey_output.grid(row=12, column=1, sticky=W, padx=2, pady=2)

#buttons to calculate and reset
calc_btn = Button(master, text='CALCULATE', width=20, command=calculate_loot, bg='green', fg='white', font=fontStyle).grid(row=14, column=0, padx=2, pady=2)
reset_btn = Button(master, text='RESET', width=20, command=reset, bg='orange', fg='white', font=fontStyle).grid(row=14, column=1, padx=2, pady=2)



master.mainloop()