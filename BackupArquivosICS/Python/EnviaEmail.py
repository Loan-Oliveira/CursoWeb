import smtplib
from email.message import EmailMessage

# Email do ICS
email = 'desenvolvimento.ics@gmail.com'
password = 'Icstotal*.0'

# Criando a mensagem
msg = EmailMessage()
msg['Subject'] = 'Atualização periódica da planilha dos beneficiários'
msg['From'] = email
msg['To'] = 'eversouza@ici.curitiba.pr.gov.br'
msg.set_content('Bom dia.\r\nEm anexo, a planilha de beneficiários atualizada.')

# Adicionando o anexo
with open("H:/Loan/Issues Resolvidos/13015 - Planilha beneficiarios DENTALUNI/Arquivos Gerados/Atualizacoes Automaticas/Atualização_Automática.xlsx", 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# Enviando o email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)

print('Email enviado com sucesso!')