# ia-ecom-031
Projeto final da disciplina de Inteligência Artificial 2020.1

A proposta desse projeto será a construção de um sistema especialista dotado da capacidade de diagnosticar o desempenho de um aluno ao cursar disciplinas de Português ou Matemática em duas escolas do ensino médio português.

# Construção da base de conhecimento

# Construção do motor de inferência

A construção do motor de inferência se dará com o uso da biblioteca `Pyke`, disponível na linguagem de programação Python.

> http://pyke.sourceforge.net/index.html

Dada a base de conhecimento consolidada na etapa anterior e um conjunto de fatos dados como entrada do programa, o objetivo do módulo de inferência será:

* Através do _encadeamento para frente_:
    * Concluir novos _fatos_;
    * Ativar outras regras de bases de conhecimento mais específicas;
* Através do _encademeamento para trás_:
    * Provar um fato específico (_goal_), isto é responder uma _pergunta_;


# Integração com o RASA
