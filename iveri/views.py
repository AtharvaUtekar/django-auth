from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PersonalDetails
from .serializers import PersonalDetailsSerializer
from rest_framework.response import Response

"""
class PersonalDetailsView(generics.RetrieveUpdateAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user)

        response = {
                'success': True,
                'message': 'Created successfully.',
                'data': {
                    'user_role': user.role,
                    'user_email': user.email,
                    'user_id': user.id,
                    
                }
            }

        return Response(response)
"""


class PersonalDetailsView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        personal_details, _ = PersonalDetails.objects.get_or_create(user=self.request.user)
        return personal_details

    def create(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)