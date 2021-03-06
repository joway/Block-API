from django.db.transaction import non_atomic_requests
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from captcha.exceptions import LinkCaptchaError, LinkCaptchaExpired, VerifyTimeFrequently
from sendcloud.exceptions import SendcloudError
from user.constants import ANONYMOUS_USER
from utils.permissions import IsAdminOrSelf, check_permission
from .exceptions import EmailExist, UserNotExist, PasswordError, UserHasActivated
from .models import User
from .serializers import UserSerializer, ProfileChangeSerializer, UserAuthSerializer, \
    UserLinkActivateSerializer
from .services import UserService


class ProfileViewSet(viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin):
    """
    用户个人信息
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    def list(self, request, *args, **kwargs):
        """
        获取用户自己的信息
        """
        if not request.user.is_authenticated():
            serializer = self.get_serializer(data=ANONYMOUS_USER)
            serializer.is_valid(raise_exception=True)
        else:
            serializer = self.get_serializer(request.user)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        """
        修改用户信息
        """
        check_permission((IsAuthenticated, IsAdminOrSelf), self, request)
        instance = request.user
        serializer = ProfileChangeSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


class AuthViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    @list_route(methods=['post'])
    @non_atomic_requests
    def register(self, request):
        """
        注册
        """
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            UserService.register(email=serializer.data['email'], password=serializer.data['password'])
            return Response(data={'detail': '注册成功'}, status=status.HTTP_200_OK)
        except EmailExist:
            return Response(data={'detail': '邮箱已被注册'}, status=status.HTTP_403_FORBIDDEN)
        except VerifyTimeFrequently:
            return Response(data={'detail': '获取验证码过于频繁'}, status=status.HTTP_403_FORBIDDEN)
        except SendcloudError:
            return Response(data={'detail': '服务器邮件发送失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @list_route(methods=['post'])
    @non_atomic_requests
    def login(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            token = UserService.login(serializer.data['email'], serializer.data['password'])
            return Response(data={'token': token}, status=status.HTTP_200_OK)
        except UserNotExist:
            return Response(data={'detail': '用户不存在'}, status=status.HTTP_404_NOT_FOUND)
        except PasswordError:
            return Response(data={'detail': '用户密码错误'}, status=status.HTTP_403_FORBIDDEN)

    @list_route(methods=['post'])
    @non_atomic_requests
    def activate(self, request):
        serializer = UserLinkActivateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            UserService.activate(alink_verify_code=serializer.data['captcha'])
            return Response(data={'detail': '激活成功'}, status=status.HTTP_200_OK)
        except LinkCaptchaError:
            return Response(data={'detail': '验证码错误'}, status=status.HTTP_403_FORBIDDEN)
        except UserHasActivated:
            return Response(data={'detail': '用户已经激活'}, status=status.HTTP_403_FORBIDDEN)
        except LinkCaptchaExpired:
            return Response(data={'detail': '验证码过期'}, status=status.HTTP_403_FORBIDDEN)
