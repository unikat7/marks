from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Student

# Create your views here.
def createstudent(request):
    if request.method=="POST":
        name=request.POST.get("name")
        address=request.POST.get("address")
        semester=request.POST.get("semester")
        students=Student(name=name,address=address,semester=semester)
        students.save()
        return HttpResponse("Student inserted successfully")
    return render(request,"createstudent.html")

def viewstudent(request):
    students=Student.objects.all()
    return render(request,"viewstudent.html",{
        "students":students
    })


def assign(request, id):
   
    # st = get_object_or_404(Student, pk=id)
    # print(st.semester)
    # print(f"Found student: {st.name},id:{st.id} Semester: {st.semester}")  
    if st.semester == 1:
        print("Rendering sem1.html")  
        return render(request, "sem1.html", {"st": st})
    else:
        return HttpResponse("This functionality is not available for this semester.")

