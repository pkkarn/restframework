from django.shortcuts import render, redirect
from .models import Query

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuerySerializers
from .forms import QueryForm


# Create your views here.

def home(request):
    return render(request, 'api/home.html')


# Api Creation
@api_view(['GET'])
def apiUrls(request):
    api_urls = {
        'Teacher API': '/api/teachersQuestion/',
        'Student API': '/api/studentQuestionSubmit/',
    }
    return Response(api_urls)


@api_view(['GET'])
def teachersQuestion(request):
    queries = Query.objects.all()
    serializer = QuerySerializers(queries, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def question(request, pk):
    queries = Query.objects.get(id=pk)
    serializer = QuerySerializers(queries, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def studentQuestionSubmit(request):
    serializer = QuerySerializers(data=request.data)
    return Response(serializer.data)


def submitQuestionForm(request):
    if request.method == 'POST':
        form = QueryForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            return redirect('questions')
    else:
        return render(request, 'api/submit.html', {'form': QueryForm()})
