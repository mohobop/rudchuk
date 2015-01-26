from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import  Context
from django.shortcuts import render_to_response, redirect
from model.models import Head, BodyText, Category
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from model.forms import HeadForm, BodyTextForm, HeadFormH

# Create your views here.
def model_views(request):
    head_form = HeadForm
    args = {}
    args.update(csrf(request))
    args['head_form'] = head_form
    args['all_category'] = Category.objects.all()
    args['head'] = Head.objects.all()
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    return render_to_response('model.html', args)

def category(request, category_id):
    head_form = HeadFormH
    args = {}
    args.update(csrf(request))
    args['head_form'] = head_form
    args['all_category'] = Category.objects.all()
    args['category'] = Category.objects.get(id=category_id)
    args['heads'] = Head.objects.filter(head_category_id=category_id)
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    return render_to_response('category.html', args)

def head(request, head_id):
    head_form = HeadFormH
    body_text_form = BodyTextForm
    args = {}
    args.update(csrf(request))
    args['head_form'] = head_form
    args['body_text_form'] = body_text_form
    args['all_category'] = Category.objects.all()
    args['head'] = Head.objects.get(id=head_id)
    args['heads'] = Head.objects.filter(head_category_id=Head.objects.get(id=head_id).head_category_id)
    args['bodys'] = BodyText.objects.filter(body_text_head_id=head_id)
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    return render_to_response('head.html', args)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "no people"
            return render_to_response('model.html', args)
    else:
        return render_to_response('model.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['forms'] = newuser_form
    return render_to_response('register.html', args)

def addhead(request):
    if request.POST:
        form = HeadForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/')

def addhead_c(request, category_id):
    if request.POST:
        form = HeadFormH(request.POST)
        if form.is_valid():
            title = form.save(commit=False)
            title.head_category = Category.objects.get(id=category_id)
            form.save()
    return redirect('/content/category/%s/' % category_id)

def addhead_h(request, head_id):
    head = Head.objects.get(id=head_id)
    if request.POST:
        form = HeadFormH(request.POST)
        if form.is_valid():
            title = form.save(commit=False)
            title.head_category = Category.objects.get(id=head.head_category_id)

            form.save()
            title_id = title.id
    return redirect('/content/category/head/%s/' % title_id)

def addbodytext(request, head_head_category_id, head_id):
    if request.POST:
        form = BodyTextForm(request.POST)
        if form.is_valid():
            text = form.save(commit=False)
            text.body_text_head = Head.objects.get(id=head_id)
            form.save()
    return redirect('/content/category/head/%s/' % head_id)