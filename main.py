
from entity.courier import Courier
from entity.exeptions import BaseError
from entity.request import Request
from entity.shop import Shop
from entity.store import Store

shop = Shop(
    items={
        "печенька": 3,
        "ноутбук": 10,
        "Елка": 1,
        "собака": 2,
        "кошка": 1
    },
)
store = Store(
    items={
        "печенька": 3,
        "ноутбук": 2,
        "компьютер": 1
    },
)

storages = {
    "магазин": shop,
    "склад": store
}

def main():
    while True:

        for storage_name in storages:
            print(f"В {storage_name} хранится: {storages[storage_name].get_items()}")

        user_input = input(
            "Введите строку в формате: ""Достать 3 печенька из склад в магазин"".\n"
            "Введите ""стоп"" или ""stop"", чтобы продолжить\n"
        )

        if user_input in ("stop", "стоп"):
            break

        try:
            request = Request(request_str=user_input, storages=storages)

        except BaseError as error:
            print(error.message)
            continue

            courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        except BaseError as error:
            courier.cancel()
            print(error.message)




if __name__ == "__main__":
    main()