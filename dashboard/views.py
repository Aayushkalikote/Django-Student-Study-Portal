from django.shortcuts import render
from . forms import *
from django.contrib import messages
from django.shortcuts import redirect
from youtubesearchpython import VideosSearch
import requests

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

def update_homework(request,pk=None):
    homework=Homeworks.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished=False
    else:
        homework.is_finished=True
    homework.save()
    messages.success(request,f"Homework Status Updated Successfully!")
    return redirect('homeworks') 

def delete_homework(request,pk=None):
    homework=Homeworks.objects.get(id=pk)
    homework.delete()
    messages.success(request,f"Homework Deleted Successfully!")
    return redirect('homeworks') 

def youtube(request):
    if request.method == 'POST':  
        form = DashboardForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            video = VideosSearch(text, limit=10)
            result_list = []
            for i in video.result()['result']:
                result_dict = {
                    'input': text,
                    'title': i['title'],
                    'duration': i['duration'],
                    'thumbnails': i['thumbnails'][0]['url'],
                    'channel': i['channel']['name'],
                    'link': i['link'],
                    'views': i['viewCount']['short'],
                    'published': i['publishedTime']
                }
                desc = ''
                if i['descriptionSnippet']:
                    for j in i['descriptionSnippet']:
                        desc += j['text']
                result_dict['description'] = desc
                result_list.append(result_dict)
            messages.success(request, "Youtube Search Successful!")
            context = {
                'form': form,
                'results': result_list
            }
            return render(request, 'dashboard/youtube.html', context)
    else:
        form = DashboardForm()
    context = {'form': form}
    return render(request, 'dashboard/youtube.html', context)
def todo(request):
    if request.method=='POST':
        form = TodosForm(request.POST)
        if form.is_valid():
            try:
                finished=request.POST['is_finished']
                if finished=='on':
                    finished = True
                else:
                    finished=False
            except:
                finished=False
            todos = Todos(
                user=request.user,
                title=request.POST['title'],
                is_finished=finished
            )
            todos.save()
            messages.success(request,f"Todos Added from{request.user.username} Successfully!")
            return redirect('todos') 
    else:    
        form = TodosForm()
    todos=Todos.objects.filter(user=request.user)
    if len(todos)==0:
        todo_complete = True
    else:
        todo_complete = False
    context={
        'form':form,
        'todo_complete':todo_complete,
        'todos':todos
    }
    return render(request,"dashboard/todo.html",context)

def update_todo(request,pk=None):
    todo=Todos.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished=False
    else:
        todo.is_finished=True
    todo.save()
    messages.success(request,f"Todo Status Updated Successfully!")
    return redirect('todos') 
def delete_todo(request,pk=None):
    todo=Todos.objects.get(id=pk)
    todo.delete()
    messages.success(request,f"Todo Deleted Successfully!")
    return redirect('todos') 

def book(request):
    if request.method == 'POST':  
        form = DashboardForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            url ="https://www.googleapis.com/books/v1/volumes?q="+text
            r = requests.get(url)
            answer =r.json()
            result_list = []
            for i in range(10):
                result_dict = {
                    'title': answer['items'][i]['volumeInfo']['title'],
                    'subtitle': answer['items'][i]['volumeInfo'].get('subtitle'),
                    'description': answer['items'][i]['volumeInfo'].get('description'),
                    'count': answer['items'][i]['volumeInfo'].get('pageCount'),
                    'categories': answer['items'][i]['volumeInfo'].get('categories'),
                    'rating': answer['items'][i]['volumeInfo'].get('pageRating'),
                    'thumbnail': answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                    'preview': answer['items'][i]['volumeInfo'].get('previewLink'),
                    
                }
                result_list.append(result_dict)
            messages.success(request, "Book Search Successful!")
            context = {
                'form': form,
                'results': result_list
            }
            return render(request, 'dashboard/books.html', context)
    else:
        form = DashboardForm()
    context = {'form': form}
    return render(request, 'dashboard/books.html', context)    

def dictionary(request):
    if request.method=='POST':
        form= DashboardForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            url ="https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
            r = requests.get(url)
            answer =r.json()
            try:
                phonetics=answer[0]['phonetics'][0]['text']
                print(phonetics)
                audio=answer[0]['phonetics'][0]['audio']
                definition=answer[0]['meanings'][0]['definitions'][0]['definition']
                example=answer[0]['meanings'][0]['definitions'][0]['example']
                synonyms=answer[0]['meanings'][0]['definitions'][0]['synonyms']
                context = {
                    'form': form,
                    'input': text,
                    'phonetics':phonetics,
                    'audio':audio,
                    'definition':definition,
                    'example':example,
                    'synonyms':synonyms
                }
            except:
                context={
                    'form':form,
                    'input':''
                }
            return render(request, 'dashboard/dictionary.html', context)
    else:
        form = DashboardForm()
        context={
            'form':form
        }
    return render(request,'dashboard/dictionary.html',context)