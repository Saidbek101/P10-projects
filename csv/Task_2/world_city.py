class Cities:
    def __init__(self, file: str) -> None:
        self.file = file

    def get_citites_of(self, country: str, with_location=False) -> None:
        cities = self.get_column(0)
        countries = self.get_column(4)

        if with_location:
            with open(f'Cities of {country}.txt', 'w', encoding='utf-8') as file:
                for i in range(len(cities)):
                    if countries[i] == country:
                        file.write(f'{cities[i]}\n')

        else:
            lat = self.get_column(2)
            lng = self.get_column(3)

            with open(f'Cities of {country} with locations.txt', 'w', encoding='utf-8') as file:
                for i in range(len(cities)):
                    if countries[i] == country:
                        file.write(f'{cities[i]} https://my-location.org/?lat={lat[i]}&lng={lng[i]}\n')

    def get_column(self, column: int) -> list:

        with open(self.file, encoding='utf-8') as file:
            return [
                line.split(',')[column].replace('"', '').strip()
                for line in file.readlines()
            ]


cities = Cities('world_cities.csv')
cities.get_citites_of('Uzbekistan')
cities.get_citites_of('Uzbekistan', with_location=True)