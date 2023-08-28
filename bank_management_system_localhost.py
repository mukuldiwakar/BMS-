import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import smtplib
import mysql.connector
import requests
import PIL
from PIL import ImageTk, Image
import customtkinter as ctk
import pygame

root = tk.Tk()
root.geometry('1920x1080')
root.title('MY APP')
root.iconbitmap('icon.ico')

# ------------------------------------------------image-----------------------------------------------------------------------
image = Image.open( 'bankground.jpg')
image = image.resize((1540,800)) # Resize the image to fit the window
photo = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
img_label = Label(root, image=photo)
img_label.place(x=0,y=0)

# ---------------------------------------------------frame-------------------------------------------------------------------
f1 = Frame(root, bg='light blue', borderwidth=10, relief=GROOVE, width=500, height=550)
f1.place(x=985, y=135)

# -------------------------------------------------------label-----------------------------------------------------------------
welcome=Label(root,text="🛡ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴘᴀɪɴᴜᴍ🛡",bg='steel blue',fg='white',font=("Times New Roman",'30'))
welcome.pack(fill='x')

login_label = tk.Label(root, text="Login",bg='white', font=("Times New Roman", 24))
login_label.place(x=70,y=230)

create = tk.Label(root, text="Create Account",bg='white', font=("Times New Roman", 24))
create.place(x=70,y=430)
# =============================================================================================================================================================


def hide_root():
    root.withdraw() 
def win3():
    
    import tkinter as tk
    from tkinter import Tk, Label, Button, Entry, Frame, Canvas, Text, Scrollbar, Listbox, Radiobutton, Checkbutton, Toplevel
    from tkinter import messagebox
    import PIL
    from PIL import ImageTk, Image
    from tkinter import PhotoImage
    import tkinter as tk
    from tkinter import ttk
    import tkinter as tk
    from customtkinter import CTk, CTkLabel, CTkButton, CTkScrollableFrame,CTkEntry
    from tkinter import Tk, Label, Button, Entry, Frame, Canvas, Text, Scrollbar, Listbox, Radiobutton, Checkbutton, Toplevel
    import customtkinter as ctk
    import mysql.connector
    from tkinter import messagebox
    import pygame
    from tkinter import ttk, Y, RIGHT
    
    global root3
    root3 = tk.Toplevel(root)
    root3.geometry('1920x1080+0+0')
    root3.title("Admin Dashboard")
    hide_root()
    
# ------------------------------------------------------------------------------------------------------------------   
    image = Image.open( 'bankground3.jpg')
    image = image.resize((1540,800))
    photo = ImageTk.PhotoImage(image)

    img_label = Label(root3, image=photo)
    img_label.photo = photo  
    img_label.place(x=0, y=0)
    
# -----------------------------------------------------------------------------------------------------------------------------    
    f4 = ctk.CTkFrame(root3, width=370, height=340,bg_color="black",fg_color="sky blue")
    f4.place(x=10, y=220)
    
    f5 = ctk.CTkFrame(root3, width=370, height=180, bg_color="black", fg_color="light green")
    f5.place(x=10, y=600) 


# ============================================================================================================================    
    global admin_inf
    admin_inf="Admin"
    
    global user_id_entry3, password_entry3, name_entry3, account_number_entry3, address_entry3, current_amount_entry3,user_id_entry4
# ---------------------------------------------------------------------------------------------------------------------------------  
    
    def update_treeview():
        for i in tree.get_children():
            tree.delete(i)

        lol = mysql.connector.connect(host='localhost', user='root', password='Qwertyios123@', database='bank')
        cur = lol.cursor()
        cur.execute('''SELECT * FROM test2''')

        i = 0
        for row in cur:
            tree.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            i += 1

        cur.close()
        lol.close() 
        tree.update()
# ====================================================================================================================================
  
    def create_user():
        user_id3 = user_id_entry3.get()
        password3 = password_entry3.get()
        name3 = name_entry3.get()
        account_number3 = account_number_entry3.get()
        email3 = None
        address3 = address_entry3.get()
        bank_code3 = 'painum653'
        last_transaction3 = None
        current_amount3 = current_amount_entry3.get()

        if not (user_id3 and password3 and name3 and account_number3 and address3 and current_amount3):
            messagebox.showerror("Error", "All fields must be filled.")
            return False

        try:
            account_number3 = int(account_number3)
            current_amount3 = int(current_amount3)
        except ValueError:
            messagebox.showerror("Error", "Account number and current amount must be integers.")
            return False

        try:
            connection = mysql.connector.connect(host='localhost', user='root', password='Qwertyios123@', database='bank')
            cursor = connection.cursor()

            query = """INSERT INTO test2 (User_ID, Password, Name, `Account_number`, `E-mail`,Address,Last_trasaction, Bank_code, `Current_amount`)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            values = (user_id3, password3, name3, account_number3, email3, address3, last_transaction3, bank_code3, current_amount3)

            cursor.execute(query, values)

            connection.commit()

            messagebox.showinfo("Success", "User created successfully.")
            update_treeview()
            return True

        except Exception as e:
            print(f"Error: {str(e)}")
            messagebox.showerror("Error", "An error occurred while creating the user.")
            return False

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# ---------------------------------------------------------------------------------------------------------------------------------------   
    s=ttk.Style(root3)
    s.theme_use('winnative')
    s.configure('.',font=('Helvetica',10))
    s.configure('Treeview.Heading',foreground='black',background='sky blue',font=('Helvetica',10,'bold'))

    tree = ttk.Treeview(root3,height=26)
    tree['show']='headings'
    tree["columns"] = ['User_ID', 'Password', 'Name', 'Account_number', 'E-mail', 'Address', 'Bank_code', 'Last_trasaction', 'Current_amount']

    tree.column('User_ID', width=120, minwidth=50, anchor=tk.CENTER)
    tree.column('Password', width=120, minwidth=120, anchor=tk.CENTER)
    tree.column('Name', width=120, minwidth=120, anchor=tk.CENTER)
    tree.column('Account_number', width=120, minwidth=120, anchor=tk.CENTER)
    tree.column('E-mail', width=120, minwidth=120, anchor=tk.CENTER)
    tree.column('Address', width=120, minwidth=120, anchor=tk.CENTER)
    tree.column('Bank_code', width=120, minwidth=120, anchor=tk.CENTER)
    tree.column('Last_trasaction', width=120, minwidth=120, anchor=tk.CENTER)
    tree.column('Current_amount', width=120, minwidth=120, anchor=tk.CENTER)

    tree.heading('User_ID', text="User ID", anchor=tk.CENTER)
    tree.heading('Password', text="Password", anchor=tk.CENTER)
    tree.heading('Name', text="Name", anchor=tk.CENTER)
    tree.heading('Account_number', text="Account Number", anchor=tk.CENTER)
    tree.heading('E-mail', text="E-mail", anchor=tk.CENTER)
    tree.heading('Address', text="Address", anchor=tk.CENTER)
    tree.heading('Bank_code', text="Bank Code", anchor=tk.CENTER)
    tree.heading('Last_trasaction', text="Last Transaction", anchor=tk.CENTER)
    tree.heading('Current_amount', text="Current Amount", anchor=tk.CENTER)

    lol = mysql.connector.connect(host='localhost', user='root', password='Qwertyios123@', database='bank')
    cur = lol.cursor()
    cur.execute('''SELECT * FROM test2''')

    i = 0
    for row in cur:
        tree.insert('',i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        i += 1

    vsb=ttk.Scrollbar(root3,orient='vertical')
    vsb.configure(command=tree.xview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y,side=RIGHT)

    tree.place(x=400,y=13)
    cur.close()
    lol.close()
    
    

# ================================================================================================================================================

    def del_acc():
        uid = user_id_entry4.get()
        if not uid:
            messagebox.showerror("Error", "Please enter a User ID to delete.")
            return
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='Qwertyios123@', database='bank')
            cursor = conn.cursor()
            del_q = "DELETE FROM test2 WHERE User_ID = %s"
            cursor.execute(del_q, (uid,))
            conn.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", f"Account with User ID {uid} deleted.")
                update_treeview()
                user_id_entry4.delete(0, END)
            else:
                messagebox.showerror("Error", f"Account with User ID {uid} not found.")
        except Exception as e:
            print(f"Error: {str(e)}")
            messagebox.showerror("Error", "An error occurred while deleting the account.")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

            
        

        
# =====================================================================================================================================================
    
    
    
    user_inf = ctk.CTkLabel(root3, text=f'Welcome { admin_inf}', font=("Arial", 20, "bold"))
    user_inf.place(x=10, y=10)
    
    am_label = ctk.CTkLabel(root3, text='Admin Dashboard:', font=("Arial", 20, "bold"))
    am_label.place(x=20, y=180)
# ----------------------------------------------------------------------------------------------------------
    create_user_label = ctk.CTkLabel(f4, text='Create User Account:', font=("Arial", 16, "bold"))
    create_user_label.place(x=20, y=10)
    

    user_id3 = CTkLabel(f4, text="User_ID:", font=("Arial", 14, "bold"))
    user_id3.place(x=20, y=60)

    password_label3 = CTkLabel(f4, text="Password:", font=("Arial", 14, "bold"))
    password_label3.place(x=20, y=100)

    name_label3 = CTkLabel(f4, text="Name:", font=("Arial", 14, "bold"))
    name_label3.place(x=20, y=140)

    account_number_label3 = CTkLabel(f4, text="Account_number:", font=("Arial", 14, "bold"))
    account_number_label3.place(x=20, y=180)

    address_label3 = CTkLabel(f4, text="Address:", font=("Arial", 14, "bold"))
    address_label3.place(x=20, y=220)

    current_amount_label3 = CTkLabel(f4, text="Initial_amount:", font=("Arial", 14, "bold"))
    current_amount_label3.place(x=20, y=260)

    

    user_id_entry3 = CTkEntry(f4, font=("Arial", 14))
    user_id_entry3.place(x=200, y=60)

    password_entry3 = CTkEntry(f4, font=("Arial", 14))
    password_entry3.place(x=200, y=100)

    name_entry3 = CTkEntry(f4, font=("Arial", 14))
    name_entry3.place(x=200, y=140)

    account_number_entry3 = CTkEntry(f4, font=("Arial", 14))
    account_number_entry3.place(x=200, y=180)

    address_entry3 = CTkEntry(f4, font=("Arial", 14))
    address_entry3.place(x=200, y=220)

    current_amount_entry3 = CTkEntry(f4, font=("Arial", 14))
    current_amount_entry3.place(x=200, y=260)
    
    submit3 = ctk.CTkButton(f4, text="Submit", font=("Arial", 15), hover_color='red',command=create_user)
    submit3.place(x=20, y=300)
    
# -------------------------------------------------------------delete user-------------------------------------------------------------------------------------------
    delete_user_label = ctk.CTkLabel(f5, text='DeleteUser Account:', font=("Arial", 18, "bold"))
    delete_user_label.place(x=20, y=10)
    
    user_id4 = CTkLabel(f5, text="User_ID:", font=("Arial", 16, "bold"))
    user_id4.place(x=20, y=60)
    
    user_id_entry4 = CTkEntry(f5, font=("Arial", 15))
    user_id_entry4.place(x=180, y=60)
    
    submit3 = ctk.CTkButton(f5, text="Submit", font=("Arial", 15), hover_color='red',command=del_acc)
    submit3.place(x=20, y=120)
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# ================================================================================================================================================================

def hide_root():
    root.withdraw() 

def win2():
    from tkinter import messagebox
    import PIL
    from PIL import ImageTk, Image
    from tkinter import PhotoImage
    import tkinter as tk
    from tkinter import ttk
    import tkinter as tk
    from customtkinter import CTk, CTkLabel, CTkButton, CTkScrollableFrame
    from tkinter import Tk, Label, Button, Entry, Frame, Canvas, Text, Scrollbar, Listbox, Radiobutton, Checkbutton, Toplevel
    import customtkinter as ctk
    import mysql.connector
    from tkinter import messagebox
    import pygame
 # -------------------------------------------------------------sound-----------------------------------------------------------------
    pygame.mixer.init()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    global root2
    root2 = Toplevel(root)
    root2.geometry('1920x1080+0+0')
    root2.title('Customer Dashboard')
    hide_root()
 # =========================================================================BACKGROUND=======================================   
    image = Image.open( 'bankground2.jpg')
    image = image.resize((1540,800))
    photo = ImageTk.PhotoImage(image)

    img_label = Label(root2, image=photo)
    img_label.place(x=0,y=0)
#################################################################################    
    global user_inf
    user_inf=user_entry.get()
# =======================================================================================================================================
    f2 = ctk.CTkScrollableFrame(root2, width=500, height=550)
    f2.place(x=980, y=20)
# ===========================================================================================================================================
    def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()
    

    
    
    def check_balance():
        clear_frame(f2)
        try:
            connection = mysql.connector.connect(host='localhost', user='root', password='Qwertyios123@', database='bank')
            cursor = connection.cursor()
            query = f"SELECT Name, Bank_code, Current_amount FROM test2 WHERE User_ID = '{user_id}'"
            cursor.execute(query)
            user_data = cursor.fetchone()
            if user_data:
                name, bank_code, current_amount = user_data
                global message
                message = f"Name: {name}\nBank Code: {bank_code}\nCurrent Amount: {current_amount}"
                bal_label = ctk.CTkLabel(f2, text=message, justify="center", anchor="w", padx=5, wraplength=480, pady=5, font=("Arial", 25))
                bal_label.place(x=15, y=5)
                pygame.mixer.music.load('baltone.mp3')
                pygame.mixer.music.play()
            else:
                bal_label = ctk.CTkLabel(f2, text="User not found", justify="center", anchor="w", padx=5, wraplength=480, pady=5, font=("Arial", 25))
                bal_label.place(x=15, y=5)
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
        


        
# ========================================================================================================================================
   

    def update_balance():
        try:
            sender_user_id = t_user_id_entry.get()
            receiver_user_id = t_receiver_id_entry.get()
            amount = int(t_money_entry.get())
            bank_code = t_bank_code_entry.get()

            if bank_code != 'painum653':
                messagebox.showerror("Error", "Invalid bank code.")
                return

            connection = mysql.connector.connect(host='localhost',user='root',password='Qwertyios123@',database='bank')
            cursor = connection.cursor()

            cursor.execute(f"SELECT Current_amount FROM test2 WHERE User_ID = '{sender_user_id}'")
            sender_balance = cursor.fetchone()

            if sender_balance is None:
                messagebox.showerror("Error", "Invalid sender user ID.")
                return

            sender_balance = sender_balance[0]

            if sender_balance < amount:
                messagebox.showerror("Error", "Insufficient balance for the transfer.")
                return

            new_sender_balance = sender_balance - amount
            cursor.execute(f"UPDATE test2 SET Current_amount = {new_sender_balance} WHERE User_ID = '{sender_user_id}'")

            cursor.execute(f"SELECT Current_amount FROM test2 WHERE User_ID = '{receiver_user_id}'")
            receiver_balance = cursor.fetchone()

            if receiver_balance is None:
                messagebox.showerror("Error", "Invalid receiver user ID.")
                return

            receiver_balance = receiver_balance[0]

            new_receiver_balance = receiver_balance + amount
            cursor.execute(f"UPDATE test2 SET Current_amount = {new_receiver_balance} WHERE User_ID = '{receiver_user_id}'")

            connection.commit()

            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Transfer successful.")
            pygame.mixer.music.load('phonepay.mp3')
            pygame.mixer.music.play()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error: {error}")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")


        
    def money_transfer():
        clear_frame(f2)
        global t_user_id_entry,t_money_entry,t_receiver_id_entry,t_bank_code_entry
        transfer_heading_label = ctk.CTkLabel(f2, text="Transfer Money", font=("Arial", 25, "bold"))
        transfer_heading_label.place(x=15, y=20)

        t_user_id_label = ctk.CTkLabel(f2, text="Your User ID:", font=("Arial", 20))
        t_user_id_label.place(x=15, y=70)

        t_user_id_entry = ctk.CTkEntry(f2, font=("Arial", 20))
        t_user_id_entry.insert(0, user_entry.get())
        t_user_id_entry.place(x=250, y=70)

        t_amount_label = ctk.CTkLabel(f2, text="Enter Amount (₹):", font=("Arial", 20))
        t_amount_label.place(x=15, y=110)

        t_money_entry = ctk.CTkEntry(f2, font=("Arial", 20))
        t_money_entry.place(x=250, y=110)

        t_receiver_id_label = ctk.CTkLabel(f2, text="Receiver User ID:", font=("Arial", 20))
        t_receiver_id_label.place(x=15, y=150)

        t_receiver_id_entry = ctk.CTkEntry(f2, font=("Arial", 20))
        t_receiver_id_entry.place(x=250, y=150)

        t_bank_code_label = ctk.CTkLabel(f2, text="Bank Code:", font=("Arial", 20))
        t_bank_code_label.place(x=15, y=190)

        t_bank_code_entry = ctk.CTkEntry(f2, font=("Arial", 20))
        t_bank_code_entry.place(x=250, y=190)

        transfer_button = ctk.CTkButton(f2, text="Transfer Money", font=("Arial", 25),hover_color='red',command =update_balance)
        transfer_button.place(x=115, y=250)
# =======================================================================debit=====================================================================================
 

    def update_debit():
        try:
            connection = mysql.connector.connect(host='localhost',user='root',password='Qwertyios123@',database='bank')

            cursor = connection.cursor()

            current_user_id = user_entry.get()
            amount_str = debit_amount_entry.get()

            cursor.execute(f"SELECT Current_amount FROM test2 WHERE User_ID = '{current_user_id}'")
            current_balance = cursor.fetchone()

            if current_balance is None:
                messagebox.showerror("Error", "Invalid user ID.")
                return

            current_balance = current_balance[0]

            amount = float(amount_str)

            if current_balance < 500 or  amount > current_balance:
                messagebox.showerror("Error", "Invalid debit amount or insufficient balance.")
                return

            new_current_balance = current_balance - amount

            cursor.execute(f"UPDATE test2 SET Current_amount = {new_current_balance} WHERE User_ID = '{current_user_id}'")

            connection.commit()

            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Debit successful. New balance: ₹" + str(new_current_balance))
            pygame.mixer.music.load('phonepay.mp3')
            pygame.mixer.music.play()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Database Error: {error}")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")



    def debit_money():
        clear_frame(f2)
        global debit_amount_entry
        debit_heading_label = ctk.CTkLabel(f2, text="Debit Money", font=("Arial", 25, "bold"))
        debit_heading_label.place(x=15, y=20)

        amount_label = ctk.CTkLabel(f2, text="Enter Amount (₹):", font=("Arial", 20))
        amount_label.place(x=15, y=70)

        debit_amount_entry = ctk.CTkEntry(f2, font=("Arial", 20))
        debit_amount_entry.place(x=250, y=70)

        debit_button = ctk.CTkButton(f2, text="Submit", font=("Arial", 25), hover_color='red',command=update_debit)
        debit_button.place(x=115, y=150)
# -----------------------------------------------------------------------credit----------------------------------------------------------------------        
 

    def update_credit():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Qwertyios123@',
                database='bank'
            )

            cursor = connection.cursor()

            current_user_id = c_user_id_entry.get()
            amount_str = c_money_entry.get()

            cursor.execute(f"SELECT Current_amount FROM test2 WHERE User_ID = '{current_user_id}'")
            current_balance = cursor.fetchone()

            if current_balance is None:
                messagebox.showerror("Error", "Invalid user ID.")
                return

            current_balance = current_balance[0]

            amount = float(amount_str)

            if amount < 100:
                messagebox.showerror("Error", "Invalid amount.")
                return

            new_current_balance = current_balance + amount

            cursor.execute(f"UPDATE test2 SET Current_amount = {new_current_balance} WHERE User_ID = '{current_user_id}'")

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "Credit successful. New balance: ₹" + str(new_current_balance))
            pygame.mixer.music.load('phonepay.mp3')
            pygame.mixer.music.play()
            
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Database Error: {error}")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")

    def credit_money():
        clear_frame(f2)
        global c_user_id_entry, c_money_entry
        credit_heading_label = ctk.CTkLabel(f2, text="Credit Money", font=("Arial", 25, "bold"))
        credit_heading_label.place(x=15, y=20)

        c_user_id_label = ctk.CTkLabel(f2, text="Your User ID:", font=("Arial", 20))
        c_user_id_label.place(x=15, y=70)

        c_user_id_entry = ctk.CTkEntry(f2, font=("Arial", 20))
        c_user_id_entry.insert(0, user_entry.get())
        c_user_id_entry.place(x=250, y=70)

        c_amount_label = ctk.CTkLabel(f2, text="Enter Amount (₹):", font=("Arial", 20))
        c_amount_label.place(x=15, y=110)

        c_money_entry = ctk.CTkEntry(f2, font=("Arial", 20))
        c_money_entry.place(x=250, y=110)

        

        credit_button = ctk.CTkButton(f2, text="Credit Money", font=("Arial", 25), hover_color='red',command=update_credit)
        credit_button.place(x=115, y=170)

# -----------------------------------------------------------------------email---------------------------------------------------        

    def send_email_alert(message):
        receiver_emai2=gmail_entry.get()
        smtp_server2 = "smtp.gmail.com"  
        smtp_port2 = 587  
        sender_email2 = "painumbank@gmail.com"  
        sender_password2 = "gkbu kjqb qcar hqky"  

        subject2 = "Balance info"
        body2 = f"Dear customer\n:{message}"

        try:
            server2 = smtplib.SMTP(smtp_server2, smtp_port2)
            server2.starttls()
            server2.login(sender_email2, sender_password2)

            message2 = f"Subject: {subject2}\n\n{body2}"
            server2.sendmail(sender_email2, receiver_emai2, message2)
            server2.quit()
            messagebox.showinfo("Success", "Your balance info sent sucessfully on your mail")
            return True
        except Exception as e:
            print("Error sending email:", str(e))
            return False

        
    def email_alert_button():
        check_balance() 
        send_email_alert(message)
# --------------------------------------------------------------------------------debit------------------------------------------------------------
    def submit_application():
        full_name = name_entry1.get()
        dob = dob_entry1.get()
        address = address_entry1.get()
        contact_number = identification_entry1.get()

        if not full_name or not dob or not address or not contact_number:
            messagebox.showerror("Error", "All fields must be filled.")
        elif len(contact_number) != 10 :
            messagebox.showerror("Error", "Contact number must be a 10-digit number.")
        else:
            # Application is valid, show success message
            success_message = "Your response has been successfully recorded.\nYour application is under process."
            messagebox.showinfo("Success", success_message)
     
    
    
    def apply_for_debit_card():
        clear_frame(f2)
        global name_entry1,dob_entry1,address_entry1,identification_entry1
        debit_card_heading = ctk.CTkLabel(f2, text="Apply for Debit Card", font=("Arial", 25, "bold"))
        debit_card_heading.place(x=10, y=10)

        name_label = ctk.CTkLabel(f2, text="Full Name:", font=("Arial", 20))
        name_label.place(x=10, y=50)
        name_entry1 = ctk.CTkEntry(f2, font=("Arial", 20))
        name_entry1.place(x=200, y=50)

        dob_label = ctk.CTkLabel(f2, text="Date of Birth:", font=("Arial", 20))
        dob_label.place(x=10, y=90)
        dob_entry1= ctk.CTkEntry(f2, font=("Arial", 20))
        dob_entry1.place(x=200, y=90)

        address_label = ctk.CTkLabel(f2, text="Address:", font=("Arial", 20))
        address_label.place(x=10, y=130)
        address_entry1 = ctk.CTkEntry(f2, font=("Arial", 20))
        address_entry1.place(x=200, y=130)

        identification_label = ctk.CTkLabel(f2, text="Contact number", font=("Arial", 20))
        identification_label.place(x=10, y=170)
        identification_entry1 = ctk.CTkEntry(f2, font=("Arial", 20))
        identification_entry1.place(x=200, y=170)

        terms_label = ctk.CTkLabel(f2, text="Terms and Conditions:", font=("Arial", 20, "bold"))
        terms_label.place(x=10, y=210)

        terms_text = """
        By submitting this application,
        You agree by the terms and conditions of our bank.
        
        """
        terms_info = ctk.CTkLabel(f2, text=terms_text, font=("Arial", 16), justify="left")
        terms_info.place(x=10, y=240)

        submit_button = ctk.CTkButton(f2, text="Submit Application", font=("Arial", 20), hover_color='green', command=submit_application)
        submit_button.place(x=10, y=310)
        

        
# ----------------------------------------------------------------------------logout----------------------------------------------
    def log_out():
        result = messagebox.askokcancel("Exit", "Are you sure you want to exit ?")
        if result:
            root2.destroy()


# =======================================================================================================================    
    import tkinter as tk
    from tkinter import ttk
    def calwin():
    
        import tkinter as tk
        from tkinter import Tk, Label, Button, Entry, Frame, Canvas, Text, Scrollbar, Listbox, Radiobutton, Checkbutton, Toplevel

        global cal
        cal = Toplevel(root2)
        cal.maxsize(300,420)
        cal.title("Calculator")

        def button_click(char):
            current_text = entry.get()
            entry.delete(0, tk.END)
            entry.insert(tk.END, current_text + char)

        def calculate():
            try:
                expression = entry.get()
                result = eval(expression)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
            except Exception as e:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")

        def clear():
            entry.delete(0, tk.END)


        entry = tk.Entry(cal, font=('Arial', 20))
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        button_frame = tk.Frame(cal)
        button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        
        btn_7 = tk.Button(button_frame, text='7', font=('Arial', 14), width=4, height=2, command=lambda: button_click('7'), bg='light green', fg='black')
        btn_8 = tk.Button(button_frame, text='8', font=('Arial', 14), width=4, height=2, command=lambda: button_click('8'), bg='light green', fg='black')
        btn_9 = tk.Button(button_frame, text='9', font=('Arial', 14), width=4, height=2, command=lambda: button_click('9'), bg='light green', fg='black')
        btn_divide = tk.Button(button_frame, text='/', font=('Arial', 14), width=4, height=2, command=lambda: button_click('/'), bg='sky blue', fg='black')

        btn_4 = tk.Button(button_frame, text='4', font=('Arial', 14), width=4, height=2, command=lambda: button_click('4'), bg='light green', fg='black')
        btn_5 = tk.Button(button_frame, text='5', font=('Arial', 14), width=4, height=2, command=lambda: button_click('5'), bg='light green', fg='black')
        btn_6 = tk.Button(button_frame, text='6', font=('Arial', 14), width=4, height=2, command=lambda: button_click('6'), bg='light green', fg='black')
        btn_multiply = tk.Button(button_frame, text='*', font=('Arial', 14), width=4, height=2, command=lambda: button_click('*'), bg='sky blue', fg='black')

        btn_1 = tk.Button(button_frame, text='1', font=('Arial', 14), width=4, height=2, command=lambda: button_click('1'), bg='light green', fg='black')
        btn_2 = tk.Button(button_frame, text='2', font=('Arial', 14), width=4, height=2, command=lambda: button_click('2'), bg='light green', fg='black')
        btn_3 = tk.Button(button_frame, text='3', font=('Arial', 14), width=4, height=2, command=lambda: button_click('3'), bg='light green', fg='black')
        btn_subtract = tk.Button(button_frame, text='-', font=('Arial', 14), width=4, height=2, command=lambda: button_click('-'), bg='sky blue', fg='black')

        btn_0 = tk.Button(button_frame, text='0', font=('Arial', 14), width=4, height=2, command=lambda: button_click('0'), bg='light green', fg='black')
        btn_decimal = tk.Button(button_frame, text='.', font=('Arial', 14), width=4, height=2, command=lambda: button_click('.'), bg='light green', fg='black')
        btn_equals = tk.Button(button_frame, text='=', font=('Arial', 14), width=4, height=2, command=calculate, bg='yellow', fg='black')
        btn_add = tk.Button(button_frame, text='+', font=('Arial', 14), width=4, height=2, command=lambda: button_click('+'), bg='sky blue', fg='black')

        btn_clear = tk.Button(button_frame, text='C', font=('Arial', 14), width=4, height=2, command=clear, bg='green', fg='black')

        
        btn_7.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        btn_8.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        btn_9.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
        btn_divide.grid(row=0, column=3, padx=5, pady=5, sticky='nsew')

        btn_4.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        btn_5.grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
        btn_6.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')
        btn_multiply.grid(row=1, column=3, padx=5, pady=5, sticky='nsew')

        btn_1.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        btn_2.grid(row=2, column=1, padx=5, pady=5, sticky='nsew')
        btn_3.grid(row=2, column=2, padx=5, pady=5, sticky='nsew')
        btn_subtract.grid(row=2, column=3, padx=5, pady=5, sticky='nsew')

        btn_0.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')
        btn_decimal.grid(row=3, column=1, padx=5, pady=5, sticky='nsew')
        btn_equals.grid(row=3, column=2, padx=5, pady=5, sticky='nsew')
        btn_add.grid(row=3, column=3, padx=5, pady=5, sticky='nsew')

        btn_clear.grid(row=4, column=0, padx=5, pady=5, columnspan=4, sticky='nsew')

        cal.mainloop()



    
    




    
    
# =============================================================gif===========================================================================================================================================================
    file="money2.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None
    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = root2.after(50,lambda :animation(count))

    def stop_animation():
        root.after_cancel(anim)

    gif_label = tk.Label(root2,image="")
    gif_label.place(x=1280,y=620)

    animation(count) 
    
    
    
    
    
# =================================================================================================================================

    # Create labels for different categories
    user_inf = ctk.CTkLabel(root2, text=f'Welcome { user_inf}', font=("Arial", 20, "bold"))
    user_inf.place(x=10, y=10)
    
    am_label = ctk.CTkLabel(root2, text='Account Management:', font=("Arial", 20, "bold"))
    am_label.place(x=20, y=180)

    # Create buttons for Account Management category
    cb_image = PhotoImage(file='cb.png')  
    cb_image = cb_image.subsample(25)
    btn_cb = ctk.CTkButton(root2, text='Check Balance', image=cb_image, compound='top', font=("Arial", 21), command=check_balance, width=20, fg_color='transparent', bg_color='green', border_width=2, height=5)
    btn_cb.place(x=20, y=240)


    mt_image=PhotoImage(file='mt.png')
    mt_image = mt_image.subsample(25)
    btn_mt = ctk.CTkButton(root2, image=mt_image, text=' Money Transfer ', compound='top',font=("Arial", 21),command=money_transfer,width=20,fg_color='green',bg_color='white',border_width=2, height=4)
    btn_mt.place(x=225, y=240)


    dm_image = PhotoImage(file='dm.png')
    dm_image = dm_image.subsample(25)
    btn_dm = ctk.CTkButton(root2, text=' Debit  Money  ', image=dm_image, compound='top', font=("Arial", 21), command=debit_money, width=15, fg_color='red', bg_color='white', border_width=2, height=5)
    btn_dm.place(x=20, y=410)

    cm_image = PhotoImage(file='cm.png')
    cm_image = cm_image.subsample(25)
    btn_cm = ctk.CTkButton(root2, text='  Credit  Money  ', image=cm_image, compound='top', font=("Arial", 21), command=credit_money, width=15, fg_color='red', bg_color='white', border_width=2, height=5)
    btn_cm.place(x=225, y=410)

    ad_image = PhotoImage(file='ad.png')
    ad_image = ad_image.subsample(25)
    btn_ad = ctk.CTkButton(root2, text='Card  Request', image=ad_image, compound='top', font=("Arial", 21), command=apply_for_debit_card, width=30, fg_color='green', bg_color='white', border_width=2, height=5)
    btn_ad.place(x=430, y=240)

    ea_image = PhotoImage(file='ea.png')
    ea_image = ea_image.subsample(25)
    btn_ea = ctk.CTkButton(root2, text='Message Alert ', image=ea_image, compound='top', font=("Arial", 22), command=email_alert_button, width=15, fg_color='green', bg_color='white', border_width=2, height=5)
    btn_ea.place(x=620, y=240)

    lo_image = PhotoImage(file='lo.png')
    lo_image = lo_image.subsample(25)
    btn_lo = ctk.CTkButton(root2, text=' End Session', image=lo_image, compound='top', font=("Arial", 22), command=log_out, width=15, fg_color='red', bg_color='white', border_width=2, height=5)
    btn_lo.place(x=430, y=410)

    calculator_image = PhotoImage(file='calculator.png')
    calculator_image = calculator_image.subsample(25)
    btn_calculator = ctk.CTkButton(root2, text='Calculator App', image=calculator_image, compound='top', font=("Arial", 22), command=calwin, width=15, fg_color='red', bg_color='white', border_width=2, height=5)
    btn_calculator.place(x=620, y=410)


    terms_and_conditions = """
    Bank Management System Project - Terms and Conditions

    1. Project Overview:

       - This project, titled "Bank Management System," is a fictional/academic exercise created solely for educational and demonstration purposes.

    2. Scope:

       - The project scope is limited to the creation of a simulated bank management system with predefined functionalities.
       - The project does not involve real banking operations or transactions.

    3. Educational Use:

       - The project is intended for educational and training purposes only.
       - Any resemblance to real-world financial systems or institutions is purely coincidental.

    4. Data and Privacy:

       - All data used in this project is fictional and does not represent real customer information.
       - No personal or sensitive data is collected or stored.

    5. Intellectual Property:

       - All project assets, including code, documentation, and design, are created for educational purposes and do not hold any commercial value.
       - All intellectual property rights remain with the project creators.

    6. Liability:

       - The project creators are not liable for any consequences or actions resulting from the use of this fictional bank management system.

    7. Usage Restrictions:

       - This project should not be used for any illegal, unethical, or commercial purposes.
       - Users are expected to abide by all relevant laws and ethical guidelines.

    8. Support and Maintenance:

       - The project creators do not provide support or maintenance for this project beyond its educational objectives.

    9. Disclaimer:

       - This project is a simulation and should not be considered a substitute for real-world financial systems or practices.

    10. Acknowledgment:

        - Users of this project acknowledge that it is a fictional/academic exercise and agree to use it responsibly and ethically.

    11. Governing Law:

        - Any legal matters related to this project are subject to the laws of the jurisdiction where the project is hosted or accessed.
    """

   
    
    
    info_lab=ctk.CTkLabel(f2,text=terms_and_conditions, justify="left",anchor="w",  padx=5,wraplength=480, pady=5, font=("Arial", 15))
    info_lab.pack()

    root2.mainloop()


    





   
    
   


 
  


  







    

     


# --------------------------------------------------------------------------------customer----------------------------------------------------------------




def send_otp(receiver_email, otp):
    smtp_server = "smtp.gmail.com"  
    smtp_port = 587  
    sender_email = "painumbank@gmail.com"  
    sender_password = "gkbu kjqb qcar hqky" 

    subject = "OTP Verification"
    body = f"Your OTP is: {otp}"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

        return True
    except Exception as e:
        print("Error sending email:", str(e))
        return False



def get_and_send_otp():
    receiver_email = gmail_entry.get()

    if receiver_email == '':
        text_label.config(text="⚠Please fill your registered Gmail account⚠")
    else:
        global otp_value
        otp_value = str(random.randint(1000, 9999))
        print(otp_value)
        sent_successfully = send_otp(receiver_email, otp_value)

        if sent_successfully:
            text_label.config(text="OTP successfully sent to your Gmail✔️")
        else:
            text_label.config(text="⚠Failed to send OTP. Check your email settings⚠")

        otp_entry.delete(0, 'end')  # Clear the OTP entry field




def validate_otp_and_login():
    global user_id
    user_id = user_entry.get()  # Get User ID from the entry field
    password = password_entry.get()  # Get Password from the entry field
    entered_otp = otp_entry.get()
     
    try:
        
        connection = mysql.connector.connect(host='localhost',user='root',password='Qwertyios123@',database='bank')
        cursor = connection.cursor()

        # Query 
        query = "SELECT * FROM test2 WHERE User_ID = %s AND Password = %s"
        cursor.execute(query, (user_id, password))
        global user
        user = cursor.fetchone()

        if user:
            if entered_otp == otp_value:
                text_label.config(text="Login successful. Welcome, " + user[2]) 
                win2()
                
                
                
            else:
                text_label.config(text="⚠ Incorrect OTP ⚠") 
        else:
            text_label.config(text="⚠ Login failed. Please check your User ID, Password, and OTP. ⚠") 
    except mysql.connector.Error as e:
        print("Error:", str(e))
        text_label.config(text="⚠ Database Error. Please try again later. ⚠")  

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()





def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def cus():
    clear_frame(f1)
    global user_entry, password_entry, otp_entry, text_label
    customer_login = tk.Label(f1, text="Customer Login", bg='light blue', font=("Times New Roman", '20'))
    customer_login.place(x=140, y=5)

    user = Label(f1, text="User ID  ", bg='light blue', fg='black', font=('Arial', 15))
    user.place(x=10, y=60)
    
    global user_entry
    user_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    user_entry.place(x=150, y=60)

    password_label = Label(f1, text="Password  ", bg='light blue', fg='black', font=('Arial', 15))
    password_label.place(x=10, y=100)
    
    global password_entry
    password_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15), show='*')
    password_entry.place(x=150, y=100)

    gmail_label = Label(f1, text="Gmail  ", bg='light blue', fg='black', font=('Arial', 15))
    gmail_label.place(x=10, y=140)

    global gmail_entry
    gmail_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    gmail_entry.place(x=150, y=140)

    otp_button = Button(f1, text="Get OTP", bg='blue', fg='white', relief='groove', font=('arial', '12'), width=10,
                        command=get_and_send_otp)
    otp_button.place(x=150, y=180)

    otp_label = Label(f1, text="Enter OTP  ", bg='light blue', fg='black', font=('Arial', 15))
    otp_label.place(x=10, y=225)

    global otp_entry
    otp_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    otp_entry.place(x=150, y=225)

    submit_button = Button(f1, text="Submit", bg='green', fg='white', relief='groove', font=('arial', '12', 'bold'),
                           width=10, command=validate_otp_and_login)
    submit_button.place(x=270, y=270)

    global text_label
    text_label = Label(f1, text="", bg='light blue', fg='red', font=('Arial', 15))
    text_label.place(x=10, y=350)


# -----------------------------------------------------------------admin--------------------------------------------------------------------------    

def send_otp1(receiver_email, otp):
    smtp_server1 = "smtp.gmail.com"  
    smtp_port1 = 587  
    sender_email1 = "painumbank@gmail.com"  
    sender_password1 = "gkbu kjqb qcar hqky"  

    subject1 = "OTP Verification"
    body1 = f"Your OTP is: {otp}"

    try:
        server1 = smtplib.SMTP(smtp_server1, smtp_port1)
        server1.starttls()
        server1.login(sender_email1, sender_password1)

        message1 = f"Subject: {subject1}\n\n{body1}"
        server1.sendmail(sender_email1, receiver_email, message1)
        server1.quit()

        return True
    except Exception as e:
        print("Error sending email:", str(e))
        return False


def get_and_send_otp1():
    receiver_email1 = gmail_entry1.get()

    if receiver_email1 == '':
        text_label1.config(text="⚠Please fill your registered Gmail account⚠")
    else:
        global otp_value1
        otp_value1 = str(random.randint(1000, 9999))
        sent_successfully1 = send_otp1(receiver_email1, otp_value1)

        if sent_successfully1:
            text_label1.config(text="OTP successfully sent to your Gmail✔️")
        else:
            text_label1.config(text="⚠Failed to send OTP. Check your email settings⚠")

        otp_entry1.delete(0, 'end')  # Clear the OTP entry field


def validate_otp_and_login1():
    entered_admin = admin_entry.get()  
    entered_password = password_entry1.get()  
    entered_otp1 = otp_entry1.get()

    if entered_admin == "admin" and entered_password == "admin123":
        if entered_otp1 == otp_value1:
            text_label1.config(text="Login successful. Welcome, Admin")
            win3()
        else:
            text_label1.config(text="⚠ Incorrect OTP ⚠")
    else:
        text_label1.config(text="⚠ Login failed. Please check your admin ID, Password, and OTP. ⚠")

    
        
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def ad1():
    clear_frame1(f1)
    global admin_entry, password_entry1, otp_entry1, text_label1
    Admin_login1 = tk.Label(f1, text="Admin Login", bg='light blue', font=("Times New Roman", '20'))
    Admin_login1.place(x=140, y=5)

    admin = Label(f1, text="Admin ID  ", bg='light blue', fg='black', font=('Arial', 15))
    admin.place(x=10, y=60)

    global admin_entry
    admin_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    admin_entry.place(x=150, y=60)

    password_label1 = Label(f1, text="Password  ", bg='light blue', fg='black', font=('Arial', 15))
    password_label1.place(x=10, y=100)

    global password_entry1
    password_entry1 = Entry(f1, bg='white', fg='black', font=('Arial', 15), show='*')
    password_entry1.place(x=150, y=100)

    gmail_label1 = Label(f1, text="Gmail  ", bg='light blue', fg='black', font=('Arial', 15))
    gmail_label1.place(x=10, y=140)

    global gmail_entry1
    gmail_entry1 = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    gmail_entry1.place(x=150, y=140)

    otp_button1 = Button(f1, text="Get OTP", bg='blue', fg='white', relief='groove', font=('arial', '12'), width=10,
                         command=get_and_send_otp1)
    otp_button1.place(x=150, y=180)

    otp_label1 = Label(f1, text="Enter OTP  ", bg='light blue', fg='black', font=('Arial', 15))
    otp_label1.place(x=10, y=225)

    global otp_entry1
    otp_entry1 = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    otp_entry1.place(x=150, y=225)

    submit_button1 = Button(f1, text="Submit", bg='green', fg='white', relief='groove', font=('arial', '12', 'bold'),
                            width=10, command=validate_otp_and_login1)
    submit_button1.place(x=270, y=270)

    global text_label1
    text_label1 = Label(f1, text="", bg='light blue', fg='red', font=('Arial', 15))
    text_label1.place(x=10, y=350)


def clear_frame1(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# -----------------------------------------------buttons-----------------------------------------------------------------------
admin = Button(root, text='Admin Login', bg='RED', fg='white',relief='groove', font=('arial', '15', 'bold'), width=15,command=ad1)
admin.place(x=70, y=295)

customer = Button(root, text='Customer Login', bg='RED', fg='white',relief='groove', font=('arial', '15', 'bold'), width=15,command=cus)
customer.place(x=330, y=295)

new_account = Button(root, text='New Account', bg='blue', fg='white',relief='groove', font=('arial', '15', 'bold'), width=15)
new_account.place(x=70, y=495)



# ----------------------------------------------------------currency convertor------------------------------------------------------------------------

def convert():
    from_currency = from_currency_combo.get()
    to_currency = to_currency_combo.get()
    amount = amount_entry.get()
    
    if from_currency == "" or to_currency == "":
        result_label.config(text='Select both "From Currency" and "To Currency".')
    elif amount == "":
        result_label.config(text='Enter an amount to convert.')
    else:
        amount = float(amount)
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        if exchange_rate !='':
            converted_amount = amount * exchange_rate
            result_label.config(text=f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')
        else:
            result_label.config(text="Currency conversion failed.")

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data.get("rates", {}).get(to_currency)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def cur():
    clear_frame(f1)
    global from_currency_combo,to_currency_combo,amount_entry,result_label
    title_label = tk.Label(f1, text="Currency Converter", bg='LightGray', font=("Arial", 16, "bold"))
    title_label.place(x=100, y=10)

    from_currency_label = tk.Label(f1, text="From Currency:", bg='LightGray', font=("Arial", 12))
    from_currency_label.place(x=20, y=50)

    from_currency_combo = ttk.Combobox(f1, values=["USD", "EUR", "KRW", "JPY", "CAD", "INR"], state='readonly')
    from_currency_combo.place(x=180, y=50)

    to_currency_label = tk.Label(f1, text="To Currency:", bg='LightGray', font=("Arial", 12))
    to_currency_label.place(x=20, y=90)

    to_currency_combo = ttk.Combobox(f1, values=["USD", "EUR", "KRW", "JPY", "CAD", "INR"], state='readonly')
    to_currency_combo.place(x=180, y=90)

    amount_label = tk.Label(f1, text="Amount:", bg='LightGray', font=("Arial", 12))
    amount_label.place(x=20, y=130)

    amount_entry = tk.Entry(f1)
    amount_entry.place(x=180, y=130)

    convert_button = tk.Button(f1, text="Convert", command=convert, bg='Green', fg='white', font=("Arial", 12))
    convert_button.place(x=180, y=170)

    result_label = tk.Label(f1, text="", bg='LightGray', font=("Arial", 12))
    result_label.place(x=20, y=210, width=400)

currency = Button(root, text='Currency Converter', bg='blue', fg='white',relief='groove', font=('arial', '15', 'bold'), width=15,command=cur)
currency.place(x=330, y=495)


# ------------------------------------------------------------new account--------------------------------------------------------------------------------
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
def create():
    clear_frame(f1)
    global full_name_entry,address_entry,contact_entry,email_entry,gendervar, aadhar_entry ,password_entry ,account_type_var,agree_var,result_label
    create_label = Label(f1, text="Create New Account", bg='light blue', font=("Times New Roman", '20'))
    create_label.place(x=50, y=5)

    full_name_label = Label(f1, text="Full Name:", bg='light blue', fg='black', font=('Arial', 15))
    full_name_label.place(x=10, y=60)

    full_name_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    full_name_entry.place(x=200, y=60)

    address_label = Label(f1, text="Address:", bg='light blue', fg='black', font=('Arial', 15))
    address_label.place(x=10, y=100)

    address_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    address_entry.place(x=200, y=100)

    contact_label = Label(f1, text="Contact No:", bg='light blue', fg='black', font=('Arial', 15))
    contact_label.place(x=10, y=140)

    contact_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    contact_entry.place(x=200, y=140)

    email_label = Label(f1, text="Email Address:", bg='light blue', fg='black', font=('Arial', 15))
    email_label.place(x=10, y=180)

    email_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    email_entry.place(x=200, y=180)

    gender_label = Label(f1, text="Gender:", bg='light blue', fg='black', font=('Arial', 15))
    gender_label.place(x=10, y=220)
    
    gendervar=StringVar()
    gendervar.set("none") 
    gender=Radiobutton(f1,text='Male',bg='sky blue',font=('arial','13'),variable=gendervar,value="Male").place(x=200,y=220)
    gender=Radiobutton(f1,text='Female',bg='sky blue',font=('arial','13'),variable=gendervar,value="Female").place(x=300,y=220)
    gender=Radiobutton(f1,text='Other',bg='sky blue',font=('arial','13'),variable=gendervar,value='Other').place(x=400,y=220)

    

    aadhar_label = Label(f1, text="Aadhar No:", bg='light blue', fg='black', font=('Arial', 15))
    aadhar_label.place(x=10, y=260)

    aadhar_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15))
    aadhar_entry.place(x=200, y=260)

    password_label = Label(f1, text="Create Password:", bg='light blue', fg='black', font=('Arial', 15))
    password_label.place(x=10, y=300)

    password_entry = Entry(f1, bg='white', fg='black', font=('Arial', 15), show='*')
    password_entry.place(x=200, y=300)

    account_type_label = Label(f1, text="Account Type:", bg='light blue', fg='black', font=('Arial', 15))
    account_type_label.place(x=10, y=340)

    account_type_var = StringVar()
    account_type_combo = ttk.Combobox(f1, textvariable=account_type_var, values=["Savings", "Current"], state='readonly', font=('Arial', 15))
    account_type_combo.place(x=200, y=340)
    
    agree_var = IntVar()
    agree_var.set(0)  
    agree_checkbox = Checkbutton(f1, variable=agree_var, text="I agree to all terms and conditions", bg='light blue', font=('Arial', 12))
    agree_checkbox.place(x=10, y=380)

    submit_button = Button(f1, text="Submit", bg='green', fg='white', relief='groove', font=('arial', '12', 'bold'), width=7,command=submit)
    submit_button.place(x=200, y=420)
    
    result_label = Label(f1, text="", bg='light blue', fg='red', font=('Arial', 15))
    result_label.place(x=10, y=460)


def submit():
    if full_name_entry.get() == "" or address_entry.get() == "" or contact_entry.get() == "" or email_entry.get() == "" or aadhar_entry.get() == "" or password_entry.get() == "" or gendervar.get() == "none":
        result_label.config(text="⚠ All fields are mandatory to fill ⚠")
    elif len(contact_entry.get()) != 10:
        result_label.config(text="⚠ Contact number must be a 10 digits number ⚠")
    elif agree_var.get() == 0:  
        result_label.config(text="⚠ Please agree to all terms and conditions ⚠")
    elif len(aadhar_entry.get()) != 12: 
        result_label.config(text="⚠ Aadhar number must have 12 digits ⚠")
    elif account_type_var.get() == "":
        result_label.config(text="⚠ Please select an account type ⚠")
    else:
        lol = mysql.connector.connect(host='localhost', user='root', password='Qwertyios123@', database='bank')
        cur = lol.cursor()
        insert_query = """INSERT INTO new_account (full_name, address, contact_no, email_address, gender, aadhar_no, password, account_type)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        data = (full_name_entry.get(), address_entry.get(), contact_entry.get(),
                email_entry.get(), gendervar.get(), aadhar_entry.get(), 
                password_entry.get(), account_type_var.get())
        cur.execute(insert_query, data)
        lol.commit()
        lol.close()
        result_label.config(text="Form submitted successfully!\nYour account will be created within 48 hours ") 


    
new_account = Button(root, text='New Account', bg='blue', fg='white',relief='groove', font=('arial', '15', 'bold'), width=15,command=create)
new_account.place(x=70, y=495)


# --------------------------------------------------------close--------------------------------------------------------------------

root.mainloop()
    


    
