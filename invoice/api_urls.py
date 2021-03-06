from django.conf.urls import include, url
from invoice import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'fiscalpositions', views.FiscalPositionViewSet)
router.register(r'contacts', views.ContactInvoiceViewSet)
router.register(r'companies', views.CompanyInvoiceViewSet)
router.register(r'vats', views.VATViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'invoicelines', views.InvoiceLineViewSet)
router.register(r'invoicetypes', views.InvoiceTypeViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(
    r'fiscalpositionshaveinvoicetypesallowed',
    views.FiscalPositionHasInvoiceTypeAllowedViewSet,
    base_name='fiscalpositionhasinvoicetypeallowed'
)

app_name = 'invoice'
urlpatterns = [
    url(
        r'^companies/(?P<pk>\d+)/products/$',
        views.ProductsByCompanyList.as_view(),
        name='companyinvoice-products'
    ),
    url(
        r'^companies/(?P<pk>\d+)/invoices/$',
        views.InvoicesByCompanyList.as_view(),
        name='companyinvoice-invoices'
    ),
    url(
        r'^contacts/(?P<pk>\d+)/invoices/$',
        views.InvoicesByContactList.as_view(),
        name='contactinvoice-invoices'
    ),
    url(
        r'^products/(?P<pk>\d+)/invoicelines/$',
        views.InvoiceLinesByProductList.as_view(),
        name='product-invoicelines'
    ),
    url(
        r'^vats/(?P<pk>\d+)/products/$',
        views.ProductsByVATList.as_view(),
        name='vat-products'
    ),
    url(
        r'^fiscalpositions/(?P<pk>\d+)/companies/$',
        views.CompaniesByFiscalPositionList.as_view(),
        name='fiscalposition-companies'
    ),
    url(
        r'^fiscalpositions/(?P<pk>\d+)/contacts/$',
        views.ContactsByFiscalPositionList.as_view(),
        name='fiscalposition-contacts'
    ),
    url(
        r'^invoicetypes/(?P<pk>\d+)/invoices$',
        views.InvoicesByInvoiceTypeList.as_view(),
        name='invoicetype-invoices'
    ),
    url(
        r'^invoicetypes/bills/$',
        views.InvoiceTypesByBillClassList.as_view(),
        name='invoicetype-bills'
    ),
    url(
        r'^invoicetypes/debits/$',
        views.InvoiceTypesByDebitClassList.as_view(),
        name='invoicetype-debits'
    ),
    url(
        r'^invoicetypes/credits/$',
        views.InvoiceTypesByCreditClassList.as_view(),
        name='invoicetype-credits'
    ),
    url(r'^', include(router.urls)),
]
