from django import template

from blog.models import Category

register = template.Library()


#  здесь мы пишем тэмплейт тэг для последующей подгрузки в header и footer
@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}


