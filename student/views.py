from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import stud

def index(request):
    students = stud.objects.all().filter(roll='377029')
    context = {'students': students}
    return render(request, 'index.html', context)

def details(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        sem = request.POST.get("sem")
        s = stud(naam=name, roll=int(roll), sem=int(sem))
        try:
            s.save()
        except:
            return HttpResponse("RollNo exists")

        return HttpResponse("YOUR FORM HAS BEEN SUBMITTED")
    else:
        return render(request, 'create.html')