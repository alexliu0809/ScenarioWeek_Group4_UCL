from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Task, Todolist


class IndexView(generic.ListView):
    template_name = 'taskmanager/index.html'
    context_object_name = 'latest_todo_list'
    
    def get_queryset(self):
        return Todolist.objects.order_by('-pub_date')[:50]


class DetailView(generic.DetailView):
    model = Todolist
    template_name = 'taskmanager/detail.html'