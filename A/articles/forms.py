
from django.forms import ModelForm
from .models import Article , Sefaresh
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm  

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
    
    
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'


class SefareshForm(ModelForm):
    class Meta:
        model = Sefaresh
        fields = '__all__'


