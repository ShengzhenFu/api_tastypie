from tastypie.api import Api
from services.api import ProductResource, OrderResource, TeamResource, TechnicalServiceResource, ServerResource
from django.urls import path, include

v1_api = Api(api_name='v1')
v1_api.register(ProductResource())
v1_api.register(OrderResource())
v1_api.register(TeamResource())
v1_api.register(TechnicalServiceResource())
v1_api.register(ServerResource())

urlpatterns = [path('api/', include(v1_api.urls))]
