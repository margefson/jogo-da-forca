from datetime import datetime

class Player:
    """Representa um jogador com estatísticas avançadas"""
    
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.games_played = 0
        self.games_won = 0
        self.total_errors = 0
        self.total_hints_used = 0
        self.created_at = datetime.now()
        self.last_played = datetime.now()
    
    def add_win(self, points=10):
        """Adiciona uma vitória"""
        self.score += points
        self.games_played += 1
        self.games_won += 1
        self.last_played = datetime.now()
    
    def add_loss(self, errors=0, hints_used=0):
        """Adiciona uma derrota"""
        self.games_played += 1
        self.total_errors += errors
        self.total_hints_used += hints_used
        self.last_played = datetime.now()
    
    def __str__(self):
        return f"{self.name} - Pontuação: {self.score} | Vitórias: {self.win_rate:.1f}%"
    
    def __repr__(self):
        return f"Player('{self.name}', score={self.score}, games={self.games_played})"
    
    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.name.lower() == other.name.lower()
    
    def __lt__(self, other):
        """Ordena por score (decrescente)"""
        if not isinstance(other, Player):
            return NotImplemented
        return self.score > other.score
    
    def __add__(self, other):
        """Combina estatísticas de dois jogadores (mesmo nome)"""
        if not isinstance(other, Player) or self.name != other.name:
            raise ValueError("Só é possível combinar jogadores com o mesmo nome")
        
        combined = Player(self.name)
        combined.score = self.score + other.score
        combined.games_played = self.games_played + other.games_played
        combined.games_won = self.games_won + other.games_won
        combined.total_errors = self.total_errors + other.total_errors
        combined.total_hints_used = self.total_hints_used + other.total_hints_used
        combined.created_at = min(self.created_at, other.created_at)
        combined.last_played = max(self.last_played, other.last_played)
        
        return combined
    
    @property
    def win_rate(self):
        """Taxa de vitórias em porcentagem"""
        if self.games_played == 0:
            return 0.0
        return (self.games_won / self.games_played) * 100
    
    @property
    def average_errors(self):
        """Média de erros por jogo"""
        if self.games_played == 0:
            return 0.0
        return self.total_errors / self.games_played
    
    def get_detailed_stats(self):
        """Retorna estatísticas detalhadas formatadas"""
        stats = [
            f"👤 Jogador: {self.name}",
            f"🏆 Pontuação Total: {self.score}",
            f"📊 Partidas: {self.games_played}",
            f"✅ Vitórias: {self.games_won}",
            f"❌ Derrotas: {self.games_played - self.games_won}",
            f"📈 Taxa de Vitórias: {self.win_rate:.1f}%",
            f"🎯 Média de Erros: {self.average_errors:.1f} por jogo",
            f"💡 Dicas Usadas: {self.total_hints_used}",
            f"🕒 Última Partida: {self.last_played.strftime('%d/%m/%Y %H:%M')}"
        ]
        return "\n".join(stats)