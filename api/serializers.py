from rest_framework import serializers
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


class ProductModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class InventoryModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = InventoryModel
        fields = "__all__"


class OrderItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        fields = "__all__"


class OrdersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersModel
        fields = "__all__"


class CustomerEmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerEmployeeModel
        fields = "__all__"


class CustomerCompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCompanyModel
        fields = "__all__"


class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = "__all__"


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = "__all__"


class PhoneNumberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumberModel
        fields = "__all__"


class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = "__all__"


class WarehouseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseModel
        fields = "__all__"


class PersonLocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonLocationModel
        fields = "__all__"


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = "__all__"

class EmploymentJobsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentJobsModel
        fields = "__all__"
        
class RestrictedInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestrictedInfoModel
        fields = "__all__"
        
class EmploymentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentModel
        fields = "__all__"