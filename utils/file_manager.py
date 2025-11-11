import os
import json
from pathlib import Path
from datetime import datetime

class FileManager:
    """Gerencia operações de arquivo com tratamento robusto de erros"""
    
    def __init__(self, filename):
        self.filename = filename
        self.data_dir = Path(__file__).parent.parent / "data"
        self.filepath = self.data_dir / filename
        
        # Garante que o diretório data existe
        self._ensure_data_directory()
    
    def _ensure_data_directory(self):
        """Garante que o diretório data existe"""
        try:
            self.data_dir.mkdir(exist_ok=True)
        except PermissionError:
            raise PermissionError(f"Sem permissão para criar diretório: {self.data_dir}")
        except Exception as e:
            raise Exception(f"Erro ao criar diretório: {e}")
    
    def read_words(self) -> list:
        """Lê palavras do arquivo com tratamento robusto"""
        try:
            if not self.filepath.exists():
                raise FileNotFoundError(f"Arquivo de palavras não encontrado: {self.filename}")
            
            with open(self.filepath, 'r', encoding='utf-8') as file:
                words = [line.strip().lower() for line in file if line.strip()]
            
            if not words:
                raise ValueError(f"Arquivo de palavras vazio: {self.filename}")
            
            # Filtra palavras válidas
            valid_words = [word for word in words if word.isalpha()]
            
            if len(valid_words) != len(words):
                print(f"⚠️  Aviso: {len(words) - len(valid_words)} palavras inválidas removidas")
            
            return valid_words
            
        except UnicodeDecodeError:
            raise UnicodeDecodeError("Erro de codificação no arquivo de palavras. Use UTF-8.")
        except Exception as e:
            raise Exception(f"Erro ao ler palavras: {e}")
    
    def save_score(self, player_name: str, score: int):
        """Salva pontuação no arquivo de placar com timestamp"""
        score_file = self.data_dir / "placar.json"
        
        try:
            scores = self.read_scores()
            
            # Adiciona nova pontuação
            new_score = {
                "player": player_name,
                "score": score,
                "timestamp": datetime.now().isoformat(),
                "date": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            scores.append(new_score)
            
            # Ordena por score (decrescente)
            scores.sort(key=lambda x: x["score"], reverse=True)
            
            # Mantém apenas top 100
            scores = scores[:100]
            
            with open(score_file, 'w', encoding='utf-8') as file:
                json.dump(scores, file, ensure_ascii=False, indent=2)
                
        except Exception as e:
            print(f"⚠️  Aviso: Não foi possível salvar a pontuação: {e}")
    
    def read_scores(self) -> list:
        """Lê o placar do arquivo JSON"""
        score_file = self.data_dir / "placar.json"
        
        if not score_file.exists():
            return []
        
        try:
            with open(score_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, UnicodeDecodeError):
            # Fallback para formato antigo ou cria novo
            return []
    
    def backup_words(self):
        """Cria backup do arquivo de palavras"""
        try:
            if self.filepath.exists():
                backup_path = self.data_dir / f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{self.filename}"
                with open(self.filepath, 'r', encoding='utf-8') as source:
                    with open(backup_path, 'w', encoding='utf-8') as target:
                        target.write(source.read())
        except Exception as e:
            print(f"⚠️  Aviso: Backup falhou: {e}")
    
    def __str__(self):
        return f"FileManager(file='{self.filename}', path='{self.filepath}')"
    
    def __repr__(self):
        return f"FileManager('{self.filename}')"