from django.shortcuts import render,redirect, get_object_or_404
from .models import ToDoItem
from .forms import TodoItemForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


# Create your views here.
@login_required
def index(request):

    items = ToDoItem.objects.filter(user=request.user)
    context = {'items': items}
    return render(request,'ToDos/index.html', context)


@login_required
def add_item(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            to_do_item = form.save(commit=False)
            to_do_item.user = request.user
            to_do_item.save()
            return redirect('ToDos:index')
    else:
        form = TodoItemForm()
        context = {'form': form}
        return render(request,'ToDos/add.html', context)


@login_required
def update_item(request,pk):
    item = ToDoItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('ToDos:index')
    else:
        form = TodoItemForm(instance=item)
        context = {'form': form}
        return render(request,'ToDos/add.html', context)


@login_required
def delete_item(request,pk):
    item = ToDoItem.objects.get(pk=pk)
    item.delete()
    return redirect('ToDos:index')


@login_required
def delete_item(request,pk):
    item = ToDoItem.objects.get(pk=pk)
    item.delete()
    return redirect('ToDos:index')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ToDos:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'registration/profile.html')


class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('login')
