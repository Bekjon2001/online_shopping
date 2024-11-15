from apps.contact.models import Contact


from django import forms

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'