from django.urls import path
from .views import createstudent,viewstudent,assign,viewmarks

urlpatterns = [
    path("create/",createstudent,name="creatstudent"),
    path("view/",viewstudent,name="viewstudent"),
    path("assign/<int:id>",assign,name="assign"),
    path("viewmarks/<int:id>",viewmarks,name="viewmarks")
]
