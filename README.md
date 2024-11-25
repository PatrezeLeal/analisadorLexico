# Analisador Léxico em Python
Este projeto é um Analisador Léxico desenvolvido em Python com interface gráfica utilizando a biblioteca tkinter. Ele permite identificar e categorizar tokens em um código-fonte com base em expressões regulares para diferentes tipos de tokens.

🚀 Funcionalidades
Identificação de tokens: Reconhece palavras-chave, identificadores, números, strings literais, delimitadores, operadores e espaços.
Interface gráfica: Possui uma interface intuitiva para entrada de código e exibição dos tokens identificados.
Contagem de tokens: Exibe o número total de tokens identificados no código.

🛠️ Tecnologias Utilizadas
Python 
tkinter: Para construção da interface gráfica.
re: Para uso de expressões regulares.

📋 Pré-requisitos
Certifique-se de ter o Python instalado em seu sistema. 

🏗️ Como Usar
1.Clone este repositório:
clone este repositório e copie o código do analisador ou baixe o código em seu pc
Se for usar o git bash
utilize esse codigo a seguir subistituindo /seu-usuario/ por seu nome de usuario:git clone https://github.com/seu-usuario/analisador-lexico.git

2.Acesse o diretório do projeto:
Se for usar o git bash utilize esse codigo a seguir:cd analisador-lexico

3.Execute o script:
Se for usar o git bash utilize esse codigo a seguir: python analisador_lexico.py

Na interface gráfica que será exibida ao rodar o codigo no vscode ou outra IDE:
Digite ou cole o código que deseja analisar no campo de entrada.
Clique no botão "Analisar Código".
Os tokens identificados serão exibidos na área de saída, juntamente com o número total de tokens.

📖 Estrutura do Código
O analisador utiliza expressões regulares para identificar os seguintes tipos de tokens:
Palavra-chave	Palavras reservadas da linguagem Python	if, while, return
Identificador	Nomes de variáveis e funções	minha_var, soma
Número	Valores numéricos	123, 45
String Literal	Texto entre aspas	"texto", 'exemplo'
Delimitador	Símbolos de separação	{, [, ,, :
Operador	Operadores matemáticos e lógicos	+, -, ==, **
Espaços	Espaços e tabulações	, \t
Desconhecido	Qualquer token que não se encaixe nos padrões acima	@, #

🖼️ Demonstração
Aqui está uma prévia da interface gráfica do analisador:

div align="center"
img src="https://github.com/user-attachments/assets/227ef05c-86e3-4bad-8716-3f984f882b8d" /
/div

📌 Observações
Este projeto é uma implementação básica de um analisador léxico e pode ser expandido para suportar mais casos de uso ou linguagens específicas.
O foco está na identificação de tokens em Python, mas a lógica pode ser adaptada para outras linguagens.

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
