import os
import django
from rango.models import Page,Category

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
django.setup()


#
def add_page(cat, title, url, views=0):
    page = Page.objects.get_or_create(category=cat, title=title)[0]
    page.url=url
    page.views=views
    page.save()
    return page

#
def add_cat(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes
    category.save()
    return category
#
def populate():
    python_pages = [
        {'title':'Learn Python in 10 Minutes','url':'http://www.korokithakis.net/tutorials/python/','views':11},
        {'title':'How to Think like a Computer Scientist','url':'http://www.greenteapress.com/thinkpython/','views': 49},
        {'title': 'Official Python Tutorial','url':'http://docs.python.org/3/tutorial/','views': 101} ]
    
    django_pages = [
        {'title':'Django Rocks', 'url':'http://www.djangorocks.com/','views': 0},
        {'title':'Official Django Tutorial','url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 31},
        {'title':'How to Tango with Django', 'url':'http://www.tangowithdjango.com/',  'views': 1008} ]
    
    other_pages = [
        {'title':'Flask', 'url':'http://flask.pocoo.org','views': 60},
        {'title':'Bottle','url':'http://bottlepy.org/docs/dev/', 'views': 51} ]
    
    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},'Django': {'pages': django_pages, 'views': 64, 'likes': 32},'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }
    
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()