# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Invoice
# from .serializers import InvoiceSerializer
# from .swagger_docs import invoice_post_swagger, invoice_put_swagger
#
# from django.http import HttpResponse
#
# def home_view(request):
#     return HttpResponse("Welcome to the Invoice API! Go to /swagger/ for API documentation.")
#
#
#
# class InvoiceCreateOrUpdateView(APIView):
#     @invoice_post_swagger
#     def post(self, request):
#         # Handle creation of a new invoice with details
#         serializer = InvoiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     @invoice_put_swagger
#     def put(self, request, pk):
#         # Handle update of an existing invoice with details
#         try:
#             invoice = Invoice.objects.get(pk=pk)
#         except Invoice.DoesNotExist:
#             return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = InvoiceSerializer(invoice, data=request.data, partial=True)  # Support partial updates
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice
from .serializers import InvoiceSerializer
from .swagger_docs import invoice_post_swagger, invoice_put_swagger
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("Welcome to the Invoice API! Go to /swagger/ for API documentation.")


class InvoiceCreateOrUpdateView(APIView):

    # POST method for creating a new invoice
    @invoice_post_swagger
    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT method for updating an existing invoice
    @invoice_put_swagger
    def put(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceSerializer(invoice, data=request.data, partial=True)  # Support partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
