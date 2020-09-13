from base.templator import render


def index_view(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('index.html', secret=secret)


def about_view(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('about.html', secret=secret)


def contact_view(request):
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Получено сообщение от\t {email}\n'
              f'Тема сообщения:\t {title}\n'
              f'Содержимое сообщения:\t {text}\n')
    return '200 OK', render('contact.html')
