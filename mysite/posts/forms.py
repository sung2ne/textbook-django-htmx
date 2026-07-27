'title': forms.TextInput(attrs={
    'class': 'form-control',
    'aria-describedby': 'error-title',
    'hx-post': reverse_lazy('posts:validate'),
    ...
}),
