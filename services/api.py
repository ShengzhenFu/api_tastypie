from tastypie.resources import ModelResource
from services.models import Product, Order, Team, TechnicalService, Server
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from rest_framework import serializers


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        fields = ['name', 'price']
        filtering = {'price': ['exact', 'lt', 'lte', 'gt', 'gte']}
        allowed_methods = ['get']
        # authentication = ApiKeyAuthentication()


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        allowed_methods = ['get', 'post', 'put']


class TeamResource(ModelResource):
    class Meta:
        queryset = Team.objects.all()
        resource_name = 'Team'
        allowed_methods = ['get']


class TechnicalServiceResource(ModelResource):
    class Meta:
        queryset = TechnicalService.objects.all()
        resource_name = 'TechnicalService'
        allowed_methods = ['get']


class ServerResource(ModelResource):
    class Meta:
        queryset = Server.objects.all()
        resource_name = 'Server'
        fields = ['server_name', 'server_status', 'server_environment',
                  'server_function', 'server_location',
                  'team_id', 'ts_id']
        filtering = {'tid': 'exact',
                     'ts_id': 'exact'}
        allowed_methods = ['get']


