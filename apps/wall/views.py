from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def wall(request):
    context = {
        "messages" : Message.objects.all(),    
    }
    return render(request, 'wall/index.html', context)

def postMessage(request):
    currentUser = User.objects.get(id=request.session['activeuser'])
    newMessage = Message.objects.create(message=request.POST['message'], creator=currentUser)
    return redirect('/wall')

def postComment(request):
    currentUser = User.objects.get(id=request.session['activeuser'])
    currentMessage = Message.objects.get(id=request.POST['message_id'])
    newComment = Comment.objects.create(comment=request.POST['comment'], creator=currentUser, parent_message=currentMessage)
    return redirect('/wall')

def deleteMessage(request, id):
    c = Message.objects.get(id=id)
    c.delete()
    return redirect('/wall')

def deleteComment(request, id):
    c = Comment.objects.get(id=id)
    c.delete()
    return redirect('/wall')


def logout(request):
    request.session.clear()
    return redirect('/')
