operator = ("Daria", "Daria@example.com")

orders = {
    "state": 0,
    "data": [
        {
            "_id": "3d8c861f-e2c0-442a-9d82-810ae5eb5f52",
            "count": 1,
            "brand_id": 84375,
            "delay": 1,
            "startedAt": "2024-03-21T16:48:03.513Z",
            "completedAt": "2024-03-21T16:48:03.513Z",
            "completed": 0,
            "wait_refund": 0,
            "refunded": 0
        },
        {
            "_id": "4816385b-a5a5-4341-aedf-6f80bedbdce4",
            "count": 2,
            "brand_id": 88339,
            "delay": 2,
            "startedAt": "2024-03-21T16:27:32.062Z",
            "completedAt": "2024-03-21T16:28:32.062Z",
            "completed": 0,
            "wait_refund": 2,
            "refunded": 0
        },
        {
            "_id": "7e0882b5-38b8-4dcb-9825-625158a92314",
            "count": 16,
            "brand_id": 88339,
            "delay": 3,
            "startedAt": "2024-03-21T16:17:04.723Z",
            "completedAt": "2024-03-21T16:17:04.723Z",
            "completed": 7,
            "wait_refund": 3,
            "refunded": 6
        }
    ]
}

# 1. Надо убедиться, что заказы вообще есть в ответе от сервера

assert len(orders["data"]) > 0

# 2. Надо убедиться, что время выполнение первого и второго **заказов** не превышает 6 часов
time_1 = orders["data"][0]["delay"]
time_2 = orders["data"][1]["delay"]
time = time_1 + time_2
assert time <= 6

# 3. Надо убедиться, что для третьего заказа все услуги обработаны И выполнено не меньше половины.
# Ну или по крайней мере на текущий момент возвращено не больше, чем выполнено, а ожидают возврат не больше, чем уже возвращено
services_total = orders["data"][2]["count"]

services_completed = orders["data"][2]["completed"]
services_wait_refund = orders["data"][2]["wait_refund"]
services_refunded = orders["data"][2]["refunded"]

assert ((services_total == (services_completed + services_wait_refund + services_refunded))
        and (
                (services_total <= (services_completed * 2))
                or (
                        (services_refunded <= services_completed)
                        and (services_wait_refund <= services_refunded)
                )
        )
        )

# Подготовь словарь, который будет содержать:
# 1. массив айдишников заказов

ids = []
for order in orders["data"]:
    ids.append(order["_id"])

print(ids)


# 2. объект, который будет содержать в себе инфу о том, сколько выполненных заказов, возвращенных и ожидающих возврат

status = {
    "completed": 0,
    "wait_refund": 0,
    "refunded": 0
}

for order in orders["data"]:
    status["completed"] = status["completed"] + order["completed"]
    status["wait_refund"] = status["wait_refund"] + order["wait_refund"]
    status["refunded"] = status["refunded"] + order["refunded"]

print(status)

print(f"Отчет подготовлен {operator=}")

# Ну и последнее - я хочу немного приукрасить наш отчет. Сделай так, чтобы в массив с id добавился еще один id - вот такой  326b23a1-e6ab-4b4a-84a1-a3ecb33afc97

ids.append("326b23a1-e6ab-4b4a-84a1-a3ecb33afc97")

print(ids)