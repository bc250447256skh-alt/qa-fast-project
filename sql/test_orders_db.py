import pymysql

def test_insert_and_read_order():
    connection = pymysql.connect(
    host="localhost",
    user="qa_user",
    password="qa_pass",
    database="qa_test"
    )

    cursor = connection.cursor()

    # Insert record
    cursor.execute(
        "INSERT INTO orders (name, job) VALUES (%s, %s)",
        ("neo", "tester")
    )
    connection.commit()

    # Read record
    cursor.execute("SELECT name, job FROM orders WHERE name='neo'")
    result = cursor.fetchone()

    assert result[0] == "neo"
    assert result[1] == "tester"

    connection.close()
