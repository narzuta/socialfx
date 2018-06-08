from django.db import models
from django.utils import timezone
# models
class Brokers(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    broker_name = models.CharField(max_length=200, default='Broker name')
    broker_url = models.CharField(max_length=300, default='www.broker.com')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.broker_name