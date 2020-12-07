show_db = "SHOW DATABASES"
create_database = "CREATE DATABASE IF NOT EXISTS VALUESTOCKS"
create_table_query = """
                        CREATE TABLE IF NOT EXISTS {} (
                            NGAY DATE PRIMARY KEY,
                            GIADIEUCHINH FLOAT(5,2),
                            GIADONGCUA FLOAT(5,2)
                        )"""
drop_table_query = "DROP TABLE IF EXISTS {} "
            
insert_query = "INSERT INTO {} (NGAY, GIADIEUCHINH,GIADONGCUA) VALUES ('{}', '{}', '{}')"
