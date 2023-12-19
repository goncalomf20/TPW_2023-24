from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Modalidade,
    Liga,
    Grupo,
    Equipa,
    Jogador,
    Jogo,
    Evento,
    Classificacao,
    User,
    FantasyTeam,
)
from .serializers import (
    ModalidadeSerializer,
    LigaSerializer,
    GrupoSerializer,
    EquipaSerializer,
    JogadorSerializer,
    JogoSerializer,
    EventoSerializer,
    ClassificacaoSerializer,
    UserSerializer,
    FantasyTeamSerializer,
)

# Web Services for Modalidade
@api_view(['GET'])
def get_all_modalidade(request):
    modalidades = Modalidade.objects.all()
    serializer = ModalidadeSerializer(modalidades, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_modalidadeid(request, id):
    try:
        modalidade = Modalidade.objects.get(id=id)
    except Modalidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ModalidadeSerializer(modalidade)
    return Response(serializer.data)

@api_view(['POST'])
def post_modalidade(request):
    serializer = ModalidadeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_modalidade(request, id):
    try:
        modalidade = Modalidade.objects.get(id=id)
    except Modalidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ModalidadeSerializer(modalidade, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def del_modalidade(request, id):
    try:
        modalidade = Modalidade.objects.get(id=id)
    except Modalidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    modalidade.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def del_all_modalidade(request):
    Modalidade.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Web Services for Liga
@api_view(['DELETE'])
def del_all_liga(request):
    Liga.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def del_liga(request, id):
    try:
        liga = Liga.objects.get(id=id)
        liga.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Liga.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_ligaid(request, id):
    try:
        liga = Liga.objects.get(id=id)
        serializer = LigaSerializer(liga)
        return Response(serializer.data)
    except Liga.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_liga(request):
    ligas = Liga.objects.all()
    serializer = LigaSerializer(ligas, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_liga(request, id):
    try:
        liga = Liga.objects.get(id=id)
    except Liga.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = LigaSerializer(liga, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def post_liga(request):
    serializer = LigaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Web Services for Grupo
@api_view(['DELETE'])
def del_all_grupo(request):
    Grupo.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def del_grupo(request, id):
    try:
        grupo = Grupo.objects.get(id=id)
        grupo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Grupo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_grupoid(request, id):
    try:
        grupo = Grupo.objects.get(id=id)
        serializer = GrupoSerializer(grupo)
        return Response(serializer.data)
    except Grupo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_grupo(request):
    grupos = Grupo.objects.all()
    serializer = GrupoSerializer(grupos, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_grupo(request, id):
    try:
        grupo = Grupo.objects.get(id=id)
    except Grupo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GrupoSerializer(grupo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_grupo(request):
    serializer = GrupoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Web Services for Equipa
@api_view(['DELETE'])
def del_all_equipa(request):
    Equipa.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def del_equipa(request, id):
    try:
        equipa = Equipa.objects.get(id=id)
        equipa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Equipa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_equipaid(request, id):
    try:
        equipa = Equipa.objects.get(id=id)
        serializer = EquipaSerializer(equipa)
        return Response(serializer.data)
    except Equipa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_equipa(request):
    equipas = Equipa.objects.all()
    serializer = EquipaSerializer(equipas, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_equipa(request, id):
    try:
        equipa = Equipa.objects.get(id=id)
    except Equipa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EquipaSerializer(equipa, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_equipa(request):
    serializer = EquipaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Web Services for Jogador
@api_view(['DELETE'])
def del_all_jogador(request):
    Jogador.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def del_jogador(request, id):
    try:
        jogador = Jogador.objects.get(id=id)
        jogador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Jogador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_jogadorid(request, id):
    try:
        jogador = Jogador.objects.get(id=id)
        serializer = JogadorSerializer(jogador)
        return Response(serializer.data)
    except Jogador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_jogador(request):
    jogadores = Jogador.objects.all()
    serializer = JogadorSerializer(jogadores, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_jogador(request, id):
    try:
        jogador = Jogador.objects.get(id=id)
    except Jogador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = JogadorSerializer(jogador, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def post_jogador(request):
    serializer = JogadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Web Services for Jogo
@api_view(['DELETE'])
def del_all_jogo(request):
    Jogo.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def del_jogo(request, id):
    try:
        jogo = Jogo.objects.get(id=id)
        jogo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Jogo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_jogoid(request, id):
    try:
        jogo = Jogo.objects.get(id=id)
        serializer = JogoSerializer(jogo)
        return Response(serializer.data)
    except Jogo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_jogo(request):
    jogos = Jogo.objects.all()
    serializer = JogoSerializer(jogos, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_jogo(request, id):
    try:
        jogo = Jogo.objects.get(id=id)
    except Jogo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = JogoSerializer(jogo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_jogo(request):
    serializer = JogoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Web Services for Evento
@api_view(['DELETE'])
def del_all_evento(request):
    Evento.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def del_evento(request, id):
    try:
        evento = Evento.objects.get(id=id)
        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_eventoid(request, id):
    try:
        evento = Evento.objects.get(id=id)
        serializer = EventoSerializer(evento)
        return Response(serializer.data)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_evento(request):
    eventos = Evento.objects.all()
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_evento(request, id):
    try:
        evento = Evento.objects.get(id=id)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EventoSerializer(evento, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_evento(request):
    serializer = EventoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Web Services for Classificacao
@api_view(['DELETE'])
def del_all_classificacao(request):
    Classificacao.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def del_classificacao(request, id):
    try:
        classificacao = Classificacao.objects.get(id=id)
        classificacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Classificacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_classificacaoid(request, id):
    try:
        classificacao = Classificacao.objects.get(id=id)
        serializer = ClassificacaoSerializer(classificacao)
        return Response(serializer.data)
    except Classificacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_classificacao(request):
    classificacoes = Classificacao.objects.all()
    serializer = ClassificacaoSerializer(classificacoes, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_classificacao(request, id):
    try:
        classificacao = Classificacao.objects.get(id=id)
    except Classificacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClassificacaoSerializer(classificacao, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def post_classificacao(request):
    serializer = ClassificacaoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Web Services for User
@api_view(['DELETE'])
def del_all_user(request):
    User.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def del_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_userid(request, id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Web Services for FantasyTeam
@api_view(['DELETE'])
def del_all_fantasyteam(request):
    FantasyTeam.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def del_fantasyteam(request, id):
    try:
        fantasyteam = FantasyTeam.objects.get(id=id)
        fantasyteam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except FantasyTeam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_fantasyteamid(request, id):
    try:
        fantasyteam = FantasyTeam.objects.get(id=id)
        serializer = FantasyTeamSerializer(fantasyteam)
        return Response(serializer.data)
    except FantasyTeam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_fantasyteam(request):
    fantasyteams = FantasyTeam.objects.all()
    serializer = FantasyTeamSerializer(fantasyteams, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_fantasyteam(request, id):
    try:
        fantasyteam = FantasyTeam.objects.get(id=id)
    except FantasyTeam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FantasyTeamSerializer(fantasyteam, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def post_fantasyteam(request):
    serializer = FantasyTeamSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)