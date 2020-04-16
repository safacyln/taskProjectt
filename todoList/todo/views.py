from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .form import TodoForm

# Create your views here.


def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()
    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    print("henüz kayıt edilmedi")
    if form.is_valid():
        new_todo = Todo(text=require_POST['text'])
        new_todo.save()
        print("kayıt edildi")

    return redirect('index')