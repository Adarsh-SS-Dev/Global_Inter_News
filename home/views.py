from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Blog, Comment, ContactMessage
from django.contrib import messages
from django.core.paginator import Paginator
from taggit.managers import TaggableManager
from taggit.models import Tag
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse





def index(request):
    blog = Blog.objects.all().order_by('-date')
    smallbusiness = Blog.objects.filter(category="smallbusiness").order_by('-date')
    marketing = Blog.objects.filter(category="marketing").order_by('-date')
    entrepreneurship = Blog.objects.filter(category="entrepreneurship").order_by('-date')
    businessideas = Blog.objects.filter(category="businessideas").order_by('-date')
    ecommerce = Blog.objects.filter(category="ecommerce").order_by('-date')
    return render(request, "index.html", {"blog": blog, "smallbusiness": smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce})

def content(request):
    slug = request.GET.get("search")
    id = request.GET.get("id")
    data = Blog.objects.filter(slug=slug)
    random=Blog.objects.order_by('?')
    comment = Comment.objects.filter(pro=id)
    blog = Blog.objects.all().order_by('-date')
    if data.exists():
        current_blog = data.first()
        groups = current_blog.tags.all()
    else:
        groups = []
    smallbusiness = Blog.objects.filter(category="smallbusiness")
    marketing = Blog.objects.filter(category="marketing")
    entrepreneurship = Blog.objects.filter(category="entrepreneurship")
    businessideas = Blog.objects.filter(category="businessideas")
    ecommerce = Blog.objects.filter(category="ecommerce")
    return render(request, "content.html", {"pro": data,"random":random,"blog": blog ,"smallbusiness":smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce, "comment": comment, "groups": groups})

def fullnews(request):
    category = request.GET["category"]
    data = Blog.objects.filter(category=category).order_by('-date')
    blog = Blog.objects.all().order_by('-date')
    random=Blog.objects.order_by('?')
    tags = TaggableManager()
    smallbusiness = Blog.objects.filter(category="smallbusiness")
    marketing = Blog.objects.filter(category="marketing")
    entrepreneurship = Blog.objects.filter(category="entrepreneurship")
    businessideas = Blog.objects.filter(category="businessideas")
    ecommerce = Blog.objects.filter(category="ecommerce")
    paginator = Paginator(data, 4)
    page_number = request.GET.get('page')
    datafinal = paginator.get_page(page_number)
    totalpage = datafinal.paginator.num_pages
    return render(request, "list.html", {"pro": data,"random":random, "blog": blog,"tags":tags, "smallbusiness": smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce, "datafinal": datafinal, "lastpage": totalpage, "totalpagelist": [n+1 for n in range(totalpage)]})

def contact(request):
    smallbusiness = Blog.objects.filter(category="smallbusiness")
    marketing = Blog.objects.filter(category="marketing")
    entrepreneurship = Blog.objects.filter(category="entrepreneurship")
    businessideas = Blog.objects.filter(category="businessideas")
    ecommerce = Blog.objects.filter(category="ecommerce")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
    return render(request, 'contact.html',{"smallbusiness": smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce})
   
def about(request):
    smallbusiness = Blog.objects.filter(category="smallbusiness")
    marketing = Blog.objects.filter(category="marketing")
    entrepreneurship = Blog.objects.filter(category="entrepreneurship")
    businessideas = Blog.objects.filter(category="businessideas")
    ecommerce = Blog.objects.filter(category="ecommerce")
    return render(request, "about.html",{"smallbusiness": smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce})
def privacy(request):
    smallbusiness = Blog.objects.filter(category="smallbusiness")
    marketing = Blog.objects.filter(category="marketing")
    entrepreneurship = Blog.objects.filter(category="entrepreneurship")
    businessideas = Blog.objects.filter(category="businessideas")
    ecommerce = Blog.objects.filter(category="ecommerce")
    return render(request, "privacypolicy.html",{"smallbusiness": smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce})
def disclaimer(request):
    smallbusiness = Blog.objects.filter(category="smallbusiness")
    marketing = Blog.objects.filter(category="marketing")
    entrepreneurship = Blog.objects.filter(category="entrepreneurship")
    businessideas = Blog.objects.filter(category="businessideas")
    ecommerce = Blog.objects.filter(category="ecommerce")
    return render(request, "disclaimer.html",{"smallbusiness": smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce})
def terms(request):
    smallbusiness = Blog.objects.filter(category="smallbusiness")
    marketing = Blog.objects.filter(category="marketing")
    entrepreneurship = Blog.objects.filter(category="entrepreneurship")
    businessideas = Blog.objects.filter(category="businessideas")
    ecommerce = Blog.objects.filter(category="ecommerce")
    return render(request, "termsandconditions.html",{"smallbusiness": smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce})


def new(request):
    return render(request, "new.html")


def new2(request):
    return render(request, "new2.html")


def list(request):
    return render(request, "list.html")

def login(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["pass"]
        check = auth.authenticate(username=username, password=password)
        if check is not None:
            auth.login(request, check)
            response = redirect("/")
            return response
        else:
            msg = "Invalid Username or password"
            return render(request, "login.html", {"c": msg})
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["uname"]
        email = request.POST["email"]
        password = request.POST["pass"]
        repassword = request.POST["repass"]
        ucheck = User.objects.filter(username=username)
        echeck = User.objects.filter(email=email)
        if ucheck:
            msg = "Username Exits"
            return render(request, "register.html", {"msg": msg})
        elif echeck:
            msg = "Email Exits"
            return render(request, "register.html", {"msg": msg})
        elif password == "" or password != repassword:
            msg = "Invalid Password"
            return render(request, "register.html", {"msg": msg})
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            return redirect("/")
    else:
        return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def comment(request):
    comment_text = request.POST.get("comment")
    name = request.POST.get("user")
    pro_id = request.POST.get("id")
    slug = request.POST.get("slug")
    if comment_text and pro_id:
        comment = Comment.objects.create(
            cmt=comment_text, name=name, pro_id=pro_id)
        comment.save()
    else:
        message = "Comment could not be posted due to missing information."
        messages.warning(request, message)
    return redirect("/content/?search=" + slug + "&id=" + pro_id)

def tag(request):
    smallbusiness = Blog.objects.filter(category="smallbusiness")
    marketing = Blog.objects.filter(category="marketing")
    entrepreneurship = Blog.objects.filter(category="entrepreneurship")
    businessideas = Blog.objects.filter(category="businessideas")
    ecommerce = Blog.objects.filter(category="ecommerce")
    tagitem = request.GET.get("key")
    blog = Blog.objects.filter(tags__name=tagitem)
    random=Blog.objects.order_by('?')
    paginator = Paginator(blog, 4)
    page_number = request.GET.get('page')
    datafinal = paginator.get_page(page_number)
    totalpage = datafinal.paginator.num_pages
    return render(request, "tagdisplay.html", {"blog": blog,"random":random,"smallbusiness": smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce,"datafinal": datafinal, "lastpage": totalpage, "totalpagelist": [n+1 for n in range(totalpage)]})



def sidetag(request):
    smallbusiness = Blog.objects.filter(category="smallbusiness")
    marketing = Blog.objects.filter(category="marketing")
    entrepreneurship = Blog.objects.filter(category="entrepreneurship")
    businessideas = Blog.objects.filter(category="businessideas")
    ecommerce = Blog.objects.filter(category="ecommerce")
    random=Blog.objects.order_by('?')
    tagitem = request.GET.get("key")
    tag = Tag.objects.get(slug=tagitem)
    blog = Blog.objects.filter(tags=tag).order_by('-date')
    paginator = Paginator(blog, 4)
    page_number = request.GET.get('page')
    datafinal = paginator.get_page(page_number)
    totalpage = datafinal.paginator.num_pages
    return render(request,"sidetag.html",{"blog": blog,"random":random,"smallbusiness": smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce,"datafinal": datafinal, "lastpage": totalpage, "totalpagelist": [n+1 for n in range(totalpage)]})

def search(request):
    smallbusiness = Blog.objects.filter(category="smallbusiness")
    marketing = Blog.objects.filter(category="marketing")
    entrepreneurship = Blog.objects.filter(category="entrepreneurship")
    businessideas = Blog.objects.filter(category="businessideas")
    ecommerce = Blog.objects.filter(category="ecommerce")
    query = request.POST.get('query')
    trimmed_query = query.strip()  
    blog = Blog.objects.filter(heading__icontains=trimmed_query).order_by('-date')
    random=Blog.objects.order_by('?')
    paginator = Paginator(blog, 4)
    page_number = request.GET.get('page')
    datafinal = paginator.get_page(page_number)
    totalpage = datafinal.paginator.num_pages
    if trimmed_query:
        return render(request, 'search.html', {"blog": blog, "random":random,"smallbusiness": smallbusiness, "marketing": marketing, "entrepreneurship": entrepreneurship, "businessideas": businessideas, "ecommerce": ecommerce,"datafinal": datafinal, "lastpage": totalpage, "totalpagelist": [n+1 for n in range(totalpage)]})
    else:
        return redirect("/")


   
