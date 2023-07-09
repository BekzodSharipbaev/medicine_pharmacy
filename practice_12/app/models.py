from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    pharmacies = models.ManyToManyField('Pharmacy', related_name='medicines')
    
    def get_cheapest_price(self, distance):
        min_price = None
        for pharmacy in self.pharmacies.all():
            price = pharmacy.calculate_price(self.price, distance)
            if min_price is None or price < min_price:
                min_price = price
        return min_price
    
    def __str__(self) -> str:
        return f"{self.name}-{self.price}"


class Pharmacy(models.Model):
    name = models.CharField(max_length=50)
    distance = models.PositiveIntegerField()
    markup_factor = models.FloatField()
    
    def calculate_price(self, base_price, distance):
        price = base_price * (1 + distance * 0.0001 * self.markup_factor)
        return price
    
    def __str__(self) -> str:
        return f"{self.name}-{self.distance}"
    
    