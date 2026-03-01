from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import QRHistory
from .serializers import QRSerializer
# REGISTER
@api_view(["POST"])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return Response({"error": "User exists"}, status=400)

    User.objects.create_user(username=username, password=password)
    return Response({"message": "User created"})


# SAVE QR
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def save_qr(request):
    serializer = QRSerializer(data={
        "user": request.user.id,
        "value": request.data.get("value"),
        "type": request.data.get("type"),
    })

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


# HISTORY
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def history(request):
    qs = QRHistory.objects.filter(user=request.user)
    return Response(QRSerializer(qs, many=True).data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_qr(request, pk):

    try:
        qr = QRHistory.objects.get(id=pk, user=request.user)
        qr.delete()
        return Response({"deleted": True})

    except QRHistory.DoesNotExist:
        return Response({"error": "Not found"}, status=404)