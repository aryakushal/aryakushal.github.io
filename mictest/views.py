from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    #return HttpResponse("Dang! Working.")
    context = { "theNorth" : [ { "id" : 1, "name" : "John Snow" }, { "id" : 2, "name" : "Daenarys Targeryn" } ] }
    template = loader.get_template('mictest/index.html')
    return HttpResponse( template.render(context, request) )

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)

