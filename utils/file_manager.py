import os
from pathlib import Path

class FileManager:
    """Gerencia operações de arquivo para o jogo da forca"""
    
    def __init__(self, filename):
        self.filename = filename
        self.data_dir = Path(__file__).parent.parent / "data"
        self.filepath = self.data_dir / filename
    
    def read_words(self):
        """Lê palavras do arquivo"""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                return [line.strip().lower() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Arquivo {self.filename} não encontrado!")
            return []
    
    def save_score(self, player_name, score):
        """Salva pontuação no arquivo de placar"""
        score_file = self.data_dir / "placar.txt"
        with open(score_file, 'a', encoding='utf-8') as file:
            file.write(f"{player_name}: {score}\n")
    
    def read_scores(self):
        """Lê o placar do arquivo"""
        score_file = self.data_dir / "placar.txt"
        if score_file.exists():
            with open(score_file, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file if line.strip()]
        return []
    
    def __str__(self):
        return f"FileManager(file='{self.filename}')"
    
    def __repr__(self):
        return f"FileManager('{self.filename}')"