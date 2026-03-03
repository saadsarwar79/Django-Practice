from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "content", "category"]
        exclude = ["author"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        qs = Post.objects.filter(title=title)
        if self.instance and getattr(self.instance, "pk", None):
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Title must be unique.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) < 100:
            raise forms.ValidationError(
                "Content must be at least 100 characters long."
            )
        return content