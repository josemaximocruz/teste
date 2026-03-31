Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import random
import time
import sys

class JogoJequie:
    def __init__(self):
        self.vidas = 3
        self.pontos = 0
        self.fase_atual = 1
        self.total_fases = 4
        self.cartas_descobertas = []
        
        # Dicionário com todas as perguntas organizadas por fase
        self.perguntas = {
            1: self._carregar_perguntas_fase1(),
            2: self._carregar_perguntas_fase2(),
            3: self._carregar_perguntas_fase3(),
            4: self._carregar_perguntas_fase4()
        }
    
    def _carregar_perguntas_fase1(self):
        """Fase 1: Origens e Emancipação (até 1897)"""
        return [
            {
                "pergunta": "Qual é o significado da palavra 'Jequié' na língua tupi?",
                "alternativas": [
                    "A) Rio Rápido",
                    "B) Cesto afunilado (armadilha de pesca)",
                    "C) Terra da Onça",
                    "D) Feira Grande"
                ],
                "resposta_correta": 1,
                "explicacao": "A palavra vem de 'Jequi' ou 'Jequiê', que significa cesto afunilado usado como armadilha para pegar peixes no Rio de Contas.",
                "contexto": "💡 Além de 'jequi', alguns historiadores também associam o nome à palavra indígena para 'onça', animal comum na região no passado.",
                "pontos": 10
            },
            {
                "pergunta": "Em que ano Jequié foi emancipada politicamente, tornando-se município?",
                "alternativas": [
                    "A) 1875",
                    "B) 1897",
                    "C) 1911",
                    "D) 1920"
                ],
                "resposta_correta": 1,
                "explicacao": "Jequié foi emancipada em 25 de outubro de 1897, desmembrando-se do município de Maracás.",
                "contexto": "📍 A emancipação ocorreu através da Lei Estadual nº 263, durante o governo de Luís Viana.",
                "pontos": 10
            },
            {
                "pergunta": "Qual elemento geográfico foi fundamental para o surgimento do povoado que originou Jequié?",
                "alternativas": [
                    "A) Serra do Mar",
                    "B) Rio de Contas",
                    "C) Lagoa Encantada",
                    "D) Cachoeira de Paulo Afonso"
                ],
                "resposta_correta": 1,
                "explicacao": "O Rio de Contas foi essencial para o desenvolvimento do povoado, tanto para transporte quanto para atividades econômicas.",
                "contexto": "🌊 O Rio de Contas nasce na Chapada Diamantina e deságua no Oceano Atlântico, sendo um dos principais rios da Bahia.",
                "pontos": 10
            },
            {
                "pergunta": "Qual foi a atividade econômica inicial que impulsionou o crescimento de Jequié?",
                "alternativas": [
                    "A) Mineração de ouro",
                    "B) Feira livre",
                    "C) Indústria têxtil",
                    "D) Plantação de cana-de-açúcar"
                ],
                "resposta_correta": 1,
                "explicacao": "A feira livre atraía comerciantes e tropeiros da região, tornando-se um importante centro de trocas comerciais.",
                "contexto": "🏪 A feira acontecia às margens do Rio de Contas e era ponto de encontro de produtores rurais e comerciantes.",
                "pontos": 10
            },
            {
                "pergunta": "Qual grupo de imigrantes teve papel importante no comércio de Jequié no final do século XIX?",
                "alternativas": [
                    "A) Italianos",
                    "B) Japoneses",
                    "C) Alemães",
                    "D) Sírio-libaneses"
                ],
                "resposta_correta": 3,
                "explicacao": "Os sírio-libaneses se estabeleceram como comerciantes e tiveram papel fundamental no desenvolvimento comercial da cidade.",
                "contexto": "🤝 Além dos sírio-libaneses, imigrantes italianos como Vicente Grillo também contribuíram para o desenvolvimento local.",
                "pontos": 10
            }
        ]
    
    def _carregar_perguntas_fase2(self):
        """Fase 2: Resiliência e Crescimento (1910-1950)"""
        return [
            {
                "pergunta": "Em 1911, Jequié teve um curioso episódio político. O que tentou se tornar?",
                "alternativas": [
                    "A) Estado independente",
                    "B) Capital da Bahia",
                    "C) República autônoma",
                    "D) Cidade-estado"
                ],
                "resposta_correta": 1,
                "explicacao": "Durante a Revolta de 1911, houve uma tentativa de transferir a capital de Salvador para Jequié.",
                "contexto": "🏛️ A tentativa foi liderada por Rui Barbosa, que via em Jequié uma localização estratégica para a capital.",
                "pontos": 15
            },
            {
                "pergunta": "Por qual apelido Jequié ficou conhecida após a grande enchente de 1914?",
                "alternativas": [
                    "A) Veneza Baiana",
                    "B) Chicago Baiana",
                    "C) Paris do Sertão",
                    "D) Terra da Chuva"
                ],
                "resposta_correta": 1,
                "explicacao": "A rápida recuperação após a enchente de 1914 fez Jequié ganhar o apelido de 'Chicago Baiana'.",
                "contexto": "🌧️ A enchente de 1914 destruiu grande parte da cidade, mas sua rápida reconstrução impressionou a todos.",
                "pontos": 15
            },
            {
                "pergunta": "Qual foi uma das principais atividades econômicas de Jequié na primeira metade do século XX?",
                "alternativas": [
                    "A) Cultivo de cacau",
                    "B) Extração de petróleo",
                    "C) Indústria automobilística",
                    "D) Turismo internacional"
                ],
                "resposta_correta": 0,
                "explicacao": "Jequié se destacou como importante região produtora de cacau, contribuindo para a economia baiana.",
                "contexto": "🍫 A região sudoeste da Bahia, incluindo Jequié, foi uma das principais produtoras de cacau do Brasil.",
                "pontos": 15
            },
            {
                "pergunta": "Como ficou conhecido o período de intenso desenvolvimento urbano de Jequié nas décadas de 1940-1950?",
                "alternativas": [
                    "A) Era do Progresso",
                    "B) Fase da Modernização",
                    "C) Ciclo do Cacau",
                    "D) Anos Dourados"
                ],
                "resposta_correta": 0,
                "explicacao": "O período foi marcado por obras de infraestrutura e crescimento populacional significativo.",
                "contexto": "🏗️ Nesta época foram construídos importantes prédios públicos e melhorada a infraestrutura urbana.",
                "pontos": 15
            },
            {
                "pergunta": "Qual importante via de transporte contribuiu para o crescimento de Jequié como centro regional?",
                "alternativas": [
                    "A) Estrada de Ferro",
                    "B) Aeroporto Internacional",
                    "C) Hidrovia do São Francisco",
                    "D) Rodovia Rio-Bahia"
                ],
                "resposta_correta": 3,
                "explicacao": "A BR-116 (Rio-Bahia) fortaleceu a posição de Jequié como ponto estratégico no interior da Bahia.",
                "contexto": "🛣️ A rodovia facilitou o escoamento da produção agrícola e o transporte de passageiros.",
                "pontos": 15
            }
        ]
    
    def _carregar_perguntas_fase3(self):
        """Fase 3: Geografia e Economia Atual"""
        return [
            {
                "pergunta": "Em qual região da Bahia Jequié está localizada?",
                "alternativas": [
                    "A) Litoral Norte",
                    "B) Sudoeste Baiano",
                    "C) Recôncavo Baiano",
                    "D) Chapada Diamantina"
                ],
                "resposta_correta": 1,
                "explicacao": "Jequié está situada na região sudoeste do estado da Bahia.",
                "contexto": "🗺️ A cidade está a aproximadamente 365 km de Salvador, a capital do estado.",
                "pontos": 20
            },
            {
                "pergunta": "Qual é o bioma predominante na região de Jequié?",
                "alternativas": [
                    "A) Mata Atlântica",
                    "B) Cerrado",
                    "C) Caatinga",
                    "D) Transição Cerrado-Caatinga"
                ],
                "resposta_correta": 3,
                "explicacao": "Jequié está em uma área de transição entre o Cerrado e a Caatinga.",
                "contexto": "🌵🌿 Essa transição confere à região uma biodiversidade única, com espécies dos dois biomas.",
                "pontos": 20
            },
            {
                "pergunta": "Qual setor econômico NÃO faz parte da base econômica tradicional de Jequié?",
                "alternativas": [
                    "A) Pecuária",
                    "B) Cultivo de café",
                    "C) Mineração industrial",
                    "D) Comércio regional"
                ],
                "resposta_correta": 2,
                "explicacao": "A mineração industrial não é tradicional em Jequié, que tem base agropecuária e comercial.",
                "contexto": "💰 A pecuária e o cultivo de café e cacau foram os pilares econômicos históricos da região.",
                "pontos": 20
            },
            {
                "pergunta": "Por que Jequié é considerada um importante centro regional?",
                "alternativas": [
                    "A) Por ser a capital do estado",
                    "B) Por sua posição estratégica no interior",
                    "C) Por ter o maior porto da Bahia",
                    "D) Por abrigar a única universidade do estado"
                ],
                "resposta_correta": 1,
                "explicacao": "Sua localização estratégica a torna um centro de abastecimento e serviços para municípios vizinhos.",
                "contexto": "📍 Jequié serve como polo comercial, educacional e de saúde para mais de 30 municípios da região.",
                "pontos": 20
            },
            {
                "pergunta": "Qual é o principal rio que banha a cidade de Jequié?",
                "alternativas": [
                    "A) Rio São Francisco",
                    "B) Rio de Contas",
                    "C) Rio Paraguassu",
                    "D) Rio Jequitinhonha"
                ],
                "resposta_correta": 1,
                "explicacao": "O Rio de Contas é fundamental para a história e desenvolvimento de Jequié.",
                "contexto": "🌊 O Rio de Contas tem aproximadamente 620 km de extensão e sua bacia abrange várias cidades baianas.",
                "pontos": 20
            }
        ]
    
    def _carregar_perguntas_fase4(self):
        """Fase 4: Legislação e Governo Municipal"""
        return [
            {
                "pergunta": "Qual é o poder responsável pela elaboração das leis municipais em Jequié?",
                "alternativas": [
                    "A) Prefeitura Municipal",
                    "B) Câmara de Vereadores",
                    "C) Governo do Estado",
                    "D) Assembleia Legislativa"
                ],
                "resposta_correta": 1,
                "explicacao": "A Câmara de Vereadores é o poder legislativo municipal, responsável por criar as leis locais.",
                "contexto": "🏛️ A Câmara Municipal de Jequié é composta por vereadores eleitos pela população.",
                "pontos": 25
            },
            {
                "pergunta": "Segundo a Lei Municipal nº 175/1953, à qual referência salarial foram equiparadas as funções de Guardas Municipais?",
                "alternativas": [
                    "A) Referência VII",
                    "B) Referência VIII",
                    "C) Referência IX",
                    "D) Referência FG-3"
                ],
                "resposta_correta": 2,
                "explicacao": "A lei estabeleceu que os Guardas Municipais teriam equiparação salarial à Referência IX.",
                "contexto": "📜 Esta lei é um exemplo da estruturação do funcionalismo público municipal na década de 1950.",
                "pontos": 25
            },
            {
                "pergunta": "Qual documento estabelece as normas fundamentais da organização político-administrativa do município?",
                "alternativas": [
                    "A) Estatuto do Município",
                    "B) Regimento Interno",
                    "C) Lei Orgânica do Município",
                    "D) Carta Constitucional Municipal"
                ],
                "resposta_correta": 2,
                "explicacao": "A Lei Orgânica do Município funciona como uma 'constituição municipal'.",
                "contexto": "📄 Cada município brasileiro tem sua própria Lei Orgânica, dentro dos limites da Constituição Federal.",
                "pontos": 25
            },
            {
                "pergunta": "Qual destes NÃO é um cargo do poder executivo municipal?",
                "alternativas": [
                    "A) Prefeito",
                    "B) Vice-Prefeito",
                    "C) Secretário Municipal",
                    "D) Vereador"
                ],
                "resposta_correta": 3,
                "explicacao": "Vereador é cargo do poder legislativo, não do executivo municipal.",
                "contexto": "⚖️ O município tem três poderes independentes: Executivo (Prefeito), Legislativo (Vereadores) e Judiciário (Justiça Estadual).",
                "pontos": 25
            },
            {
                "pergunta": "O que a Lei Municipal nº 485/1962 estabelecia?",
                "alternativas": [
                    "A) Criação do Parque Municipal",
                    "B) Regulamentação do comércio",
                    "C) Estruturação do funcionalismo público",
                    "D) Definição dos limites urbanos"
                ],
                "resposta_correta": 2,
                "explicacao": "Esta lei tratava da estruturação e organização do funcionalismo público municipal.",
                "contexto": "📋 Leis como esta mostram a evolução da administração pública municipal ao longo das décadas.",
                "pontos": 25
            }
        ]
    
    def limpar_tela(self):
        """Limpa a tela do terminal"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def exibir_introducao(self):
        """Exibe a tela de introdução do jogo"""
        self.limpar_tela()
        print("=" * 60)
        print("DESAFIO JEQUIÉ: CONHEÇA SUA HISTÓRIA E SUAS LEIS")
        print("=" * 60)
        print("\n🎮 Bem-vindo ao jogo de conhecimentos sobre Jequié!")
        print("\n📚 Você passará por 4 fases temáticas:")
        print("   Fase 1: Origens e Emancipação")
        print("   Fase 2: Resiliência e Crescimento")
        print("   Fase 3: Geografia e Economia Atual")
        print("   Fase 4: Legislação e Governo Municipal")
        print("\n💡 Regras do jogo:")
        print("   • Você tem 3 vidas")
        print("   • Cada fase tem 5 perguntas")
        print("   • Para passar de fase: acerte pelo menos 3 perguntas")
        print("   • Acertos desbloqueiam Cartas de Contexto")
        print("\n🏆 Boa sorte! Prepare-se para testar seus conhecimentos!")
        print("=" * 60)
        input("\nPressione ENTER para começar...")
    
    def exibir_status(self):
        """Exibe o status atual do jogador"""
        print(f"\n{'='*50}")
        print(f"FASE {self.fase_atual}/4 | ❤️ Vidas: {self.vidas} | 📊 Pontos: {self.pontos}")
        print(f"Cartas descobertas: {len(self.cartas_descobertas)}/20")
        print(f"{'='*50}\n")
    
    def fazer_pergunta(self, pergunta_dict):
        """Faz uma pergunta ao jogador e retorna se acertou"""
        print(f"\n{pergunta_dict['pergunta']}\n")
        
        for alternativa in pergunta_dict['alternativas']:
            print(alternativa)
        
        while True:
            try:
                resposta = input("\nSua resposta (A/B/C/D): ").upper()
                if resposta in ['A', 'B', 'C', 'D']:
                    indice_resposta = ord(resposta) - ord('A')
                    break
                else:
                    print("Por favor, digite A, B, C ou D")
            except:
                print("Resposta inválida. Tente novamente.")
        
        acertou = indice_resposta == pergunta_dict['resposta_correta']
        
        if acertou:
            print(f"\n✅ CORRETO! +{pergunta_dict['pontos']} pontos")
            print(f"💡 {pergunta_dict['explicacao']}")
            self.pontos += pergunta_dict['pontos']
            
            # Adicionar carta de contexto
            if pergunta_dict['contexto'] not in self.cartas_descobertas:
                self.cartas_descobertas.append(pergunta_dict['contexto'])
                print(f"\n✨ NOVA CARTA DESBLOQUEADA!")
                print(f"📜 {pergunta_dict['contexto']}")
        else:
            letra_correta = chr(ord('A') + pergunta_dict['resposta_correta'])
            alternativa_correta = pergunta_dict['alternativas'][pergunta_dict['resposta_correta']]
            print(f"\n❌ ERRADO! A resposta correta era: {letra_correta}) {alternativa_correta.split(') ')[1]}")
            print(f"💡 {pergunta_dict['explicacao']}")
            self.vidas -= 1
        
        time.sleep(2)
        return acertou
    
    def jogar_fase(self, numero_fase):
        """Executa uma fase completa do jogo"""
        self.limpar_tela()
        print(f"\n{'='*60}")
        print(f"FASE {numero_fase}: {self.obter_titulo_fase(numero_fase)}")
        print(f"{'='*60}")
        
        perguntas_fase = self.perguntas[numero_fase].copy()
        random.shuffle(perguntas_fase)  # Embaralha as perguntas
        perguntas_fase = perguntas_fase[:5]  # Pega 5 perguntas
        
        acertos = 0
        
        for i, pergunta in enumerate(perguntas_fase, 1):
            self.limpar_tela()
            self.exibir_status()
            print(f"Pergunta {i}/5 da Fase {numero_fase}")
            
            if self.fazer_pergunta(pergunta):
                acertos += 1
            
            if self.vidas <= 0:
                print("\n💔 SUAS VIDAS ACABARAM!")
                return False
        
        # Verifica se passou de fase
        self.limpar_tela()
        print(f"\n{'='*60}")
        print(f"RESULTADO DA FASE {numero_fase}")
        print(f"{'='*60}")
        print(f"Acertos: {acertos}/5")
        
        if acertos >= 3:
            print(f"\n🎉 PARABÉNS! Você passou para a próxima fase!")
            if numero_fase < self.total_fases:
                print(f"Prepare-se para a Fase {numero_fase + 1}!")
            return True
        else:
            print(f"\n❌ Você precisa de pelo menos 3 acertos para passar.")
            print("Tente novamente!")
            return False
    
    def obter_titulo_fase(self, numero_fase):
        """Retorna o título da fase"""
        titulos = {
            1: "Origens e Emancipação (até 1897)",
            2: "Resiliência e Crescimento (1910-1950)",
            3: "Geografia e Economia Atual",
            4: "Legislação e Governo Municipal"
        }
        return titulos.get(numero_fase, "Fase Desconhecida")
    
    def exibir_cartas_descobertas(self):
        """Exibe todas as cartas de contexto descobertas"""
        self.limpar_tela()
        print("=" * 60)
        print("📚 CARTAS DE CONTEXTO DESBLOQUEADAS")
        print("=" * 60)
        
        if not self.cartas_descobertas:
            print("\nNenhuma carta descoberta ainda.")
        else:
            for i, carta in enumerate(self.cartas_descobertas, 1):
                print(f"\n{i}. {carta}")
        
        print("\n" + "=" * 60)
        input("\nPressione ENTER para continuar...")
    
    def exibir_game_over(self):
        """Exibe tela de game over"""
        self.limpar_tela()
        print("=" * 60)
        print("💔 GAME OVER")
        print("=" * 60)
        print(f"\nSua pontuação final: {self.pontos} pontos")
        print(f"Cartas descobertas: {len(self.cartas_descobertas)}/20")
        print(f"\nFase alcançada: {self.obter_titulo_fase(self.fase_atual)}")
        print("\nObrigado por jogar! Estude mais sobre Jequié e tente novamente!")
        print("=" * 60)
    
    def exibir_vitoria(self):
        """Exibe tela de vitória"""
        self.limpar_tela()
        print("=" * 60)
        print("🏆 PARABÉNS! VOCÊ COMPLETOU O DESAFIO JEQUIÉ!")
        print("=" * 60)
        print(f"\n🎯 Pontuação final: {self.pontos} pontos")
        print(f"📚 Cartas descobertas: {len(self.cartas_descobertas)}/20")
        
        # Classificação baseada na pontuação
        if self.pontos >= 300:
            classificacao = "EXPERT EM JEQUIÉ 🏅"
        elif self.pontos >= 200:
            classificacao = "CONHECEDOR AVANÇADO 🥈"
        elif self.pontos >= 100:
            classificacao = "APRENDIZ DE HISTÓRIA 🥉"
        else:
            classificacao = "INICIANTE"
        
        print(f"🏅 Sua classificação: {classificacao}")
        print("\nVocê demonstrou grande conhecimento sobre:")
        print("• História e origens de Jequié")
        print("• Desenvolvimento e crescimento da cidade")
        print("• Geografia e economia regional")
        print("• Legislação e governo municipal")
        print("\nContinue estudando e preservando a história da nossa cidade!")
        print("=" * 60)
    
    def menu_principal(self):
        """Exibe o menu principal durante o jogo"""
        while True:
            self.limpar_tela()
            self.exibir_status()
            print("\nMENU PRINCIPAL:")
            print("1. Continuar jogando")
            print("2. Ver cartas descobertas")
            print("3. Sair do jogo")
            
            opcao = input("\nEscolha uma opção (1-3): ")
            
            if opcao == "1":
                return True
            elif opcao == "2":
                self.exibir_cartas_descobertas()
            elif opcao == "3":
                print("\nAté logo! Obrigado por jogar!")
                return False
            else:
                print("Opção inválida. Tente novamente.")
                time.sleep(1)
    
    def jogar(self):
        """Função principal que controla o fluxo do jogo"""
        self.exibir_introducao()
        
        while self.fase_atual <= self.total_fases and self.vidas > 0:
            # Pergunta se quer continuar ou ver menu
            self.limpar_tela()
            if self.fase_atual > 1:
                print(f"\nPronto para a Fase {self.fase_atual}?")
                print("1. Sim, continuar")
                print("2. Ver menu")
                
                opcao = input("\nEscolha (1-2): ")
...                 if opcao == "2":
...                     if not self.menu_principal():
...                         return
...             
...             # Joga a fase atual
...             if self.jogar_fase(self.fase_atual):
...                 if self.fase_atual < self.total_fases:
...                     self.fase_atual += 1
...                     print("\n" + "=" * 60)
...                     input("Pressione ENTER para continuar para a próxima fase...")
...                 else:
...                     # Última fase completada
...                     break
...             else:
...                 # Não passou na fase
...                 if self.vidas > 0:
...                     print("\n" + "=" * 60)
...                     input("Pressione ENTER para tentar novamente esta fase...")
...                 else:
...                     break
...         
...         # Fim do jogo
...         if self.vidas <= 0:
...             self.exibir_game_over()
...         elif self.fase_atual > self.total_fases:
...             self.exibir_vitoria()
...         
...         # Pergunta se quer jogar novamente
...         print("\nDeseja jogar novamente? (S/N): ")
...         if input().upper() == "S":
...             self.__init__()  # Reinicia o jogo
...             self.jogar()
...         else:
...             print("\nObrigado por jogar Desafio Jequié! Até a próxima!")
... 
... # Inicia o jogo
... if __name__ == "__main__":
...     jogo = JogoJequie()
