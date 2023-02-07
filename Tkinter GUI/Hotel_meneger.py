class HotelGuests:
    def __init__(self, fullname, day_of_birthday, place, date_of_stay, doj):
        self.fullname = fullname
        self.day_of_birthday = day_of_birthday
        self.place = place
        self.date_of_stay = date_of_stay
        self.doj = doj

    def get_attrs(self, as_dict=False):
        if as_dict:
            return {
                "Fullname": self.fullname,
                "Day of birthday": self.day_of_birthday,
                "Place": self.place,
                'Date of stay': self.date_of_stay,
                "DOJ": self.doj
            }
        return [
            self.fullname,
            self.day_of_birthday,
            self.place,
            self.date_of_stay,
            self.doj
        ]