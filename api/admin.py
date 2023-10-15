from django.contrib import admin
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

admin.site.register(ProductModel)
admin.site.register(InventoryModel)
admin.site.register(OrderItemModel)
admin.site.register(OrdersModel)
admin.site.register(CustomerEmployeeModel)
admin.site.register(CustomerCompanyModel)
admin.site.register(CustomerModel)
admin.site.register(PersonModel)
admin.site.register(LocationModel)
admin.site.register(PhoneNumberModel)
admin.site.register(WarehouseModel)
admin.site.register(PersonLocationModel)
admin.site.register(CountryModel)
admin.site.register(EmploymentJobsModel)
admin.site.register(RestrictedInfoModel)
admin.site.register(EmploymentModel)
