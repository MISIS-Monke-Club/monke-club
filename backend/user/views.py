from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserBio

User = get_user_model()


class BobritoBanditoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            bio = UserBio.objects.filter(user=user).first()
            bio_data = {
                "description": bio.description if bio else "",
                "photo": bio.photo.url if bio and bio.photo else None,
                "rating": str(bio.rating) if bio else "0.0",
                "course": bio.course if bio else 1,
                "faculty": bio.faculty if bio else "",
            }

            data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                **bio_data,
            }
            return Response(data)
        except User.DoesNotExist:
            return Response({"detail": "Пользователь не найден."}, status=404)

    def put(self, request, username):
        try:
            user = User.objects.get(username=username)
            new_username = request.data.get("username", user.username)
            new_email = request.data.get("email", user.email)
            new_password = request.data.get("password")

            user.username = new_username
            user.email = new_email
            if new_password:
                user.set_password(new_password)
            user.save()

            bio, _ = UserBio.objects.get_or_create(user=user)
            bio.description = request.data.get("description", bio.description)
            bio.rating = request.data.get("rating", bio.rating)
            bio.course = request.data.get("course", bio.course)
            bio.faculty = request.data.get("faculty", bio.faculty)
            bio.save()

            data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "description": bio.description,
                "rating": str(bio.rating),
                "course": bio.course,
                "faculty": bio.faculty,
            }
            return Response(data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"detail": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, username):
        try:
            user = User.objects.get(username=username)
            new_username = request.data.get("username")
            new_email = request.data.get("email")
            new_password = request.data.get("password")

            if new_email is not None:
                user.email = new_email
            if new_username is not None:
                user.username = new_username
            if new_password is not None:
                user.set_password(new_password)
            user.save()

            bio, _ = UserBio.objects.get_or_create(user=user)
            if "description" in request.data:
                bio.description = request.data["description"]
            if "rating" in request.data:
                bio.rating = request.data["rating"]
            if "course" in request.data:
                bio.course = request.data["course"]
            if "faculty" in request.data:
                bio.faculty = request.data["faculty"]
            bio.save()

            data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "description": bio.description,
                "rating": str(bio.rating),
                "course": bio.course,
                "faculty": bio.faculty,
            }
            return Response(data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"detail": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, username):
        try:
            user = User.objects.get(username=username)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(
                {"detail": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND
            )


class CreateBobritoBandito(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"detail": "username и password обязательны"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if User.objects.filter(username=username).exists():
            return Response(
                {"detail": "Пользователь с таким username уже существует"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not email:
            return Response(
                {"detail": "email обязателен"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        # сразу создаём пустой UserBio
        UserBio.objects.create(user=user)

        data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
        return Response(data, status=status.HTTP_201_CREATED)

    def get(self, request):
        users = User.objects.all()
        data = []
        for user in users:
            bio = UserBio.objects.filter(user=user).first()
            bio_data = {
                "description": bio.description if bio else "",
                "rating": str(bio.rating) if bio else "0.0",
                "course": bio.course if bio else 1,
                "faculty": bio.faculty if bio else "",
            }
            data.append(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "slug": user.username,
                    **bio_data,
                }
            )
        return Response(data, status=status.HTTP_200_OK)
