from rest_framework import serializers
from .models import Modalidade, Liga, Grupo, Equipa, Jogador, Jogo, Evento, Classificacao, User, FantasyTeam

class ModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidade
        fields = '__all__'

class LigaSerializer(serializers.ModelSerializer):
    ligas = LigaSerializer(many=True, read_only=True)
    class Meta:
        model = Liga
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

class EquipaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipa
        fields = '__all__'

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class ClassificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacao
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FantasyTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyTeam
        fields = '__all__'
