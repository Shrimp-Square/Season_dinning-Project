from django import forms
from django.core.exceptions import ValidationError
from users.models import User
import requests
import json
from urllib import parse

class LoginForm(forms.Form):
    username = forms.CharField(min_length=4,
                               widget = forms.TextInput(
                                   attrs={"placeholder": "사용자명 (4자리 이상)"},
                               )
                                )
    password = forms.CharField(min_length=4,
                               widget = forms.PasswordInput(
                                   attrs = {"placeholder": "비밀번호 (4자리 이상)"},
                               )
                               )
    
class SignupForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
                                   attrs={"placeholder": "사용자명 (4자리 이상)"},))
    password1 = forms.CharField(widget = forms.PasswordInput(
                                   attrs = {"placeholder": "비밀번호 (4자리 이상)"},))
    password2 = forms.CharField(widget = forms.PasswordInput(
                                    attrs = {"placeholder": "비밀번호를 다시 입력하세요."},))
    profile_image = forms.ImageField(required=False)
    email = forms.CharField(widget = forms.TextInput(
                                   attrs={"placeholder": "이메일을 입력하세요"},))
    business_number = forms.CharField(max_length=10, widget = forms.TextInput(
                                   attrs={"placeholder": "사업자에 해당할 경우 10자리"},),
                                    required=False)
    

    def clean_username(self):
        username = self.cleaned_data["username"]

        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력하신 사용자명 ({username})은 이미 사용 중입니다.")
        return username

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            self.add_error("password2", "비밀번호가 일치하지 않습니다.")

    def clean_business_number(self):
        business_number = self.cleaned_data.get('business_number')

        if not business_number:
            return business_number

        api_key = "W6vMZdYroc3q6MHdKq5Efvho9N+fFvosadtaAMU4Itek72+2yRGAMVHHsyUcnfHpeDJ/YRMW3QZktT4Vm7/Hhg=="
        api_key = parse.quote(api_key)

        api_url = f"http://api.odcloud.kr/api/nts-businessman/v1/status?serviceKey={api_key}"

        # params = (('seviceKey', api_key),)

        data = { "b_no" : [ business_number ]}
        headers =  {
            'accept': 'application/json',
            'Authorization': api_key,
            'Content-Type': 'application/json',
            }
        response = requests.post(api_url, data = json.dumps(data), headers = headers)

        if response.status_code == 200:
            res = response.json()
            print(res)

            # 사업자등록번호가 유효한지 확인 
            if res.get("match_cnt") == 1 :
                return business_number
            else:
                raise forms.ValidationError("유효하지 않은 사업자등록번호입니다.")
        else:
            print(response.text)
            raise forms.ValidationError("사업자등록번호 검증에 실패했습니다. 다시 시도해 주세요.")
    
    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]
        profile_image = self.cleaned_data["profile_image"]
        email = self.cleaned_data["email"]
        business_number = self.cleaned_data["business_number"]

        user = User.objects.create_user(
            username = username,
            password = password1,
            profile_image = profile_image,
            email = email,
            business_number = business_number
        )
        
        return user

