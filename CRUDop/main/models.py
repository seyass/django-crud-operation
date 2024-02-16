from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    

    def __str__(self):
        return self.user.username + "'s Profile"


class Company(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)
    industry = models.CharField(max_length=100)
    founded_date = models.DateField()
    followers = models.ManyToManyField(User, related_name= "following", blank=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PortfolioItem(models.Model):
    cap = {
        'SC':'small cap',
        'MC':'mid cap',
        'LC':'large cap'
    }
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    size = models.CharField(max_length=2,choices=cap)
    quantity = models.PositiveIntegerField()
    purchace_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.company.name} - {self.quatitiy} shares"
    
class StockPrice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateTimeField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

    def __str__(self):
        return f"{self.company.name} - {self.date}"