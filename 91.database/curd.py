from mysql.connector import connect

# host, user, password, port, database

connection = connect(
    host="127.0.0.1", user="root", password="Aug2023", database="movie_db"
)

cursor = connection.cursor()

# query = 'CREATE TABLE employee(ID INT PRIMARY KEY, First_Name VARCHAR(20), Last_Name VARCHAR(20), Salary INT, Email_Id VARCHAR(40))'

# query= 'INSERT INTO employee(ID, First_Name, Last_Name, Salary, Email_Id) VALUES(1, "Neeta", "Korade", 59000, "neetak12@gmail.com"), (2, "Sushma", "Singh", 62000, "sushsingh67@gmail.com"), (3, "Kavita", "Rathod", 27000, "kavitar09@gmail.com"), (4, "Mrunalini", "Deshmukh", 88000, "mrunald78@gmail.com"), (5, "Swati", "Patel", 34000, "swatip67@gmail.com"), (6, "Laxmi", "Kadam", 44000, "laxmik14@gmail.com"), (7, "Lalita", "Shah", 66000, "lalita45@gmail.com"), (8, "Savita", "Kulkarni", 31000, "savitak56@gmail.com"), (9, "Shravani", "Jaiswal", 38000, "shravanij39@gmail.com"), (10, "Shweta", "Wagh", 20000, "shwetaw03@gmail.com");'

# query = '  SELECT *FROM employee WHERE Salary > 35000;  '

# query = ' UPDATE employee SET Last_Name = "Bose" WHERE ID = 6;  '

query = " DELETE FROM employee;  "

cursor.execute(query)

connection.commit()

result = cursor.fetchall()

for res in result:
    print(res)

print("connected successfully!!!!!!")

# fetchone -> one record
# fetchmany(n) --> n=2, n=5, n=10
# fetchall() --> all the records.
