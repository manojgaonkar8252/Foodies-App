from django.db import models

VEG_NON_VEG_CHOICES = [
('Veg', 'Veg'),
('Non-Veg', 'Non-Veg')
]

SUB_CATEGORY = [
('Starters', 'Starters'),
('Main-Course', 'Main-Course'),
('Desserts', 'Desserts')
]

class Restaurant(models.Model):
    """The model class generates a table for Restaurant in the database.
    :param name: Name of the restaurant
    :param address: Address of the restaurant
    :param rating: Rating given by customers(default: 0)
    :param delivery_time: Delivery Time Range
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(default=0)
    delivery_time = models.CharField(max_length=50)


class Item(models.Model):
    """The model class Item generates the Item table in the database. It stores the
    item information and dtails.
    :param name: Name of the item(primary_key)
    :param description: Description of the item
    :param category: Category(veg or non-veg)
    :param sub_category: sub_category(main or desserts or starters)
    """
    name = models.CharField(max_length=20, primary_key=True)
    description = models.TextField(max_length=200)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=20, choices=VEG_NON_VEG_CHOICES)
    sub_category = models.CharField(max_length=20, choices=SUB_CATEGORY)


class Menu(models.Model):
    """The model class Menu maintains an many to many mapping between Item and
    Resaurant
    """
    restaurant = models.ForeignKey(Restaurant, related_name='menus', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='menus', on_delete=models.CASCADE)
