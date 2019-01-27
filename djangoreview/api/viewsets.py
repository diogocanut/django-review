from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Review.objects.all()
        else:
            return Review.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            ip_address=get_client_ip(self.request),
            user=self.request.user
        )
