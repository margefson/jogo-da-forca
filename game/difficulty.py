from enum import Enum

class Difficulty(Enum):
    """Define os níveis de dificuldade do jogo"""
    
    EASY = 1
    NORMAL = 2
    HARD = 3
    EXPERT = 4
    
    @property
    def max_errors(self):
        """Número máximo de erros permitidos"""
        return {
            Difficulty.EASY: 8,
            Difficulty.NORMAL: 6,
            Difficulty.HARD: 4,
            Difficulty.EXPERT: 3
        }[self]
    
    @property
    def word_length_range(self):
        """Faixa de tamanho de palavras para esta dificuldade"""
        return {
            Difficulty.EASY: (3, 6),
            Difficulty.NORMAL: (5, 8),
            Difficulty.HARD: (7, 10),
            Difficulty.EXPERT: (9, 15)
        }[self]
    
    def is_word_suitable(self, word):
        """Verifica se uma palavra é adequada para esta dificuldade"""
        min_len, max_len = self.word_length_range
        return min_len <= len(word) <= max_len
    
    def __str__(self):
        return self.name.title()