#!/usr/bin/env python3
"""
Jogo da Forca Aprimorado
Autor: Margefson Barros
Descrição: Jogo clássico da forca com interface colorida e recursos avançados
"""

from game.core import HangmanGame
import sys

def main():
    """Função principal do jogo"""
    try:
        game = HangmanGame()
        game.run()
    except KeyboardInterrupt:
        print("\n\nJogo interrompido pelo usuário. Até mais!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("Por favor, reinicie o jogo.")
        sys.exit(1)

if __name__ == "__main__":
    main()