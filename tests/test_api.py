from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch

from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {"status": "ok"}


def test_products_mock():
    fake_conn = MagicMock()
    fake_cursor = MagicMock()

    # 配置 with conn.cursor(...) 返回 fake_cursor，供接口执行查询。
    fake_conn.cursor.return_value.__enter__.return_value = fake_cursor

    fake_products = [
        {"id": 1, "name": "Phone", "price": 3999, "stock": 50}
    ]
    # 让 fetchall() 返回预设商品，测试时无需依赖真实数据库数据。
    fake_cursor.fetchall.return_value = fake_products

    # 临时替换数据库连接函数，让接口使用 mock 连接而不是连 MySQL。
    with patch("pymysql.connect", return_value=fake_conn):
        response = client.get("/products")
        fake_cursor.execute.assert_called_once_with(
        "SELECT * FROM products;"
    )
    # 验证接口成功，并且返回预设的商品列表。
    assert response.status_code == 200
    assert response.json() == fake_products
    # 验证接口 finally 中确实关闭了数据库连接。
    fake_conn.close.assert_called_once_with()

def test_products_mysql_error():
    import pymysql

    # 模拟 pymysql.connect() 抛出数据库异常
    with patch(
        "pymysql.connect",
        side_effect=pymysql.MySQLError("连接失败")
    ):
        response = client.get("/products")

    # 验证异常时的 HTTP 状态码
    assert response.status_code == 500

    # 验证返回给客户端的错误信息
    assert response.json() == {"detail": "Database error"}
    
