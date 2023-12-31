class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = []

    def name(self):
        return self._name

    def reviews(self):
        return self._reviews

    def customers(self):
        customers = []
        for review in self._reviews:
            customer = review.customer().full_name()
            if customer not in customers:
                customers.append(customer)
        return customers

    def average_star_rating(self):
        if not self._reviews:
            return 0
        total_rating = sum(review.rating() for review in self._reviews)
        return total_rating / len(self._reviews)