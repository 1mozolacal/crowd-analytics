from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'annotators', views.AnnotatorViewSet)
# router.register(r'is-auth',views.TestIsAuthViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('is-auth/',views.TestIsAuthViewSet.as_view(),name='testing'),
    path('whoami/',views.TestAuthViewSet.as_view({'get':'get'}),name='whoami')
]