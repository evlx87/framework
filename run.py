from base.core import CoreApp
from urls import urls_pattern


def secret_controller(request):
    request['secret_key'] = 'SECRET'


front = [
    secret_controller
]


application = CoreApp(urls_pattern, front)
