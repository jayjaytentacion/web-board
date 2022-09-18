
from django.shortcuts import render,get_object_or_404
from .models import Board, Topic
from .forms import NewTopicForm

# Create your views here.
def index(request):
    context={
        'boards':Board.objects.all()
    }
    return render(request,'index.html',context)


def board_topics(request,pk):
    board=get_object_or_404(Board,pk=pk)
    topics=Topic.objects.filter(board=board)
    context={
        'board':board,
        'topics':topics
    }
    return render(request,'topics.html',context)



def new_topic(request,pk):
    board=get_object_or_404(Board,pk=pk)
    topics=Topic.objects.filter(board=board)
    context={
        'board':board,
       'form':NewTopicForm,
        'topics':topics
    }
    
    

    return render(request,'new_topic.html',context)