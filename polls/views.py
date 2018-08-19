from django.shortcuts import render,get_object_or_404
from django.http import Http404
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms
from .forms import UserRegistrationForm

def index(request):
    question_set = Question.objects.all()
    context = {
        'question_set': question_set
    }
    return render(request, 'polls/question.html', context)
def details(request,question_id):
    try:
        question=Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    context={
        'question': question
    }
    return render(request,'polls/choices.html',context)

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    context={
        'question':question
    }
    return render(request,'polls/results.html',context)

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        context={
            'question':question,
            'error_message':"Choice does not exist"
             }
        return(render(request,'polls/question.html',context))
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=[question.id]))




def homepage(request):
    question_count=Question.objects.count()
    context={
        'question_count':question_count
    }
    return render(request,'polls/homepage.html',context)

def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


