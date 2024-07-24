# auto_complete_planilha

## Descrição da Automação

A automação `auto_complete_planilha` realiza uma série de tarefas para integrar e processar dados provenientes no Talkdesk, diretamente do WhatsApp e autopilot. Abaixo estão as principais funcionalidades e o fluxo de trabalho da automação:

### Funcionalidades Principais

1. **Acesso ao Talkdesk**:
   - Conecta-se à API do Talkdesk para obter IDs de interações e mensagens do bot e dos agentes do WhatsApp e autopilot na plataforma.

2. **Captura e Análise de Mensagens**:
   - Extrai e analisa mensagens, aplicando critérios de qualificação para classificar os dados.

3. **Geração e Aplicação de Analisadores**:
   - Cria e aplica analisadores automaticamente para validar as mensagens de acordo com critérios específicos.

4. **Exportação e Atualização de Dados**:
   - Exporta os dados qualificados e analisados para uma planilha Excel no diretório `output`.

5. **Criação de Novos Analisadores**:
   - Gera e atualiza analisadores conforme necessário para manter a eficácia da análise.

### Resumo do Fluxo de Trabalho

1. **Coleta de Dados**: Acessa o Talkdesk para obter IDs e mensagens.
2. **Processamento**: Analisa e qualifica as mensagens.
3. **Geração de Analisadores**: Cria e aplica analisadores para validação.
4. **Exportação para Excel**: Atualiza e exporta dados para um arquivo Excel.
5. **Atualização Contínua**: Gera novos analisadores conforme necessário.

## Configuração do Ambiente

### Instalação de Pacotes e debug

Para instalar os pacotes necessários e rodar o programa, execute o seguinte comando:

```bash
pip install selenium schedule pyyaml python-dotenv
pip install Helperxls

python main.py
python main2.py
python main3.py

