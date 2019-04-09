from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json
from customerapi.models import Customer
from rest_framework.views import APIView
from rest_framework.response import Response


class CustomerView(APIView):

    def cust_display(req):
        details = Customer.objects.all()
        data = [(i.cust_name, i.cust_address, i.cust_dept) for i in details]
        return HttpResponse(json.dumps(data))

    def get_display(self, request, pk=None, format=None):
        details = Customer.objects.get(id=1)
        # data = [(d.cust_name,d.cust_address,d.cust_dept) for d in details]
        return Response(details.cust_address)

    def post_display(self, request, format=None):
        data = self.request.data
        #customer = Customer(**data)
        customer = Customer(cust_name=data.get("Arav"),cust_address=data.get("New York"), cust_dept=data.get("Security"))
        #res = Customer(**data)
        customer.save()
        return Response("Customer created successfully!!")

    def put_display(self, request, pk, format=None):
        data1 = Customer.objects.get(id=2)
        data1 = self.request.data
        print(data1)
        if "Ishaan" in data1:
            data1.cust_name = data1.get("Ram")
        if "San Jose" in data1:
            data1.cust_address = data1.get("Cupertino")
        if "Sales" in data1:
            data1.cust_dept = data1.get("XXXX")

        data1.save()
        resp = Response("Customer updated successfully!!")
        print(resp)

    def delete_display(self,request,pk,format=None):
        data = Customer.objects.get(id=pk)
        data.delete()
        return Response("Customer deleted successfully!!")


