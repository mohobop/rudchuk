from django.forms import ModelForm
from model.models import Head, BodyText

class HeadForm(ModelForm):
    class Meta():
        model = Head
        # fields = ['head_title']

class HeadFormH(ModelForm):
    class Meta():
        model = Head
        fields = ['head_title']

class BodyTextForm(ModelForm):
    class Meta():
        model = BodyText
        fields = ['body_text']