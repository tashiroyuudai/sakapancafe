from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Menu,Category
from django.shortcuts import render, redirect

class IndexView(ListView):
    template_name = 'index.html'
    model = Menu
    context_object_name = 'menu_items'  # contextの名前を変更
    paginate_by = 6  # ページネーションを設定する場合
    
    def get_queryset(self):
        return Menu.objects.order_by('?')[:6]
    
class MenuView(ListView):
    template_name = 'menu.html'
    model = Menu
    context_object_name = 'menu_items'  # contextの名前を変更
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorylist = Category.objects.all()
        context['category'] = categorylist
        menulistset = []
        for categorys in categorylist:
            menulist = Menu.objects.filter(category=categorys.id)
            menulistset.append(menulist)
        context['menu'] = menulistset
        print(context['menu'])
        return context

    def get_queryset(self):
        return Menu.objects.order_by('category')
    
class DetaView(DetailView):
    template_name = 'post.html'
    model = Menu
