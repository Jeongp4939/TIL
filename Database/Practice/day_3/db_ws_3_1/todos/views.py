from django.shortcuts import get_object_or_404, render,redirect
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from .models import Todo
from .forms import TodoForm

# Create your views here.
@require_safe
def index(request):
    if not request.user.is_authenticated:
            return redirect('accounts:login')

    # todos = Todo.objects.all()
    todos = request.user.todo_set.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    
    context = {
        'form': form,
    }
    return render(request, 'todos/create.html', context)