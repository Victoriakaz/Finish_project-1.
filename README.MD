# Казакова Виктория, 27 - я когорта - Финальный проект. Инженер по тестированию плюс

Папка "Скриншоты" содержит скриншоты в ответ на задание №1, №2, №3. Все файлы пронумерованы. 

В ответ на задание № 1 сообщаю, что для вывода списка логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true), необходимо использовать следующий SQL-запрос:

SELECT c.login, COUNT(o.id) AS "deliveryCount"
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId" AND o."inDelivery" = true
GROUP BY c.login;

Дополнительно сообщаю, что скриншот выполненного задания находится по ссылке:
https://github.com/Victoriakaz/Finish_project-1./blob/master/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%D1%8B/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201.png

В ответ на задание № 1 сообщаю, что для того, чтобы убедиться, что в базе данных статусы заказов записываются корректно. необходимо выведи все трекеры заказов и их статусы. 
Для этого необходимо выполнить следующий SQL-запрос:

SELECT track,
       CASE 
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
           ELSE 0 
       END AS status
FROM "Orders";

Дополнительно сообщаю, что скриншот выполненного задания находится по ссылке:
https://github.com/Victoriakaz/Finish_project-1./blob/master/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%D1%8B/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%202.jpg

Ответ на задание №3 (Автоматизация теста к API), расположен по ссылке:
https://github.com/Victoriakaz/Finish_project-1./blob/master/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%D1%8B/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%203.%20%D0%B0%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82.jpg
