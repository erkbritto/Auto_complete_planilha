from basics.helper_xlsx import HelperXlsx, INTERACTION_ID, OPCAO_SELECIONADA, JORNADA_DO_CLIENTE_NO_CHATBOT, FINALIZACAO_DO_CONTATO, ANALYZER_ID
from basics.get_file_name import get_file_name
from basics.find_ticket_in_json import find_ticket_in_json
from basics.find_ticket_agent_in_json import find_ticket_agent_in_json
from basics.getAnalyzers2 import getAnalyzers

fileName:str = get_file_name()

# Instancia a classe para lidar com o xlsx
helperXlsx = HelperXlsx()

# Ler os dados do arquivo xlsx
file = helperXlsx.read(fileName)

# Pular a primeira linha
for index, line in enumerate(file):
    
    if index == 0:
        continue

    # Forma de obter(e definir os dados do ticket)
    messagesBot = find_ticket_in_json(line[INTERACTION_ID])
    allMessages = find_ticket_agent_in_json(line[INTERACTION_ID])

    # pula os vazios
    if not line[INTERACTION_ID]:
        continue

    # pula os vazios
    # if not (line[INTERACTION_ID] == '70f62ed74c894ad9a118d2213c694aab'):
    #     continue

    # instancia o analisador
    analyzers = getAnalyzers()
    
    for analyzerId, analyzer in enumerate(analyzers):

        # Incrementa o id do analyzer
        analyzerId+=1

        # Pula caso a estrutura não seja valida
        if not analyzer.isValid(messagesBot, allMessages):
            continue
    
        # Pega as qualificações
        qualifications = analyzer.getQualifications(messagesBot, allMessages)

        # Insere as qualificações no ticket
        file[index][OPCAO_SELECIONADA] = qualifications['selectedOption']
        file[index][JORNADA_DO_CLIENTE_NO_CHATBOT] = qualifications['customerJourney']
        file[index][FINALIZACAO_DO_CONTATO] = qualifications['finalizationOfTheContract']
        file[index][ANALYZER_ID] = analyzerId
        
        # Salva o arquivo a cada alteração
        # helperXlsx.write('./output/file.xlsx', file)
        
        # Encerra o loop dos analyzers caso o ticket tenha sido validado
        break


# Salva o arquivo no fim da execução
helperXlsx.write('./output/file2.xlsx', file)
