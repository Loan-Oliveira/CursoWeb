import pyodbc
import pandas as pd
import openpyxl
from ftplib import FTP
import datetime

# Dados da conexão
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DBPRDSQLICS;"
    "Database=ics;"
    "uid=ics;"
    "pwd=icstotal*.0;"
)

# Variaveis gerais
log_erro = ""
crlf = "\r\n"

try:
  # Cria a string de data ex: '19_03_2025'
  try:
    data_sistema = datetime.datetime.now()
    data = data_sistema.date()
    data_formatada = data_sistema.strftime("%d_%m_%Y")
    header_log = "[" + data_sistema.strftime("%d/%m/%Y %H:%M:%S") + "] -> "
  except:
    log_erro = log_erro + "ERRO AO OBTER DATA DO SISTEMA" + crlf

  # Obtém a instrução SQL
  try:
    with open("H:/Loan/Issues Resolvidos/13015 - Planilha beneficiarios DENTALUNI/SQL/BeneficiariosAtivos.sql", 'r') as arquivo:
      comando = arquivo.read()
  except:
    log_erro = log_erro + header_log + "Falha ao carregar o SQL" + crlf

  # Estabelece conexão ao banco de dados
  try:
    conn = pyodbc.connect(dados_conexao)
  except:
    log_erro = log_erro + header_log + "Falha ao conectar com o banco de dados" + crlf

  # Gera a planilha
  with pd.ExcelWriter("H:/Loan/Issues Resolvidos/13015 - Planilha beneficiarios DENTALUNI/Arquivos Gerados/Atualizacoes Automaticas/Atualizacao_Automatica_" + data_formatada + ".xlsx", engine="openpyxl") as writer:
    try:
      df = pd.read_sql(comando, conn)
      df.to_excel(writer, sheet_name = "Tab1", header = True, index = False)

      print("Gerando Planilha...")
      log_erro = log_erro + header_log + "Gerando arquivo..." + crlf
    except:
      print("Erro!")
      log_erro = log_erro + header_log + "Falha ao gerar a planilha" + crlf

  print("Arquivo Salvo!")
  log_erro = log_erro + header_log + "Arquivo salvo com sucesso" + crlf

  # Conecta no servidor FTP
  try:
    ftp = FTP('172.31.31.22', 'loaoliveira', '4EGSZ7MF')
  except:
    log_erro = log_erro + header_log + "Falha ao conectar ao servidor FTP" + crlf

  # Verifica se já existe o diretório
  pastasFTP = ftp.nlst()
  if 'DentalUni' not in pastasFTP:
    try:
      ftp.mkd('DentalUni')
    except:
      log_erro = log_erro + header_log + "Falha ao criar diretório DentalUni" + crlf

  # Acessa o diretório
  try:
    ftp.cwd('/DentalUni')
  except:
    log_erro = log_erro + header_log + "Falha ao acessar diretório DentalUni" + crlf

  # Lista arquivos
  #arquivosFTP = ftp.nlst()
  #for arquivoFTP in arquivosFTP:
  #    print(arquivoFTP)
  # Exlui os arquivos existentes

  # Faz o upload do arquivo
  try:
    with open('H:/Loan/Issues Resolvidos/13015 - Planilha beneficiarios DENTALUNI/Arquivos Gerados/Atualizacoes Automaticas/Atualizacao_Automatica_' + data_formatada + '.xlsx', 'rb') as arquivo_local:
      ftp.storbinary('STOR Atualizacao_Automatica_' + data_formatada + '.xlsx', arquivo_local)
  except:
    log_erro = log_erro + header_log + "Falha ao realizar o upload do arquivo para o ftp" + crlf

  # Chamar a rotina de envio de email a partir daqui

  log_erro = log_erro + header_log + "Fim do programa!" + crlf
except:
  log_erro = log_erro + header_log + "Falha ao executar o programa." + crlf
finally:
  # Salva log erro
  print(log_erro)
  with open('LogServicoDentalUni.txt', 'w') as f:
    f.write('{}\n'.format(log_erro))