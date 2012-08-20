from pyramid.response import Response
from pyramid.view import view_config


from .models import (
    DBSession,
    FASUser,
    Topic,
    )

@view_config(route_name='index', renderer='index.mak')
def index(request):
    return {}

@view_config(route_name='choose_topics', renderer='prefs.mak')
def topics(request):
    return {}
@view_config(route_name='login', renderer='login.mak')
def login(request):
    return {}

@view_config(route_name='logout', renderer='logout.mak')
def logout(request):
    return {}
