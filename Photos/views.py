from typing import Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormAddPhoto
from .forms import FormAddCategory
from .models import Shot
from .models import Category
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (DetailView,
                                  CreateView,
                                  DeleteView)


def home(request):
    return render(request, 'Photos/home.html', {})



def gallery(request):
    requested_category = request.GET.get('category_name')
    if requested_category == None:
        photos = Shot.objects.all()        
    else:
        photos = Shot.objects.filter(category__category_name=requested_category)
    categories = Category.objects.all()    
    context = {'categories': categories, 'photos': photos}
    return render(request, 'Photos/shot_list.html', context)


class ViewOne(DetailView):
    model = Shot


class AddCategoryView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = FormAddCategory

    def get_success_message(self, cleaned_data: Dict[str, str]) -> str:
        return f"Category '{cleaned_data.get('category_name')}' was added"



class AddPhotoView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Shot
    form_class = FormAddPhoto

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.camera_man = self.request.user
        return super().form_valid(form)
    
    def get_success_message(self, cleaned_data: Dict[str, str]) -> str:
        return f"Picture '{cleaned_data.get('title')}' was added"
    

class DeletePhoto(SuccessMessageMixin, DeleteView):
    model = Shot
    success_url = reverse_lazy('gallery')
    success_message = 'Picture was deleted'

