🏥 Projeto: Sistema de Fila de Espera com Prioridade
Este projeto simula um sistema de fila de espera para atendimento, utilizando listas encadeadas simples em Python. O sistema prioriza pacientes com cartões amarelos (A) sobre os pacientes com cartões verdes (V).

📋 Funcionalidades
Inserção de pacientes na fila com ou sem prioridade;

Exibição da fila atual;

Atendimento por ordem de prioridade;

Interface de menu interativo no terminal.

🎯 Lógica de Prioridade
Pacientes com cartão amarelo (A) têm prioridade na fila.

Pacientes com cartão verde (V) são inseridos no final da fila.

A chamada para atendimento sempre começa pelo primeiro da fila.

🧠 Estrutura de Dados
Utiliza uma lista encadeada simples com nós (Nodo) que armazenam:

Número do cartão (gerado automaticamente);

Cor do cartão (A ou V);

Referência para o próximo paciente.

🚀 Como Executar
Certifique-se de ter o Python 3 instalado.

Clone ou baixe este repositório.

No terminal, execute o arquivo:

bash
Copiar
Editar
python main.py
Utilize o menu interativo para:

Adicionar pacientes;

Visualizar a fila;

Chamar pacientes;

Encerrar o programa.

📌 Exemplo de Uso
less
Copiar
Editar
1 – Adicionar paciente à fila
2 – Mostrar pacientes na fila
3 – Chamar paciente
4 – Sair
Escolha uma opção: 1
Digite a cor do cartão (A para amarelo, V para verde): A

1 – Adicionar paciente à fila
2 – Mostrar pacientes na fila
3 – Chamar paciente
4 – Sair
Escolha uma opção: 2
Fila de Espera:
Cartão A-201

🛠️ Tecnologias Utilizadas
Linguagem: Python 3
Conceitos: Programação Orientada a Objetos (POO), Estrutura de Dados (Listas Encadeadas)

👩‍💻 Autor(a)
Projeto desenvolvido por Lorena Muller
