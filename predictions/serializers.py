from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    HighBP = serializers.IntegerField()
    HighChol = serializers.IntegerField()
    BMI = serializers.IntegerField()
    Smoke = serializers.IntegerField()
    Fruit = serializers.IntegerField()
    Genhlth = serializers.IntegerField()
    MentHlth = serializers.IntegerField()
    PhysHlth = serializers.IntegerField()
    DiffWalk = serializers.IntegerField()
    Sex = serializers.IntegerField()
    Age = serializers.IntegerField()
