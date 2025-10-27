# Programação Orientada a Objetos

Este repositório contém scripts que resolvem exercícios práticos de programação, cada um abordando um conceito ou problema específico relacionado à Programação Orientada a Objetos (POO) em Python.

## Descrição das questões

**Questão 1 – Tipo de triângulo**  
O script recebe as coordenadas de três pontos e determina se os pontos formam um triângulo e, caso positivo, classifica-o como Equilátero, Isósceles ou Escaleno.

**Questão 2 – Quadriláteros**  
O script solicita as coordenadas de quatro pontos e identifica o tipo de quadrilátero formado (Quadrado, Retângulo, Losango, Paralelogramo, Trapézio ou Quadrilátero qualquer).

**Questão 3 – Menu interativo**  
Apresenta um menu que permite ao usuário escolher entre identificar um triângulo ou um quadrilátero, executando a lógica correspondente a cada opção.

**estoque_cantina.py (15/10/2025)**  
Sistema modular para controle de estoque de uma cantina escolar. Permite registrar, atualizar e consultar produtos (comidas e bebidas), realizar reposição automática e gerar relatórios em arquivo de texto.

**sistema_bancario.py (27/10/2025)**  
Sistema orientado a objetos que simula um ambiente bancário simples.  
Inclui diferentes tipos de contas (Digital, Corrente e Poupança), além de um gerenciamento centralizado pelo banco.  
Permite **cadastrar contas, realizar transferências, aplicar rendimentos, cobrar taxas e listar contas**.

---

## Diagrama de Classes – Sistema Bancário

O diagrama abaixo representa a estrutura do sistema bancário, destacando as relações entre as classes `Banco`, `Conta`, `Corrente`, `Poupanca` e `Digital`.

```mermaid
classDiagram
    class Registro {
        -str agencia
        -str conta
        +getAgencia()
        +getConta()
    }

    class Conta {
        -str nome
        -Registro registro
        -float saldo
        +getSaldo() float
        +creditar(valor: float)
        +debitar(valor: float)
    }

    class Digital {
        +__init__(nome, registro, saldo)
    }

    class Corrente {
        -float limite
        -float taxa_manutencao
        +limiteDisponivel() float
        +cobrarTaxa()
    }

    class Poupanca {
        -float taxa_rendimento
        +calcularRendimento() float
        +aplicarRendimento()
    }

    class Banco {
        -list contas
        +cadastrar(conta: Conta)
        +procurarConta(registro: Registro)
        +transferir(origem: Conta, destino: Conta, valor: float)
        +listarContas() list
    }

    Conta <|-- Digital
    Conta <|-- Corrente
    Conta <|-- Poupanca
    Banco --> Conta : "gerencia"
    Conta --> Registro : "possui"
