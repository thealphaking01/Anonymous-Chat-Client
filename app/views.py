from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib import messages
import time

val = 0
not_connected = []
connected_pairs = {}

# Create your views here.
def index(request):
    # return HttpResponse("hey")
    return render(request, "index_page.html", {})

def chat(request):
    # whole logic goes here
    return render(request, "chat.html",{})

def hit(request):
    global val
    val+=1
    return HttpResponse(val)

def connect(request,id):
    global not_connected, connected_pairs
    id = int(id)
    print not_connected,id,"here"
    try:
        a = not_connected.pop()
        connected_pairs[id] = a
        connected_pairs[a] = id
        return HttpResponse(str(a))
    except:
        not_connected.append(id)
        timeout = time.time() + 10
        val=False
        while connected_pairs.get(id,-1)==-1:
            time.sleep(1)
            if connected_pairs.get(id,-1)!=-1:
                t = connected_pairs[id]
                # not_connected.remove(t)
                not_connected.remove(id)
                return HttpResponse(connected_pairs[id])
            if time.time() > timeout:
                not_connected.remove(id)
                return HttpResponse(-1)
    return HttpResponse(str(id))

def sendText(request):
    print request.GET
    return HttpResponse("hey")