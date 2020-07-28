from views import IndexView, About, Contacts

routes = {
    '/': IndexView(),
    '/about/': About(),
    '/contacts/': Contacts(),
}