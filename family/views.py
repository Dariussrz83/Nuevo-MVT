from django.shortcuts import render
from django.http import HttpResponse
from family.models import Family


def create_family(request):
   new_family = Family.objects.create()
   print(new_family)
   return HttpResponse('se creo un nuevo miembro')

def list_members(request):
    all_members = Family.objects.all()
    print(all_members)
    context = {
        'family':all_members
    }
    return render(request,'list_members.html',context=context)

