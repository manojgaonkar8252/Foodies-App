# Foodies

The Foodies app is online food ordering app. The project is under development. Complete REST based.

### Table of Contents
  - Requirements
  - API's
  - Instruction to run the project
  - Models

### Requirements:
Download python from https://www.python.org/downloads/

    Django==2.1.1
    djangorestframework==3.8.2
    
    $ pip install requirement.txt

### API's:
1. **Get All Restaurants**:
    Get all the restaurants registered.
    parameters: None
    usage: /foodies/restaurants/

2. **Get Restaurants Based on Location**:
    Get restaurants from the specific location given the specific location.
    parameters: 'location'
    usage: /foodies/restaurants/location/

3. **Get Menu Based On Restaurant**:
    Get the menu based on the restaurant selected.
    paramter: 'restaurantId'
    usage: /foodies/restaurant/items/

4. **Generate CSV**:
    Get the menu based on the restaurant selected.
    paramter: 'restaurantId'
    usage: /foodies/restaurant/download/

### Instructions to run the Project:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```


### Models
1.  **Restaurant**:
    The model class generates a table for Restaurant in the database.
    :param name: Name of the restaurant
    :param address: Address of the restaurant
    :param rating: Rating given by customers(default: 0)
    :param delivery_time: Delivery Time Range

2.  **Item**:
    The model class Item generates the Item table in the database. It stores the
    item information and dtails.
    :param name: Name of the item(primary_key)
    :param description: Description of the item
    :param category: Category(veg or non-veg)
    :param sub_category: sub_category(main or desserts or starters)  

3. **Menu**:
    The model class Menu maintains an many to many mapping between Item and
    Resaurant

**Admin Login Details**:
username: **admin**
password: **admin123**
usage: **/admin/**
