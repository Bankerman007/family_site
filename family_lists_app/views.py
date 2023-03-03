from django.shortcuts import render
from . models import Events,Need,Issue,Repair
from . forms import EventsForm
from django.http import HttpResponseRedirect

def base(request):
    items = Events.objects.all()
    needs_week=Need.objects.all()
    issues_week=Issue.objects.all()
    repairs_week=Repair.objects.all()
    return render(request,'base.html',{'items':items,'needs_week':needs_week,'issues_week':issues_week,'repairs_week':repairs_week})

def cards(request):
    items = Events.objects.all()
    return render(request, "cards.html",{'items':items,})

def add_items_form(request):
        submitted=False
        if request.method == "POST":
            form = EventsForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/')
            
        else:
            form = EventsForm
            if 'submitted' in request.GET:
                submitted = True
        return render(request, 'add_items_form.html', {'form': form, 'submitted': submitted})