from django import forms
from .models import Receipts, ReceiptSteps


class ReceiptsForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'content', 'ingredients', 'image_main')
        model = Receipts


    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError('content is too long')
        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content =="":
            content = None
        image = data.get("image", None)
        if content is None:# and image is None
            raise forms.ValidationError('content or image is required.')
        return super().clean(*args, **kwargs)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Загаловок"
        self.fields["content"].label = "Описание"
        self.fields["ingredients"].label = "Ингредиенты"
        self.fields["image_main"].label = "Картинка"



class ReceipStepsForm(forms.ModelForm):
    class Meta:
        fields = ()
        model = ReceiptSteps
