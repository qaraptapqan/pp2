import psycopg2
import csv

# Подключение к базе данных PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="pp2",  # Твоя база данных
        user="www",  # Имя пользователя
        password="12345",  # Твой пароль
        host="localhost"
    )
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error connecting to the database:", e)
    exit()

# Функция для добавления нового контакта
def add_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    try:
        cur.execute("INSERT INTO phonebook (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)", 
                    (first_name, last_name, phone, email))
        conn.commit()
        print("Contact saved!")
    except psycopg2.Error as e:
        print(f"Error inserting contact: {e}")
        conn.rollback()

# Функция для отображения всех контактов
def show_all():
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)

# Функция для обновления контакта (по имени)
def update_user():
    first_name = input("Whose phone to update: ")
    last_name = input("Enter last name: ")
    new_phone = input("New phone: ")
    try:
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s AND last_name = %s", 
                    (new_phone, first_name, last_name))
        conn.commit()
        print("Phone updated!")
    except psycopg2.Error as e:
        print(f"Error updating contact: {e}")
        conn.rollback()

# Функция для удаления контакта (по имени)
def delete_user():
    first_name = input("Who to delete: ")
    last_name = input("Enter last name: ")
    try:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s AND last_name = %s", 
                    (first_name, last_name))
        conn.commit()
        print("Contact deleted!")
    except psycopg2.Error as e:
        print(f"Error deleting contact: {e}")
        conn.rollback()

# Функция для загрузки данных из CSV файла
def load_from_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)  # Используем DictReader для удобной работы с заголовками
            for row in reader:
                first_name = row.get('first_name')
                last_name = row.get('last_name')
                phone = row.get('phone')
                email = row.get('email')
                if first_name and last_name and phone and email:  # Проверяем, что все данные присутствуют
                    cur.execute("""
                        INSERT INTO phonebook (first_name, last_name, phone, email)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (phone) DO NOTHING
                    """, (first_name, last_name, phone, email))
            conn.commit()
        print("Data loaded from CSV!")
    except Exception as e:
        print(f"Error loading data from CSV: {e}")

# Функция для поиска по паттерну
def search_by_pattern(pattern):
    try:
        cur.execute("""
            SELECT first_name, last_name, phone, email 
            FROM phonebook 
            WHERE first_name LIKE %s OR last_name LIKE %s OR phone LIKE %s OR email LIKE %s
        """, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
        for row in cur.fetchall():
            print(row)
    except Exception as e:
        print(f"Error in search_pattern: {e}")

# Функция для постраничного вывода
def show_paginated(limit_count, offset_count):
    try:
        cur.execute("""
            SELECT first_name, last_name, phone, email 
            FROM phonebook
            LIMIT %s OFFSET %s
        """, (limit_count, offset_count))
        for row in cur.fetchall():
            print(row)
    except Exception as e:
        print(f"Error in show_paginated: {e}")

# Функция для удаления контакта по имени или телефону
def delete_user_by_name_or_phone(identifier):
    try:
        cur.execute("""
            DELETE FROM phonebook 
            WHERE first_name = %s OR phone = %s
        """, (identifier, identifier))
        conn.commit()
        print("User deleted successfully!")
    except Exception as e:
        print(f"Error in delete_user_by_name_or_phone: {e}")

# Основной цикл программы
while True:
    print("\n--- PhoneBook Menu ---")
    print("1. Add or update user")
    print("2. Load from CSV")
    print("3. Search by pattern")
    print("4. Show paginated")
    print("5. Delete user by name/phone")
    print("6. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_user()
    elif choice == '2':
        file_path = input("Enter CSV file path: ")
        load_from_csv(file_path)
    elif choice == '3':
        pattern = input("Enter pattern (name, surname, or phone part): ")
        search_by_pattern(pattern)
    elif choice == '4':
        limit_count = int(input("Enter limit: "))
        offset_count = int(input("Enter offset: "))
        show_paginated(limit_count, offset_count)
    elif choice == '5':
        identifier = input("Enter name or phone to delete: ")
        delete_user_by_name_or_phone(identifier)
    elif choice == '6':
        break
    else:
        print("Invalid choice!")

# Закрыть курсор и соединение с базой данных
cur.close()
conn.close()
