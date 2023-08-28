
# Bank_Management_System

` This is a  Python-based Bank Management System built with Tkinter GUI allows users to manage their bank accounts, perform transactions, check balances, and more.`

## Features

- **User Registration and Authentication**: Users can create new accounts and log in securely via password and otp protected login system.

- **Currency convertor**: This program has real time Currency convertor.

- **Account Management**: Users can view their account balance,get alerts via email.

- **Transactions**: Perform various transactions such as deposits, withdrawals, and fund transfers between accounts.

- **Admin Panel**: Admin have access to create and delete users in database.



## Installation for VS code users

To run the Bank Management System project, first you need to install the following Python libraries. You can do this using `pip`, the Python package manager.Then you can simply use run command to run the code in terminal.

```bash
    pip install tkinter
    pip install Pillow
    pip install customtkinter
    pip install pygame
    pip install mysql-connector-python
    pip install requests
    pip install secure-smtplib
```

## Installation git users 


1. **Clone the Repository**:
- Open your terminal or command prompt.
- Navigate to the directory where you want to clone the repository.
- Run the following command to clone your Git repository:

```bash
git clone https://github.com/trafalgar653/BMS-.git
```
2. **Navigate to the Project Directory:**

 ```bash
 cd BMS-
 ```

3. **Install Libraries :**

 ```bash
 pip install -r requirements.txt
 ```

4. **Run the Application:** 
 ``` bash 
 python bank_management_system_localhost.py
 ```

``` bash
 python bank_management_system_remote.py
 ```
                 






 



# Versions 💻
we have two versions of BMS 
- Remote version : Use sql data from server. You can run it directly  (usually slow)

- Local host version: You have to create database to use it locally.(fast)

### *Remote version :*
It is the easy to use version but it takes time to update data because of slow server speed.
      
### *Local host version :*

Make sure to replace host ,user and password with your's

`lol = mysql.connector.connect(host='localhost', user='root', password='YOUR PASSWORD HERE', database='bank')`
- To create database and table for accounts
```python

import mysql.connector
lol=mysql.connector.connect(host='localhost',user='root',password='YOUR PASSWORD HERE')
cur=lol.cursor()
cur.execute('''CREATE DATABASE IF NOT EXISTS bank''')
print(cur)

lol=mysql.connector.connect(host='localhost', user='root', password='YOUR PASSWORD HERE', database='bank')
print('done')
cur=lol.cursor()
cur.execute("""
CREATE TABLE `test2` (
  `User_ID` VARCHAR(1024),
  Password VARCHAR(1024),
  Name VARCHAR(1024),
  `Account_number`BIGINT,
  `E-mail` VARCHAR(1024),
  Address VARCHAR(1024),
  Bank_code VARCHAR(1024),
  Last_trasaction VARCHAR(1024),
  `Current_amount` BIGINT
)""")
cur.close()
lol.close()
print("success2")```

- Insert some data into table for use
```python
 import mysql.connector

# Connect to the MySQL server
lol = mysql.connector.connect(host='localhost', user='root', password='YOUR PASSWORD HERE', database='bank')
cur = lol.cursor()

# Define the data to be inserted
data_to_insert = [
    ('user123', 'zxcvbnm', 'Ankit', 1597534565, 'None', 'Uttrakahnd', 'painum653', 'None', 20000),
    ('user124', 'asdfghjkl', 'Rahul', 9513574568, 'None', 'Dharamshala', 'painum653', 'None', 50000),
    ('user125', 'qwertyuiop', 'Mukul', 2584535745, 'None', 'Jaipur', 'painum653', 'None', 80000),
    ('user126', 'qazwsx', 'Sanya', 7894515945, 'None', 'Chandigarh', 'painum653', 'None', 90000),
    ('user127', 'mnbvcx', 'Priya', 3574869512, 'None', 'Mumbai', 'painum653', 'None', 75000),
    ('user128', 'lkjhgfdsa', 'Amit', 8521473690, 'None', 'Kolkata', 'painum653', 'None', 60000),
    ('user129', 'poiuytrewq', 'Neha', 4567890123, 'None', 'Delhi', 'painum653', 'None', 45000),
    ('user130', 'zxcvbnm', 'Rajesh', 6543217890, 'None', 'Bangalore', 'painum653', 'None', 85000),
    ('user131', 'ytrewq', 'Sara', 1234567890, 'None', 'Pune', 'painum653', 'None', 35000),
    ('user132', 'lkjhg', 'Vikram', 9876543210, 'None', 'Hyderabad', 'painum653', 'None', 95000),
    ('user133', 'bvcxz', 'Pooja', 6541237890, 'None', 'Chennai', 'painum653', 'None', 72000),
    ('user134', 'nmvbn', 'Ravi', 1478523690, 'None', 'Ahmedabad', 'painum653', 'None', 58000),
    ('user135', 'qwerty', 'Deepak', 3698521470, 'None', 'Shimla', 'painum653', 'None', 42000),
    ('user136', 'zxcvbn', 'Aarti', 7852143690, 'None', 'Kullu', 'painum653', 'None', 68000),
    ('user137', 'asdfgh', 'Sanjeev', 1236547890, 'None', 'Manali', 'painum653', 'None', 53000),
    ('user138', 'poiuyt', 'Nehal', 9856321470, 'None', 'Dharamshala', 'painum653', 'None', 77000),
    ('user139', 'mnbvcx', 'Preeti', 3698741250, 'None', 'Chamba', 'painum653', 'None', 60000),
    ('user140', 'lkjhgf', 'Suresh', 7854123690, 'None', 'Palampur', 'painum653', 'None', 45000),
    ('user141', 'ytrewq', 'Manisha', 1254789630, 'None', 'Solan', 'painum653', 'None', 59000),
    ('user142', 'nmvbnm', 'Rajeev', 9876543210, 'None', 'Mandi', 'painum653', 'None', 62000),
    ('user143', 'asdfg', 'Simran', 9871234560, 'None', 'Bilaspur', 'painum653', 'None', 51000),
    ('user144', 'zxcvb', 'Ajay', 3698521470, 'None', 'Una', 'painum653', 'None', 71000)
]




# SQL query to insert data into the table
insert_query = """
INSERT INTO test2 (User_ID, Password, Name, Account_number, `E-mail`, Address, Bank_code, `Last_trasaction`, Current_amount)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Execute the insert query for each row of data
for row in data_to_insert:
    cur.execute(insert_query, row)

# Commit the changes and close the cursor and connection
lol.commit()
cur.close()
lol.close()

print("Data inserted successfully")
```
- To create table for new account:
```python
import mysql.connector
lol=mysql.connector.connect(host='localhost',user='root',password='Qwertyios123@')
cur=lol.cursor()
print(cur)


lol=mysql.connector.connect(host='localhost', user='root', password='YOUR PASSWORD HERE', database='bank')
print('done')
cur=lol.cursor()
cur.execute('''CREATE TABLE new_account (
    full_name VARCHAR(255),
    address VARCHAR(255),
    contact_no VARCHAR(15),
    email_address VARCHAR(255),
    gender VARCHAR(10),
    aadhar_no VARCHAR(12),
    password VARCHAR(255),
    account_type VARCHAR(10)
)''')

cur.close()
lol.close()
print("success2")
```


## Admin login:
```
Admin ID -admin
Password- admin123

```

## User login:
```
User ID- user123
Password- zxcvbnm

User ID- user124
Password- asdfghjkl

```
## Bank code:
```
painum653
```

## Screenshots

![App Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtRxwhN5bidLsGGw-OHj_ErbJDKRMt1n0Tdt72a4Bct9Zqd7cFeo1Nk1T2Uh_TTYFfLh0F_5v8tabdRaQbsi6xsld009PMf3s8kwTsyFdjLjon66vTQx3qwraLOKzMZIIJlFVWsPezwRQlTpoxPirWWkMbQU12T6vBkGajz1mHrYaeg3T6QBs-NG4JDoEM/s1920/Annotation%202023-08-28%20202130.png) 

![App Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPQREjZDtrvPOkRsRYTEcFNRkf7VP2oP1gEpb7C09gj6QZPUQu2cRpRK4t_Tv2fuUKN8SqCA6CltrMQUenI9cF84jGBxgVLD7f58KIlUjRQe7X-JmXghboHXxFTt1zhM8LviDoql1-VQ5gRH8cNYZXbu0BmUUmIDyyy7njw3zJobrPGYjRTqLKuxQbL3Oa/s1920/Annotation%202023-08-28%20202908.png)

![App Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrTna3p8qUpcSs9odgbbjM3v1p0dQQAb9QEjSgO9kTNNmCcaidfKVp2_CeZku1Op6bd0LQgbaXP_Wbw0SBiX0cCLfqxR7RSqZHPYj4-1SmG4JA_D5JoY8Hyjn6_6Xeh_S4FIYjEGMf6BCqBnjzY7vxaJ2r3e05DyjoD_54WE8wziDh2ovuWAXmWrcQISKv/s1920/Annotation%202023-08-28%20203317.png)

![App Screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAYluKOG6SabWdER3qU4pdY9ewyEHDg0pqWaHnkY2DlxwV1LZeD3LxuJXHUtQtZivgHmEV5rmTmEBK8rr2SBrbnyYy0M54zEbcOa-OtKAZME9-SoSguWQ9YoxBGY6SRfARZDSDrQvWzdI93Ug0bPSIHdQPZvetpOFNw8mFu9Mjr9VlkrO4GOXkJ3h4tzle/s1918/Annotation%202023-08-28%20203117.png)



## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Demo


![Demo](https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif)

