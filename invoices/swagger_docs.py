# # swagger_docs.py
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
# from .serializers import InvoiceSerializer
#
# # Swagger for POST method (Create Invoice)
# invoice_post_swagger = swagger_auto_schema(
#     operation_description="Create a new invoice along with its details.",
#     operation_summary="Create Invoice",
#     request_body=InvoiceSerializer,
#     responses={
#         201: openapi.Response(
#             description="Invoice created successfully.",
#             schema=InvoiceSerializer
#         ),
#         400: openapi.Response(
#             description="Invalid input, please check your data.",
#             schema=openapi.Schema(
#                 type=openapi.TYPE_OBJECT,
#                 properties={
#                     'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
#                     'detail': openapi.Schema(type=openapi.TYPE_STRING, description='Detailed error explanation')
#                 }
#             )
#         )
#     }
# )
#
# # Swagger for PUT method (Update Invoice)
# invoice_put_swagger = swagger_auto_schema(
#     operation_description="Update an existing invoice along with its details.",
#     operation_summary="Update Invoice",
#     request_body=InvoiceSerializer,
#     responses={
#         200: openapi.Response(
#             description="Invoice updated successfully.",
#             schema=InvoiceSerializer
#         ),
#         404: openapi.Response(
#             description="Invoice not found with the provided ID.",
#             schema=openapi.Schema(
#                 type=openapi.TYPE_OBJECT,
#                 properties={
#                     'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message')
#                 }
#             )
#         ),
#         400: openapi.Response(
#             description="Invalid input, please check your data.",
#             schema=openapi.Schema(
#                 type=openapi.TYPE_OBJECT,
#                 properties={
#                     'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
#                     'detail': openapi.Schema(type=openapi.TYPE_STRING, description='Detailed error explanation')
#                 }
#             )
#         )
#     }
# )
#
#

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import InvoiceSerializer

# Swagger for POST method (Create Invoice)
invoice_post_swagger = swagger_auto_schema(
    operation_description="Create a new invoice along with its details.",
    operation_summary="Create Invoice",
    request_body=InvoiceSerializer,  # Request body does not include 'id'
    responses={
        201: openapi.Response(
            description="Invoice created successfully.",
            schema=InvoiceSerializer
        ),
        400: openapi.Response(
            description="Invalid input, please check your data.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
                    'detail': openapi.Schema(type=openapi.TYPE_STRING, description='Detailed error explanation')
                }
            )
        )
    }
)

# Swagger for PUT method (Update Invoice)
invoice_put_swagger = swagger_auto_schema(
    operation_description="Update an existing invoice along with its details.",
    operation_summary="Update Invoice",
    request_body=InvoiceSerializer,  # The 'id' is handled via the URL, not the body
    responses={
        200: openapi.Response(
            description="Invoice updated successfully.",
            schema=InvoiceSerializer
        ),
        404: openapi.Response(
            description="Invoice not found with the provided ID.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message')
                }
            )
        ),
        400: openapi.Response(
            description="Invalid input, please check your data.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
                    'detail': openapi.Schema(type=openapi.TYPE_STRING, description='Detailed error explanation')
                }
            )
        )
    }
)


