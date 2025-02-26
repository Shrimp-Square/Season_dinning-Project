from django import forms
from markets.models import Market
from users.models import User

class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields =  [
            "name",
            "call_number",
            "address",
            "tags",
        ]