from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import List
from .forms import EditListForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# TODO: refactor these to use sessions when users are a real thing
#https://docs.djangoproject.com/en/2.1/topics/http/sessions/
def home(request):
    lists = List.objects.all()
    return render(request, 'home.html', {'lists':lists})
    #return HttpResponse('<p>home view</p>')

def list_detail(request, id):
    try:
        list = List.objects.get(id=id)
    except List.DoesNotExist:
        raise Http404('List not found')
    return render(request, 'list_detail.html', {'list':list}, {'id':id})
    #return HttpResponse('<p>list_detail view wioth id {}</p>'.format(id))

def edit_list(request, id):
    if request.method == "POST":
        form = EditListForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
    else:
        list = List.objects.get(id=id)
        #form = EditListForm()
        form = EditListForm(instance=list)
        return render(request, 'edit_list.html', {'list':list,'form':form})

    #try:
    #    list = List.objects.get(id=id)
    #    form = EditListForm(instance=list)
    #except List.DoesNotExist:
    #    raise Http404('List not found')
    #return render(request, 'edit_list.html', {'list':list}, {'form':form})

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})
