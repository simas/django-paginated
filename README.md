django-paginated
================

Installation
------------

```
pip install django-paginated
```

and add `paginated` to project's `INSTALLED_APPS`


Example
-------

To add pagination just change from:

```python
def events(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }
    return render_to_response(request, 'events.html', context)
```

to

```python
def events(request):
    events, pagination = paginated(Event.objects.all(), request)

    context = {
        'events': events,
        'pagination': pagination,
    }
    return render_to_response(request, 'events.html', context)
```


and in template add line:

```
{{ pagination|safe }}
```
