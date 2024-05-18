import psycopg2


# username = "postgres"
# password = "python1234"
# host = "localhost"
# port = 5432

# url = r"postgresql+psycopg2://postgres:python1234@localhost:5432"
# URL = f"postgresql+psycopg2://{username}:{password}@{host}:{port}"

try:
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="python1234",
        host="localhost",
        port="5432",
    )

    cursor = conn.cursor()

    print("connection established!!!")

    # query = """CREATE TABLE PUBLISHER(
    #                 publisher_id SERIAL PRIMARY KEY,
    #                 publisher_name VARCHAR(255) NOT NULL,
    #                 publisher_estd INT,
    #                 publsiher_location VARCHAR(255),
    #                 publsiher_type VARCHAR(255)
    # )"""

    
    # insert_query = """ INSERT INTO publisher(publisher_id,
    # publisher_name, publisher_estd, publsiher_location, publsiher_type) 
    # VALUES (2, 'Mcgrahill', 1850,'Delhi', 'books')"""

    # select_Query = "select * from publisher"

    delete_query = "delete from publisher where publisher_id = 2"

    cursor.execute(delete_query)

    conn.commit()  # DML satement - insert, update, delete

    # records = cursor.fetchall() # read operation (select)

    print("record deleted!")

    conn.close()

except Exception as exce:
    print(exce)
