class PostInlineTitleForm(forms.ModelForm):
    """제목만 편집하는 인라인 폼."""

    class Meta:
        model = Post
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'maxlength': 200,
                'autofocus': True,
            }),
        }
