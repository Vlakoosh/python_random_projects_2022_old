from logging import PlaceHolder
from operator import ge
from tkinter import *
from turtle import width
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.iconbitmap("cog.ico")
root.title("Python Program")

#Create a function to delete a record

def delete():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid="+delete_entry.get())

    #Commit changes
    conn.commit()

    #Close Connection
    conn.close()



#Create submit function for database
def submit():

    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :country, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'country': country.get(),
                'zipcode': zipcode.get()
            })
    
    #Clear the textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    country.delete(0, END)
    zipcode.delete(0, END)

    #Commit changes
    conn.commit()

    #Close Connection
    conn.close()

#Create a query function for the database
def query():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)
    #Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " \t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8,column=0,columnspan=2)

    #Commit changes
    conn.commit()

    #Close Connection
    conn.close()

#Create an update function for the database
def update():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    record_id = delete_entry.get()

    c.execute("""UPDATE addresses SET 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        country = :country,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
        'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'address': address_editor.get(),
        'city': city_editor.get(),
        'country': country_editor.get(),
        'zipcode': zipcode_editor.get(),
        'oid': record_id
        })


    #Commit changes
    conn.commit()

    #Close Connection
    conn.close()

    editor.destroy()


#Create an edit function for the database
def edit():
    global editor
    editor = Tk()
    editor.iconbitmap("cog.ico")
    editor.title("Record Editor")

    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    #Create cursor
    c = conn.cursor()

    #Create a variable for oid of edited item from the database
    records_id = delete_entry.get()

    #Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + records_id)
    records = c.fetchall()
    #print(records)

    #Make global variables for entry boxes
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global country_editor
    global zipcode_editor

    #Define entry boxes
    f_name_editor = Entry(editor, width=30)
    l_name_editor = Entry(editor, width=30)
    address_editor = Entry(editor, width=30)
    city_editor = Entry(editor, width=30)
    country_editor = Entry(editor, width=30)
    zipcode_editor = Entry(editor, width=30)

    #Display entry boxes
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    l_name_editor.grid(row=1,column=1)
    address_editor.grid(row=2,column=1)
    city_editor.grid(row=3,column=1)
    country_editor.grid(row=4,column=1)
    zipcode_editor.grid(row=5,column=1)

    #Define text box labels
    f_name_label = Label(editor,text="First Name")
    l_name_label = Label(editor,text="Last Name")
    address_label = Label(editor,text="Address")
    city_label = Label(editor,text="City")
    country_label = Label(editor,text="Country")
    zipcode_label = Label(editor,text="Zipcode")

    #Display text box labels
    f_name_label.grid(row=0,column=0,pady=(10,0))
    l_name_label.grid(row=1,column=0)
    address_label.grid(row=2,column=0)
    city_label.grid(row=3,column=0)
    country_label.grid(row=4,column=0)
    zipcode_label.grid(row=5,column=0)

    #Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        country_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    

    save_button = Button(editor, text="Save record", command=update)
    save_button.grid(row=6,column=0, columnspan=2,padx=10,pady=10,ipadx=131)

    

    #Commit changes
    conn.commit()

    #Close Connection
    conn.close()



#Databases

#Create a database or connect to one
conn = sqlite3.connect('address_book.db')

#Create cursor
c = conn.cursor()

#Create table

'''
c.execute("""CREATE TABLE addresses (
        first_name text, 
        last_name text,
        address text,
        city text,
        country text,
        zipcode integer
    )""")
'''

#Define entry boxes
f_name = Entry(root, width=30)
l_name = Entry(root, width=30)
address = Entry(root, width=30)
city = Entry(root, width=30)
country = Entry(root, width=30)
zipcode = Entry(root, width=30)
delete_entry = Entry(root,width=30)

#Display entry boxes
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name.grid(row=1,column=1)
address.grid(row=2,column=1)
city.grid(row=3,column=1)
country.grid(row=4,column=1)
zipcode.grid(row=5,column=1)
delete_entry.grid(row=9,column=1)


#Define text box labels
f_name_label = Label(root,text="First Name")
l_name_label = Label(root,text="Last Name")
address_label = Label(root,text="Address")
city_label = Label(root,text="City")
country_label = Label(root,text="Country")
zipcode_label = Label(root,text="Zipcode")
delete_label = Label(root,text="Select ID")


#Display text box labels
f_name_label.grid(row=0,column=0,pady=(10,0))
l_name_label.grid(row=1,column=0)
address_label.grid(row=2,column=0)
city_label.grid(row=3,column=0)
country_label.grid(row=4,column=0)
zipcode_label.grid(row=5,column=0)
delete_label.grid(row=9,column=0)

#Create Submit button
submit_button = Button(root, text="Add record to database", command=submit)
submit_button.grid(row=6, column=0,columnspan=2, padx=10, pady=10, ipadx=100)

#Create query button
query_button = Button(root, text="Show records", command=query)
query_button.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=127)

#Create a delete button
delete_button = Button(root, text="Delete record", command=delete)
delete_button.grid(row=10,column=0, columnspan=2,padx=10,pady=10,ipadx=126)

#Create an editor button
edit_button = Button(root, text="Edit record", command=edit)
edit_button.grid(row=11,column=0, columnspan=2,padx=10,pady=10,ipadx=131)

#Commit changes
conn.commit()

#Close Connection
conn.close()

root.mainloop()