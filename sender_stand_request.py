import configuration
import requests
import data

def create_order(body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)

def get_order(track_number):
   get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
   response = requests.get(get_order_url)
   return response

def test_order_creation_and_retrieval():
   response = create_order(data.order_body)

   if response.status_code == 201:
       track_number = response.json()["track"]
       print("Заказ создан. Номер трека:", track_number)

       order_response = get_order(track_number)

       if order_response.status_code == 200:
           order_data = order_response.json()
           print("Данные заказа:")
           print(order_data)
       else:
           print(f"Ошибка получения заказа: {order_response.status_code}. {order_response.text}")
   else:
       print(f"Ошибка создания заказа: {response.status_code}. {response.text}")


if __name__ == "__main__":
   test_order_creation_and_retrieval()