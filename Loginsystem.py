import pyodbc
import os
import getpass



user_login = False


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')


def get_login_info():

    user_id = input('Enter user Name > ')
    user_pass = getpass.getpass('Enter Password > ')
    return user_id, user_pass


def menu():
    clear_screen()
    print('''
    -------------------------+
    {1} - LOGIN              |
    {2} - Register           |
    {3} - Remove users       |
    {4} - Search for user    |
    {5} - Quite              |
    -------------------------+
    ''')


def get_menu_input():
    p_input = int(input("Select From 1-10 \n>"))
    if p_input == 1:
        login(my_db_cursor)
    elif p_input == 2:
        register(my_db_cursor)
    elif p_input == 5:
        exit()
    else:
        print('wrong Selection Please select again')
        exit()


def login(my_db_cursor):
    clear_screen()
    print('+--------------------+')
    print('|        LOGIN       |')
    print('+--------------------+')
    found_user = False
    found_password = False
    userName, userPassword = get_login_info()
    isExecuted = my_db_cursor.execute(
        'select userName from dbo.userinfo;'
    )
    if isExecuted:
        row = my_db_cursor.fetchall()
        for x in row:
            if x[0] == userName:
                found_user = True
    isExecuted = my_db_cursor.execute(
        'select userPassword from dbo.userinfo;'
    )
    if isExecuted:
        row = my_db_cursor.fetchall()
        for x in row:
            if x[0] == userPassword:
                found_password = True
    if found_password and found_user:
        clear_screen()
        print('welcome you are loged in!')
        wait = input('Press Enter')
    if not found_user and not found_password:
        print('username or password is incorrect\nif you are not'
              'Register here\nplease register first')
        wait = input('press y for Registration or q or quite :')



def register(my_db_cursor):
    clear_screen()
    print('+-----------------------+')
    print('|        Register       |')
    print('+-----------------------+')

    userName, userPassword = get_login_info()
    isExecuted = my_db_cursor.execute(
        'insert into users.dbo.userinfo(userName,userPassword) values(?,?);',
        (userName, userPassword)
        )
    if isExecuted:
        print('You are Registered successfully\nPlease login')
        my_db_cursor.commit()
        wait = input('press any key to to login')
        clear_screen()



my_db = pyodbc.connect(
    r"Driver={SQL Server};"
    r"Server=DESKTOP-R4D63H8\SQLEXPRESS;"
    r"Database=users;"
    r"Trusted_Connection=yes;"
)


my_db_cursor = my_db.cursor()
while True:
    menu()
    get_menu_input()
