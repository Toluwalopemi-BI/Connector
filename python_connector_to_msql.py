import mysql.connector

conn=mysql.connector.connect(host='localhost', username='Tolu',password='Geosciences1985.')

from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import Error

cursor = conn.cursor()

try:
    cursor.execute("CREATE DATABASE little_lemon_Tl")
except:
    cursor.execute("DROP DATABASE little_lemon_Tl")
    cursor.execute("CREATE DATABASE little_lemon_Tl")

cursor.execute("USE little_lemon_Tl")


# The SQL query for the MenuItems table is: 
create_menuitem_table="""
CREATE TABLE MenuItems (
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY (ItemID)
);"""

# Create MenuItems table
cursor.execute(create_menuitem_table)
print("MenuItems table is created.\n")

insert_menuitems="""
INSERT INTO MenuItems (ItemID, Name, Type, Price)
VALUES
(1,'Olives','Starters',5),
(2,'Flatbread','Starters', 5),
(3, 'Minestrone', 'Starters', 8),
(4, 'Tomato bread','Starters', 8),
(5, 'Falafel', 'Starters', 7),
(6, 'Hummus', 'Starters', 5),
(7, 'Greek salad', 'Main Courses', 15),
(8, 'Bean soup', 'Main Courses', 12),
(9, 'Pizza', 'Main Courses', 15),
(10,'Greek yoghurt','Desserts', 7),
(11, 'Ice cream', 'Desserts', 6),
(12, 'Cheesecake', 'Desserts', 4),
(13, 'Athens White wine', 'Drinks', 25),
(14, 'Corfu Red Wine', 'Drinks', 30),
(15, 'Turkish Coffee', 'Drinks', 10),
(16, 'Turkish Coffee', 'Drinks', 10),
(17, 'Kabasa', 'Main Courses', 17);"""

print("Inserting data in MenuItems table.")
# Populate MenuItems table
cursor.execute(insert_menuitems)
print("Total number of rows in MenuItem table: {}\n".format(cursor.rowcount))
# Once the query is executed,  commit the change to the database 
conn.commit()

create_menu_table="""
CREATE TABLE Menus (
MenuID INT,
ItemID INT,
Cuisine VARCHAR(100),
PRIMARY KEY (MenuID, ItemID)
);"""

# Create Menus table
cursor.execute(create_menu_table)
print("Menu table is created.\n")

insert_menus="""
INSERT INTO Menus (MenuID, ItemID, Cuisine)
VALUES
(1, 1, 'Greek'),
(1, 7, 'Greek'),
(1, 10, 'Greek'),
(1, 13, 'Greek'),
(2, 3, 'Italian'),
(2, 9, 'Italian'),
(2, 12, 'Italian'),
(2, 15, 'Italian'),
(3, 5, 'Turkish'),
(3, 17, 'Turkish'),
(3, 11, 'Turkish'),
(3, 16, 'Turkish');"""

print("Inserting data in Menus table.")
# Populate Menus table
cursor.execute(insert_menus)
print("Total number of rows in Menu table: {}\n".format(cursor.rowcount))
conn.commit()

create_booking_table="""
CREATE TABLE Bookings (
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY (BookingID)
);"""

# Create Bookings table
cursor.execute(create_booking_table)
print("Bookings table is created.\n")

insert_bookings="""
INSERT INTO Bookings (BookingID, TableNo, GuestFirstName, 
GuestLastName, BookingSlot, EmployeeID)
VALUES
(1,12,'Anna','Iversen','19:00:00',1),
(2, 12, 'Joakim', 'Iversen', '19:00:00', 1),
(3, 19, 'Vanessa', 'McCarthy', '15:00:00', 3),
(4, 15, 'Marcos', 'Romero', '17:30:00', 4),
(5, 5, 'Hiroki', 'Yamane', '18:30:00', 2),
(6, 8, 'Diana', 'Pinto', '20:00:00', 5);"""

print("Inserting data in Bookings table.")
# Populate Bookings table
cursor.execute(insert_bookings)
print("Total number of rows in Bookings table: {}\n".format(cursor.rowcount))
conn.commit()

create_orders_table="""
CREATE TABLE Orders (
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY (OrderID,TableNo)
);"""

# Create Orders table
cursor.execute(create_orders_table)
print("Orders table is created.\n")

insert_orders="""
INSERT INTO Orders (OrderID, TableNo, MenuID, BookingID, Quantity, BillAmount)
VALUES
(1, 12, 1, 1, 2, 86),
(2, 19, 2, 2, 1, 37),
(3, 15, 2, 3, 1, 37),
(4, 5, 3, 4, 1, 40),
(5, 8, 1, 5, 1, 43);"""

print("Inserting data in Orders table.")
# Populate Orders table
cursor.execute(insert_orders)
print("Total number of rows in Orders table: {}\n".format(cursor.rowcount))
conn.commit()

create_employees_table="""
CREATE TABLE Employees (
EmployeeID INT AUTO_INCREMENT,
Name VARCHAR(200),
Role VARCHAR(100),
Address VARCHAR(200),
Contact_Number INT,
Email VARCHAR(100),
Annual_Salary VARCHAR(100),
PRIMARY KEY (EmployeeID)
);"""

# Create Employees table
cursor.execute(create_employees_table)

insert_employees="""
INSERT INTO Employees (EmployeeID, Name, Role, Address, Contact_Number, Email, Annual_Salary)
VALUES
(01,'Mario Gollini','Manager','724, Parsley Lane, Old Town, Chicago, IL',351258074,'Mario.g@littlelemon.com','$70,000'),
(02,'Adrian Gollini','Assistant Manager','334, Dill Square, Lincoln Park, Chicago, IL',351474048,'Adrian.g@littlelemon.com','$65,000'),
(03,'Giorgos Dioudis','Head Chef','879 Sage Street, West Loop, Chicago, IL',351970582,'Giorgos.d@littlelemon.com','$50,000'),
(04,'Fatma Kaya','Assistant Chef','132  Bay Lane, Chicago, IL',351963569,'Fatma.k@littlelemon.com','$45,000'),
(05,'Elena Salvai','Head Waiter','989 Thyme Square, EdgeWater, Chicago, IL',351074198,'Elena.s@littlelemon.com','$40,000'),
(06,'John Millar','Receptionist','245 Dill Square, Lincoln Park, Chicago, IL',351584508,'John.m@littlelemon.com','$35,000');"""


print("Inserting data in the Employees table.")
# Populate Employees table
cursor.execute(insert_employees)
print("Total number of rows in the Employees table: ", cursor.rowcount)
# Once the query is executed, you can commit the change to the database 
conn.commit()

from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import Error

dbconfig = {
    "database":"little_lemon_tl",
    "user" : "Tolu",
    "password" : "Geosciences1985."
}

try:
    pool = MySQLConnectionPool(pool_name = "pool_a",
                           pool_size = 2, #default is 5
                           **dbconfig)
    print("The connection pool is created with a name: ",pool.pool_name)
    print("The pool size is:",pool.pool_size)

except Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)

    conn = pool.get_connection()
cursor = conn.cursor()

cursor.execute("DROP PROCEDURE IF EXISTS PeakHours;")
stored_procedure_peakhours_query="""
CREATE PROCEDURE PeakHours()
BEGIN
    SELECT 
    HOUR(BookingSlot) AS booking_hour,
    COUNT(HOUR(BookingSlot)) AS n_bookings
    FROM Bookings
    GROUP BY booking_hour
    ORDER BY n_bookings DESC;
END
"""
cursor.execute(stored_procedure_peakhours_query)

cursor.callproc("PeakHours")
results = next(cursor.stored_results() )
dataset = results.fetchall()
#retrieve column
for column_id in cursor.stored_results():
    columns = [column[0] for column in column_id.description]

print(columns)
for data in dataset:
    print(data)

stored_procedure_gueststatus_query="""
CREATE PROCEDURE GuestStatus()
BEGIN
SELECT 

    Bookings.BookingID AS OrderNumber,  
    CONCAT(GuestFirstName,' ',GuestLastName) AS GuestName, 
    Role AS Employee, 
    CASE 
        WHEN Role IN ('Manager','Assistant Manager') THEN "Ready to Pay"
        WHEN Role = 'Head Chef' THEN "Ready to serve"
        WHEN Role = 'Assistant Chef' THEN "Preparing order"
        WHEN Role = 'Head Waiter' THEN "Order served"
    ELSE "Pending"
    END AS Status
    FROM Bookings 
        LEFT JOIN 
        Employees 
        ON Employees.EmployeeID=Bookings.EmployeeID;
END
"""
cursor.execute(stored_procedure_gueststatus_query)

cursor.callproc("GuestStatus")
results = next(cursor.stored_results())
dataset = results.fetchall()

# Retrieve column 
for column_id in cursor.stored_results():
    columns = [column[0] for column in column_id.description]

print(columns)
for data in dataset:
    print(data)
    
conn.close()