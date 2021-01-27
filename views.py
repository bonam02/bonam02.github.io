from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
import json
from .models import Student
from .models import Table1
from .models import user_details
from .serializers import *
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

globalFlag = True


@api_view(['GET','POST'])
def students_register(request):
    if request.method == "GET":
        return JsonResponse("hai",safe=False)
    else:
        data = json.loads(request.body)
        payload = data['payload']
        print(payload)
        first_name = payload['first_name']
        userID = payload['userID']
        pwd = payload['password']
        user = User.objects.create_user(payload['userID'],password=pwd)
        user.is_active = True
        bb = user.save()
        return JsonResponse("hai",safe=False)


@api_view(['GET','POST'])
def students_upload(request):
    print("Method type ::: ", request.method)
    flag = True
    if request.method == 'POST':
        data = json.loads(request.body)
        payload = data['payload']
        final_data = json.loads(payload)
        if globalFlag:
            try:
                for each_obj in final_data:
                    data_base = user_details(id=each_obj["id"], user_id=each_obj["userId"], title=each_obj['title'],
                                             body=each_obj["body"])
                    data_base.save()
            except Exception as e:
                flag = False
        else:
            flag = False
        if flag:
            print("Data Saved successfully...")
        else:
            print("Exception while saving data into database...")

        get_user_data = user_details.objects.all()

        list = []
        for person in get_user_data:
            dict_map = {}
            dict_map["id"] = person.id
            dict_map["user_id"] = person.user_id
            dict_map["title"] = person.title
            dict_map["body"] = person.body
            list.append(dict_map)
    print("list ::: ",list)
    #data = [{"id":"1","user_id":"1","title":"hai","body":"1234"},{"id":"2","user_id":"12","title":"sri","body":"hai"}]
    return JsonResponse({'data': list, 'flag': "true"}, status=200)

@api_view(['GET','POST'])
def students_login(request):
    print("Method type ::: ",request.method)
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, context={'request': request}, many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        print(data,type(data))
        payload = data['payload']
        print("payload ",payload)
        userName = payload['userid']
        password = payload['password']
        request.session['userName'] = userName
        users = User.objects.all()

        print(" userName ::: ",userName," password ::: ",password)

        errorMessage = None
        try:
            user = User.objects.get(username=userName)
            print("Dadaad",user)
            if userName == "sbonam" :
                return JsonResponse({'userName': userName,"flag":"true"}, status=200)
        except Exception as e:
            errorMessage = "User does not exist"
            print("--Exception--",e)

        print("error ",errorMessage)
        if errorMessage is not None:
            return JsonResponse({ 'errorMessage': errorMessage,"flag":"false" }, status=500)
        print("user ", user)
        if user is None:
            print("ooo")
            totalData = Student.objects.all()
            serializer = StudentSerializer(totalData, context={'request': request}, many=True)
            return JsonResponse({'data': data, 'userName': userName, 'totalData': serializer.data}, status=200)
        else:
            errorMsg = 'User doesnot exist please register'
            return JsonResponse({'data': data,'errorMsg':errorMsg}, status=500)

        data = Student.objects.filter(name=userName).exists()
        print("data:::::::::",data)
        if data :
            request.session['userName'] = userName
            totalData = Student.objects.all()
            serializer = StudentSerializer(totalData, context={'request': request}, many=True)
            return JsonResponse({'data': data,'userName': userName,'totalData' : serializer.data}, status=200)
        else :
            return JsonResponse({'data': data}, status=500)





@api_view(['GET', 'POST'])
def students_list(request):

    if request.method == 'GET':
        data = Student.objects.all()

        serializer = StudentSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def students_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


