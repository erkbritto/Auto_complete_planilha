from basics.analyzers.analyzer2 import Analyzer2

""" from basics.find_ticket_by_id import find_ticket_by_id

print(find_ticket_by_id('a3436e09b33c4029838d7062445bf2bc'))

# a3436e09b33c4029838d7062445bf2bc """

messages = [
    {
        "sender": "client",
        "message": "Olá, NIO Digital!"
    },
    {
        "sender": "bot",
        "message": "Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sobre os assuntos abaixo: \n\n- Adquirir o Cartão Nio\n- Consultar o status da sua proposta\n- Informações sobre Saque Parcelado\n- Atendimento para correspondentes Nio Digital\n- Órgãos/Empresas Conveniadas\nClique neste link:  https://api.whatsapp.com/send?phone=551130793682&text=Ol%C3%A1,%20NIO%20Digital\n\nAgora, se você já é cliente NIO Digital e deseja informações sobre o seu Cartão de Crédito Consignado, nosso horário de atendimento com especialistas é de segunda a sexta-feira, das 8h às 20h, exceto em feriados.\n\nPor favor, anote seu protocolo de atendimento: 14062024a3436e09b3. ㅤ\nPara iniciarmos seu atendimento, por favor informe o número do seu CPF. (apenas números)."
    },
    {
        "sender": "client",
        "message": "09730487600"
    },
    {
        "sender": "bot",
        "message": "Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a sua fatura\n3 - Bloqueio, desbloqueio, 2ª via ou outras informações\n4 - Não reconhecimento de compras ou saques\n5 - Contestação de taxas\n6 - Elogio, sugestão ou reclamação\n7 - Atualização cadastral\n8 - Informações sobre entrega do cartão\n9 - Aplicativo Nio Digital\n10 - Problemas no Boleto/Pagamento da Fatura\n0 - Outros assuntos"
    }
]

analyzer = Analyzer2()

isValid = analyzer.isValid(messages)

qualification = analyzer.getQualifications(messages)

print(isValid, qualification)