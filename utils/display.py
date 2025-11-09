class Display:
    """Responsável pela exibição do jogo"""
    
    # Arte ASCII da forca
    STAGES = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    
    @classmethod
    def show_hangman(cls, errors):
        """Exibe o estado atual da forca"""
        print(cls.STAGES[errors])
    
    @classmethod
    def show_word(cls, word, correct_letters):
        """Exibe a palavra com letras descobertas"""
        display_word = [letter if letter in correct_letters else '_' for letter in word]
        print("Palavra: " + " ".join(display_word))
        print()
    
    @classmethod
    def show_used_letters(cls, used_letters):
        """Exibe letras já utilizadas"""
        if used_letters:
            print(f"Letras usadas: {', '.join(sorted(used_letters))}")
    
    @classmethod
    def show_scores(cls, scores):
        """Exibe o placar"""
        print("\n=== PLACAR ===")
        for i, score in enumerate(scores[-10:], 1):  # Mostra últimos 10
            print(f"{i}. {score}")
        print()
    
    @classmethod
    def clear_screen(cls):
        """Limpa a tela"""
        print("\n" * 50)