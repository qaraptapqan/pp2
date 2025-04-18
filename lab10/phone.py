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
            reader = csv.reader(file)
            next(reader)  # Пропустить заголовки
            for row in reader:
                if len(row) == 4:  # Проверка, что строка содержит ровно 4 элемента
                    cur.execute("""
                        INSERT INTO phonebook (first_name, last_name, phone, email)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (phone) DO NOTHING
                    """, (row[0], row[1], row[2], row[3]))
            conn.commit()
        print("Data loaded from CSV!")
    except Exception as e:
        print(f"Error loading data from CSV: {e}")

# Основной цикл программы
while True:
    print("\n1. Add contact\n2. Show all\n3. Update\n4. Delete\n5. Load data from CSV\n6. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_user()
    elif choice == '2':
        show_all()
    elif choice == '3':
        update_user()
    elif choice == '4':
        delete_user()
    elif choice == '5':
        file_path = input("Enter CSV file path: ")
        load_from_csv(file_path)
    elif choice == '6':
        break
    else:
        print("Invalid choice!")

# Закрыть курсор и соединение с базой данных
cur.close()
conn.close()
