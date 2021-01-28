from db import db, cursor, Error
try:
    sql_select_Query = "select * from AAA ORDER BY NGAY DESC LIMIT 7"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)
    print("+---------------------------------------------+")
    print("| NGAY        | GIA DIEU CHINH | GIA DONG CUA |")
    for row in records:
        print("|",row[0]," "*(9-len(str(row[0]))),
              "|",row[1]," "*(13-len(str(row[1]))),
             "|",row[2]," "*(11-len(str(row[2]))),"|")
    print("+---------------------------------------------+")
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (db.is_connected()):
        cursor.close()
        db.close()
        print("MySQL connection is closed !")