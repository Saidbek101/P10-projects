from funcition import error_log


class Sales:
    def __init__(self, file: str) -> None:
        self.file = file

    def count_product(self, product: str) -> str:
        products = self.get_column(1)
        quantity = self.get_column(2)
        count = 0

        for i in range(len(products)):
            try:
                if products[i] == product:
                    count += int(quantity[i])
            except ValueError as e:
                error_log('error.log', e)

        return f'{product}: {count}'

    def get_orders_over(self, price: int) -> None:

        with open(self.file, encoding='utf-8') as file:
            orders = file.readlines()

        prices = self.get_column(3)

        with open(f'Products over {price}.txt', 'w') as file:

            for i in range(len(prices)):
                try:
                    if int(prices[i]) > 300:
                        file.write(f'{orders[i]}\n')
                except ValueError as e:
                    error_log('error.log', e)

    def get_column(self, column: int) -> list:

        with open(self.file, encoding='utf-8') as file:
            return [
                line.split(',')[column].replace('"', '').strip()
                for line in file.readlines()
            ]

    def get_orders_after(self, date: str) -> None:
        # UNFINISHED FUNCTION.
        pass
        # with open(self.file, encoding='utf-8') as file:
        #     orders = file.readlines()

        # dates = self.get_column(4)

        # with open('New orders.csv', 'w') as file:
        #     for i in range(len(orders)):
        #         print(dates[i].split()[0][::-1])


products = Sales('Sales_April_2019.csv')
print(products.count_product('Macbook Pro Laptop'))
products.get_orders_over(300)
