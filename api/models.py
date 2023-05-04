from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Cakes(models.Model):
    cake_name=models.CharField(max_length=100,unique=True)
    shape_choices=[
        ("circle","circle"),
    ("rectangle","rectangle"),
    ("oval","oval"),
    ]
    shape=models.CharField(max_length=10,choices=shape_choices,default="circle")
    layer_choices=[
        ("one","one"),
        ("two","two"),
        ("three","three")
    ]
    layers=models.CharField(max_length=50,choices=layer_choices,default="one")
    image=models.ImageField(upload_to="images",null=True,blank=True)
    weight=models.CharField(max_length=200)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.cake_name
    
    @property
    def cake_review(self):
        return Reviews.objects.filter(cake=self)

class Carts(models.Model):

    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    qty=models.PositiveIntegerField(default=1)

class Orders(models.Model):
    
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("shipped","shipped"),
        ("order-placed","order-placed"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    curDate=datetime.date.today()
    expdate=curDate+datetime.timedelta(days=1)
    expected_deliverydate=models.DateTimeField(default=expdate)
    address=models.CharField(max_length=300,null=True)
    matter=models.CharField(max_length=200,null=True)

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    comment=models.CharField(max_length=240)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.comment