from django.shortcuts import render

from .models import Menu, SubMenu, Noticia


def index(request):
    menus = Menu.objects.filter().order_by('id')
    submenus = SubMenu.objects.filter().order_by('id')
    noticias = Noticia.objects.filter(age__contains='2023').order_by('-id')[:3]
    return render(request, 'index.html', {'menus': menus,'submenus': submenus,'noticias': noticias})
def about(request):
    menus = Menu.objects.filter().order_by('id')
    submenus = SubMenu.objects.filter().order_by('id')
    noticias = Noticia.objects.filter(age__contains='2023').order_by('-id')[:3]
    return render(request, 'about.html', {'menus': menus,'submenus': submenus,'noticias': noticias})
def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')
def project(request):
    return render(request, 'project.html')
def single(request):
    return render(request, 'single.html')