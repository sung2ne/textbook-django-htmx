from common.sanitize import clean_html


class PostCreateForm(forms.ModelForm):
    ...

    def clean_content(self):
        return clean_html(self.cleaned_data.get('content'))
