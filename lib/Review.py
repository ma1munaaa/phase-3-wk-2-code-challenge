class Review:
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating

    def rating(self):
        return self._rating

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    @staticmethod
    def all():
        reviews_data =(
            {"customer": "Customer1", "restaurant": "Restaurant1", "rating": 4},
            {"customer": "Customer2", "restaurant": "Restaurant2", "rating": 5},
        )

    
        return all-reviews_data()
    print(("customer1"))