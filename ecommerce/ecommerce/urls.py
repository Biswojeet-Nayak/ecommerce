"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from ecommerce.Controller import ProductController
from django.http import HttpResponse
from rest_framework.decorators import api_view


urlpatterns = [
    path('products/', ProductController.getAllProducts, name='product-list'),
    path('products/<int:product_id>/', ProductController.getSingleProduct, name='product-detail'),
    path('products/add/', ProductController.addNewProduct, name='add-new-product'),
    path('products/update/<int:product_id>/', ProductController.updateProduct, name='update-product'),
    path('products/patch/<int:product_id>/', ProductController.patchProduct, name='patch-product'),
    path('products/delete/<int:product_id>/', ProductController.deleteProduct, name='delete-product'),
]
# urlpatterns = [
#     path('categories/', CategoryController.as_view({'get': 'getAllCategories'})),
#     path('categories/<int:category_id>/', CategoryController.as_view({'get': 'getSingleCategory'})),
# ]

# urlpatterns = [
#     path('', root_view, name='root'),
#     path('products/', ProductListCreateView.as_view(), name='product-list-create'),
#     path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
# ]
"""Here is a summary of the URL patterns:



* `/products/`: This URL pattern maps to the `getAllProducts()` method in  controller. 
This method will return a list of all products.

* `/products/<int:product_id>/`: This URL pattern maps to the `getSingleProduct()` method in controller. 
This method will return a single product based on the product ID.

* `/products/add/`: This URL pattern maps to the `addNewProduct()` method in controller. 
This method will create a new product based on the data that is provided in the request body.

* `/products/update/<int:product_id>/`: This URL pattern maps to the `updateProduct()` method in controller. 
This method will update an existing product based on the product ID and 
the data that is provided in the request body.

* `/products/patch/<int:product_id>/`: This URL pattern maps to the `patchProduct()` method in controller. 
This method will partially update an existing product or its compnents based on the product ID and 
the data that is provided in the request body.

* `/products/delete/<int:product_id>/`: This URL pattern maps to the `deleteProduct()` method in controller. 
This method will delete an existing product based on the product ID.
"""


