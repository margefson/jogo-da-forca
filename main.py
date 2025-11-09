#!/usr/bin/env python3
"""
Jogo da Forca
Autor: Margefson Barros
Descrição: Jogo clássico da forca com sistema de pontuação
"""

from game.core import HangmanGame

def main():
    """Função principal do jogo"""
    print("=" * 50)
    print("         🎮 JOGO DA FORCA 🎮")
    print("=" * 50)
    print()
    
    try:
        game = HangmanGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\nJogo interrompido. Até mais!")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    main()