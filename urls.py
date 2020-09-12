from views import index_view, about_view, contact_view

URLS = {
    '/': index_view,
    '/about/': about_view,
    '/contact/': contact_view,
}
