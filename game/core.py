import random
import sys
from utils.file_manager import FileManager
from utils.display import Display
from game.player import Player
from game.difficulty import Difficulty

class HangmanGame:
    """Classe principal do jogo da forca com todos os recursos avançados"""
    
    def __init__(self):
        self.file_manager = FileManager("palavras.txt")
        self.words = self.file_manager.read_words()
        self.player = None
        self.difficulty = Difficulty.NORMAL
        self.hints_used = 0
        self.max_hints = 2
    
    def setup_game(self):
        """Configura o jogo com interface avançada"""
        Display.show_welcome()
        
        # Configuração do jogador
        name = Display.get_input("Digite seu nome: ", required=True)
        self.player = Player(name if name else "Jogador")
        
        # Seleção de dificuldade
        self.choose_difficulty()
        
        Display.show_message(f"Bem-vindo, {self.player.name}! Dificuldade: {self.difficulty.name}", "info")
    
    def choose_difficulty(self):
        """Permite ao jogador escolher a dificuldade"""
        Display.show_title("SELECIONE A DIFICULDADE")
        options = [
            "1 - Fácil (8 erros permitidos)",
            "2 - Normal (6 erros permitidos)", 
            "3 - Difícil (4 erros permitidos)",
            "4 - Especialista (3 erros permitidos)"
        ]
        
        for option in options:
            Display.show_message(option, "menu")
        
        while True:
            choice = Display.get_input("Escolha (1-4): ")
            try:
                difficulty_map = {
                    '1': Difficulty.EASY,
                    '2': Difficulty.NORMAL,
                    '3': Difficulty.HARD,
                    '4': Difficulty.EXPERT
                }
                self.difficulty = difficulty_map[choice]
                break
            except (KeyError, ValueError):
                Display.show_message("Opção inválida! Escolha entre 1-4.", "error")
    
    def choose_word(self):
        """Escolhe uma palavra baseada na dificuldade"""
        if not self.words:
            raise ValueError("Nenhuma palavra disponível no dicionário!")
        
        # Filtra palavras por dificuldade
        filtered_words = [word for word in self.words if self.difficulty.is_word_suitable(word)]
        
        if not filtered_words:
            # Fallback para palavras do nível normal se não houver para a dificuldade
            filtered_words = self.words
        
        return random.choice(filtered_words)
    
    def get_hint(self, word, correct_letters, used_letters):
        """Fornece uma dica ao jogador"""
        if self.hints_used >= self.max_hints:
            Display.show_message("Você já usou todas as dicas disponíveis!", "warning")
            return False
        
        # Encontra letras não descobertas e não tentadas
        available_letters = [letter for letter in set(word) 
                           if letter not in correct_letters and letter not in used_letters]
        
        if not available_letters:
            Display.show_message("Não há dicas disponíveis para esta palavra!", "info")
            return False
        
        hint_letter = random.choice(available_letters)
        self.hints_used += 1
        Display.show_message(f"💡 DICA: A palavra contém a letra '{hint_letter.upper()}'!", "hint")
        Display.show_message(f"Dicas restantes: {self.max_hints - self.hints_used}", "info")
        return True
    
    def validate_guess(self, guess, used_letters):
        """Valida robustamente o palpite do jogador"""
        if not guess:
            raise ValueError("Entrada vazia! Digite uma letra.")
        
        if len(guess) != 1:
            raise ValueError("Digite apenas UMA letra!")
        
        if not guess.isalpha():
            raise ValueError("Entrada inválida! Use apenas letras do alfabeto.")
        
        if guess in used_letters:
            raise ValueError(f"Você já tentou a letra '{guess.upper()}'!")
        
        return guess.lower()
    
    def calculate_score(self, word, errors, hints_used):
        """Calcula a pontuação baseada no desempenho"""
        base_points = len(word) * 10
        error_penalty = errors * 5
        hint_penalty = hints_used * 15
        difficulty_bonus = self.difficulty.value * 20
        
        score = base_points - error_penalty - hint_penalty + difficulty_bonus
        return max(score, 10)  # Pontuação mínima
    
    def play_round(self):
        """Executa uma rodada completa do jogo"""
        try:
            word = self.choose_word()
        except ValueError as e:
            Display.show_message(str(e), "error")
            return
        
        correct_letters = set()
        used_letters = set()
        errors = 0
        self.hints_used = 0
        
        Display.clear_screen()
        Display.show_title("JOGO DA FORCA")
        Display.show_message(f"Palavra: {len(word)} letras | Dificuldade: {self.difficulty.name}", "info")
        Display.show_message(f"Dicas disponíveis: {self.max_hints}", "info")
        
        while errors < self.difficulty.max_errors:
            # Exibe estado atual do jogo
            Display.show_game_state(word, correct_letters, used_letters, errors, self.difficulty.max_errors)
            
            # Verifica vitória
            if all(letter in correct_letters for letter in word):
                score = self.calculate_score(word, errors, self.hints_used)
                self.player.add_win(score)
                Display.show_victory(word, score)
                break
            
            # Obtém ação do jogador
            action = Display.get_input("\nDigite uma letra ou 'dica' para ajuda: ").lower().strip()
            
            try:
                if action == 'dica' or action == 'd':
                    self.get_hint(word, correct_letters, used_letters)
                    continue
                
                guess = self.validate_guess(action, used_letters)
                used_letters.add(guess)
                
                if guess in word:
                    Display.show_message(f"✅ Letra '{guess.upper()}' correta!", "success")
                    correct_letters.add(guess)
                else:
                    errors += 1
                    Display.show_message(f"❌ Letra '{guess.upper()}' incorreta! Erros: {errors}/{self.difficulty.max_errors}", "error")
                    
            except ValueError as e:
                Display.show_message(str(e), "error")
                continue
            except Exception as e:
                Display.show_message(f"Erro inesperado: {e}", "error")
                continue
        
        else:
            # Game Over
            Display.show_game_over(word)
            self.player.add_loss()
    
    def show_stats(self):
        """Mostra estatísticas detalhadas"""
        Display.show_title("ESTATÍSTICAS")
        print(self.player.get_detailed_stats())
        
        # Mostra placar geral
        scores = self.file_manager.read_scores()
        if scores:
            Display.show_leaderboard(scores)
    
    def run(self):
        """Loop principal do jogo"""
        try:
            self.setup_game()
            
            while True:
                self.play_round()
                self.file_manager.save_score(self.player.name, self.player.score)
                self.show_stats()
                
                if not Display.get_yes_no_input("\nDeseja jogar novamente?"):
                    Display.show_message("Obrigado por jogar! Até a próxima! 🎮", "info")
                    break
                
                # Oferece mudar dificuldade
                if Display.get_yes_no_input("Deseja alterar a dificuldade?"):
                    self.choose_difficulty()
                
                Display.clear_screen()
                
        except Exception as e:
            Display.show_message(f"Erro crítico: {e}", "error")
            sys.exit(1)