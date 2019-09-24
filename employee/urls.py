from rest_framework_mongoengine import routers
from employee.views import EmployeeView

# router will generate the urls automatically for all CRUD operations
router = routers.DefaultRouter()
router.register(r'employee', EmployeeView)

urlpatterns = []
urlpatterns += router.urls 
