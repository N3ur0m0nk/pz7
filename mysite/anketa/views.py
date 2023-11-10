from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, CreateView, DetailView, UpdateView, ListView

from mysite.anketa.models import Vopros
from mysite.car.models import MyCar


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosView(ListView):
	model = Vopros
	context_object_name = 'vopros_list'
	success_url = reverse_lazy('anketa: Vopros')

	#paginate_by = item_for_page
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(VoprosView,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name_plural
		context['col1name'] = self.model._meta.get_field("title").verbose_name
		context['col2name'] = self.model._meta.get_field("score").verbose_name
		context['col3name'] = self.model._meta.get_field("navik1").verbose_name
		context['collastname'] = 'Cервисы'
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosUpdate(UpdateView):
	model = Vopros
	template_name_suffix = '_update_form'
	fields = '__all__'
	success_url = '/car/mycar/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(VoprosUpdate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'name','color'}
		context['secslovar'] = {'nomb'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosDetail(DetailView):
	model = Vopros
	context_object_name = 'mycar_one'
	success_url = '/car/mycar/'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(VoprosDetail,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['slovar'] = {'name','color'}
		context['secslovar'] = {'nomb'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		context['model'] = self.model
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosCreate(CreateView):
	model = Vopros
	context_object_name = 'mycar_one'
	success_url = '/car/mycar/'

	template_name_suffix = '_create_form'
	fields = '__all__'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(VoprosCreate,self).get_context_data(**kwargs)
		context['sometry'] = self.model._meta.verbose_name
		context['model'] = self.model
		context['slovar'] = {'name','color'}
		context['secslovar'] = {'nomb'}
		context['hidenslovar'] = {'id'}
		context['dopslovar'] = {'updated_at','erem','edesc','created_at'}
		return context

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class VoprosDelete(DeleteView):
	model = Vopros
	success_url = '/car/mycar/'



