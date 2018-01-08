from django.http import HttpResponse
from django.shortcuts import render

from add.models import Test

#添加的方法
def add(request):
    stul=Test(name='王琪',sex='男',age='23')
    stul.save()
    return render(request,'wq.html')

#查询的方法
def select(request):
    # list=Test.objects.all() #Queryset
    # print(type(list))
    list=Test.objects.filter(name='王琪')
    return render(request,'list.html',{'list':list})

#修改的方法1
def update(request):
    list1=Test.objects.get(id=1)
    list1.name='魏东'
    list1.save()
    list=Test.objects.all()
    return render(request,'update.html',{'list':list})

#修改方法2
def update2(request):
    lise=Test.objects.filter(id=2).update(name="贾旭")
    print(lise)
    if lise>0:
        return HttpResponse("修改成功")
    else:
        return HttpResponse("修改失败")

#删除的方法1
def dele(request):
    list1=Test.objects.get(id=3)
    list1.delete()
    list=Test.objects.all()
    return render(request,'success1.html',{'list':list})

#删除的方法2
def del2(request):
    list=Test.objects.get(id=4).delete()
    print(type(list))
    if len(list)>0:
        return HttpResponse("删除成功")
    else:
        return HttpResponse("删除失败")