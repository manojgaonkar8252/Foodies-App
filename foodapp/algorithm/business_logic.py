from django.conf import settings
import csv

from foodapp.models import Restaurant, Item, Menu


def get_all_restaurants():
    """The module fetches all the restaurants from the database using ORM.
    :return: All the restaurants
    """
    return list(Restaurant.objects.all().values())


def get_restaurants_based_on_location(location):
    """The module fetches all the restaurants in the particular location
    :param location: Location to get the restaurants in the particular location
    :return: list of restaurants in the particular location
    """
    return list(Restaurant.objects.all().filter(address__contains=location).values())


def get_menu_items_based_on_restaurant(restaurant_id):
    """The module fetches the menu card for the restaurant based on the
    restaurant_id. The complete items list and details of restaurant will be
    returned
    :param restaurant_id: Primary Key of the restaurant
    :return JSON structure with restaurant and menu details
    """
    result_dictionary = dict()
    result_items_list = []
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    result_dictionary['restaurant'] = {
    'name': restaurant.name,
    'location': restaurant.address,
    'deliveryTime': restaurant.delivery_time
    }
    items = list(restaurant.menus.all().values())
    for item in items:
        item_instance = Item.objects.get(pk=item.get('item_id', None))
        result_items_list.append({
        'name': item_instance.name,
        'description': item_instance.description,
        'price': item_instance.price,
        'category': item_instance.category,
        'sub_category': item_instance.sub_category
        })
    result_dictionary['itemsList'] = result_items_list
    return result_dictionary


def download_excel(restaurant_id):
    """The module generates the csv file for the restaurant with the items
    available in the restaurant.
    :param restaurant_id: Primary Key of the restaurant
    :return csv file path
    """
    raw_data = get_menu_items_based_on_restaurant(restaurant_id=restaurant_id)
    csv_file_path = "{}/file.csv".format(settings.BASE_DIR)
    static_form = ['name', 'description', 'price', 'category', 'sub_category']
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=static_form)
        writer.writeheader()
        writer.writerows(raw_data['itemsList'])
    csv_file.close()
    return csv_file_path
