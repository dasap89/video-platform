from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from .models import Video
from .forms import VideoForm


class VideoListView(ListView):
	model = Video
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(VideoListView, self).get_context_data(**kwargs)
		q = self.request.GET.get('q')
		if q:
			objs = Video.objects.filter(title__icontains=q)
		else:
			objs = Video.objects.all()
		context['rent_videos'] = objs.filter(rent_available=False)
		context['available_videos'] = objs.filter(rent_available=True)
		return context


class VideoDetailView(DetailView):
	model = Video
	template_name = 'video_details.html'
	form_class = VideoForm

	def get_context_data(self, **kwargs):
		context = super(VideoDetailView, self).get_context_data(**kwargs)
		context['form'] = VideoForm
		return context

	def post(self, request, *args, **kwargs):
		obj = self.get_object()
		form_data = obj.__dict__
		form_data['rent_by'] = request.POST.get('rent_by')
		form_data['rent_by_phone'] = request.POST.get('rent_by_phone')
		
		form = VideoForm(form_data)

		if form.is_valid():
			obj.rent_by = form_data['rent_by']
			obj.rent_by_phone = form_data['rent_by_phone']
			obj.rent_available = False
			obj.rent_manager = request.user
			obj.save()
			return redirect('video-list')
		else:
			return redirect('video_details', pk=form.pk)


class ReturnView(DetailView):
	form_class = VideoForm
	model = Video

	def post(self, request, *args, **kwargs):
		obj = self.get_object()
		obj.rent_by = obj.rent_by_phone = obj.rent_manager = None
		obj.rent_available = True

		obj.save()

		return redirect('video-list')

