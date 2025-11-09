import random
from utils.file_manager import FileManager
from utils.display import Display
from game.player import Player

class HangmanGame:
    """Classe principal do jogo da forca"""
    
    def __init__(self):
        self.file_manager = FileManager("palavras.txt")
        self.words = self.file_manager.read_words()
        self.player = None
        self.max_errors = 6
    
    def setup_player(self):
        """Configura o jogador"""
        name = input("Digite seu nome: ").strip()
        if not name:
            name = "Jogador"
        self.player = Player(name)
    
    def choose_word(self):
        """Escolhe uma palavra aleatória"""
        return random.choice(self.words) if self.words else "python"
    
    def play_round(self):
        """Executa uma rodada do jogo"""
        if not self.words:
            print("Nenhuma palavra disponível!")
            return
        
        word = self.choose_word()
        correct_letters = set()
        used_letters = set()
        errors = 0
        
        Display.clear_screen()
        print(f"Bem-vindo, {self.player.name}!")
        print("Jogo da Forca - Adivinhe a palavra!")
        print(f"Dica: É uma palavra relacionada à programação com {len(word)} letras\n")
        
        while errors < self.max_errors:
            Display.show_hangman(errors)
            Display.show_word(word, correct_letters)
            Display.show_used_letters(used_letters)
            print(f"Erros: {errors}/{self.max_errors}")
            
            # Verifica se ganhou
            if all(letter in correct_letters for letter in word):
                print(f"\n🎉 Parabéns! Você acertou: {word.upper()}")
                self.player.add_win(len(word))  # Mais pontos para palavras maiores
                break
            
            # Obtém palpite do jogador
            guess = input("\nDigite uma letra: ").lower().strip()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Por favor, digite apenas uma letra!")
                continue
            
            if guess in used_letters:
                print("Você já tentou esta letra!")
                continue
            
            used_letters.add(guess)
            
            if guess in word:
                print("✅ Letra correta!")
                correct_letters.add(guess)
            else:
                print("❌ Letra incorreta!")
                errors += 1
        else:
            Display.show_hangman(errors)
            print(f"\n💀 Game Over! A palavra era: {word.upper()}")
            self.player.add_loss()
        
        # Salva pontuação
        self.file_manager.save_score(self.player.name, self.player.score)
    
    def show_stats(self):
        """Mostra estatísticas do jogador"""
        print(f"\n=== ESTATÍSTICAS DE {self.player.name.upper()} ===")
        print(self.player)
        print(f"Taxa de vitórias: {self.player.win_rate:.1f}%")
        
        # Mostra placar geral
        scores = self.file_manager.read_scores()
        if scores:
            Display.show_scores(scores)
    
    def run(self):
        """Executa o jogo principal"""
        self.setup_player()
        
        while True:
            self.play_round()
            self.show_stats()
            
            play_again = input("\nDeseja jogar novamente? (s/n): ").lower().strip()
            if play_again not in ['s', 'sim', 'y', 'yes']:
                print("Obrigado por jogar!")
                break
            
            Display.clear_screen()