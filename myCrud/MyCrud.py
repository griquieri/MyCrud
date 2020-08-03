#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


# In[2]:


def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id=='' or name=='' or phone==''):
        MessageBox.showerror('Insert status','All fields are required')
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            passwd="mYsqltest",
            database="Mycrud"
        )
        cursor = con.cursor()
        cursor.execute("insert into student values('" +id+"', '" +name+"', '" +phone+"')")
        cursor.execute('commit')

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')

        show()

        MessageBox.showinfo('Insert status', 'Inserted successufully')


# In[3]:


def delete():
    if(e_id == ''):
        MessageBox.showerror('Delete status', 'ID are required for delete')
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            passwd="mYsqltest",
            database="Mycrud"
        )
        cursor = con.cursor()
        cursor.execute("delete from student where id='" + e_id.get() + "'")
        cursor.execute('commit')

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')

        show()

        MessageBox.showinfo('Delete status', 'Deleted successufully')


# In[4]:


def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if (id == '' or name == '' or phone == ''):
        MessageBox.showerror('Update status', 'All fields are required')
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            passwd="mYsqltest",
            database="Mycrud"
        )
        cursor = con.cursor()
        cursor.execute("update student set name='" + name + "', phone='" + phone + "' where id='" + id + "'")
        cursor.execute('commit')

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')

        show()

        MessageBox.showinfo('update status', 'Updated successufully')


# In[5]:


def get():
    if (e_id == ''):
        MessageBox.showerror('Fetch status', 'ID are required for delete')
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            passwd="mYsqltest",
            database="Mycrud"
        )
        cursor = con.cursor()
        cursor.execute("select * from student where id='" + e_id.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0,row[1])
            e_phone.insert(0, row[2])


# In[6]:


def show():
    con = mysql.connect(
        host="localhost",
        user="root",
        passwd="mYsqltest",
        database="Mycrud"
    )
    cursor = con.cursor()
    cursor.execute("select * from student")
    rows = cursor.fetchall()

    list.delete(0, list.size())

    for row in rows:
        insertData =str(row[0])+'        '+row[1]
        list.insert(list.size()+1, insertData)


# In[7]:




#Window
root = Tk()
root.geometry('600x300')
root.title('CRUD')

#Labels
id = Label(root, text='Enter ID: ',font=('bold',10))
id.place(x=20, y=30)

name = Label(root, text='Enter Name: ',font=('bold',10))
name.place(x=20, y=60)

phone = Label(root, text='Enter Phone: ',font=('bold',10))
phone.place(x=20, y=90)

#Entries
e_id = Entry()
e_id.place(x=150,y=30)

e_name = Entry()
e_name.place(x=150,y=60)

e_phone = Entry()
e_phone.place(x=150,y=90)

#Buttons
insert = Button(root, text='INSERT',font=('italic',10), bg='white', command=insert)
insert.place(x=20, y=140)

delete = Button(root, text='DELETE',font=('italic',10), bg='white', command=delete)
delete.place(x=100, y=140)

update = Button(root, text='UPDATE',font=('italic',10), bg='white', command=update)
update.place(x=20, y=180)

get = Button(root, text='GET',font=('italic',10), bg='white', command=get)
get.place(x=100, y=180)

list = Listbox(root)
list.place(x=290, y=30)
show()

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




