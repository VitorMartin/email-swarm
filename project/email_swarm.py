#Imports ====================================================
import os

import yagmail as yg

os.system('cls')


#Functions ==================================================
def get_contacts(filename, separator):
    '''
    Returns a list of emails.
    '''
    emails = []
    with open(filename, mode='r', encoding='utf-8') as file:
        contacts = file.read()
        emails = contacts.split(separator)
    emails = [email.strip(' ') for email in emails]
    return emails

def get_body(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        body = file.read()
    return body

def get_file_name(input_text):
    inp = input(input_text)

    if inp == '':
        return inp

    wrong_inp = True
    while wrong_inp:
        try:
            open(inp, 'rb')
        except FileNotFoundError:
            print('\nArquivo não encontrado! Verifique o nome do arquivo e sua extensão.')
            inp = input('\nDigite o nome do arquivo a ser anexado COM extensão: ')
        except:
            print('\nErro desconhecido')
            inp = ''
            wrong_inp = False
        else:
            wrong_inp = False
            print()
    return inp

def get_server():
    user = input('Digite o email remetente: ')
    password = input('Digite a senha: ')
    print()
    wrong_login = True
    while wrong_login:
        try:
            server = yg.SMTP(user, password=password)
        except:
            print('Email ou senha inválidos! Tente novamente.')
            user = input('Digite o email remetente: ')
            password = input('Digite a senha: ')
            print()
        else:
            wrong_login = False
    return server


#Variables ==================================================
attachment_file_name = get_file_name('Digite o nome do arquivo a ser anexado: ')
# attachment_file_name = 'picture.png'

contacts_file = 'contacts.txt'
contacts_separator = input('Digite o separador dos emails: ')
if contacts_separator == '':
    contacts_separator = '\n'
emails = get_contacts(contacts_file, contacts_separator)

subject = input('Digite o assunto do email: ')
# subject = 'Assunto'
print()

body_file_name = 'message.txt'
source_body = get_body(body_file_name)


#Sending email ==============================================
server = get_server()
print('Enviando emails. Não feche essa janela! Você será notificado por email quando terminar...\n')

wrong_password = True
while wrong_password:
    try:
        if attachment_file_name == '':
            server.send(subject=subject, contents=source_body, bcc=emails)
        else:
            server.send(subject=subject, contents=source_body, attachments=attachment_file_name, bcc=emails)
    except:
        print('Email ou senha do remetente incorretos! Digite-os novamente.')
        server = get_server()
        print('Enviando emails. Não feche essa janela! Você será notificado por email quando terminar...\n')
    else:
        wrong_password = False

server.send(subject='Sua lista de transmissão terminou', contents='Sua lista de transmissão terminou.')

input('Fim do processo. Para sair, aperte [ENTER]\n')
