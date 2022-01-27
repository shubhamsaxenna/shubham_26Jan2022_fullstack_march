from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import AllCoupons

class Coupans(APIView):
    def get(self, request):
        result = []
        for item in AllCoupons.objects.all():
            data = {
                "id": item.id,
                "name":item.code,
                "discountpercentage" : item.discountPercent,
                "fixeddiscount" : item.fixeddiscount,
                "minamounttouse" : item.minAmounttouse
            }
            result.append(data)
        return Response(result)

    def post(self, request):
        return Response("Post response")

    def put(self, request):
        return Response("Put response")

    def delete(self, request):
        return Response("Delete response")