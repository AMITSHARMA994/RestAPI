from django.contrib import admin
from django.urls import path
from mainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage),
    path('create/',views.createRecord),
    path('get/',views.getRecord),
    path('get-single/<int:id>/',views.getSingleRecord),
    path('search/<str:search>/',views.searchRecord),
    path('update/<int:id>/',views.updateRecord),
    path('delete/<int:id>/',views.deleteRecord),
]
