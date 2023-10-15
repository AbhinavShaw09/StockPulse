# Generated by Django 4.2.5 on 2023-10-14 10:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('country_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=24)),
                ('country_code', models.CharField(max_length=3)),
                ('nat_lang_code', models.IntegerField()),
                ('currency_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCompanyModel',
            fields=[
                ('company_id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=45)),
                ('company_credit_limit', models.IntegerField()),
                ('credit_limit_currency', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerEmployeeModel',
            fields=[
                ('customer_employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('badge_number', models.CharField(max_length=20)),
                ('job_title', models.CharField(max_length=45)),
                ('department', models.CharField(max_length=45)),
                ('credit_limit', models.IntegerField()),
                ('credit_limit_currency', models.CharField(max_length=5)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_employee', to='api.customercompanymodel')),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentJobsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr_job_id', models.IntegerField()),
                ('job_title', models.CharField(max_length=45)),
                ('min_salary', models.IntegerField()),
                ('max_salary', models.IntegerField()),
                ('countries_country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_model', to='api.countrymodel')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_id', models.IntegerField()),
                ('warehouse_id', models.IntegerField()),
                ('quantity_on_hand', models.IntegerField()),
                ('quantity_available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('location_id', models.IntegerField(primary_key=True, serialize=False)),
                ('address_line_1', models.CharField(max_length=45)),
                ('address_line_2', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=24)),
                ('district', models.CharField(max_length=24)),
                ('postal_code', models.CharField(max_length=20)),
                ('location_type_code', models.IntegerField()),
                ('description', models.TextField()),
                ('shipping_notes', models.TextField()),
                ('countries_country_id', models.IntegerField()),
                ('country_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='persons_location', to='api.countrymodel')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_item_id', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('person_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=45)),
                ('nick_name', models.CharField(max_length=20)),
                ('nat_lang_code', models.IntegerField()),
                ('gender', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.IntegerField()),
                ('weight_class', models.IntegerField()),
                ('warranty_period', models.IntegerField(blank=True, null=True)),
                ('supplier_id', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=15)),
                ('list_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('minimum_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_currency', models.CharField(max_length=5)),
                ('catalog_url', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_name', models.CharField(max_length=45)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_location', to='api.locationmodel')),
                ('warehouse_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse', to='api.inventorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='RestrictedInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('date_of_death', models.DateField(default=datetime.date.today)),
                ('government_id', models.CharField(max_length=24)),
                ('passport_id', models.CharField(max_length=24)),
                ('hire_date', models.DateField(default=datetime.date.today)),
                ('seniority_code', models.IntegerField()),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restricted_info', to='api.personmodel')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumberModel',
            fields=[
                ('phone_number_id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_number', models.IntegerField()),
                ('country_code', models.IntegerField()),
                ('phone_type_id', models.IntegerField()),
                ('locations_location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_location', to='api.locationmodel')),
                ('persons_person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='api.personmodel')),
            ],
        ),
        migrations.CreateModel(
            name='PersonLocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_address', models.CharField(max_length=45)),
                ('location_usage', models.CharField(max_length=45)),
                ('notes', models.TextField()),
                ('locations_location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons_location', to='api.locationmodel')),
                ('persons_person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons_person', to='api.personmodel')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('sales_rep_id', models.IntegerField()),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
                ('order_code', models.IntegerField()),
                ('order_status', models.CharField(max_length=15)),
                ('order_total', models.IntegerField()),
                ('order_currency', models.CharField(max_length=5)),
                ('promotion_code', models.CharField(max_length=45)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='api.orderitemmodel')),
            ],
        ),
        migrations.AddField(
            model_name='orderitemmodel',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_product', to='api.productmodel'),
        ),
        migrations.AddField(
            model_name='inventorymodel',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='api.productmodel'),
        ),
        migrations.CreateModel(
            name='EmploymentModel',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('manager_employee_id', models.IntegerField()),
                ('star_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('salary', models.IntegerField()),
                ('commission_percentage', models.CharField(max_length=5)),
                ('hr_job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_info', to='api.employmentjobsmodel')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employment_of_person', to='api.personmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_mgr_id', models.IntegerField()),
                ('Income_level', models.IntegerField()),
                ('customer_employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_employee', to='api.customeremployeemodel')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='api.ordersmodel')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_customer', to='api.personmodel')),
            ],
        ),
    ]
