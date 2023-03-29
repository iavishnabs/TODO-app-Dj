from django.shortcuts import render,redirect
from . models import taskList


# Create your views here.

def indexpage(request):
    tak= taskList.objects.all()
    
    if request.method=='POST':
        tname=request.POST.get('task')
        tdesc = request.POST.get('desc')
        tdate=request.POST.get('date')
        object = taskList(name=tname,desc=tdesc,date=tdate)
        object.save()
        return redirect(indexpage)
    
    return render(request,'index.html',{'tak':tak})

def delete(request,taskid):
    ts = taskList.objects.get(id=taskid)   #object's id assigned to ts
    ts.delete()
    return redirect(indexpage)


def edit(request,taskid):
    ts = taskList.objects.get(id=taskid) 
    if request.method=='POST':
        tname=request.POST.get('task')
        tdesc = request.POST.get('desc')
        tdate=request.POST.get('date')
        taskList.objects.filter(id=taskid).update(name=tname,desc=tdesc,date=tdate)
        return redirect(indexpage)
    
    return render (request,'edit.html',{'ts':ts})