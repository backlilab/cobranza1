import requests
from collections import OrderedDict
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import pagination, permissions
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework import permissions


class PageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 999999

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_number', self.page.number),
            ('num_pages', self.page.paginator.num_pages),
            ('per_page', self.page.paginator.per_page),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        authorization = request.META.get('HTTP_AUTHORIZATION')

        if not authorization:
            return None

        url = settings.URL_AUTHENTICATION_VERIFY
        headers = {'Authorization': authorization}

        try:
            response = requests.get(url, headers=headers, verify=False, timeout=5)
        except Exception as ex:
            raise exceptions.AuthenticationFailed(ex)

        if response.status_code == 200:
            data = response.json()
        else:
            try:
                data = response.json()
            except:
                data = response.text
                raise Exception(data)

            raise exceptions.AuthenticationFailed(data)

        user_data = data.get('usuario', {})

        user = User()
        user.id = user_data.get('id')
        user.nombre = user_data.get('nombre')
        user.apellido = user_data.get('apellido')
        user.email = user_data.get('email')
        user.perfil = user_data.get('perfil')
        user.perfil_descripcion = user_data.get('perfil_descripcion')
        user.cliente = user_data.get('cliente')
        user.cliente_nombre = user_data.get('cliente_nombre')
        user.externo = user_data.get('externo')
        user.restablecer_password = user_data.get('restablecer_password')

        return (user, None)


class IsNotExternalUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return not request.user.externo

class NeedUpdatePassword(permissions.BasePermission):

    def has_permission(self, request, view):
        return not request.user.restablecer_password