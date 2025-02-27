from django import forms
from markets.models import Market
from users.models import User
from markets.models import Comment

class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields =  [
            "name",
            "call_number",
            "address",
            "content",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "market",
            "content",
        ]
        widgets = {
            "content" : forms.Textarea(
                attrs = {
                    "placeholder" : "리뷰 작성..."
                }
            )
        }