from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ReceiptSerializer
from ..models import Receipts
import json


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

# class ReceipListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Receipts.objects.all()
#         serializer = ReceiptSerializer(data=qs, many=True)
#         json_data = serializer.data
#         return Response(json_data)
#
#     def post(self, request, format=None):
#         qs = Receipts.objects.all()
#         serializer = ReceiptSerializer(qs, many=True)
#         json_data = serializer.data
#         return Response(json_data)


class ReceiptAPIView(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    # queryset = Receipts.objects.all()
    serializer_class = ReceiptSerializer

    def get_queryset(self):
        qs = Receipts.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get("id", None)
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        url_passed_id = request.GET.get('id',None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id',None)
        passed_id = url_passed_id or new_passed_id or None
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     passed_id = request.GET.get('id', None)
    #     if passed_id is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class ReceiptCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Receipts.objects.all()
#     serializer_class = ReceiptSerializer
#
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)
#
#
# class ReceiptDetailAPIView(generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Receipts.objects.all()
#     serializer_class = ReceiptSerializer
#     lookup_field = 'id'
#
#     # def get_object(self,*args,**kwargs):
#     #     kwargs = self.kwargs
#     #     kw_id = kwargs.get('id')
#     #     return Receipts.objects.get(id=kw_id)
#
#
# class ReceiptUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Receipts.objects.all()
#     serializer_class = ReceiptSerializer
#
#
# class ReceiptDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Receipts.objects.all()
#     serializer_class = ReceiptSerializer
