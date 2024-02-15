from django.shortcuts import render
from . forms import *
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request,'dashboard/home.html')

def notes(request):
    if request.method=="POST":
        form=NotesForm(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"Notes Added from{request.user.username} Successfully!")
        return redirect('notes') 

    else:
        form=NotesForm()
    form=NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)

def delete_notes(request,pk=None):
    querySelect = Notes.objects.get(id=pk)
    querySelect.delete()
    messages.success(request, f"Note deleted successfully!")
    return redirect('notes')

def NoteDetailView(request,pk=None):
    queryset=Notes.objects.get(id=pk)
    context = {'note':queryset}
    return render(request,'dashboard/notes_detail.html',context)

def homework(request):
    if request.method=="POST":
        form = HomeworksForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=='on':
                    finished = True
                else:
                    finished=False
            except:
                finished=False
            homeworks = Homeworks(
                user=request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                due=request.POST['due'],
                is_finished=finished
            )
            homeworks.save()
            messages.success(request,f"Homeworks Added from{request.user.username} Successfully!")
            return redirect('homeworks') 

    else:
        form = HomeworksForm()
    
    homeworks = Homeworks.objects.filter(user=request.user)
    if len(homeworks)==0:
        homework_done = True
    else:
        homework_done = False
    context={
        'homeworks':homeworks,
        'homework_done':homework_done,
        'form':form,
        }
    return render(request,'dashboard/homework.html',context)