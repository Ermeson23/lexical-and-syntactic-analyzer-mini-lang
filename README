# Desenvolvimento de um Analisador Léxico e Sintático

## Introdução
Este documento apresenta o desenvolvimento de um analisador léxico e sintático para a linguagem fictícia MiniLang, inspirada em C. O projeto foi implementado em Python.

## Objetivo
O objetivo deste trabalho é criar um programa que possa processar código-fonte, identificar tokens e validar a estrutura sintática das instruções.

# Documentação do Analisador Léxico e Sintático

## O que foi feito no trabalho

Neste trabalho, foi desenvolvido um analisador léxico e sintático para uma simples linguagem. O projeto foi modularizado em quatro componentes principais:

- **Lexer**: Analisa o código-fonte e converte o texto em uma lista de tokens.
- **Parser**: Realiza a análise sintática e verifica se os tokens seguem as regras da gramática da linguagem.
- **Tokens**: Define os tipos de tokens reconhecidos pelo lexer, como palavras reservadas, números, identificadores, operadores, colchetes chaves e ponto e vírgula.
- **Main**: Representa o ponto de entrada do programa. Ele é responsável por ler o código-fonte, processá-lo e analisá-lo.

Esta estrutura modular foi escolhida pois ela permite uma melhor organização do código, o que facilita em futuras expansões e manutenções.

## Como o programa funciona

O funcionamento do programa segue os seguintes passos:

1. O **Lexer** recebe o código-fonte como entrada e divide o texto em tokens.
2. O **Parser** recebe a lista de tokens e verifica se estão organizados corretamente de acordo com as regras sintáticas da linguagem.
3. Se o código estiver correto, o programa finaliza sem erros. Caso contrário, uma mensagem de erro sintático é exibida.

## Exemplos de entrada e saída

### Entrada:
```c
int x = 10 + 3 * 5;
float y = 5;
if (x > 5) {
    print(x);
} else {
    print(x);
}
```

### Saída:
```
Análise sintática concluída com sucesso!
```

Se houver erro sintático:

### Entrada:
```c
int x = 10 + ;
```

### Saída:
```
Erro de sintaxe! Problema em ('SEMICOLON', ';')
```

## Dificuldades enfrentadas

Durante o desenvolvimento do projeto, algumas das dificuldades encontradas foram:

- Definir uma gramática que cobrisse as construções da linguagem sem gerar ambiguidades.
- Implementar corretamente a precedência de dos tipos de tokens.
- Implementar corretamente a precedência dos operadores matemáticos.
- Lidar com blocos aninhados, como estruturas `if-else` e loops `while`.

## Próximas etapas do compilador

Uma vez que o analisador léxico e sintático estão funcionando, as próximas etapas incluem:

- Implementar um analisador semântico para verificar erros como uso de variáveis não declaradas.
- Criar uma geração de código intermediário para facilitar a execução.
- Melhorar a detecção e a descrição de erros para facilitar a depuração.
- Otimizar a eficiência do lexer e parser.