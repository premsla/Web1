from django.urls import path
from .views import home_view,my_first_view,Fashion_views,Men_views,kids_views,all_brands_views,Beauty_views,Accessories_views,Personal_care_views,cart_views,Face_views,Eyes_views,Lips_views
urlpatterns = [
    path('', home_view, name='home'),

    path('my_first/', my_first_view, name='my_first'),
    path('beauty/Face', Face_views, name='Face'),
    path('beauty/eyes', Eyes_views, name='eyes'),
    path('beauty/lips', Lips_views, name='lips'),
    path('accessories/', Accessories_views, name='accessories'),
    path('personalcare/', Personal_care_views, name='personalcare'),
    path('Fashion/', Fashion_views, name='Fashion'),
    path('Fashion/men/', Men_views, name='men'),
    path('Fashion/kids/', kids_views, name='kids'),
    path('Fashion/all_brands/', all_brands_views, name='all_brands'),
    path('cartPage/', cart_views, name='cartPage')
    

]

