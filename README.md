# Bem vindo ao Email Swarm!

Esta é uma ferramenta para enviar emails para uma lista de contatos. Siga o tutorial de como configurar esse serviço.

# Tutorial

## Conta

Você precisará de uma conta Gmail, **obrigatoriamente**. É recomendado que você crie uma nova conta Gmail descartável.

Para permitir o acesso do Email Swarm ao seu email, acesse esse **[link](https://myaccount.google.com/lesssecureapps)** e permita o acesso de aplicativos menos seguros ("Less secure app access") para a conta que irá enviar os emails.

Caso tenha dúvidas de como permitir o acesso, entre na conta em questão e siga as intruções desse **[link](https://support.google.com/accounts/answer/6010255?hl=en)**.

## Destinatários

Crie um arquivo de texto simples (`.txt`) chamado `contacts.txt` e salve-o na mesma pasta que o Email Swarm (`email_swarm.exe`).

Esse arquivo deve conter todos os endereços de email que você deseja enviar.

Você pode decidir qual o separador de emails você deseja usar. Pode ser uma nova linha, vírgula, ponto e vírgula etc. Isso pois o programa irá te solicitar: `Digite o separador dos emails`.

Não é preciso se preocupar com espaços em branco, pois o programa retira-os automaticamente.

**Caso você tenha escolhido uma nova linha por email,** quando o programa te perguntar, basta deixar o espaço em branco e apertar `ENTER`.

**Atenção:** Tab (`\t`) não funciona como separador!

Aqui estão alguns exemplos de como separar seus emails:

```
NOVA LINHA (\n):
email@dominio.com
email_2@dominio.com
arroz@feijao.com.br
-----------------------------------------------------------
PONTO E VÍRGULA (;):
email@dominio.com;email_2@dominio.com;arroz@feijao.com.br
-----------------------------------------------------------
VÍRGULA (,):
email@dominio.com,email_2@dominio.com,arroz@feijao.com.br
```

## Assunto

Esse é simples! Quando o Email Swarm solicitar "`Digite o nome do arquivo a ser anexado: `", digite o que quiser e aperte `ENTER`.

## Corpo do email

Igual à lista de destinatários, você deverá escrever o corpo do email em um arquivo de texto simples (`.txt`) e salvá-lo como `message.txt`, no mesmo local que o Email Swarm se encontra (`email_swarm.exe`).

Essa distribuição do Email Swarm **não suporta** textos customizáveis, por uma questão de simplicidade de uso ao usuário. Para utilizar textos customizáveis, como adicionar o nome do destinatário em cada email automaticamente, contate o dono do programa.

## Anexo

Quando o programa solicitar "`Digite o nome do arquivo a ser anexado: `", digite o nome do arquivo, **incluindo extensão**. Se não quiser nenhum anexo, basta deixar o espaço em branco e apertar `ENTER`.

Você tem duas opções para incluir seu anexo:

1. Copie o arquivo a ser anexado para a mesma pasta que o Email Swarm se encontra (`email_swarm.exe`). Em seguida, escreva o nome do arquivo **incluindo extensão** no Email Swarm, quando for solicitado.

    Exemplo: `anexo.png`

2. Não é preciso copiar o arquivo para a pasta do Email Swarm, porém, você precisa escrever o caminho completo de onde o arquivo se encontra. Essa informação se encontra nas propriedades do arquivo, no campo `Local: ` ou `Location: `

    Exemplo: `C:\Users\user\Documents\ANEXO.JPG`



# Sources

## Easiest module: `yagmail`

Site: Python Package Index (PyPI)

Article: Yagmail

https://pypi.org/project/yagmail/


## Alternate (harder to work with) modules: `email` and `smtplib`

1. Sending emails **without** attachment

    Site: Free Code Camp

    Article: Send Emails Using Python

    https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/

2. Sending emails **with** attachment

    Article: Send mail with attachment from your Gmail account using Python

    https://www.tutorialspoint.com/send-mail-with-attachment-from-your-gmail-account-using-python

