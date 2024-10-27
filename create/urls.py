from django.urls import path
from .views import createstudent,viewstudent,assign

urlpatterns = [
    path("create/",createstudent,name="creatstudent"),
    path("view/",viewstudent,name="viewstudent"),
    path("assign/<int:id>",assign,name="assign")
]
