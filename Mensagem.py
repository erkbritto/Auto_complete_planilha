class Mensagem:
    def __init__(self, sender: str, message: str):
        self.sender = sender
        self.message = message

# Exemplo de dados de entrada simulados
chat_data = [
    {
        "sender": "client",
        "message": "Bom dia"
    },
    {
        "sender": "bot",
        "message": "Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sobre os assuntos abaixo: \n\n- Adquirir o Cartão Nio\n- Consultar o status da sua proposta\n- Informações sobre Saque Parcelado\n- Atendimento para correspondentes Nio Digital\n- Órgãos/Empresas Conveniadas\nClique neste link:  https://api.whatsapp.com/send?phone=551130793682&text=Ol%C3%A1,%20NIO%20Digital\n\nAgora, se você já é cliente NIO Digital e deseja informações sobre o seu Cartão de Crédito Consignado, nosso horário de atendimento com especialistas é de segunda a sexta-feira, das 8h às 20h, exceto em feriados.\n\nPor favor, anote seu protocolo de atendimento: 14062024069ecd639d. \nPara iniciarmos seu atendimento, por favor informe o número do seu CPF. (apenas números)."
    },
    {
        "sender": "client",
        "message": "30275103803"
    },
    {
        "sender": "bot",
        "message": "Ótimo. Em que posso ajudar?\n *Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a sua fatura\n3 - Bloqueio, desbloqueio, 2ª via ou outras informações\n4 - Não reconhecimento de compras ou saques\n5 - Contestação de taxas\n6 - Elogio, sugestão ou reclamação\n7 - Atualização cadastral\n8 - Informações sobre entrega do cartão\n9 - Aplicativo Nio Digital\n10 - Problemas no Boleto/Pagamento da Fatura\n0 - Outros assuntos"
    },
    {
        "sender": "client",
        "message": "3"
    },
    {
        "sender": "bot",
        "message": "*Digite a opção desejada para*:\n\n1 - Bloqueio\n2 - Desbloqueio\n3 - Segunda via ou cartão adicional\n4 - Senha\n5 - Aumento de limite\n6 - Programa Mastercard Surpreenda\n0 - Retornar ao menu anterior"
    },
    {
        "sender": "client",
        "message": "2"
    },
    {
        "sender": "bot",
        "message": "Para efetuar o desbloqueio do seu cartão, NIO Digital, precisamos que nos forneça algumas informações:\n\nQuais os últimos 4 dígitos do cartão que deseja desbloquear?"
    },
    {
        "sender": "client",
        "message": "8056"
    },
    {
        "sender": "bot",
        "message": "Qual o nome completo da sua mãe?"
    },
    {
        "sender": "client",
        "message": "Rita de Cacia Ferreira da Silva"
    },
    {
        "sender": "bot",
        "message": "Qual a sua data de nascimento? (dd/mm/aaaa)"
    },
    {
        "sender": "client",
        "message": "06/04/1980"
    },
    {
        "sender": "bot",
        "message": "Não conseguimos validar as informações fornecidas, pode por favor nos fornecer as seguintes informações:\n\nQuais os últimos 4 dígitos do cartão que deseja desbloquear?"
    },
    {
        "sender": "client",
        "message": "8056"
    },
    {
        "sender": "bot",
        "message": "Qual o nome completo da sua mãe?"
    },
    {
        "sender": "client",
        "message": "Rita de Cássia Ferreira da Silva"
    },
    {
        "sender": "bot",
        "message": "Qual a sua data de nascimento? (dd/mm/aaaa)"
    },
    {
        "sender": "client",
        "message": "06/04/1980"
    },
    {
        "sender": "bot",
        "message": "Não conseguimos validar as informações fornecidas, pode por favor nos fornecer as seguintes informações.\nPeço que confirme as informações solicitadas e retorno o contato. \nTe ajudo em algo mais? (Sim ou Não)"
    },
    {
        "sender": "client",
        "message": "Sim"
    },
    {
        "sender": "bot",
        "message": "*Digite a opção desejada para*:\n\n1 - Limite disponível para utilização\n2 - Informações sobre a sua fatura\n3 - Bloqueio, desbloqueio, 2ª via ou outras informações\n4 - Não reconhecimento de compras ou saques\n5 - Contestação de taxas\n6 - Elogio, sugestão ou reclamação\n7 - Atualização cadastral\n8 - Informações sobre entrega do cartão\n9 - Aplicativo Nio Digital\n10 - Problemas no Boleto/Pagamento da Fatura\n0 - Outros assuntos"
    },
    {
        "sender": "client",
        "message": "2"
    },
    {
        "sender": "bot",
        "message": "Por favor informe os 4 últimos dígitos do cartão que deseja consultar."
    },
    {
        "sender": "client",
        "message": "8056"
    }
]

# Verificar a estrutura das mensagens do usuário
structure_result = Mensagem(chat_data)
print("Structure Result:", structure_result)