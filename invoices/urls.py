from django.urls import path
from .views import InvoiceCreateOrUpdateView

urlpatterns = [
    path('', InvoiceCreateOrUpdateView.as_view(), name='invoice-create'),  # POST to create
    path('<int:pk>/', InvoiceCreateOrUpdateView.as_view(), name='invoice-update'),  # PUT to update
]

