import os
import sys
from typing import List, Set

class Colors:
    """Códigos ANSI para cores no terminal"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'

class Display:
    """Responsável pela exibição avançada do jogo com cores"""
    
    # Arte ASCII melhorada da forca
    STAGES = [
        f"""
{Colors.CYAN}
   ┌─────
   │    
   │    
   │    
   │    
   │    
━━━━━━━{Colors.RESET}
        """,
        f"""
{Colors.CYAN}
   ┌─────
   │    {Colors.YELLOW}🎯{Colors.CYAN}
   │    
   │    
   │    
   │    
━━━━━━━{Colors.RESET}
        """,
        f"""
{Colors.CYAN}
   ┌─────
   │    {Colors.YELLOW}😟{Colors.CYAN}
   │    {Colors.BLUE}│{Colors.CYAN}
   │    
   │    
   │    
━━━━━━━{Colors.RESET}
        """,
        f"""
{Colors.CYAN}
   ┌─────
   │    {Colors.YELLOW}😬{Colors.CYAN}
   │    {Colors.BLUE}│{Colors.CYAN}
   │    {Colors.BLUE}○{Colors.CYAN}
   │    
   │    
━━━━━━━{Colors.RESET}
        """,
        f"""
{Colors.CYAN}
   ┌─────
   │    {Colors.YELLOW}😨{Colors.CYAN}
   │   {Colors.BLUE}╱│{Colors.CYAN}
   │    {Colors.BLUE}○{Colors.CYAN}
   │    
   │    
━━━━━━━{Colors.RESET}
        """,
        f"""
{Colors.CYAN}
   ┌─────
   │    {Colors.YELLOW}😰{Colors.CYAN}
   │   {Colors.BLUE}╱│╲{Colors.CYAN}
   │    {Colors.BLUE}○{Colors.CYAN}
   │    
   │    
━━━━━━━{Colors.RESET}
        """,
        f"""
{Colors.CYAN}
   ┌─────
   │    {Colors.YELLOW}😱{Colors.CYAN}
   │   {Colors.BLUE}╱│╲{Colors.CYAN}
   │    {Colors.BLUE}○{Colors.CYAN}
   │   {Colors.BLUE}╱ {Colors.CYAN}
   │    
━━━━━━━{Colors.RESET}
        """,
        f"""
{Colors.CYAN}
   ┌─────
   │    {Colors.RED}💀{Colors.CYAN}
   │   {Colors.BLUE}╱│╲{Colors.CYAN}
   │    {Colors.BLUE}○{Colors.CYAN}
   │   {Colors.BLUE}╱ ╲{Colors.CYAN}
   │    
━━━━━━━{Colors.RESET}
        """
    ]
    
    @classmethod
    def clear_screen(cls):
        """Limpa a tela de forma cross-platform"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @classmethod
    def show_welcome(cls):
        """Exibe tela de boas-vindas"""
        cls.clear_screen()
        print(f"{Colors.MAGENTA}{'='*60}{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}          🎮 JOGO DA FORCA 🎮{Colors.RESET}")
        print(f"{Colors.MAGENTA}{'='*60}{Colors.RESET}")
        print(f"{Colors.YELLOW}✨ Recursos:{Colors.RESET}")
        print(f"  • {Colors.GREEN}Interface colorida{Colors.RESET}")
        print(f"  • {Colors.GREEN}Múltiplas dificuldades{Colors.RESET}") 
        print(f"  • {Colors.GREEN}Sistema de dicas{Colors.RESET}")
        print(f"  • {Colors.GREEN}Estatísticas detalhadas{Colors.RESET}")
        print(f"{Colors.MAGENTA}{'='*60}{Colors.RESET}\n")
    
    @classmethod
    def show_title(cls, title: str):
        """Exibe um título formatado"""
        print(f"\n{Colors.CYAN}{Colors.BOLD}=== {title} ==={Colors.RESET}\n")
    
    @classmethod
    def show_message(cls, message: str, msg_type: str = "info"):
        """Exibe uma mensagem colorida baseada no tipo"""
        colors = {
            "error": Colors.RED,
            "success": Colors.GREEN,
            "warning": Colors.YELLOW,
            "info": Colors.BLUE,
            "hint": Colors.MAGENTA,
            "menu": Colors.CYAN
        }
        color = colors.get(msg_type, Colors.WHITE)
        print(f"{color}{message}{Colors.RESET}")
    
    @classmethod
    def show_game_state(cls, word: str, correct_letters: Set[str], used_letters: Set[str], 
                       errors: int, max_errors: int):
        """Exibe o estado completo do jogo"""
        cls.show_hangman(errors)
        cls.show_word(word, correct_letters)
        cls.show_used_letters(used_letters)
        
        # Barra de progresso
        progress = errors / max_errors
        if progress < 0.33:
            color = Colors.GREEN
        elif progress < 0.66:
            color = Colors.YELLOW
        else:
            color = Colors.RED
            
        bar = "█" * int(progress * 20) + "░" * (20 - int(progress * 20))
        print(f"\nErros: {color}{errors}/{max_errors}{Colors.RESET}")
        print(f"Progresso: [{color}{bar}{Colors.RESET}]")
    
    @classmethod
    def show_hangman(cls, errors: int):
        """Exibe o estado atual da forca"""
        stage = min(errors, len(cls.STAGES) - 1)
        print(cls.STAGES[stage])
    
    @classmethod
    def show_word(cls, word: str, correct_letters: Set[str]):
        """Exibe a palavra com letras descobertas coloridas"""
        display_word = []
        for letter in word:
            if letter in correct_letters:
                display_word.append(f"{Colors.GREEN}{letter.upper()}{Colors.RESET}")
            else:
                display_word.append(f"{Colors.GRAY}_{Colors.RESET}")
        
        print(f"{Colors.BOLD}Palavra:{Colors.RESET} {' '.join(display_word)}")
        print()
    
    @classmethod
    def show_used_letters(cls, used_letters: Set[str]):
        """Exibe letras já utilizadas"""
        if used_letters:
            sorted_letters = sorted(used_letters)
            colored_letters = [f"{Colors.YELLOW}{letter.upper()}{Colors.RESET}" for letter in sorted_letters]
            print(f"{Colors.BOLD}Letras usadas:{Colors.RESET} {', '.join(colored_letters)}")
    
    @classmethod
    def show_victory(cls, word: str, score: int):
        """Exibe tela de vitória"""
        print(f"\n{Colors.GREEN}{'🎉'*20}{Colors.RESET}")
        print(f"{Colors.GREEN}{Colors.BOLD}          PARABÉNS! VOCÊ VENCEU! 🏆{Colors.RESET}")
        print(f"{Colors.GREEN}{Colors.BOLD}          Palavra: {word.upper()}{Colors.RESET}")
        print(f"{Colors.GREEN}{Colors.BOLD}          Pontuação: +{score} pontos{Colors.RESET}")
        print(f"{Colors.GREEN}{'🎉'*20}{Colors.RESET}")
    
    @classmethod
    def show_game_over(cls, word: str):
        """Exibe tela de game over"""
        print(f"\n{Colors.RED}{'💀'*20}{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}          GAME OVER!{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}          A palavra era: {word.upper()}{Colors.RESET}")
        print(f"{Colors.RED}{'💀'*20}{Colors.RESET}")
    
    @classmethod
    def show_leaderboard(cls, scores: List[str]):
        """Exibe o placar formatado"""
        cls.show_title("PLACAR GERAL - TOP 10")
        for i, score in enumerate(scores[-10:], 1):
            print(f"{Colors.YELLOW}{i:2d}.{Colors.RESET} {score}")
    
    @classmethod
    def get_input(cls, prompt: str, required: bool = False):
        """Obtém entrada do usuário com tratamento robusto"""
        while True:
            try:
                user_input = input(f"{Colors.CYAN}{prompt}{Colors.RESET}").strip()
                if required and not user_input:
                    cls.show_message("Este campo é obrigatório!", "error")
                    continue
                return user_input
            except (EOFError, KeyboardInterrupt):
                cls.show_message("\nOperação cancelada pelo usuário.", "warning")
                sys.exit(0)
    
    @classmethod
    def get_yes_no_input(cls, prompt: str) -> bool:
        """Obtém entrada sim/não do usuário"""
        while True:
            response = cls.get_input(f"{prompt} (s/n): ").lower().strip()
            if response in ['s', 'sim', 'y', 'yes']:
                return True
            elif response in ['n', 'não', 'nao', 'no']:
                return False
            else:
                cls.show_message("Por favor, responda com 's' ou 'n'", "error")