import pytest
import time
from modules.common.database import Database
import sqlite3

@pytest.mark.database
def test_database_connection():
    db= Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1,25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt [0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)
    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    #Check quantity of orders equal to 1
    assert len(orders) == 1

    #Check struture of data
    assert orders [0][0] == 1
    assert orders [0][1] == "Sergii"
    assert orders [0][2] == "солодка вода"
    assert orders [0][3] == "з цукром"

@pytest.mark.database
def test_check_customer_postalCode_more_3000():
    db = Database()
    user = db.customer_postalcode(3000)
    assert user [0][0] == "Sergii"
    

@pytest.mark.database
def test_update_user_inf():
    db = Database()
    db.new_user_info('Stepan', 'Peremohi str,3', 'Dnipro', 3999)
    user_inf = db.select_inf_user_by_name('Stepan')
    assert user_inf [0][0] == 'Peremohi str,3'
    
@pytest.mark.database
def test_insert_product():
    db = Database()
    db.insert_product(5, 'сік', 'банановий', 150)
    water_qnt = db.select_product_qnt_by_id(5)
    assert water_qnt[0][0] == 150

@pytest.mark.database
def test_no_words_in_id():
    db = Database()
    with pytest.raises(sqlite3.IntegrityError) as error:
        db.insert_no_words_in_id("сік")
    assert "datatype mismatch" in str(error)




 

