from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Student,Semester1

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
    st = get_object_or_404(Student, pk=id)

    if st.semester == 1:
        if request.method == "POST":
            digital = request.POST.get("digital")
            cprogramming = request.POST.get("cprogramming")
            cfa = request.POST.get("cfa")
            english = request.POST.get("english")
            
            # Save the data to Semester1 model
            semester1 = Semester1(digital=digital, cprogramming=cprogramming, cfa=cfa, english=english)
            semester1.save()
            
            return HttpResponse("Marks successfully inserted")
        
        return render(request, "sem1.html", {"st": st})
    
    else:
        return HttpResponse("no semester matches")
    

def viewmarks(request,id):
    marks=get_object_or_404(Semester1,pk=id)
    st=get_object_or_404(Student,pk=id)
    percentage=((marks.digital + marks.cprogramming + marks.cfa + marks.english)/400)*100
    return render(request,"viewmarks.html",{
        "percentage":percentage,
        "st":st,
        "marks":marks
    })





