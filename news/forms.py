from django import forms
from .widgets import CustomClearableFileInput
from .models import NewsHeadline


class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsHeadline
        fields = '__all__'

    image = forms.ImageField(label="Titelbild", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        news_articles = NewsHeadline.objects.all()
        # friendly_names = [(n.get_friendly_name()) for n in news_articles]

        # self.fields['heading'].choices = friendly_names

