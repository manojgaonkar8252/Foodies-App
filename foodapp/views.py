from django.http import HttpResponse, JsonResponse
from django.http import FileResponse
from rest_framework.decorators import api_view

from foodapp.algorithm.business_logic import get_all_restaurants as get_restaurants
from foodapp.algorithm.business_logic import get_restaurants_based_on_location, download_excel, get_menu_items_based_on_restaurant


@api_view(['GET'])
def get_all_restaurants(request):
    """Gets all the restaurants"""
    restaurants = get_restaurants()
    return JsonResponse(restaurants, safe=False)


@api_view(['POST'])
def get_restaurants_based_on_location_view(request):
    """Gets all the restaurants in the particular location"""
    location = request.data.get("location", None)
    restaurants = get_restaurants_based_on_location(location=location)
    return JsonResponse(restaurants, safe=False)


@api_view(['POST'])
def get_menu_items_based_on_restaurant_view(request):
    """Get the menu for the particular restaurant"""
    restaurant_id = request.data.get('restaurantId', None)
    json_data = get_menu_items_based_on_restaurant(restaurant_id)
    return JsonResponse(json_data, safe=False)


@api_view(['POST'])
def generate_excel_view(request):
    """Generates the csv file for the restaurant with the menu items"""
    restaurant_id = request.data.get('restaurantId', None)
    csv_file_path = download_excel(restaurant_id)
    open_file = open(csv_file_path, 'rb')
    response = FileResponse(open_file, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="input.csv"'
    return response
