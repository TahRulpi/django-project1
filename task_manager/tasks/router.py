from rest_framework import routers
from .views import task_viewset

router=routers.DefaultRouter()
router.register('task',task_viewset)