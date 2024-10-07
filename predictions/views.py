from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import numpy as np
import pickle
import os
from .serializers import PredictionSerializer

# Charger ton modèle
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'new_GradientBoostingClassifier_boost.pkl')
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

@api_view(['POST'])
def predict_diabetes(request):
    # Sérialisation des données
    serializer = PredictionSerializer(data=request.data)
    
    if serializer.is_valid():
        data = serializer.validated_data
        # Extraire les données dans l'ordre requis par le modèle
        features = [
            data['HighBP'], data['HighChol'], data['BMI'], 
            data['Smoke'], data['Fruit'], data['Genhlth'], 
            data['MentHlth'], data['PhysHlth'], data['DiffWalk'], 
            data['Sex'], data['Age']
        ]
        
        # Convertir en tableau numpy et faire la prédiction
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)
        
        return Response({"prediction": int(prediction[0])})
    return Response(serializer.errors, status=400)
