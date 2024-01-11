from tkinter import *
import pandas as pd
import numpy as np
import openpyxl
from tkinter import ttk, filedialog, messagebox

root = Tk()
root.title('test')
root.geometry('850x400')

inputan = int(input('masukkan nisn: '))
tabel = ttk.Treeview(root)
tabel.pack(pady=20)


df1 = pd.read_excel('Student_data.xlsx')
df = df1.loc[df1["NISN"] == inputan]




tabel['column'] = list(df.columns[4:9])

tabel['show'] = 'headings'

for col in tabel['column']:
    tabel.heading(col, text=col)


df_rows = df.to_numpy().tolist()
for row in df_rows:
    tabel.insert("", "end", values=row[4:9])




# Tabel



# button
# my_button = Button(root, text='Open Excel File', command=open_excel)
# my_button.pack(pady=20)

root.mainloop()