import psycopg2

# PostgreSQL serveriga bog'lanish sozlamalari
def save_vacancy(name, link):

    connection_params = {
        "host": "164.92.168.96",
        "port": "5432",
        "database": "opendata",
        "user": "opendata",
        "password": "opendata"
    }

    # PostgreSQL serveriga bog'lanish
    connection = psycopg2.connect(**connection_params)

    # Ma'lumotlar omboriga bog'langan obyektni olish
    cursor = connection.cursor()

    # SQL so'rovni yozish
    insert_query = "INSERT INTO user_vacancy (name,  link) VALUES (%s, %s)"

    # Ma'lumotlar
    data_to_insert = (name,  link)

    # SQL so'rovdan foydalanib ma'lumot qo'shish
    cursor.execute(insert_query, data_to_insert)

    # Ma'lumotlar omboriga o'zgartirishlarni saqlash
    connection.commit()

    # Bog'lanishni yopish
    cursor.close()
    connection.close()
