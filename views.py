from base.templator import render


def index_view(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('index.html', secret=secret)


def about_view(request):
    secret = request.get('secret_key', None)
    return '200 OK',  render('about.html', secret=secret)

