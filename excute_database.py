import mysql.connector
from mysql.connector import Error
import os

def execute_sql_file(file_path= r'sql_script\challenges.sql', host="localhost", user="hiscryptlab_user", password="hiscryptlab123", database="HISCryptLab"):
    try:
        # Kết nối đến MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print(f"Kết nối đến MySQL server (cơ sở dữ liệu {database}) thành công!")

            # Tạo cursor để thực thi lệnh SQL
            cursor = connection.cursor()

            # Đọc nội dung file .sql
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File {file_path} không tồn tại.")

            with open(file_path, 'r', encoding='utf-8') as file:
                sql_content = file.read()

            # Thực thi nội dung SQL (có thể có nhiều lệnh, phân tách bởi ; hoặc newline)
            for statement in sql_content.split(';'):
                if statement.strip():  # Bỏ qua các dòng trống
                    try:
                        cursor.execute(statement)
                        connection.commit()
                        print(f"Thực thi lệnh SQL: {statement.strip()}")
                    except Error as e:
                        print(f"Lỗi khi thực thi lệnh: {e}")
                        connection.rollback()

            print(f"Thực thi file SQL {file_path} thành công!")

    except Error as e:
        print(f"Lỗi kết nối hoặc thực thi file SQL: {e}")

    except FileNotFoundError as e:
        print(e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Kết nối MySQL đã được đóng.")

