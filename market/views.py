from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response



@api_view(['GET'])
def api_root(request, format=None):

    response = Response({
        'products': reverse('product-list', request=request, format=format),
        'product-create': reverse('product-create', request=request, format=format),

        'categories': reverse('category-list', request=request, format=format),
        'categories-create': reverse('category-create', request=request, format=format),

        'product items': reverse('product-item-list', request=request, format=format),

        'sign-up': reverse('user-create', request=request, format=format)
    })
    return response
