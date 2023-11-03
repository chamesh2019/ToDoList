from datetime import datetime, timedelta
from django.shortcuts import redirect, render
from .models import Event
from .event_form import EventForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()

    if request.GET.get('event_id'):
        event = Event.objects.get(id=request.GET.get('event_id'))
        event.finished_at = datetime.now()
        event.finished = True
        event.save()
    
    unfinished = Event.objects.filter(finished=False)
    finished = Event.objects.filter(finished=True)
    
    filtered = finished.filter(finished_at__gte=datetime.now() - timedelta(minutes=5))
    
    content = {
        'unfinished': unfinished,
        'finished': filtered,
        'form': EventForm()
    }
    
    print(content)
    
    return render(request, template_name='home.html', context=content)

def reset(request):
    # make all events unfinished and set all finished time null
    Event.objects.update(finished=False, finished_at=None)
    return redirect('home')