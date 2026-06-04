import json
import os
import tkinter as tk

def Check_json_file():
    if os.path.exists("Contact.json") and os.path.getsize("Contact.json") > 0:
        with open("Contact.json","r") as json_file:
            return json.load(json_file)
    return {}

def save_changes(data):
    with open("Contact.json", "w") as f:
        json.dump(data, f, indent = 4)

def add(name,number):
    new_entry={}
    new_entry.update({name:number})
    data= Check_json_file()
    data.update(new_entry)
    save_changes(data)

def user_input():
    name = entry_name.get()
    number = entry_number.get()
    add(name,number)
   



root = tk.Tk()
root.title("Contact Management")
root.geometry("300x300")


tk.Label(root,text="Name").grid(row=1, column=0)
tk.Label(root,text="Number").grid(row=2, column=0)

entry_name= tk.Entry(root)
entry_number = tk.Entry(root)

entry_name.grid(row=1,column=1)
entry_number.grid(row=2,column=1)


Add_Contact = tk.Button(root,text="Add Contact",width=25,command=user_input)
Add_Contact.grid()

root.mainloop()



