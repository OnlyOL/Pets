from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'cats', CatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', add_cat, name='add-items'),
    path('all/', view_cats, name='view_items'),
    path('update/<int:pk>/', update_cat, name='update-items'),
    path('item/<int:pk>/delete/', delete_cat, name='delete-items'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]