import pytest
from sender_stand_request import create_order, get_order
import data

def test_order_creation_and_retrieval():
    response = create_order(data.order_body)
    assert response.status_code == 201, f"Ошибка создания заказа: {response.status_code}. {response.text}"
    track_number = response.json().get("track")
    order_response = get_order(track_number)
    assert order_response.status_code == 200, f"Ошибка получения заказа: {order_response.status_code}. {order_response.text}"
    order_data = order_response.json()

if __name__ == "__main__":
    pytest.main()



   # Казакова Виктория, 27 - я когорта - Финальный проект. Инженер по тестированию плюс