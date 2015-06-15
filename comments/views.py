from django.views.generic import TemplateView

class Narrative(TemplateView):
    slug = 'index'
    template_name = 'comments/narrative.html'


# @register.simple_tag()
# def user_picture(user, missing='http://gtd.wfp.org/static/images/profile-pic.gif'):
#     try:
#         url = 'http://gtd.wfp.org/media/pictures/auto/{0.email}.jpg'.format(user)
#         # r = requests.get(url, timeout=5)
#         # assert r.status_code == 200
#         return url
#     except (ConnectionError, ConnectTimeout, ReadTimeout, AttributeError, AssertionError):
#         pass
#     return missing