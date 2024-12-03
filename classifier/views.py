from django.shortcuts import render

# Create your views here.
import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# Load model
model = joblib.load('C:\\Users\\PJRao\\Desktop\\DjangoProjects\\Irisclassification\\model.joblib')

@csrf_exempt
def classify(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        features = data.get('features')  # Example: [5.1, 3.5, 1.4, 0.2]
        prediction = model.predict([features])
        return JsonResponse({'prediction': int(prediction[0])})
    return JsonResponse({'error': 'POST request required'}, status=400)
