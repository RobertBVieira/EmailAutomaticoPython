import smtplib
import ssl

# Configurações do servidor SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587 # Use 465 para conexão SSL direta

# Credenciais do remetente
EMAIL_REMETENTE = "seu email aqui " 
SENHA = "sua senha aqui"  # Use uma senha de aplicativo se a autenticação de dois fatores estiver ativada

# Lista de destinatários
lista_emails = ["lista de emails"]

# Conteúdo do e-mail
ASSUNTO = "Teste de Automatização de Email!"
MENSAGEM = """\
Subject: {}

Olá,

Aqui é o assunto do seu email;

Atenciosamente,

""".format(ASSUNTO)

# Conectando ao servidor SMTP e enviando e-mails
try:
    contexto = ssl.create_default_context()
    servidor_email = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    servidor_email.starttls(context=contexto)
    servidor_email.login(EMAIL_REMETENTE, SENHA)

    for destinatario in lista_emails:
        servidor_email.sendmail(EMAIL_REMETENTE, destinatario, MENSAGEM.encode("utf-8"))
        print(f"E-mail enviado para {destinatario}")

    servidor_email.quit()
    print("Todos os e-mails foram enviados com sucesso!")

except Exception as e:
    print(f"Erro ao enviar e-mails: {e}")
    