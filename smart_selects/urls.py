from smart_selects.views import filterchain_all,filterchain
from django.urls import path

urlpatterns = [
    path('all/<app>/<model>/<field>/<foreign_key_app_name>/<foreign_key_model_name>/<foreign_key_field_name>/<value>/',filterchain_all, name='chained_filter_all'),
    path('filter/<app>/<model>/<field>/<foreign_key_app_name>/<foreign_key_model_name>/<foreign_key_field_name>/<value>/',filterchain, name='chained_filter'),
    path('filter/<app>/<model>/<manager>/<field>/<foreign_key_app_name>/<foreign_key_model_name>/<foreign_key_field_name>/<value>/',filterchain, name='chained_filter'),
]

