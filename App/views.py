from django.shortcuts import render

from App.classification.classify import classify
from App.preprocessing.preprocesse import CleanData

def index(request):
    return render(request,'Operation.html')
def preprocess(request):
    cd = CleanData()
    cd.cleaning()
    text="Preprocessing done visit respective folder to saw dataset.txt file for out put "
    return render(request, 'Operation.html' ,{'prepro':text})
def categorization(request):
    name = request.POST['''name''']
    obj1= classify()
    category=obj1.category(name)
    return render(request, 'Operation.html',{'cat':category})
