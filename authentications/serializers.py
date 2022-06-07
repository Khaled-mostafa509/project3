from django.db import models
from rest_framework import serializers ,permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate , login
from .models import Person,Company,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'is_person']

            
class CompanyCustomRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    phone_number=serializers.CharField(source='Company.phone_number')
    tax_number=serializers.CharField(source='Company.tax_number')
    location=serializers.CharField(source='Company.location')
    class Meta:
        model=User
        fields=['username','email','password', 'password2','phone_number','tax_number','location']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_company=True
        user.save()
        
        user =Company (user=user,
                phone_number=self.validated_data.get('phone_number'),
                tax_number= self.validated_data.get('tax_number'),
                location= self.validated_data.get('location'),
            ),
        user.save()
        Company.objects.create(user=user)
        return user
    
    def get_cleaned_data(self):
            data = super(CompanyCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'phone_number' : self.validated_data.get('phone_number', ''),
                'tax_number': self.validated_data.get('tax_number', ''),
                'location': self.validated_data.get('location', ''),
            }
            data.update(extra_data)
            return data

class PersonCustomRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    phone_number=serializers.CharField(source='Person.phone_number')
    address=serializers.CharField(source='Person.address')
    class Meta:
        model=User
        fields=['username','email','password', 'password2','phone_number','address']
        extra_kwargs={
            'password':{'write_only':True}
        }
    

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_person=True
        user.save()
        Person.objects.create(user=user)
        return user



class LoginSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6 , write_only=True) 
    class Meta:
        
        model= User
        fields = ('email','password','token')
        read_only_fields = ['token']