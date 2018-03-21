import tkinter as tk
import pickle
from os.path import isfile

sa_book = []
search_book = []
searched = False

def read_ab():
    global a_book
    with open('addressbook', 'rb') as pfile:
        a_book=pickle.load(pfile)
    return a_book
def write_ab(a_book):
    with open('addressbook', 'wb') as pfile:
        pickle.dump(a_book,pfile)

#check whether file 'addressbook' exists or not
read_ab() if isfile('addressbook') else write_ab(sa_book)
            
    
root = tk.Tk()
root.title("Contact List")
#root.geometry("200x200")
table_holder = tk.Frame()
sa_book = list(a_book)
    

def add_contact(contact):
    sa_book.append(contact)
    sa_book[len(sa_book)-1]['id']=len(sa_book)-1
    write_ab(sa_book)
    print(sa_book)
    rem_table()
    gen_table()

def del_contact(contact_id):
    print(contact_id)
    sa_book.pop(contact_id)
    write_ab(sa_book)
    print(sa_book)
    rem_table()
    gen_table()

def mod_contact(contact_id, name, number):
    print(name,number)
    #contacti_id=int(contact_id)
    sa_book[contact_id]['name']=name
    sa_book[contact_id]['number']=number
    write_ab(sa_book)
    print(sa_book)
    rem_table()
    gen_table()

def rem_table():
    for child in table_holder.winfo_children():
        child.destroy()

def gen_table():
    table_data=[]
    if searched:
        table_data=search_book
    else:
        table_data=sa_book

    print('table_data',table_data)
    
    
    for it in range(len(table_data)):
        
        
        contact_container = tk.Frame(table_holder)
        
        
        contact_id = tk.Label(contact_container, text=str(it))
        contact_id.pack(side="left")
        
        name_text=tk.StringVar()
        name=tk.Entry(contact_container, textvariable=name_text)
        name.insert(0,table_data[it]['name'])
        name.pack(side='left')
        
        number_text=tk.StringVar()
        number=tk.Entry(contact_container, textvariable=number_text)
        number.insert(0,table_data[it]['number'])

        del_f= (lambda i: (lambda: del_contact(i)))(it)
        #mod_f= (lambda i,n,m: (lambda: mod_contact(i,n,m)))(it,name_text.get(),number_text.get())
        
        

        #mod_button = tk.Button(contact_container, text="mod", command=mod_f)            
        del_button = tk.Button(contact_container, text="del", command=del_f)
        
        
        #mod_button.pack(side='right')
        del_button.pack(side='right')
        
        number_text=tk.StringVar() 
        number_text.set(table_data[it]['number']) 
        number=tk.Entry(contact_container, textvariable=number_text)
        number.pack(side='left')

        
        
        contact_container.pack(side="top", fill="x")

    table_holder.pack(side='top', fill='y')
    
def namesort_up():
    global sa_book
    sorted_sa_book = sorted(sa_book, key= lambda contact:contact['name'])
    sa_book=sorted_sa_book
    rem_table()
    gen_table()

def namesort_dw():
    global sa_book     
    sorted_sa_book = sorted(sa_book, key= lambda contact:contact['name'], reverse=True)     
    sa_book=sorted_sa_book     
    rem_table()     
    gen_table()    

def search_contact(query):
    global searched
    global search_book
    if query=='':
        search_book=[]
        searched=False
        rem_table()
        gen_table()
        return
    global sa_book
    
    for i in sa_book:
        if query in i['name'] and i not in search_book:
            print(query)
            search_book.append(i)

    print(search_book)
    
    searched=True
    print(searched)
    rem_table()
    gen_table()

def gen_interface():
    header = tk.Label(root,text="Contact List")
    header.pack(side='top')
    

    #gen_table
    add_container = tk.Frame(root)
    
    name=tk.StringVar()
    name_entry=tk.Entry(root, textvariable=name)
    name_entry.pack(in_=add_container, side='left')
    
    number=tk.StringVar()
    number_entry=tk.Entry(root, textvariable=number)
    number_entry.pack(in_=add_container, side='left')
    
    
    apply_button = tk.Button(root, text="add",command= lambda: add_contact({'name':name.get(),'number':number.get()}))
    apply_button.pack(in_=add_container, side='left')
    
    add_container.pack(side="top", fill="x")

    search_sort=tk.Frame(root)
    search_sort.pack(anchor='w')
    
    name_up = tk.Button(search_sort, text="nameUp", command=namesort_up)     
    name_dw = tk.Button(search_sort, text="nameDw", command=namesort_dw)     
    
    name_up.pack(side='left')     
    name_dw.pack(side='left')
    
    search_query=tk.StringVar()
    search_entry=tk.Entry(search_sort, textvariable=search_query)
    search_entry.pack(side='left')

    search_button = tk.Button(search_sort, text='search', command=lambda: search_contact(search_query.get()) ) 
    search_button.pack(side="left")
    table_holder=tk.Frame(root)
    table_holder.pack()
    gen_table()
    
    mod_frame = tk.Frame(root)
    contact_id=tk.StringVar()
    contact_id_entry=tk.Entry(mod_frame,textvariable=contact_id)
    contact_id_entry.pack(side='left')
    
    mod_name = tk.StringVar()
    mod_name_entry=tk.Entry(mod_frame, textvariable=mod_name)
    mod_name_entry.pack(side='left')
    
    mod_number = tk.StringVar()
    mod_number_entry = tk.Entry(mod_frame, textvariable=mod_number)
    mod_number_entry.pack(side='left')
    
    #mod_f= (lambda i,n,m: (lambda: mod_contact(i,n,m)))(contact_id.get(),name.get(),number.get())
    
    mod_button = tk.Button(mod_frame, text="mod", command=lambda: mod_contact(int(contact_id.get()),mod_name.get(),mod_number.get()))
    mod_button.pack(side='right')
    mod_frame.pack()


    root.mainloop()

gen_interface()
        
    
    
        


