from django.db import models
from django.utils import timezone

# models
class Analiza(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    EUR_USD = 'EUR/USD'
    USD_JPY = 'USD/JPY'
    waluta = (
        (EUR_USD, 'EUR/USD'),
        (USD_JPY, 'USD/JPY'),
    )
    instrument = models.CharField(max_length=200,choices=waluta,default=EUR_USD,)

    NEUTRAL = 'NEUTRAL'
    SELL = 'SELL'
    BUY = 'BUY'
    direction = (
        (NEUTRAL, 'NEUTRAL'),
        (SELL, 'SELL'),
        (BUY, 'BUY'),
    )
    direction = models.CharField(max_length=200, choices=direction, default=NEUTRAL, )
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
