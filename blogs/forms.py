# forms.py
from django import forms
from .models import *

class HotelForm(forms.ModelForm):

	class Meta:
		model = Hotel
		fields = ['name', 'hotel_Main_Img']

class GeeksForm(forms.Form):	
    #name = forms.CharField(label=False,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Enter your name"}))
	#<input type="text" class="form-control" name="name" placeholder="Enter your name" required>
    geeks_field = forms.FileField(label=False,widget=forms.FileInput(attrs={'class': 'form-control'}))
	#<input type="file" name="pdf_file" class="form-control" accept=".pdf" title="Upload PDF" />

class UploadFileForm(forms.ModelForm):  
    #Act_Status = forms.CharField(label=False)
    file = forms.FileField(label=False)
    class Meta:  
        model = UploadFileForm  
        fields = "__all__"
 
    def __init__(self, *args, **kwargs):
            super(UploadFileForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'