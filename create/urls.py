from django.urls import path
from .views import createstudent,viewstudent,assign,viewmarks

urlpatterns = [
    path("create/",createstudent,name="creatstudent"),
    path("view/",viewstudent,name="viewstudent"),
<<<<<<< HEAD
    path("assign/<int:id>",assign,name="assign"),
    path("viewmarks/<int:id>",viewmarks,name="viewmarks")
=======
    path("assign/<int:id>/",assign,name="assign")
>>>>>>> 306fdfbc81093ff89e5da835419c1f129f2e36f0
]
