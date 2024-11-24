import re
import tkinter as tk
from tkinter import scrolledtext

# Expressões regulares para diferentes tipos de tokens
regex_patterns = [
    ('Palavra-chave', r'\b(print|if|else|while|return|def|for|break|continue|class|try|except|finally|import|from|as|with|pass|yield|lambda|assert|raise|del|global|nonlocal|True|False|None|and|or|not|is|in)\b'),
    ('Identificador', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('Número', r'\b\d+\b'),
    ('String Literal', r'"[^"]*"|\'[^\']*\''),
    ('Delimitador', r'[\[\](){}.,;:]'),
    ('Operador', r'[+\-*/%&|^~<>!=]=?|//|<<|>>|\*\*'),
    ('Espaços', r'[ \t]+'),
    ('Desconhecido', r'.')
]

# Função para analisar o código e identificar os tokens
def analisar_codigo():
    # Obtém o texto da caixa de entrada
    codigo = entrada.get("1.0", tk.END).strip()
    
    # Limpa a caixa de saída
    saida.delete("1.0", tk.END)
    
    # Contador total de tokens
    total_tokens = 0
    
    # Posição inicial para a análise
    pos = 0
    
    # Enquanto houver código para analisar
    while pos < len(codigo):
        match_found = False
        # Testa cada padrão de regex
        for token_type, pattern in regex_patterns:
            regex = re.compile(pattern)
            match = regex.match(codigo, pos)
            if match:
                # Conta e exibe todos os tokens, incluindo espaços
                total_tokens += 1
                saida.insert(tk.END, f" '{match.group(0)}', {token_type}\n")
                
                # Avança a posição no código
                pos = match.end()
                match_found = True
                break
        # Se nenhum padrão casar, avança um caractere
        if not match_found:
            pos += 1
    
    # Exibe o total de tokens
    saida.insert(tk.END, f"\nTotal de tokens: {total_tokens}\n")

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Analisador Léxico")

# Caixa de entrada para o código
tk.Label(janela, text="Digite o código:").pack()
entrada = scrolledtext.ScrolledText(janela, width=50, height=10)
entrada.pack()

# Botão para iniciar a análise
botao = tk.Button(janela, text="Analisar Código", command=analisar_codigo)
botao.pack()

# Caixa de saída para mostrar os tokens identificados
tk.Label(janela, text="Saída da Análise Léxica:").pack()
saida = scrolledtext.ScrolledText(janela, width=50, height=10)
saida.pack()

# Inicia a aplicação
janela.mainloop()
