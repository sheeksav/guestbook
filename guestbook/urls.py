from django.conf.urls import patterns, include, url

from engine.views import HomeView, EventListView, GuestListView, EventGuestListView, GuestSignInView, EventCreateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guestbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^events/$', EventListView.as_view(), name='events'),
    url(r'^events/guests/(?P<pk>\d+)/$', EventGuestListView.as_view(), name='events-guest-list'),
    url(r'^events/guests/add/$', EventCreateView.as_view(), name='event-create'),

    url(r'^guests/', GuestListView.as_view(), name='guests'),
    url(r'^guest/sign/$', GuestSignInView.as_view(), name='guest-sign-in'),

)

