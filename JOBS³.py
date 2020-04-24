# Para melhor experiência, recomeda-se utilizar o IDLE em modo janela (com 80
# caracteres de largura).
# O jogo baseia-se no gênero neutro (masculino).

# PARTICIPANTES: André Philipe Andriotti de Moraes       TIA: 32013965
#                Gabriel Kazuiti Aiura                        32047231
#                Thiago de Oliveira Aguirre                   32089589

from time import sleep

# MENU

sleep(1)
print('='*80)
sleep(1)
print('''
                                   Welcome to                 ____
                   ___    ________    _______     ________   (__  |
                  |   |  |        |  |   _   |   |        |    _| |
                  |   |  |   __   |  |  |_|  |   |     ___|   (_  |
                  |   |  |  |  |  |  |       |   |    |___    __| |
              __  |   |  |  |  |  |  |   __   |  |___     |  (____|
             |  |_|   |  |  |__|  |  |  |__|  |   ___|    |  
             |        |  |        |  |        |  |        |
             |________|  |________|  |________|  |________|

''')
sleep(2)
user = input('>>> Digite seu nome: ')
sleep(1)
print('''\n>>> REGRAS:
- Escolha apenas uma alternativa por vez.
- Não envie respostas vazias.
- Divirta-se!''')
sleep(4)
print('\n>>> Selecione qual carreira deseja seguir: ')
sleep(1)
print('''
[1] Cozinheiro 
[2] Clínico Geral
[3] Detetive ''')
job = input(' R: ').strip()
while job != '1' and job != '2' and job != '3':
    job = input(' R: ').strip()
sleep(1)
print()
print('='*80)

while True:

  # COZINHEIRO
 
  if job == '1':
    pontos = 0
    sleep(1)
    print(f'\n{"COZINHEIRO":^80}')
    sleep(2)
    print('''\n    Após o fim da pandemia do COVID-19, os restaurantes finalmente voltaram a
funcionar. Devido ao longo tempo sem ter acesso a eles, muitos clientes estavam
ansiosos para a reabertura do restaurante Costa Rica, onde você trabalha. Apesar
de ser um cozinheiro novato e inexperiente, sonha em ser reconhecido por suas
habilidades na cozinha, para que um dia possa ser chamado de Mestre Cuca!''')
    sleep(17)
    print('\n    Hoje, seu desafio é:')
    sleep(2)
    print('>>> Preparar um Crepe Suzette.')
    sleep(4)
    print('\n    Esta tarefa não será nem um pouco fácil! Então... MÃO NA MASSA!')
    sleep(4)
    print('''\n    Seu chefe esqueceu de organizar os ingredientes para a massa do Crepe!
Vá até a despensa e selecione-os antes que o restaurante abra.
(Obs.: não se esqueça do ingrediente que da liga à massa).''')
    sleep(10)
    print(f'''\n(Mestre {user}) Para massa, precisaremos de:

[A] 1 pitada de sal, manteiga derretida, leite integral, farinha de trigo,
licor de laranja, açúcar e um pouco de óleo de soja.
[B] 4 ovos, 1 pitada de sal, licor de laranja e só!
[C] 4 ovos, 1 pitada de sal, manteiga derretida, leite integral, farinha de
trigo, licor de laranja e um pouco de óleo de soja.''')
    resp = input(' R: ').strip().upper()
    while resp not in 'ABC':
      resp = input(' R: ').strip().upper()
    sleep(1)
    if resp == 'A':
      print('\n    Não acha que está faltando algo? Enfim, podemos prosseguir com a montagem.')
      sleep(4)
    elif resp == 'B':
      print('''\n    Certo de sua escolha, você leva esses ingredientes a sua bancada. Porém, ao
prepará-los, percebe que faltam vários ingredientes.''')
      sleep(6)
      print('\n    Seu chefe, enfurecido, caminha até sua bancada e diz:')
      sleep(4)
      print(f'\n(Chefe) Você é um cozinheiro amador, {user}! Fora do meu restaurante!')
      sleep(4)
      print('\n>>> Classificação: Vergonha da Profissão!')
      sleep(3)
      print(f'\n{" GAME OVER ":=^80}')
      break
    elif resp == 'C':
      pontos += 1
      print('''\n    Ótima escolha! Você pegou todos os ingredientes! Agora podemos prosseguir
com a montagem do crepe.''')
      sleep(5)
    print(f'\n    Mestre {user}, qual desssas maneiras é a mais adequada para prepará-lo?')
    sleep(5)
    print('''\n[A] Em um liquidificador, bata os ingredientes selecionados para massa até
obter uma mistura homogênea. Despeje-a em uma frigideira média untada com
manteiga, cobrindo todo o fundo. Deixe dourar dos dois lados e repita esse
processo até acabar a massa.''')
    sleep(1)
    print('''\n[B] Em um liquidificador, bata todos os ingredientes com exceção da farinha,
pois ela será usada no recheio, até obter uma mistura homogênea. Não será
necessário fritar a massa, apenas aquecê-la no microondas até tornar-se firme.
Afinal, uma massa mácia também é saborosa!''')
    resp = input(' R: ').strip().upper()
    while resp not in 'AB':
      resp = input(' R: ').strip().upper()
    sleep(1)
    if resp == 'A':
      pontos += 1
      print('\n    Corretíssimo!')
      sleep(2)
    elif resp == 'B':
      print('\n    Péssima escolha! A massa não terá consistência, devido à falta de farinha.')
      sleep(5)
    print(f'''\n    Massa pronta! Chegou a hora de fazer o recheio. Mestre {user}, como
ele deve ser preparado?''')
    sleep(6)
    print('''\n[A] Em uma frigideira, derreta a manteiga e misture ao açúcar, mexendo até obter
um creme liso. Cuidadosamente, acrescente o licor, as raspas de laranja e de
limão e reserve o conteúdo. Espalhe um pouco de recheio sobre a massa e dobre
em quatro. Ao servir, polvilhe açúcar sobre os crepes e despeje uma mistura de
conhaque e licor de laranja (em chamas) para dar um toque final.''')
    sleep(1)
    print('''\n[B] Em uma frigideira, derreta a manteiga e misture ao açúcar, mexendo até obter
uma pasta. Cuidadosamente, acrescente o licor, as raspas de laranja e de limão e
reserve o conteúdo. Espalhe bastante recheio sobre a massa e dobre ao meio. Ao
servir, polvilhe açúcar sobre os crepes e despeje uma mistura de conhaque e
licor de laranja (em chamas) para dar um toque final.''')
    resp = input(' R: ').strip().upper()
    while resp not in 'AB':
      resp = input(' R: ').strip().upper()
    if resp == 'A':
      pontos += 1
    elif resp == 'B':
      print(''' \n    Esta definitivamente não foi a melhor escolha! Você deveria fazer Crepes
Suzette e não tacos de laranja!''')
      sleep(6)
    print('\n    Tudo pronto! Agora é só esperar os clientes degustarem...')
    sleep(4) 
    print('\n    Ah não! Lá vem o chefe. O que será que ele dirá?!')
    sleep(6)
    if 2 <= pontos <= 3:
      print(f'\n(Chefe) Parabéns, Mestre {user}!')
      sleep(3)
      print('\n(Chefe) Eu e os clientes amamos o seu Crepe Suzette!')
      sleep(3)
      print('\n>>> Classificação: Mestre Cuca!')
      sleep(3)
      print(f'\n{" YOU WIN! ":=^80}')
    else:
      print('''\n(Chefe) Você fez um bom trabalho para um iniciante, mas o restaurante Costa Rica
exige os melhores cozinheiros. Infelizmente, o sr. está demitido!''')
      sleep(6)
      print('\n>>> Classificação: Vergonha da Profissão!')
      sleep(3)
      print(f'\n{" GAME OVER ":=^80}')
    break

  # CLÍNICO GERAL

  elif job == '2':
    pontos = 0
    sleep(1)
    print(f'\n{"CLÍNICO GERAL":^80}')
    sleep(2)
    print('''\n    Durante a pandemia do COVID-19, hospitais, clínicas e outros institutos
voltados a saúde estão congestionados.''')
    sleep(5)
    print('''\n    Você, como um clínico geral, sonha em trabalhar em hospitais famosos,
porém não foi reconhecido pelo seu chefe. Para conseguir ascender em sua
carreira, você decide trabalhar voluntariamente em um hospital filial à clínica
de seu chefe, que está lotada de pacientes e com falta de funcionários.''')
    sleep(11)
    print('''\n    Durante o seu dia como voluntário, você deve analisar a situação dos
pacientes e averiguar qual medicamento/tratamento será mais eficaz para cada
indivíduo.''')
    sleep(8)
    
    # Paciente 1
    print('\n    O primeiro paciente está entrando...')
    sleep(4)
    print('''\n    O paciente não aparenta estar muito bem... Está pálido, com febre e vomitou
na sala de espera.''')
    sleep(5)
    print('''\n    Escolha uma ação:
    
[A] Verificar o corpo do paciente.
[B] Perguntar se há outros sintomas.''')
    dedu = input(' R: ').strip().upper()
    while dedu not in 'AB':
      dedu = input(' R: ').strip().upper()
    sleep(1)
    if dedu == 'A':
      print('\n    Você encontrou uma picada na região do pescoço do paciente!')
    elif dedu == 'B':
      print('\n    O paciente disse que está com dores atrás dos olhos.')
    sleep(4)
    print('''\n    Após refletir sobre os sintomas, você decide diagnosticá-lo:

[A] Gripe
[B] Virose
[C] Dengue''')
    doenca = input(' R: ').strip().upper()
    while doenca not in 'ABC':
      doenca = input(' R: ').strip().upper()
    sleep(1)
    if doenca == 'A':
      print(f'''\n(Dr. {user}) Estes são sintomas de uma gripe comum. O tratamento é:

[A] Recomendar repouso domiciliar.
[B] Recomendar hidratação.
[C] Recomendar lavagem nasal.''')
      medicam = input(' R: ').strip().upper()
      while medicam not in 'ABC':
        medicam = input(' R: ').strip().upper()
      sleep(1)
      if medicam == 'A':
        print(f'\n(Dr. {user}) O sr. deve ficar de repouso.')
      elif medicam == 'B':
        print(f'\n(Dr. {user}) Recomendo que o sr. beba muita água para se recuperar logo.')
        pontos += 1
      elif medicam == 'C':
        print(f'\n(Dr. {user}) O sr. deve fazer uma lavagem nasal ao dia.')
      sleep(3)
      print('\n(Paciente 1) Okay doutor, obrigado pela consulta.')
      sleep(3)
      print('\n    Sinto que não foi uma boa escolha... Espero que ele fique bem.')
    elif doenca == 'B':
      print(f'''\n(Dr. {user}) Estes são sintomas de uma virose. O tratamento é:

[A] Recomendar analgésicos.
[B] Internar o paciente.''')
      medicam = input(' R: ').strip().upper()
      while medicam not in 'AB':
        medicam = input(' R: ').strip().upper()
      sleep(1)
      if medicam == 'A':
        print(f'\n(Dr. {user}) Recomendo que use analgésicos para aliviar a dor.')
        pontos += 1
      elif medicam == 'B':
        print(f'\n(Dr. {user}) O sr. terá que ser internado por um tempo para observação.')
        pontos += 1
      sleep(3)
      print('\n(Paciente 1) Okay doutor, obrigado pela consulta.')
      sleep(3)
      print('\n    Sinto que não foi um bom diagnóstico... Bom, espero que ele fique bem.')
    elif doenca == 'C':
      pontos += 2
      print(f'''\n(Dr. {user}) Estes são sintomas de dengue. O tratamento é:

[A] Recomendar repouso domiciliar.
[B] Internar o paciente.
[C] Analgésicos e hidratação.''')
      medicam = input(' R: ').strip().upper()
      while medicam not in 'ABC':
        medicam = input(' R: ').strip().upper()
      sleep(1)
      if medicam == 'A':
        print(f'\n(Dr. {user}) Recomendo que repouse em sua casa até a febre abaixar.')
      elif medicam == 'B':
        print(f'\n(Dr. {user}) O sr. deve ser internado até que esteja completamente curado.')
        pontos += 1
      elif medicam == 'C':
        print(f'\n(Dr. {user}) Recomendo que tome analgésicos e beba bastante água.')
        pontos += 2
      sleep(3)
      print('\n(Paciente 1) Okay doutor, obrigado pela consulta.')
      sleep(3)
      print('\n    Bom diagnósitco! Certamente o paciente irá se recuperar logo.')

    # Paciente 2
    sleep(5)  
    print('\n    Finalmente um pouco de descans... (TOC TOC)')
    sleep(3)
    print('\n    Foi só dizer e o segundo paciente do dia chegou.')
    sleep(3)
    print('''\n    Ele está com dificuldades para andar, conseguindo apenas com o apoio em
objetos.''')
    sleep(4)
    print('''\n    Escolha uma ação:

[A] Perguntar a situação do paciente.
[B] Examinar o corpo.''')
    dedu = input(' R: ').strip().upper()
    while dedu not in 'AB':
      dedu = input(' R: ').strip().upper()
    sleep(1)
    if dedu == 'A':
      print('''\n    O paciente afirma ter caído da escada e desde então está mancando, mas
disse para não se preocupar, uma vez que que veio apenas para fazer exames
de rotina.''')
      sleep(7)
      print('''\n    Após analisar a situação, você decide:

[A] Proceder com exames de rotina.
[B] Insistir no caso do pé.''')
      duvida = input(' R: ').strip().upper()
      while duvida not in 'AB':
          duvida = input(' R: ').strip().upper()
      sleep(1)
      if duvida == 'A':
        print('\n    Você realiza os devidos exames no paciente. Ele agradece e se despede.')
        sleep(4)
        print('\n    O paciente sai da sala mancando...')
        sleep(2)
      elif duvida == 'B':
        print('''\n    Ao ver a situação do paciente, você não pôde ignorar essa situação, então
acabou realizando alguns exames extras.''')
        sleep(6)
    elif dedu == 'B':
      duvida = 'B'
    if duvida == 'B':
      print('\n    Feito isso, descobriu-se que havia um grande inchaço e vermelhidão no local.')
      sleep(4)
      print('''\n    Ao fazer uma análise geral, você decide diagnosticá-lo:
    
[A] Luxação.
[B] Osso quebrado.''')
      doenca = input(' R: ').strip().upper()
      while doenca not in 'AB':
        doenca = input(' R: ').strip().upper()
      sleep(1)
      if doenca == 'A':
        pontos += 1
        print(f'''\n(Dr. {user}) Isto é uma luxação. Para tratá-lo irei:

[A] Engessá-lo.
[B] Lhe recomendar analgésicos e repouso.
[C] Lhe dar um sedativo e analgésicos.''')
        medicam = input(' R: ').strip().upper()
        while medicam not in 'ABC':
          medicam = input(' R: ').strip().upper()
        sleep(1)
        if medicam == 'A':
          print(f'\n(Dr. {user}) Colocarei um gesso em seu pé para que ele se recupere devidamente.')
          pontos += 1
        elif medicam == 'B':
          pontos += 2
          print(f'''\n(Dr. {user}) Enquanto estiver inchado, o senhor deve tomar estes analgésicos e
ficar em casa até que melhore.''')
        elif medicam == 'C':
          pontos += 1
          print(f'''\n(Dr. {user}) Sedaremos o senhor e aplicaremos alguns analgésicos para aliviar
sua dor.''')
        sleep(4)
        print('\n(Paciente 2) Certo! Obrigado, doutor.')
        sleep(2)
      elif doenca == 'B':
        print(f'''\n(Dr. {user}) Isto é um osso quebrado. Para tratá-lo irei:

[A] Engessá-lo
[B] Lhe dar um sedativo e analgésicos.
[C] Remediá-lo com analgésicos e anti-inflamatórios.''')
        medicam = input(' R: ').strip().upper()
        while medicam not in 'ABC':
          medicam = input(' R: ').strip().upper()
        sleep(1)
        if medicam == 'A':
          print(f'\n(Dr. {user}) Colocarei um gesso em seu pé para que ele se recupere devidamente.')
          pontos += 1
          sleep(4)
        elif medicam == 'B':
          print(f'''\n(Dr. {user}) Sedaremos o senhor e aplicaremos alguns analgésicos para aliviar
sua dor.''')
          sleep(4)
        elif medicam == 'C':
          pontos += 1
          print(f'''\n(Dr. {user}) Enquanto estiver com o osso quebrado, você deve tomar estes
analgésicos para aliviar a dor e estes anti-inflamatórios para se recuperar 
devidamente.''')
          sleep(5)
        print('\n(Paciente 2) Certo! Obrigado, doutor.')
        sleep(2)
        print('''\n    Felizmente, o tratamento recomendado foi ideal, porém estou incerto sobre o
osso quebrado...''')
        sleep(4)

    # Paciente 3
    print('\n*Obs.: Para o próximo paciente, você precisa ter conhecimento sobre:')
    sleep(3)
    print('\n>>> Íngua: inchaço e vermelhidão local, nódulo flexível e dolorido.')
    sleep(4)
    print('''\n(DESAFIO) O paciente entra ansioso, diz que está com nódulos nas regiões da
axila, virilha e pescoço, sendo esse último o maior deles.''')
    sleep(6)
    print('''\n    Escolha uma ação:

[A] Analisar todos os nódulos.
[B] Analisar apenas o nódulo maior.''')
    dedu = input(' R: ').strip().upper()
    while dedu not in 'AB':
      dedu = input(' R: ').strip().upper()
    sleep(1)
    if dedu == 'A':
        print('''\n    Os nódulos não são muito flexíveis, mas sim rígidos e o paciente afirma não
doer ao aperta-los.''')
    elif dedu == 'B':
        print('''\n    A região envolta do nódulo é rígida, avermelhada e o paciente afirma não
sentir dor ao tocá-lo.''')
    sleep(5)
    print('''\n    Após refletir sobre os sintomas, você decide diagnosticá-lo:

[A] É apenas uma íngua comum.
[B] Fazer uma pesquisa sobre nódulos.''')
    doenca = input(' R: ').strip().upper()
    while doenca not in 'AB':
      doenca = input(' R: ').strip().upper()
    sleep(1)
    if doenca == 'A':
      print(f'''\n(Dr. {user}) Os sintomas aparentam ser de ínguas comuns mesmo... O tratamento
devido é:

[A] Anti-inflamatórios.
[B] Aplicar gelo no inchaço.''') 
      medicam = input(' R: ').strip().upper()
      while medicam not in 'AB':
        medicam = input(' R: ').strip().upper()
      sleep(1)
      if medicam == 'A':
        print(f'''\n(Dr. {user}) Você deve utilizar anti-inflamatórios durante 14 dias ou até 
o inchaço sumir.''')
      elif medicam == 'B':
        print(f'''\n(Dr. {user}) Você deve aplicar gelo nas regiões dos nódulos 2 vezes ao dia,
até que eles comecem a desinchar.''') 
      sleep(4)
      print('\n(Paciente 3) Entendi. Muito obrigado pela consulta, doutor!')
    elif doenca == 'B':
      pontos += 1
      print('''\n    Ao pesquisar sobre nódulos, você encontra uma doença com os sintomas
semelhantes aos do paciente:''')
      sleep(4)
      print('''\n>>> Linfoma: semelhante às ínguas, o linfoma é um câncer no sistema linfático,
no qual os nódulos inflamados sofrem mutações e começam a se multiplicar,
resultando em nódulos rígidos e indolores.''')
      sleep(8)
      print('''\n    Após realizar a pesquisa, é evidente que o caso do paciente é de linfoma,
porém há diversos meios de tratamento. Qual seria o mais efetivo nessa ocasião?

[A] Quimioterapia.
[B] Cirurgia para remoção de nódulos.''')
      medicam = input(' R: ').strip().upper()
      while medicam not in 'AB':
        medicam = input(' R: ').strip().upper()
      sleep(1)
      if medicam == 'A':
        pontos += 2
        print(f'''\n(Dr. {user}) O sr. na verdade não está com ínguas, mas sim com um caso de
Linfoma de Hodgkin. É necessário fazer quimioterápia o quanto antes, pois assim
evitaremos que as células comprometidas se multipliquem ainda mais!''')
      elif medicam == 'B':
        pontos += 1
        print(f'''\n(Dr. {user}) O sr. na verdade não está com ínguas, mas sim com um caso de
Linfoma de Hodgkin. É ncessário fazer uma cirurgia para remoção dos nódulos
comprometidos. Somente assim, todas as células cancêrigenas serão erradicadas.''')
      sleep(8)
      print('\n(Paciente 3) Pode deixar, doutor, farei isso o mais rapido que puder. Obrigado!')
    sleep(4)
    print('\nFinalmente, seu dia como voluntário no hospital chegou ao fim...')
    sleep(3)
    print('\nEita! Parece que o seu chefe está lhe chamando! ')
    sleep(3)
    print('\nApós entrar na sala do patrão, ele diz:')
    sleep(3)
    print('''\n(Chefe) Dia puxado, hein! Na verdade, todos os pacientes eram testes para
avaliar seu desempenho como profissional.''')
    sleep(5)
    if 8 <= pontos <= 10:
      print(f'\n(Chefe) Parabéns, {user}! Você é um excelente doutor!')
      sleep(3)
      print('\n(Chefe) Será um prazer trabalhar com você neste hospital a partir de hoje!')
      sleep(3)
      print(f'\n{" YOU WIN! ":=^80}')
    elif  3 <= pontos <= 7:
      print('\n(Chefe) O sr. fez um bom trabalho, mas poderia ter sido bem melhor...')
      sleep(3)
      print(f'''\n(Chefe) Infelizmente, não lhe promoverei a nível de hospital, mas darei a você
um grande aumento na clínica... Parabéns, {user}!''')
      sleep(5)
      print(f'\n{" THE END ":=^80}')
    else:
      print('\n(Chefe) Você foi péssimo! Tenho dó de seus pacientes...')
      sleep(3)
      print('\n(Chefe) Hoje foi o seu último dia de trabalho. DE-MI-TI-DO!')
      sleep(3)
      print(f'\n{" GAME OVER ":=^80}')
    break 
        
  # DETETIVE

  elif job == '3':
    sleep(1)
    print(f'\n{"DETETIVE":^80}')
    sleep(2)
    print('\n    Dia 11 de abril de 2020 - Westminster, Inglaterra.')
    sleep(3)
    print('''\n    Era uma manhã fria e nublada, clima perfeito para ficar debaixo das
cobertas o dia inteiro, mas algo te deixa inquieto. Pouco antes do café da
manhã, você decide checar a caixa de correio e se depara com um envelope preto.
Ansiosamente, senta na poltrona e o abre o mais rápido que pode:''')
    sleep(12)
    print(f'''\n    “Caro {user} Holmes,

    Peço-lhe que compareça ao casamento de Edward e Monicah esta noite, suspeito
    que haverá um assassinato no local. A seguir estão as informações do
    respectivo evento.

    Endereço: Stanborough Park, Watford WD25 9JT
    Horário: 17h - 18h30
    Chave de acesso: 40028922
            
    Obrigadx, anônimx.”''')
    sleep(14)
    print('''\n    Intrigante, não?! E então, você irá ao casamento?

[A] Lógico! Bora ver no que vai dar isso ae.
[B] Mas nem a pau que eu caio em uma fake news dessa, me respeita!''')
    resp = input(' R: ').strip().upper()
    while resp not in 'AB':
      resp = input(' R: ').strip().upper()
    sleep(2)
    if resp == 'A':
      print('''\n    É claro que vai, não esperaria outra resposta de você. Pois bem, hoje será
um dia e tanto.''')
      sleep(5)
    elif resp == 'B':
      print(''' \n    Certo de sua escolha, você decide voltar para a cama e passar o sábado
maratonando a nova temporada da série egípcia La Casa de Papiro.''')
      sleep(6)
      print(f'\n    Você não é digno de seu sobrenome, Sr. {user} Holmes!')
      sleep(3)
      print('\n>>> Seu desempenho: DESASTRE TOTAL!')
      sleep(2)
      print(f'\n{" GAME OVER ":=^80}')
      break
    print('''\n    O tempo passa voando e você acorda de uma soneca pós almoço, olha no relógio
e já são 16h! Está próximo do horário, o que o sr. fará?

[A] Ah… mais dez minutinhos de sono não mata ninguém, né?!
[B] Eita, hora de se arrumar, quero ficar lindão e cheiroso!''')
    resp = input(' R: ').strip().upper()
    while resp not in 'AB':
      resp = input(' R: ').strip().upper()
    sleep(1)
    if resp == 'A':
      print('''\n    Péssima escolha! Seu despertador não tocou e faltam apenas 15 minutos para
começar a cerimônia. Por sorte, um carro vendendo ovos passa na sua rua e te
acorda. Ao ver a hora, levanta desesperadamente e pega a primeira roupa que
encontra: um casaco neon e uma calça de estampa xadrez. Que look, hein!''')
      sleep(13)
    elif resp == 'B':
      print(f'\n    Sábias escolhas, {user}!')
      sleep(2)
      print('''\n    Você tem tempo de sobra para tomar um banho de espuma e escolher o seu
melhor traje para a cerimônia.''')
      sleep(5)
    print('''\n    Feito isso, chegou a hora de ir… cinto de segurança colocado, retrovisores
ajustados, música ligada, tudo pronto para partir. LET’S GO! (obs.: você é um
detetive, então se atente a todos os detalhes).''')
    sleep(10)
    print('''\n    Chegando no local, é necessário um código para permitir sua entrada. Espero
que você se lembre da sua chave de acesso…''')
    sleep(1)
    resp = input('\n>>> Chave de acesso: ').strip()
    while resp != '40028922':
      sleep(1)
      resp = input('Chave incorreta! Tente novamente: ').strip()
    sleep(1)
    for c in range(0, 3):
      if c == 0:
        print('''\n    Mandou bem! Agora, onde irá investigar primeiro?

[A] Capela
[B] Cozinha
[C] Jardim''')
      elif c == 1:
        print('''\n    Investigue outro lugar para obter mais informações… (obs.: lembre-se de não
ir em locais já investigados, você pode perder informações raras).

[A] Capela
[B] Cozinha
[C] Jardim''')
      else:
        print('''\n    Muito bem! Vá investigar em mais um local, quanto mais informação, melhor!

[A] Capela
[B] Cozinha
[C] Jardim''')
      resp = input(' R: ').strip().upper()
      while resp not in 'ABC':
        resp = input(' R: ').strip().upper()
      sleep(1)
      if resp == 'A':
        print('''\n    Boa escolha! A maioria dos convidados e os noivos estão aqui, ou seja, muita
gente para analisar.''')
        sleep(5)
        print('''\n    Porém duas pessoas aparentam ser mais suspeitas de cometer um assassinato: o
garçom [Análise: branco, moreno, estudante de medicina, volume suspeito no bolso
do colete] e o padre [Análise: branco, cabelo grisalho, ex-líder da facção
criminosa “Los Muertos”].''')
        sleep(13)
        print('''\n    Outra situação também te chama a atenção: como forma de testemunho do padre,
havia uma decoração na parede com armas verdadeiras [Análise: formato circular,
uma sniper de alta complexidade no centro, duas pistolas calibre 22 à esquerda,
duas katanas à direita].''')
        sleep(13)
      elif resp == 'B':
        print('''\n    Esperto! Um arsenal de facas e ingredientes perigosos são excelentes
ferramentas para um assassino.''')
        sleep(5)
        print('''\n    Dentre os cozinheiros, duas se destacaram: Regiane [Análise: branca, loira,
apaixonada por Edward, reconhecida por seus trabalhos voluntários, a única que
te conhecia no evento] e sua mãe Dona Palmira [Análise: branca, cabelo grisalho,
apresentadora de um programa de culinária e atiradora de elite aposentada].''')
        sleep(14)
        print('''\n    Também observa-se que os cozinheiros possuem aparelhos móveis para a
comunicação com os garçons, será que estão planejando algo?''')
        sleep(6)
      elif resp == 'C':
        print('''\n    Genial! Um lugar mais isolado seria ideal para um assassino se esconder
antes ou depois de cometer o crime.''')
        sleep(5)
        print('''\n    Apenas um casal [Análise: japoneses, morenos, camponeses, grandes
concorrentes de trabalho dos noivos] está passeando pelo jardim, admirando a
beleza das flores.''')
        sleep(8)
    sleep(3)
    print('\n    A cerimônia estava indo perfeitamente bem, assim como sua investigação.')
    sleep(4)
    print('''\n    Eis que todos ouvem um barulho vindo de muito longe, a janela da capela
estoura e o sangue de Monicah é derramado nos braços do noivo, que então se
ajoelhou em prantos.''')
    sleep(8)
    print('\n    O garçom prestou imediatamente os primeiros socorros, mas era tarde demais.')
    sleep(4)
    print('''\n    Após o esvaziamento do local, percebeu-se que uma peça do conjunto de armas
da parede havia sumido.''')
    sleep(5)
    print('\n    (DECISÃO FINAL) Esta é sua hora, é tudo ou nada...')
    sleep(3)
    tentativas = -1
    while resp != 'D':
      print(f'''\n    {user} Holmes, quem matou a noiva?

[A] Garçom
[B] Padre
[C] Regiane
[D] Dona Palmira
[E] Casal do jardim''')
      resp = input(' R: ').strip().upper()
      while resp not in 'ABCDE':
        resp = input(' R: ').strip().upper()
      tentativas += 1
      sleep(1)
      if resp == 'A':
        print('''\n    Você errou! Como e para que ele realizaria o assassinato e logo em seguida
prestaria os primeiros socorros? Não apenas isso, mas a única suspeita seria o
objeto em seu bolso, que poderia ser inúmeras coisas, porém era apenas seu
aparelho de comunicação com a cozinha.''')
        sleep(11)    
      elif resp == 'B':
        print('''\n    O padre, sério? Apesar de seu passado, ele nunca mais foi o mesmo após
conhecer Jesus Cristo, abraçando por completo sua nova carreira. Não só isso,
mas como ele poderia matar Monicah e não ser visto se ele estava no altar com
os noivos?''')
        sleep(11)
      elif resp == 'C':
        print('''\n    Resposta incorreta… apesar de estar completamente apaixonada pelo noivo,
Regiane tem um coração puro, faz o que é correto custe o que custar. Além disso,
por que ela te enviaria uma carta se a própria cometesse o crime?''')
        sleep(9)
      elif resp == 'D':
        print(f'\n    PARABÉNS, {user}! Eu sabia que você acertaria!')
        sleep(3)
        print('''\n    Dona Palmira, insanamente irritada ao saber que o amor de sua filha estava
se casando com outra mulher, planejou o assassinato de Monicah. Então, após
preparar as entradas, roubou discretamente a sniper que estava na decoração da
parede, tomou distância suficiente para que não fosse detectada e, por ser a
única com habilidades militares, soube manusear a arma de alta complexidade,
eliminando o alvo.''')
        sleep(18)
        print(f'''\n    O que ela não esperava era que sua própria filha suspeitasse de seu plano e
enviasse uma carta ao incrível {user} Holmes!''')
        sleep(5)
      elif resp == 'E':
        print('''\n    Erradíssimo!!! Mesmo sendo concorrentes de trabalho dos noivos, não havia
provas o suficiente para confirmar o seu suposto assassinato, aliás seria muito
raro se um casal de camponeses soubesse manusear uma sniper de alta complexidade
sem um devido treinamento.''')
        sleep(11)
    desempenho = 100 - (tentativas*20)
    sleep(2)
    if desempenho == 20 or desempenho == 40:
      print('\n>>> Seu desempenho: PÉSSIMO detetive!')
      sleep(2)
      print(f'\n{" GAME OVER ":=^80}')
    elif desempenho == 60 or desempenho == 80:
      print('\n>>> Seu desempenho: BOM detetive!')
      sleep(2)
      print(f'\n{" THE END ":=^80}')
    elif desempenho == 100:
      print('\n>>> Seu desempenho: EXCELENTE detetive!')
      sleep(2)
      print(f'\n{" YOU WIN! ":=^80}')
    break        
