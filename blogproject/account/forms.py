from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname', 'university', 'major']

# 상속 이라는게 UserCreationForm에 있는 속성과 메소드를 모두 사용할 수 있기 때문에
# RegisterForm이 다 상속 받고 Meta 클래스를 CustomUser로 바꿔줌으로써
# CustomUser에 맞는 form으로 바꿀 수 있다.
