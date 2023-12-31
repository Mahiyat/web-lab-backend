from django.shortcuts import render,redirect

from .models import Course
from .forms import CourseForm

# Create your views here.
def home(request):
  courses=Course.objects.all()
  return render(request, 'day4/home.html',{'all_courses':courses})
def remove(request,id):
  c=Course.objects.get(id=id)
  c.delete()
  return redirect(home)
def edit(request,id):
  c=Course.objects.get(id=id)
  frm=CourseForm(request.POST or None,instance=c)
  if frm.is_valid():
    frm.save()
    return redirect(home)
  return render(request,'day4/edit.html',{'form':frm})
def add(request):
  frm=CourseForm()
  if request.method=='POST':
    frm=CourseForm(request.POST, request.FILES)
    if frm.is_valid():
      frm.save()
      return redirect(home)
  return render(request,'day4/edit.html',{'form':frm})