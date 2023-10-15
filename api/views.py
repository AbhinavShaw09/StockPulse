from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    ProductModel,
    InventoryModel,
    OrderItemModel,
    OrdersModel,
    CustomerEmployeeModel,
    CustomerCompanyModel,
    CustomerModel,
    PersonModel,
    LocationModel,
    PhoneNumberModel,
    WarehouseModel,
    PersonLocationModel,
    CountryModel,
    EmploymentJobsModel,
    RestrictedInfoModel,
    EmploymentModel,
)
from .serializers import (
    ProductModelSerializers,
    InventoryModelSerializers,
    OrderItemModelSerializer,
    OrdersModelSerializer,
    CustomerEmployeeModelSerializer,
    CustomerCompanyModelSerializer,
    CustomerModelSerializer,
    PersonModelSerializer,
    LocationModelSerializer,
    PhoneNumberModelSerializer,
    WarehouseModelSerializer,
    PersonLocationModelSerializer,
    CountryModelSerializer,
    EmploymentJobsModelSerializer,
    RestrictedInfoModelSerializer,
    EmploymentModelSerializer,
)


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializers
    http_method_names = ["get", "post",'delete']
    # permission_classes = [IsAuthenticated]


class InventoryModelViewSet(viewsets.ModelViewSet):
    queryset = InventoryModel.objects.all()
    serializer_class = InventoryModelSerializers
    http_method_names = ["get", "post",'delete']
    # permission_classes = [IsAuthenticated]


class OrderItemModelViewSet(viewsets.ModelViewSet):
    queryset = OrderItemModel.objects.all()
    serializer_class = OrderItemModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class OrdersModelViewSet(viewsets.ModelViewSet):
    queryset = OrdersModel.objects.all()
    serializer_class = OrdersModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class CustomerEmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = CustomerEmployeeModel.objects.all()
    serializer_class = CustomerEmployeeModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class CustomerCompanyModelViewSet(viewsets.ModelViewSet):
    queryset = CustomerCompanyModel.objects.all()
    serializer_class = CustomerCompanyModelSerializer
    http_method_names = ["get", "post",'delete']
    # permission_classes = [IsAuthenticated]


class CustomerModelViewSet(viewsets.ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class PersonModelViewSet(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = PersonModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class LocationModelViewSet(viewsets.ModelViewSet):
    queryset = LocationModel.objects.all()
    serializer_class = LocationModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class PhoneNumberModelViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumberModel.objects.all()
    serializer_class = PhoneNumberModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = WarehouseModel.objects.all()
    serializer_class = WarehouseModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class PersonLocationModelViewSet(viewsets.ModelViewSet):
    queryset = PersonLocationModel.objects.all()
    serializer_class = PersonLocationModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class CountryModelViewSet(viewsets.ModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = CountryModelSerializer
    http_method_names = ["get", "post","delete"]
    # permission_classes = [IsAuthenticated]


class EmploymentJobsModelViewSet(viewsets.ModelViewSet):
    queryset = EmploymentJobsModel.objects.all()
    serializer_class = EmploymentJobsModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class RestrictedInfoModelViewSet(viewsets.ModelViewSet):
    queryset = RestrictedInfoModel.objects.all()
    serializer_class = RestrictedInfoModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]


class EmploymentModelViewSet(viewsets.ModelViewSet):
    queryset = EmploymentModel.objects.all()
    serializer_class = EmploymentModelSerializer
    http_method_names = ["get", "post"]
    # permission_classes = [IsAuthenticated]
