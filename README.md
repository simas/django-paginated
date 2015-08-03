================
django-paginated
================

To add pagination just change from:

'''
def events(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }
    return render_to_response(request, 'events.html', context)
'''

to

'''
def events(request):
    events, pagiantion = paginated(Event.objects.all(), request)

    context = {
        'events': events,
        'pagination': pagination,
    }
    return render_to_response(request, 'events.html', context)
'''


and in template add line:

'''
{{ pagination|safe }}
'''
