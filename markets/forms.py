from django import forms
from markets.models import Market

class MarketForm(forms.ModelForm):
    class Meta:
        model = Market
        fields =  [
            "market_name",
            "call_number",
            "address",
            "thumbnail",
        ]