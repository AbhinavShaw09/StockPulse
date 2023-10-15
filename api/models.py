from django.db import models
from django.utils import timezone
from datetime import date


class ProductModel(models.Model):
    product_id = models.IntegerField(null=True, blank=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.IntegerField()
    weight_class = models.IntegerField()
    warranty_period = models.IntegerField(null=True, blank=True)
    supplier_id = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=15)
    list_price = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=2
    )
    minimum_price = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=2
    )
    price_currency = models.CharField(max_length=5)
    catalog_url = models.CharField(max_length=128)

    def __str__(self):
        return self.product_name


class InventoryModel(models.Model):
    inventory_id = models.IntegerField()
    product_id = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, related_name="product"
    )
    warehouse_id = models.IntegerField()
    quantity_on_hand = models.IntegerField()
    quantity_available = models.IntegerField()

    def __str__(self):
        return self.product_id.product_name


class OrderItemModel(models.Model):
    order_item_id = models.IntegerField()
    order_id = models.IntegerField()
    product_id = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, related_name="ordered_product"
    )
    unit_price = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=2
    )
    quantity = models.FloatField()

    def __str__(self) -> str:
        return self.product_id.product_name


class OrdersModel(models.Model):
    order_id = models.ForeignKey(
        OrderItemModel, on_delete=models.CASCADE, related_name="order_item"
    )
    customer_id = models.IntegerField()
    sales_rep_id = models.IntegerField()
    order_date = models.DateField(default=timezone.now)
    order_code = models.IntegerField()
    order_status = models.CharField(max_length=15)
    order_total = models.IntegerField()
    order_currency = models.CharField(max_length=5)
    promotion_code = models.CharField(max_length=45)

    def __str__(self) -> str:
        return f"{self.order_code}"


class CustomerCompanyModel(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=45)
    company_credit_limit = models.IntegerField()
    credit_limit_currency = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.company_name


class CustomerEmployeeModel(models.Model):
    customer_employee_id = models.IntegerField(primary_key=True)
    company_id = models.ForeignKey(
        CustomerCompanyModel,
        on_delete=models.CASCADE,
        related_name="customer_employee",
    )
    badge_number = models.CharField(max_length=20)
    job_title = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    credit_limit = models.IntegerField()
    credit_limit_currency = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.department


class PersonModel(models.Model):
    person_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=45)
    nick_name = models.CharField(max_length=20)
    nat_lang_code = models.IntegerField()
    gender = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.first_name


class CustomerModel(models.Model):
    customer_id = models.ForeignKey(
        OrdersModel, on_delete=models.CASCADE, related_name="customer"
    )
    person_id = models.ForeignKey(
        PersonModel, on_delete=models.CASCADE, related_name="person_customer"
    )
    customer_employee_id = models.ForeignKey(
        CustomerEmployeeModel,
        on_delete=models.CASCADE,
        related_name="customer_employee",
    )
    account_mgr_id = models.IntegerField()
    Income_level = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.account_mgr_id}"


class CountryModel(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=24)
    country_code = models.CharField(max_length=3)
    nat_lang_code = models.IntegerField()
    currency_code = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.country_name


class LocationModel(models.Model):
    location_id = models.IntegerField(primary_key=True)
    country_id = models.OneToOneField(
        CountryModel, on_delete=models.CASCADE, related_name="persons_location"
    )
    address_line_1 = models.CharField(max_length=45)
    address_line_2 = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=24)
    district = models.CharField(max_length=24)
    postal_code = models.CharField(max_length=20)
    location_type_code = models.IntegerField()
    description = models.TextField()
    shipping_notes = models.TextField()
    countries_country_id = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.state}.{self.city}"


class PhoneNumberModel(models.Model):
    phone_number_id = models.IntegerField(primary_key=True)
    persons_person_id = models.ForeignKey(
        PersonModel, on_delete=models.CASCADE, related_name="person"
    )
    locations_location_id = models.ForeignKey(
        LocationModel, on_delete=models.CASCADE, related_name="number_location"
    )
    phone_number = models.IntegerField()
    country_code = models.IntegerField()
    phone_type_id = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.persons_person_id.first_name}"


class WarehouseModel(models.Model):
    warehouse_id = models.ForeignKey(
        InventoryModel, on_delete=models.CASCADE, related_name="warehouse"
    )
    location_id = models.ForeignKey(
        LocationModel,
        on_delete=models.CASCADE,
        related_name="warehouse_location",
    )
    warehouse_name = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.warehouse_name


class PersonLocationModel(models.Model):
    persons_person_id = models.ForeignKey(
        PersonModel, on_delete=models.CASCADE, related_name="persons_person"
    )
    locations_location_id = models.ForeignKey(
        LocationModel, on_delete=models.CASCADE, related_name="persons_location"
    )
    sub_address = models.CharField(max_length=45)
    location_usage = models.CharField(max_length=45)
    notes = models.TextField()

    def __str__(self) -> str:
        return self.persons_person_id.first_name


class EmploymentJobsModel(models.Model):
    hr_job_id = models.IntegerField()
    countries_country_code = models.ForeignKey(
        CountryModel, on_delete=models.CASCADE, related_name="job_model"
    )
    job_title = models.CharField(max_length=45)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()

    def __str__(self) -> str:
        return self.countries_country_code.country_name


class RestrictedInfoModel(models.Model):
    person_id = models.ForeignKey(
        PersonModel, on_delete=models.CASCADE, related_name="restricted_info"
    )
    date_of_birth = models.DateField(default=date.today)
    date_of_death = models.DateField(default=date.today)
    government_id = models.CharField(max_length=24)
    passport_id = models.CharField(max_length=24)
    hire_date = models.DateField(default=date.today)
    seniority_code = models.IntegerField()

    def __str__(self) -> str:
        return self.person_id.first_name


class EmploymentModel(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(
        PersonModel,
        on_delete=models.CASCADE,
        related_name="employment_of_person",
    )
    hr_job_id = models.ForeignKey(
        EmploymentJobsModel,
        on_delete=models.CASCADE,
        related_name="employee_info",
    )
    manager_employee_id = models.IntegerField()
    star_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    salary = models.IntegerField()
    commission_percentage = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.person_id.first_name
