from views import index_view, about_view

urls_pattern = {
    '/': index_view,
    '/about/': about_view,
}
