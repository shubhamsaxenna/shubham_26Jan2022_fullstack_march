from django.db import models

class AllCoupons(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=4, default="none", blank=False)
    discountPercent= models.BigIntegerField()
    fixeddiscount = models.CharField(max_length=3, default=0)
    minAmounttouse = models.BigIntegerField()

    def __str__(self):
        return f"{self.code}"