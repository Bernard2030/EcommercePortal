from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='Online Store API')
router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/products-all', views.ProductListView.as_view(), name='product-list'),
    path('api-docs/', schema_view, name="api-docs"),
    # path('logout/', views.LogoutView.as_view(), {"next_page": '/'}),
    path('api-token-auth/', obtain_auth_token),
    # path('<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    # path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    ]