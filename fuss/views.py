from pyramid.response import Response
from pyramid.view import view_config, forbidden_view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
        remember,
        forget,
        )
import velruse
import models as m

@view_config(route_name='index', renderer='index.mak')
def index(request):
    return {}

@view_config(route_name='prefs', renderer='prefs.mak')
def topics(request):
    return {}

@view_config(route_name='login', renderer='login.mak')
@forbidden_view_config(renderer='login.mak')
def login(request):
    url = "/"
    fas_url = "https://admin.fedoraproject.org/accounts/openid/id/"
    username = request.params.get('fas_username')
    if username:
        identifier = "openid_identifier={0}{1}".format(fas_url, username)
        url = velruse.login_url(request, 'openid') + "?" + identifier
        return HTTPFound(location=url)
    return {}

@view_config(context='velruse.AuthenticationComplete')
def login_complete_view(request):
    context = request.context
    username = context.profile['accounts'][0]['username'].split('/')[1]
    if m.FASUser.query.filter_by(username=username).count() == 0:
        new_user = m.FASUser(username=username)
        m.DBSession.add(new_user)
    headers = remember(request, username)
    response = HTTPFound(location="/")
    response.headerlist.extend(headers)
    return response

@view_config(context='velruse.AuthenticationDenied', renderer='json')
def login_denied_view(request):
    return {'result': 'denied'}

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.resource_url(request.context),
            headers=headers)
