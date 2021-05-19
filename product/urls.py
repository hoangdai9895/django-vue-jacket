from django.urls import path, include


from product import views

urlpatterns= [
    path('last-products/', views.LatestProductList.as_view())
]