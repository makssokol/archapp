def funny_front(request):
    request['funny'] = ':)))))'


def sad_front(request):
    request['sad'] = ':((((('


front_list = [funny_front, sad_front]
