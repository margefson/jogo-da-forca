🎮 Jogo da Forca em Python
Um jogo clássico da forca implementado em Python com interface de texto, sistema de pontuação e persistência de dados.

📋 Índice
- Visão Geral
- Funcionalidades
- Estrutura do Projeto
- Instalação e Execução
- Como Jogar
- Classes e Componentes
- Arquivos de Dados
- Personalização
- Contribuindo

🎯 Visão Geral
Este projeto implementa o jogo da forca com foco em boas práticas de programação, organização de código e uso de conceitos avançados de Python. O jogo inclui um sistema completo de pontuação, estatísticas de jogador e persistência em arquivos.

✨ Funcionalidades
🎮 Funcionalidades Principais
✅ Jogo da forca clássico com palavras relacionadas à programação
✅ Sistema de pontuação com bônus por palavras maiores
✅ Estatísticas detalhadas do jogador (vitórias, derrotas, taxa de sucesso)
✅ Placar geral persistente entre sessões
✅ Interface de texto com arte ASCII da forca

💾 Persistência de Dados
✅ Leitura de palavras de um arquivo de dicionário
✅ Salvamento automático do placar em arquivo
✅ Carregamento do histórico de pontuações

🏗️ Arquitetura e Organização
✅ Organização em pacotes Python (game, utils, data)
✅ Separação de responsabilidades em classes especializadas
✅ Código modular e fácil de manter
✅ Tratamento de erros robusto

🔧 Técnicas Avançadas
✅ Sobrecarga de métodos mágicos (__str__, __repr__, __eq__, __lt__)
✅ Uso de propriedades (@property)
✅ Compreensões de lista
✅ Métodos de classe e estáticos

📁 Estrutura do Projeto
text
forca/
├── 📄 main.py                 # Ponto de entrada do programa
├── 📦 game/                   # Pacote principal do jogo
│   ├── __init__.py
│   ├── 🎯 core.py            # Classe principal HangmanGame
│   └── 👤 player.py          # Classe Player e sistema de pontuação
├── 📦 utils/                  # Utilitários e helpers
│   ├── __init__.py
│   ├── 📁 file_manager.py    # Gerenciamento de arquivos
│   └── 🖥️ display.py        # Exibição e interface
└── 📁 data/                  # Dados do jogo
    ├── 📝 palavras.txt       # Lista de palavras
    └── 📊 placar.txt        # Placar (gerado automaticamente)

🚀 Instalação e Execução
- Pré-requisitos
  - Python 3.6 ou superior
  - Nenhuma dependência externa necessária

📥 Como executar
- Clone ou baixe o projeto
  - bash
    - git clone [url-do-repositorio]
    - cd forca
      
- Execute o jogo
  - bash
    - python main.py

- Ou execute diretamente (se tiver permissões de execução)
  - bash
    - ./main.py
    
🎮 Como Jogar
  🏁 Início do Jogo
    - Ao iniciar, digite seu nome
    - O jogo seleciona automaticamente uma palavra do dicionário
    - Uma dica é mostrada: "palavra relacionada à programação"

🎯 Durante o Jogo
  - Digite letras para tentar adivinhar a palavra
  - Letras corretas são reveladas na posição correspondente
  - Letras incorretas avançam o estado da forca
  - Letras repetidas são ignoradas

💀 Fim do Jogo
  - Vitória: Todas as letras são descobertas antes de 6 erros
  - Derrota: Comete 6 erros (forca completa)

📊 Sistema de Pontuação
  - Pontos base: 10 pontos por vitória
  - Bônus: +1 ponto por letra na palavra
  - Exemplo: "python" (6 letras) = 16 pontos

🏗️ Classes e Componentes
  🎯 HangmanGame (core.py)
    Classe principal que orquestra todo o jogo.

Métodos principais:
  - play_round(): Executa uma rodada completa
  - choose_word(): Seleciona palavra aleatória
  - setup_player(): Configura jogador

👤 Player (player.py)
  Representa um jogador com estatísticas.
  Características:
    - Rastreia vitórias, derrotas e pontuação
    - Calcula taxa de vitórias automaticamente
    - Ordenável por pontuação (maior primeiro)

📁 FileManager (file_manager.py)
  Gerencia todas as operações de arquivo.
  Funcionalidades:
    - Leitura de palavras do dicionário
    - Salvamento do placar
    - Carregamento do histórico

🖥️ Display (display.py)
  Responsável por toda a exibição visual.
  Componentes:
    - Arte ASCII da forca em 7 estágios
    - Formatação de palavras e letras usadas
    - Exibição do placar

📊 Arquivos de Dados
  📝 palavras.txt
    Lista de palavras usadas no jogo (uma por linha).
    Formato:
      - text
      - python
      - programacao
      - computador
      - algoritmo
      
📊 placar.txt
  Placar gerado automaticamente pelo jogo.
  Formato:
    - text
    - João: 45
    - Maria: 32
    - Pedro: 28
    
🎨 Personalização
  🔤 Adicionar Novas Palavras
  Edite o arquivo data/palavras.txt:
    - txt
    - sua_palavra_aqui
    - outra_palavra
    - mais_uma
    
⚙️ Modificar Dificuldade
  No arquivo game/core.py, altere:
  python
    self.max_errors = 6  # Mude para mais (fácil) ou menos (difícil)
    
🎨 Personalizar Arte da Forca
  Edite os estágios em utils/display.py na constante STAGES.

🔧 Desenvolvimento
  📝 Adicionando Novas Funcionalidades
    - Novas classes: Adicione no pacote apropriado
    - Novos utilitários: Coloque em utils/
    - Novos dados: Adicione em data/

🧪 Testando Modificações
  bash
    # Execute após modificações
    python main.py

    # Para debugging, adicione:
    import pdb; pdb.set_trace()
  🤝 Contribuindo
  📋 Padrões de Código
    - Use nomes descritivos em português
    - Documente classes e métodos com docstrings
    - Mantenha a organização em pacotes

🐛 Reportando Problemas
  - Descreva o comportamento esperado vs atual
  - Inclua mensagens de erro completas
  - Especifique seu ambiente (SO, versão Python)

💡 Sugestões de Melhoria
  - Interface gráfica com Tkinter
  - Modo multiplayer
  - Categorias de palavras
  - Dificuldades variáveis
  - Sistema de dicas

📄 Licença
  Este projeto é para fins educacionais. Sinta-se à vontade para usar e modificar.

👨‍💻 Autor
  Desenvolvido como exemplo de aplicação Python completa demonstrando:
    - Organização de código em pacotes
    - Princípios de OOP
    - Manipulação de arquivos
    - Boas práticas de programação

Divirta-se jogando! 🎮✨

Para dúvidas ou sugestões, abra uma issue no repositório do projeto.
