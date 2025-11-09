class Player:
    """Representa um jogador"""
    
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.games_played = 0
        self.games_won = 0
    
    def add_win(self, points=10):
        """Adiciona uma vitória"""
        self.score += points
        self.games_played += 1
        self.games_won += 1
    
    def add_loss(self):
        """Adiciona uma derrota"""
        self.games_played += 1
    
    def __str__(self):
        return f"{self.name} - Pontos: {self.score} | Vitórias: {self.games_won}/{self.games_played}"
    
    def __repr__(self):
        return f"Player('{self.name}', score={self.score})"
    
    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.name.lower() == other.name.lower()
    
    def __lt__(self, other):
        """Ordena por score (decrescente)"""
        return self.score > other.score
    
    @property
    def win_rate(self):
        """Taxa de vitórias"""
        if self.games_played == 0:
            return 0
        return (self.games_won / self.games_played) * 100