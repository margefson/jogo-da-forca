🎮 Jogo da Forca em Python
Um jogo clássico da forca implementado em Python com interface colorida, múltiplas dificuldades, sistema de dicas e estatísticas avançadas.

📋 Índice
Visão Geral
 - Funcionalidades
 - Estrutura do Projeto
 - Instalação e Execução
 - Como Jogar
 - Classes e Componentes
 - Arquivos de Dados
 - Sistema de Dificuldades
 - Personalização
 - Desenvolvimento
 - Licença

🎯 Visão Geral
Este projeto implementa o jogo da forca com foco em boas práticas de programação, organização de código e uso de conceitos avançados de Python. O jogo inclui um sistema completo de pontuação dinâmica, múltiplas dificuldades, sistema de dicas inteligente e persistência robusta em arquivos.

✨ Funcionalidades
🎮 Funcionalidades Principais
✅ Jogo da forca clássico com palavras relacionadas à programação
✅ 4 níveis de dificuldade (Fácil, Normal, Difícil, Especialista)
✅ Sistema de dicas inteligente (até 2 dicas por partida)
✅ Pontuação dinâmica baseada em desempenho e dificuldade
✅ Estatísticas detalhadas do jogador (médias, taxas, histórico)
✅ Interface colorida com arte ASCII melhorada
✅ Validação robusta de entradas do usuário

💾 Persistência de Dados
✅ Leitura de palavras de arquivo de dicionário com validação
✅ Salvamento automático do placar em formato JSON
✅ Backup automático de arquivos de palavras
✅ Carregamento do histórico de pontuações com timestamps

🏗️ Arquitetura e Organização
✅ Organização em pacotes Python (game, utils, data)
✅ Separação de responsabilidades em classes especializadas
✅ Código modular, documentado e fácil de manter
✅ Tratamento de erros robusto em todas as operações

🔧 Técnicas Avançadas
✅ Sobrecarga de métodos mágicos (__str__, __repr__, __eq__, __lt__, __add__)
✅ Uso de propriedades (@property) para cálculos dinâmicos
✅ Enumerações para gerenciamento de dificuldades
✅ Compreensões de lista e geradores
✅ Métodos de classe e estáticos
✅ Tipagem de dados e documentação completa

📁 Estrutura do Projeto
text
forca_aprimorada/
├── 📄 main.py                 # Ponto de entrada do programa
├── 📦 game/                   # Pacote principal do jogo
│   ├── __init__.py
│   ├── 🎯 core.py             # Classe principal HangmanGame
│   ├── 👤 player.py           # Classe Player com estatísticas avançadas
│   └── 🎯 difficulty.py       # Enumeração de dificuldades
├── 📦 utils/                  # Utilitários e helpers
│   ├── __init__.py
│   ├── 📁 file_manager.py     # Gerenciamento robusto de arquivos
│   └── 🖥️ display.py          # Sistema de exibição colorida
└── 📁 data/                   # Dados do jogo
    ├── 📝 palavras.txt        # Lista de palavras do dicionário
    └── 📊 placar.json         # Placar em JSON (gerado automaticamente)
🚀 Instalação e Execução
Pré-requisitos
Python 3.6 ou superior

Terminal que suporte cores ANSI (Linux, macOS, Windows Terminal)

Nenhuma dependência externa necessária

📥 Como executar
Clone ou baixe o projeto

bash
git clone [url-do-repositorio]
cd forca
Execute o jogo

bash
python main.py
Ou execute diretamente (se tiver permissões de execução):

bash
./main.py
🎮 Como Jogar
🏁 Início do Jogo
Digite seu nome quando solicitado

Escolha entre 4 níveis de dificuldade

O jogo seleciona automaticamente uma palavra adequada à dificuldade

🎯 Durante o Jogo
Digite letras para tentar adivinhar a palavra
 - Letras corretas são reveladas na posição correspondente (verde)
 - Letras incorretas avançam o estado da forca (vermelho)
 - Use 'dica' ou 'd' para receber uma letra sugerida (roxo)
 - Letras usadas são mostradas em amarelo

Barra de progresso indica proximidade do game over

💀 Fim do Jogo
🎉 Vitória: Todas as letras são descobertas dentro do limite de erros

💀 Derrota: Número máximo de erros é atingido

📊 Sistema de Pontuação
Pontuação = (Letras na palavra × 10) - (Erros × 5) - (Dicas × 15) + (Bônus de Dificuldade × 20)
Bônus de dificuldade: Fácil(20), Normal(40), Difícil(60), Especialista(80)

Pontuação mínima garantida: 10 pontos

🏗️ Classes e Componentes
🎯 HangmanGame (core.py)
Classe principal que orquestra todo o jogo.

Métodos principais:
 - setup_game(): Configura jogador e dificuldade
 - play_round(): Executa uma rodada completa
 - choose_difficulty(): Seleção interativa de dificuldade
 - get_hint(): Sistema inteligente de dicas
 - calculate_score(): Cálculo dinâmico de pontuação

👤 Player (player.py)
Representa um jogador com estatísticas avançadas.

Características:
 - Rastreia vitórias, derrotas, pontuação total
 - Calcula taxas de vitória e médias automaticamente
 - Métodos mágicos para comparação e combinação
 - Timestamps de criação e última partida

Métodos mágicos:
 - __add__: Combina estatísticas de jogadores com mesmo nome
 - __lt__: Ordenação por pontuação (maior primeiro)
 - __eq__: Comparação por nome

🎯 Difficulty (difficulty.py)
Enumeração que define os níveis de dificuldade.

Níveis disponíveis:
 - EASY: 8 erros, palavras 3-6 letras
 - NORMAL: 6 erros, palavras 5-8 letras
 - HARD: 4 erros, palavras 7-10 letras
 - EXPERT: 3 erros, palavras 9-15 letras

📁 FileManager (file_manager.py)
Gerencia todas as operações de arquivo com tratamento robusto.

Funcionalidades:
 - Leitura validada de palavras do dicionário
 - Salvamento do placar em JSON com timestamps
 - Backup automático de arquivos
 - Criação de diretórios quando necessário

🖥️ Display (display.py**)
Sistema avançado de exibição com cores ANSI.

Componentes:
 - Arte ASCII colorida da forca em 8 estágios
 - Sistema de mensagens por tipo (erro, sucesso, aviso, dica)
 - Barra de progresso colorida baseada em erros
 - Formatação consistente de todos os elementos visuais

Cores disponíveis:

🟢 Verde: acertos e sucesso
🔴 Vermelho: erros e perigo
🟡 Amarelo: avisos e letras usadas
🔵 Azul: informações
🟣 Roxo: dicas
⚪ Cinza: elementos neutros

📊 Arquivos de Dados
📝 palavras.txt
Lista de palavras usadas no jogo (uma por linha).

Formato:
 - txt
    - programacao
    - computador
    - algoritmo
    - variavel
    - funcao
    - classe
    - # ... mais palavras

Requisitos:
 - Apenas letras (sem acentos)
 - Uma palavra por linha
 - Encoding UTF-8

📊 placar.json
Placar gerado automaticamente pelo jogo em formato JSON.

Formato:
json
[
  {
    "player": "João",
    "score": 145,
    "timestamp": "2024-01-15T10:30:00",
    "date": "15/01/2024 10:30"
  }
]

🎯 Sistema de Dificuldades
Dificuldade	Erros	Tamanho das Palavras	Bônus

 - Fácil	8	3-6 letras	+20
 - Normal	6	5-8 letras	+40
 - Difícil	4	7-10 letras	+60
 - Especialista	3	9-15 letras	+80
 - 
🎨 Personalização
🔤 Adicionar Novas Palavras
Edite o arquivo data/palavras.txt:

txt
 - sua_palavra_aqui
 - outra_palavra
 - mais_uma

⚙️ Modificar Dificuldade
Edite os valores em game/difficulty.py:

python
@property
def max_errors(self):
    return {
        Difficulty.EASY: 8,      # Altere estes valores
        Difficulty.NORMAL: 6,
        Difficulty.HARD: 4,
        Difficulty.EXPERT: 3
    }[self]

🎨 Personalizar Cores
Modifique a classe Colors em utils/display.py:

python
class Colors:
    MINHA_COR = '\033[94m'  # Código ANSI para azul claro
    # ... outras cores

💡 Modificar Sistema de Dicas
Ajuste em game/core.py:

python
def __init__(self):
    self.max_hints = 3  # Aumente o número de dicas
    # ...

🔧 Desenvolvimento
📝 Adicionando Novas Funcionalidades
 - Novas classes: Adicione no pacote game/
 - Novos utilitários: Coloque em utils/
 - Novos dados: Adicione em data/

🧪 Testando Modificações
bash
# Execute após modificações
python main.py

# Para debugging específico
import pdb; pdb.set_trace()  # Adicione onde necessário

🐛 Reportando Problemas
Ao encontrar problemas:
 - Descreva o comportamento esperado vs atual
 - Inclua mensagens de erro completas
 - Especifique seu ambiente (SO, versão Python, terminal)
 - Mencione a dificuldade selecionada e palavra (se aplicável)

💡 Sugestões de Melhorias Futuras
Modo multiplayer competitivo
 - Sistema de conquistas e badges
 - Timer por rodada

Modo desafio com palavras específicas
 - Integração com API de dicionário online
 - Sons e efeitos sonoros

Modo tutorial para iniciantes

📄 Licença
Este projeto é para fins educacionais. Desenvolvido como exemplo de aplicação Python completa demonstrando:

✅ Organização de código em pacotes
✅ Princípios de OOP avançada
✅ Manipulação robusta de arquivos
✅ Sistemas de interface de usuário
✅ Tratamento completo de erros
✅ Boas práticas de programação

Sinta-se à vontade para usar, modificar e distribuir.

👨‍💻 Team: Margefson, Thyago e Amon
Desenvolvido como trabalho prático de programação em Python.

Divirta-se jogando! 🎮✨

Para dúvidas ou sugestões, abra uma issue no repositório do projeto.
