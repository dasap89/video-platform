from .models import Video
from django.forms import ModelForm


class VideoForm(ModelForm):

    class Meta:
        model = Video
        fields = ('rent_by', 'rent_by_phone',)