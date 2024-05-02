from .models import Product
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer


class ProductListAPIView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10  # 페이지당 아이템 수를 설정
        products = Product.objects.all()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)  # 현재 로그인한 사용자를 상품의 작성자로 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductPutDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        print(product.author)
        print(request.user)
        if product.author != request.user:  # 상품 작성자와 요청자가 다른 경우 권한 없음
            return Response({"error": "You don't have permission to edit this product."},
                            status=status.HTTP_403_FORBIDDEN)
        serializer = ProductSerializer(
            product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.author != request.user:  # 상품 작성자와 요청자가 다른 경우 권한 없음
            return Response({"error": "You don't have permission to delete this product."},
                            status=status.HTTP_403_FORBIDDEN)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
