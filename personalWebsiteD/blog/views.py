from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse 


class NewTaskForm(forms.Form):
    title = forms.CharField(label="New Blog Title")
    body = forms.CharField(label="Body Text")

blogs = {"Amplification of Sense Data":"Reminds me of how, during minimum wage jobs over gap year, my philosophical thoughts were amplified. I wonder how scarcity could stimulate the brain. In a world where people detest boredom (myself included), what are we losing by trying not to lose time. This idea of wordlessness is intriguing. I get this sort of meditation from swimming. Without taking the time to slow down and think, we never make the connections between ideas and events that we need to. Maybe that is what sleep is; forced wordlessness time. Maybe the brain cannot do the connection making thing while doing the daily operation thing. If this is physically/chemically impossible, that would explain the necessity of sleep."}
# Create your views here.
def index(request):
    return render(request, "blog/index.html", {
        "blogs": blogs.items()
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data["body"]
            title = form.cleaned_data["title"]
            blogs[title] = body
            return HttpResponseRedirect(reverse("blog:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "blog/add.html", {
        "form": NewTaskForm()
    })