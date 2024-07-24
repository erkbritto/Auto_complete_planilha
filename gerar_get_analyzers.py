import sys

def gerar_get_analyzers(numero):

    with open('basics/getAnalyzers2.py', 'w') as f:
        # Escreve o cabeçalho do arquivo
        f.write('from typing import List\n')
        for i in range(numero):
            f.write(f'from basics.analyzers_autopilot_usuario.analyzer{i+1} import Analyzer{i+1}\n')
        
        # Escreve a função getAnalyzers
        f.write('def getAnalyzers():\n')
        f.write('    return [\n')
        for i in range(numero):
            f.write(f'        Analyzer{i+1}(),\n')
        f.write('    ]\n')

    print("Arquivo getAnalyzers2.py gerado com sucesso!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <numero>")
    else:
        try:
            numero = int(sys.argv[1])
            gerar_get_analyzers(numero)
        except ValueError:
            print("Por favor, forneça um número inteiro válido.")