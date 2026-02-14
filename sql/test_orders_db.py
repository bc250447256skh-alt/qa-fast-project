import pymysql

def test_insert_and_read_order():
    connection = pymysql.connect(
        host="localhost",
        user="qa_user",
        password="qa_pass",
        database="qa_test"
    )

    cursor = connection.cursor()

    # 🔥 CREATE TABLE IF NOT EXISTS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            job VARCHAR(100)
        )
    """)

    # Insert record
    cursor.execute(
        "INSERT INTO orders (name, job) VALUES (%s, %s)",
        ("neo", "tester")
    )

    connection.commit()

    # Read record
    cursor.execute("SELECT * FROM orders WHERE name=%s", ("neo",))
    result = cursor.fetchone()

    assert result is not None

    connection.close()

