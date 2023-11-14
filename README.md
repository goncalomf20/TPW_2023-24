# TPW_2023-24
Cadeira de Tecnologia e Programação Web 2023/2024


### Template website : https://templatemo.com/tm-574-mexant


### Requirements : pip install sorl-thumbnail


## Credenciais:

#### Python AnyWhere (http://goncalomf.pythonanywhere.com):

	Utilizador comum:
		user: cristiano
		password: zezoca123

	Administrador:
		user: tomas
		password: zezoca123

#### Local:

	Utilizador comum: 
		user: borro
		password: zezoca123

	Administrador:
		user: tomas
		password: admin
		
		
##### Nota: É preferencial correr localmente devido ao modal na troca de jogos no python AnyWhere 



##### A tabela dos games na base de dados poderá ficar com muitos elementos um vez que estão a ser gerados jogos de 30 em 30 segundos


### O Site:

Um utilizador normal com intenções de apostar pode adicionar dinheiro e também levantar uma quantidade dele.
Um utilizador que quer apostar deverá clicar na odd (botão verde em baixo do icon da equipa) da equipa que quiser apostar.
A odd de uma equipa num jogo indica a probabilidade de uma equipa ganhar o jogo e também os ganhos possíveis consoate o dinheiro investido. ganhos = odd_total * dinheiro_investido
Um aposta pode ter vários jogos e a odd_total é calculadada pela multiplicação das odds de cada jogo.
Cada secção de jogos dura 30 segundos e no final desse tempo o se um utilizador tiver alguma aposta deverá aparecer um modal com os ganho ou perdas e infomação mais detalhada.
As informações detalhadas estão todas na página do admin
