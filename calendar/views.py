from django.views.generic import ListView, DetailView
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    # Add any additional view customizations as per your requirements

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
    # Add any additional view customizations as per your requirements
