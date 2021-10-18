from rest_framework import serializers
from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


from ..models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields= [
            "username",
            "first_name",
            "last_name",
            "cedula",
            "phone",
            "email",
            "Empresa",
            ]

    #def create(self,validate_data):
     #   usuario=User.objects.create(**validate_data).id
      #  return usuario
    
class UserLoginSerializer(serializers.Serializer):
    username= serializers.CharField(min_length=8,max_length=36)
    password= serializers.CharField(min_length=8,max_length=16)

    def validate(self,data):
        #import ipdb;
        #ipdb.set_trace()
        usuario=authenticate(username=data["username"],password=data["password"])
        
        if  usuario  is  None:
            raise serializers.ValidationError("credenciales incorrectas")
        
        self.context["username"]=usuario
        return data

    def create(self,data):
        token,created= Token.objects.get_or_create(user=self.context["username"])
        return self.context["username"] , token.key

class UserSingUpSerializer(serializers.Serializer):
    username= serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        min_length=8,
        max_length=36
    )
    password= serializers.CharField(min_length=8,max_length=16)
    password_confirmation= serializers.CharField(min_length=8,max_length=16)
    email=serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    

    def validate(self,data):
        password=data["password"]
        password_config= data["password_confirmation"]
        if password != password_config:
            raise serializers.ValidationError("la contraseña no coincide")
        password_validation.validate_password(password)
        return data
    
    def create(self,data):
        data.pop("password_confirmation")
       
        user=User.objects.create_user(**data)
        return user