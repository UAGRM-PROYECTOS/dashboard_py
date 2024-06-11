from rest_framework import serializers
from .models import PublicationStatu
from .models import Administrative
from .models import User
from .models import Editor
from .models import Presenter
from .models import ElementPresenter
from .models import ElementVideo
from .models import Element
from .models import Project
from .models import News
from .models import Fechas

class PublicationStatuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationStatu
        fields = '__all__'
class AdministrativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrative
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = '__all__'
class PresenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenter
        fields = '__all__'
class ElementPresenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementPresenter
        fields = '__all__'
class ElementVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementVideo
        fields = '__all__'
class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
class FechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fechas
        fields = '__all__'