from django.urls import path, re_path
from foodapp import views

urlpatterns = [
    re_path('^restaurants/$', views.get_all_restaurants),
    re_path('^restaurants/location/$', views.get_restaurants_based_on_location_view),
    re_path('^restaurant/items/$', views.get_menu_items_based_on_restaurant_view),
    re_path('^restaurant/download/$', views.generate_excel_view),
    
]
