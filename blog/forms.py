from django import forms
from .models import Section, Post
from django.core.exceptions import ValidationError

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Нельзя использовать это имя.')
        if Section.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Это имя уже используется.')
        return new_slug

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'filename','sections', 'similardoc_title', 'similardoc_filename']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'filename': forms.TextInput(attrs={'class': 'form-control'}),
            'sections': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'similardoc_title': forms.TextInput(attrs={'class': 'form-control'}),
            'similardoc_filename': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean_similardoc_filename(self):
        new_similardoc_filename = self.cleaned_data['similardoc_filename'].lower()

        return new_similardoc_filename.split('.')[0]

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()


        if new_slug == 'create':
            raise ValidationError('Нельзя использовать это имя.')
        return new_slug
