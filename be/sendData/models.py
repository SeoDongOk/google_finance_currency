from django.db import models

class Swap(models.Model):
  current_ticker = models.CharField(max_length=10)
  trade_ticker = models.CharField(max_length=10)

  def __str__(self):
    return f"{self.current_ticker} -> {self.trade_ticker}"

