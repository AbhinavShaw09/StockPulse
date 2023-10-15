from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
    ),
    public=True,
)

router = DefaultRouter()
router.register(r"product", views.ProductModelViewSet, basename="product")
router.register(r"inventory", views.InventoryModelViewSet, basename="inventory")
router.register(
    r"order-item", views.OrderItemModelViewSet, basename="order_item"
)
router.register(r"orders", views.OrdersModelViewSet, basename="orders")
router.register(
    r"customer-employee",
    views.CustomerEmployeeModelViewSet,
    basename="customer_employee",
)
router.register(
    r"customer-company",
    views.CustomerCompanyModelViewSet,
    basename="customer_company",
)
router.register(
    r"customer-model",
    views.CustomerModelViewSet,
    basename="customer_model",
)
router.register(
    r"person",
    views.PersonModelViewSet,
    basename="person",
)
router.register(
    r"location",
    views.LocationModelViewSet,
    basename="location",
)
router.register(
    r"phone-number",
    views.PhoneNumberModelViewSet,
    basename="phone_number",
)
router.register(
    r"warehouse",
    views.WarehouseModelViewSet,
    basename="warehouse",
)
router.register(
    r"person-location",
    views.PersonLocationModelViewSet,
    basename="person_location",
)
router.register(
    r"country",
    views.CountryModelViewSet,
    basename="country",
)
router.register(
    r"employment-jobs",
    views.EmploymentJobsModelViewSet,
    basename="employment_jobs",
)
router.register(
    r"restricted-info",
    views.RestrictedInfoModelViewSet,
    basename="restricted_info",
)
router.register(
    r"employment",
    views.EmploymentModelViewSet,
    basename="employment",
)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "docs/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "docs/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
