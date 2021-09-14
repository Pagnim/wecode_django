from django.db.models.expressions import F
from django.shortcuts import render

import json

from django.http     import JsonResponse
from django.views    import View

from owner.models import Dogs, Owners

class OwnerView(View):

    def post(self, request):
        
        data = json.loads(request.body)
        Owners.objects.create(

            name  = data['name'],
            email = data['email'],
            age   = data['age']

        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)

    # def get(self,request):
        
    #         results= []
    #         owners = Owners.objects.all()
    #         dogs = Dogs.objects.all()

    #         for owner in owners:
    #                 for dog in dogs:             

    #                         results.append({
                                
    #                                 'name'      : owner.name ,
    #                                 'age'       : owner.age ,
    #                                 'email'     : owner.email,
    #                                 'dogname'   : dog.name,
    #                                 'dogage'    : dog.age,
                                    
    #                         })
                    
    #         return JsonResponse({'owners' : results}, status=200)


    def get(self,request):
            
            results= []
            owners = Owners.objects.all()

            for owner in owners:    
                dogresults =[]
                dogs = owner.dogs_set.all()

                for dog in dogs:

                        dogresults.append({
                            
                                'dogname'    : dog.name,
                                'dogage'     : dog.age,
                                
                        })

                results.append({
                    
                        'name'      : owner.name ,
                        'age'       : owner.age ,
                        'email'     : owner.email,
                        'dogresult' : dogresults
                        
                })
                    
                    
            return JsonResponse({'owners' : results}, status=200)


class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dogs.objects.create(

            name  = data['name'],
            age   = data['age'],
            owner = Owners.objects.get(name = data["owner"])

        )

        return JsonResponse({'MESSAGE':'CREATED'}, status=201)
    
    def get(self,request):

            results = []
            dogs = Dogs.objects.all()

            for dog in dogs :
                    results.append(
                        {

                            "name"  : dog.name ,
                            "age"   : dog.age ,
                            "owner" : dog.owner.name ,

                        }
                    )
            return JsonResponse({"result" : results}, status=200)
    

'''

class OwnerGetView(View):
        def get(self,request):
            
                results= []
                owners = Owners.objects.all()

                for owner in owners:
                    results.append({

                            'name'  : owner.name ,
                            'email' : owner.email ,
                            'age'   : owner.age ,
                            
                    })
                return JsonResponse({'result' : results}, status=200)

class DogGetView(View):
     def get(self,request):

            results = []
            dogs = Dogs.objects.all()

            for dog in dogs :
                    results.append(
                        {

                            "name"  : dog.name ,
                            "age"   : dog.age ,
                            "owner" : dog.owner.name ,

                        }
                    )
            return JsonResponse({"result" : results}, status=200)

'''