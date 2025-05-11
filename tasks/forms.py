from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a comment...',
                'class': 'form-control',
            }),
        }
        error_messages = {
            'content': {
                'required': 'Please enter a comment before submitting.',
                'max_length': 'Your comment is too long. Please shorten it.',
            },
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError('Comment cannot be empty.')
        if len(content) > 500:
            raise forms.ValidationError('Comment cannot exceed 500 characters.')
        return content
