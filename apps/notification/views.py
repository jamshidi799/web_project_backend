from apps.notification.models import Notification
from apps.notification.serializers import NotificationSerializer
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class NotificationList(GenericAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        notifications = Notification.objects.filter(target=request.user)
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationDetail(GenericAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self, pk):
        try:
            return Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        notification = self.get_object(pk)
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)