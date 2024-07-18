from basics.analyzers.analyzer3 import Analyzer3
# from basics.find_ticket_by_id import find_ticket_by_id



messages = [
    {
        "sender": "client",
        "message": "oi"
    },
    {
        "sender": "bot",
        "message": "Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sobre os assuntos abaixo: \n\n- Adquirir o Cartão Nio\n- Consultar o status da sua proposta\n- Informações sobre Saque Parcelado\n- Atendimento para correspondentes Nio Digital\n- Órgãos/Empresas Conveniadas\nClique neste link:  https://api.whatsapp.com/send?phone=551130793682&text=Ol%C3%A1,%20NIO%20Digital\n\nAgora, se você já é cliente NIO Digital e deseja informações sobre o seu Cartão de Crédito Consignado, nosso horário de atendimento com especialistas é de segunda a sexta-feira, das 8h às 20h, exceto em feriados.\n\nPor favor, anote seu protocolo de atendimento: 1106202437d0d050c0. ㅤ\nPara iniciarmos seu atendimento, por favor informe o número do seu CPF. (apenas números)."
    }
]


analyzer = Analyzer3()

isValid = analyzer.isValid(messages)

qualification = analyzer.getQualifications(messages)

print(isValid, qualification)



# print(find_ticket_by_id('37d0d050c0b24194a85dbdaa883e156d'))