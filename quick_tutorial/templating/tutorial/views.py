from pyramid.view import view_config


@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {'name': 'Home View'}


@view_config(route_name='hello')
def hello(request):
    return {'name': 'Hello View'}
