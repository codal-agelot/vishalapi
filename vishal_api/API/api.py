from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('language',views.LanguagesView)
router.register('developer',views.DevelopersView)
