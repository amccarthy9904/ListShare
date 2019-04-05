from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import List
from .forms import OwnerEditListForm, EditorEditListForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

# TODO: refactor these to use sessions when users are a real thing
#https://docs.djangoproject.com/en/2.1/topics/http/sessions/
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = False
    lists = List.objects.all()
    return render(request, 'home.html', {'lists':lists, 'username':username})
    #return HttpResponse('<p>home view</p>')

def list_detail(request, id):
    try:
        list = List.objects.get(id=id)
    except List.DoesNotExist:
        raise Http404('List not found')
    return render(request, 'list_detail.html', {'list':list, 'id':id, 'username':request.user.username})

def edit_list(request, id):
    """
    Verifies the list should be edited, the type of list, handles the edit
    """
    list = List.objects.get(id=id)
    if request.method == "POST":
        if request.user == list.owner:
            form = OwnerEditListForm(request.POST)
        else:
            form = EditorEditListForm(request.POST)
        if form.is_valid():
            list.content = form.cleaned_data['content']
            if isinstance(form, OwnerEditListForm):
                list.name = form.cleaned_data['name']
                list.owner = form.cleaned_data['owner']
                list.editors.set(form.cleaned_data['editors'])
                list.private = form.cleaned_data['private']
            list.save()
            messages.success(request, f'{list.name} successfully edited')
            return redirect('home')
        else:
            messages.error(request, f'{list.name} unsuccessfully edited, {list.errors}')
            return render(request, 'edit_list.html', {'list':list,'form':form, 'username':request.user.username})
    else:
        if request.user.is_authenticated:    #user auth
            if request.user == list.owner:     #user auth, owner
                messages.success(request, f'{request.user.username} is an owner')
                form = OwnerEditListForm(instance=list)
            elif list.private and request.user in list.editors.all(): #user auth, editor, priv
                messages.success(request, f'{request.user.username} is an editor')
                form = EditorEditListForm(instance=list)
        elif not list.private:    #user not auth, public
            messages.success(request, f'{list.name} is public')
            form = EditorEditListForm(instance=list)
        if form is not None:    #form made == edit ok
            return render(request, 'edit_list.html', {'list':list,'form':form, 'username':request.user.username})
        else:    #user not auth, private
            messages.success(request, f'Private Lists cannot be edited by Users who do not have permission')
            return redirect('home')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'User {username} created')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form}, {'username':request.user.username})

def logout_view(request):
    username = request.user.username
    logout(request)
    messages.success(request, f'User {username} logged out')
    return redirect('home')
