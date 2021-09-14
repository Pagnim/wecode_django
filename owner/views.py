from django.shortcuts import render

import json

from django.http     import JsonResponse
from django.views    import View

from owner.models import Dogs, Owners

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owners.objects.create(

            name  = data['name'],
            email = data['email'],
            age   = data['age']

        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        dog = Dogs.objects.create(

            name  = data['name'],
            age   = data['age'],
            owner = Owners.objects.get(name = data["owner"])

        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)
