from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post


class PostAdminForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorUploadingWidget())