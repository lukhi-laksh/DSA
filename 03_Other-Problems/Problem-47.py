from collections import defaultdict
from bisect import insort, bisect_left

class MovieRentingSystem:

    def __init__(self, n, entries):
        self.priceMap = {}  # (shop, movie) -> price
        self.available = defaultdict(list)  # movie -> sorted list of (price, shop)
        self.rented = []  # глобальный список арендованных (price, shop, movie)

        for shop, movie, price in entries:
            self.priceMap[(shop, movie)] = price
            insort(self.available[movie], (price, shop))

    def search(self, movie):
        return [shop for price, shop in self.available[movie][:5]]

    def rent(self, shop, movie):
        price = self.priceMap[(shop, movie)]
        arr = self.available[movie]
        i = bisect_left(arr, (price, shop))
        if i < len(arr) and arr[i] == (price, shop):
            arr.pop(i)
        insort(self.rented, (price, shop, movie))

    def drop(self, shop, movie):
        price = self.priceMap[(shop, movie)]
        i = bisect_left(self.rented, (price, shop, movie))
        if i < len(self.rented) and self.rented[i] == (price, shop, movie):
            self.rented.pop(i)
        insort(self.available[movie], (price, shop))

    def report(self):
        return [[shop, movie] for price, shop, movie in self.rented[:5]]
