# data_processor.py

import pandas as pd
import traceback
from typing import List, Any, Dict

class DataProcessor:
    """
        Esta classe serve para processar dados para arquivos
    """
    def __init__(self):
        """
        Inicializa o DataProcessor.
        """
    
    def export_to_excel(self, data_list: List[Dict[str, Any]], filename: str) -> bool:
        """
        Converte uma lista de dicionários para um DataFrame e exporta para um arquivo Excel (.xlsx).
        """

        if not data_list:
            print("Lista de dicionários vazia. Nenhuma exportação para Excel realizada.")
            return False
        
        try:
            df = pd.DataFrame(data_list)
            df.to_excel(filename, index=False)
            return True
        except Exception as e:
            print(f"Falha ao exportar DataFrame para Excel: {e}")
            traceback.print_exc()
            return False