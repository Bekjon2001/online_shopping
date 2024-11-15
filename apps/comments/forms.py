from apps.comments.models import ProductComment


from django import forms

class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = ProductComment
        fields = '__all__'



