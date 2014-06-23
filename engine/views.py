from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

from engine.models import Event, Guest
from engine.forms import GuestSignInForm, EventCreateForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'engine/home.html'

    def get_context_data(self, **kwargs):

        return {
            'home_view': True,
            'events_view': False,
            'guests_view': False,
        }


class EventListView(TemplateView):
    template_name = 'engine/events.html'

    def get_context_data(self, **kwargs):

        return {
            'home_view': False,
            'events_view': True,
            'guests_view': False,
            'events': Event.objects.all(),
        }


class EventGuestListView(TemplateView):
    template_name = 'engine/event_guest_list.html'

    def dispatch(self, request, *args, **kwargs):

        try:
            event = Event.objects.get(pk=kwargs.get('pk'))

        except Event.DoesNotExist:
            return redirect('events')

        kwargs['event'] = event

        return super(EventGuestListView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):

        return {
            'event': kwargs.get('event'),
            #'guest_list': Guest.objects.filter(event=kwargs.get('event')),
        }


class GuestListView(TemplateView):
    template_name = 'engine/guests.html'

    def get_context_data(self, **kwargs):

        return {
            'home_view': False,
            'events_view': False,
            'guests_view': True,
            'guests': Guest.objects.all(),
        }


class GuestSignInView(FormView):
    form_class = GuestSignInForm
    template_name = 'engine/guest_signin_form.html'
    success_url = '/guests/'
    event = None

    def dispatch(self, request, *args, **kwargs):

        try:
            event = Event.objects.get(pk=kwargs.get('pk'))

        except Event.DoesNotExist:
            return redirect('events')

        self.event = event

        return super(GuestSignInView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super(GuestSignInView, self).get_context_data(**kwargs)
        context['event'] = self.event

        return context

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')

        guest = Guest.objects.create(first_name=first_name, last_name=last_name, email=email)
        guest.save()

        return super(GuestSignInView, self).form_valid(form)


class EventCreateView(FormView):
    form_class = EventCreateForm
    template_name = 'engine/event_create.html'
    success_url = '/events/'

    def form_valid(self, form):
        name = form.cleaned_data.get('name')

        event = Event.objects.create(name=name)
        event.save()

        return super(EventCreateView, self).form_valid(form)
