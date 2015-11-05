from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Todolist

# Create your views here.

def index(request):
    latest_todo_list = Todolist.objects.order_by('-pub_date')[:50]
    #    output = ', '.join([p.Title for p in latest_todo_list])

#template = loader.get_template('taskmanager/index.html')
    context = RequestContext(request, {
                             'latest_todo_list': latest_todo_list,
                             })
    return render(request, 'taskmanager/index.html', context)

def detail(request, Title_id):
    todolist = get_object_or_404(Todolist, pk=Title_id)
    return render(request, 'taskmanager/detail.html', {'todolist': todolist})

def results(request, Title_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % Title_id)

#def vote(request, Title_id):
#    return HttpResponse("You're voting on question %s." % Title_id)

