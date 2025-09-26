from rest_framework import serializers
from .models import Machine, Section, Step, StepBlock, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class StepBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepBlock
        fields = '__all__' 
        #fields = ['id', 'step', 'type', 'order', 'text', 'code', 'image', 'caption']

class StepSerializer(serializers.ModelSerializer):
    blocks = StepBlockSerializer(many=True, read_only=True)

    class Meta:
        model = Step
        fields = '__all__' 
        #fields = ['id', 'section', 'title', 'order', 'blocks']

class SectionSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = '__all__' 

       #fields = ['id', 'machine', 'title', 'order', 'steps']

class MachineSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Machine
        fields = '__all__' 

class MachineBasicSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)  

    class Meta:
        model = Machine
        fields = '__all__' 

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']  # los campos básicos de tu Tag

class TagWithMachinesSerializer(serializers.ModelSerializer):
    machines = serializers.StringRelatedField(many=True)  # muestra name de cada máquina
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'machines']
