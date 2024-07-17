from basics.analyzers.analyzer1 import Analyzer1
# from basics.find_ticket_by_id import find_ticket_by_id



messages = [
  {
    "sender": "client",
    "message": "24690.00117 01502.399304 00046.849865 6 00000000000000"
  },
  {
    "sender": "bot",
    "message": "Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sobre os assuntos abaixo: \n\n- Adquirir o Cartão Nio\n- Consultar o status da sua proposta\n- Informações sobre Saque Parcelado\n- Atendimento para correspondentes Nio Digital\n- Órgãos/Empresas Conveniadas\nClique neste link:  https://api.whatsapp.com/send?phone=551130793682&text=Ol%C3%A1,%20NIO%20Digital\n\nAgora, se você já é cliente NIO Digital e deseja informações sobre o seu Cartão de Crédito Consignado, nosso horário de atendimento com especialistas é de segunda a sexta-feira, das 8h às 20h, exceto em feriados.\n\nPor favor, anote seu protocolo de atendimento: 14062024808a565334. ㅤ\nPara iniciarmos seu atendimento, por favor informe o número do seu CPF. (apenas números)."
  },
  { "sender": "client", "message": "Bom.dia" },
  {
    "sender": "bot",
    "message": "Não conseguimos localizar o CPF informado, digite-o novamente, mas apenas os números, ok?"
  },
  { "sender": "client", "message": "01057157423" },
  {
    "sender": "bot",
    "message": "Que pena, mas não consegui localizar o CPF informado, peço que confirme a infirmação e nos contacte novamente, ok?\nNio Digital agradece, até logo!"
  }
]


analyzer = Analyzer1()

isValid = analyzer.isValid(messages)

qualification = analyzer.getQualifications(messages)

print(isValid, qualification)



# print(find_ticket_by_id('808a56533445406b95372be96e34c8b4'))