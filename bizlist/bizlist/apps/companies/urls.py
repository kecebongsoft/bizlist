from django.conf.urls.defaults import patterns, url

from .views import CompanyListView, CompanyDetailView, ProductListView, ProductDetailView

urlpatterns = patterns('companies.views',
    url(r'^myanmar-burma-companies/(?P<state>[-\w]+)/(?P<category>[-\w]+)/(?P<sub_category>[-\w]+)/$', CompanyListView.as_view(), name='company_list'),
    url(r'^myanmar-burma-products/(?P<state>[-\w]+)/(?P<category>[-\w]+)/(?P<sub_category>[-\w]+)/$', ProductListView.as_view(), name='product_list'),
    url(r'^company/(?P<company_pk>\d+)/(?P<company_slug>[-\w]+)/$', CompanyDetailView.as_view(), name='company_detail'),
    url(r'^company/(?P<company_pk>\d+)/(?P<company_slug>[-\w]+)/product/(?P<product_pk>\d+)/(?P<product_slug>[-\w]+)/$', ProductDetailView.as_view(), name='product_detail'),

)
