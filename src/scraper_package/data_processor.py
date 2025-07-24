# data_processor.py

import pandas as pd
import traceback
import os

class DataProcessor:
    """
        Esta classe serve para processar dados para arquivos
    """
    def __init__(self):
        """
        Inicializa o DataProcessor.
        """
    
    def export_to_excel(self, data_list: list[dict[str, str]], filename: str, dir: str) -> bool:
        """
        Converte uma lista de dicionários para um DataFrame e exporta para um arquivo Excel (.xlsx).
        """

        if not data_list:
            print("Lista de dicionários vazia. Nenhuma exportação para Excel realizada.")
            return False
        
        try:
            full_output_path = os.path.join(dir, filename)
            os.makedirs(dir, exist_ok=True)
            df = pd.DataFrame(data_list)
            df.to_excel(full_output_path, index=False)
            return True
        except Exception as e:
            print(f"Falha ao exportar DataFrame para Excel: {e}")
            traceback.print_exc()
            return False