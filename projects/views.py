from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q 
from .models import Project, Tag
from .forms import ProjectForm
from django.contrib import messages
from.utils import searchProjects
from django.core.paginator import Paginator

# Create your views here.
def projects(request):
    projects, search_query = searchProjects(request)
    
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projects, results)
    
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
        
    context = {'projects':projects, 'search_query':search_query, 'paginator':paginator}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single_projects.html', {
        'project': projectObj,
        })

@login_required(login_url="lo gin")
def CreateProject(request):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, "Project Created Successfully")
            return redirect('projects')
    
    context= {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def UpdateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project Updated Successfully")
            return redirect('account')
    
    context= {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def DeleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted Successfully")
        return redirect('account')
    context = {'object':project}
    return render(request, 'delete_template.html', context)