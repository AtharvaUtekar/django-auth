# iveri/serializers.py
from rest_framework import serializers
from .models import PersonalDetails
from users.models import NewUser

# class PersonalDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonalDetails
#         fields = ['middle_name', 'adhaar_number', 'pan_number']  # Add other fields as required
#         extra_kwargs = {
#             'middle_name': {'required': False},
#             'adhaar_number': {'required': False},
#             'pan_number': {'required': False},
#         }


class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = ['middle_name', 'adhaar_number', 'pan_number']  # Add other fields as required
