import csv

with open("spotify-2023.csv", "r", encoding='latin-1') as arquivo:
    linhas = arquivo.readlines()

# 1. Exibir as primeiras 5 linhas
print("=== Primeiras 5 linhas ===\n")
for linha in linhas[1:6]:
    print(linha.strip())

def get_top_10_streamed_songs_2012_2022_24_cols():
    filename = "spotify-2023.csv"
    all_valid_songs = [] 
    
    expected_columns = 24 
    
    try:
        with open(filename, 'r', encoding='latin-1') as f:
            header = f.readline().strip() # Ler e pular o cabeçalho
            # print(f"Cabeçalho: {header}") # Para depuração

            for line_idx, raw_line in enumerate(f):
                current_line_content = raw_line.strip()
                if not current_line_content: # Pular linhas em branco
                    continue

                # Etapa 1: Verificação para ignorar linhas com base em aspas nos primeiros dois campos (raw)
                first_comma_idx = current_line_content.find(',')
                if first_comma_idx == -1:
                    # print(f"Linha {line_idx+2} ignorada: Sem vírgulas.")
                    continue 

                potential_track_field_raw = current_line_content[:first_comma_idx]
                remainder_after_first_field = current_line_content[first_comma_idx+1:]
                
                second_comma_idx_in_remainder = remainder_after_first_field.find(',')
                if second_comma_idx_in_remainder == -1:
                    # print(f"Linha {line_idx+2} ignorada: Apenas uma vírgula.")
                    continue

                potential_artist_field_raw = remainder_after_first_field[:second_comma_idx_in_remainder]

                if potential_track_field_raw.startswith('"') or \
                   potential_artist_field_raw.startswith('"'):
                    # print(f"Linha {line_idx+2} ignorada devido à regra de aspas: Track='{potential_track_field_raw}', Artist='{potential_artist_field_raw}'")
                    continue
                
                # Etapa 2: Se a linha passou pelo filtro de aspas, parsear com csv.reader
                try:
                    parsed_fields_list = list(csv.reader([current_line_content]))
                    if not parsed_fields_list: 
                        continue
                    parsed_fields = parsed_fields_list[0]
                except csv.Error:
                    # print(f"Linha {line_idx+2} ignorada: Erro de parsing CSV.")
                    continue

                if len(parsed_fields) != expected_columns: # Verificação com expected_columns = 24
                    # print(f"Linha {line_idx+2} ignorada: Número incorreto de colunas ({len(parsed_fields)}). Esperado {expected_columns}. Linha: '{current_line_content}'")
                    continue

                # Etapa 3: Extrair e converter dados
                # Os índices [0], [1], [3], [8] devem continuar válidos para as colunas de interesse
                # track_name, artist_name, released_year, streams, respectivamente.
                try:
                    track_name = parsed_fields[0].strip()
                    artist_name = parsed_fields[1].strip()
                    released_year_str = parsed_fields[3].strip()
                    streams_str = parsed_fields[8].strip()

                    released_year = int(released_year_str)
                    streams = int(streams_str)
                except ValueError:
                    # print(f"Linha {line_idx+2} ignorada: Erro de conversão para ano/streams. Ano='{released_year_str}', Streams='{streams_str}'")
                    continue 
                except IndexError: # Se os índices 0, 1, 3 ou 8 não existirem (improvável se len(parsed_fields) == 24)
                    # print(f"Linha {line_idx+2} ignorada: Erro de índice ao acessar campos.")
                    continue

                # Etapa 4: Filtrar pelo intervalo de anos solicitado (2012 a 2022)
                if not (2012 <= released_year <= 2022):
                    # print(f"Linha {line_idx+2} ignorada: Ano {released_year} fora do intervalo 2012-2022.")
                    continue

                # Etapa 5: Adicionar música válida à lista
                all_valid_songs.append([track_name, artist_name, released_year, streams])
            
    except FileNotFoundError:
        # Esta mensagem de erro será impressa se o arquivo não for encontrado pelo script
        print(f"Erro: O arquivo '{filename}' não foi encontrado. Verifique o nome e o local do arquivo.")
        return [] 
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante o processamento do arquivo: {e}")
        return []

    # Etapa 6: Ordenar todas as músicas válidas por 'streams' em ordem decrescente
    all_valid_songs.sort(key=lambda song: song[3], reverse=True)
    
    # Etapa 7: Retornar as top 10 músicas
    return all_valid_songs[:10]

# Para executar o script e ver o resultado:
if __name__ == '__main__':
    top_10_songs = get_top_10_streamed_songs_2012_2022_24_cols()
print("\n=== Top 10 de 2012 a 2022 ===\n")
print(top_10_songs)
