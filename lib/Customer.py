from Review import Review

class Customer:
    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    def all(self):
        return self._reviews

    def restaurants(self):
        restaurants = []
        for review in self._reviews:
            restaurant = review.restaurant().name()
            if restaurant not in restaurants:
                restaurants.append(restaurant)
        return restaurants

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)