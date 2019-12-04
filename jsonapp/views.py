import json
from git import Repo, remote
import os
import subprocess
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# backend handler
def openjsonfile():
    global data
    global jsonfiledirectory
    jsonfiledirectory = os.path.dirname(
        "/home/wilson/cosas para aprender/pagina web/frontend/portfolio/2019/art/data/")
    jsonData = open(jsonfiledirectory+"/data.json")
    data = json.load(jsonData)


def savejson():
    jsonfiledirectory = os.path.dirname(
        "/home/wilson/cosas para aprender/pagina web/frontend/portfolio/2019/art/data/")
    with open(jsonfiledirectory+'/data.json', 'w') as jsonfile:
        json.dump(data, jsonfile)


# Create your views here.
def main(request):
    return render(request, "jsonapp/menu.html")


def add(request):
    if request.method == "POST":
        openjsonfile()
        toadd = request.POST.copy()
        if toadd.get("id") != "":
            newEntry = {toadd.get("id"): {
                "title": toadd.get("title"),
                "description": toadd.get("description"),
                "mainImage": toadd.get("rootUrl"),
                "extraImages": toadd.get("filenames"),
                "software": toadd.get("software"),
                "tags": toadd.get("tags")
            }}
            data["id"].update(newEntry)
            savejson()

        return HttpResponseRedirect("/view")

    else:
        openjsonfile()
        return render(request, "jsonapp/add.html")


def view(request):
    if request.method == "POST":
        openjsonfile()
        toadd = request.POST.copy()
        if toadd.get("id") != "":
            newEntry = {toadd.get("id"): {
                "title": toadd.get("title"),
                "description": toadd.get("description"),
                "mainImage": toadd.get("rootUrl"),
                "extraImages": toadd.get("filenames"),
                "software": toadd.get("software"),
                "tags": toadd.get("tags")
            }}
            data["id"].update(newEntry)
            savejson()
        return HttpResponseRedirect("/view")
    else:
        openjsonfile()
        return render(request, "jsonapp/view.html", {"datos": data})


def deleteid(request):
    openjsonfile()
    todelete = request.GET.get("id")
    del data["id"][todelete]
    savejson()
    return HttpResponseRedirect("/view")


def gitcontrol(request):
    openjsonfile()
    if request.method == "POST":
        commitdata = request.POST.copy()

        repo = Repo("/home/wilson/cosas para aprender/pagina web/frontend/portfolio/2019/art")
        repo.index.add("*")
        repo.git.commit("-m", commitdata.get("commitname"))
        origin = repo.remote(name='origin')
        origin.push()
        return HttpResponse("<h1>Check the console</h1>")

    return render(request, "jsonapp/gitcontrol.html")
