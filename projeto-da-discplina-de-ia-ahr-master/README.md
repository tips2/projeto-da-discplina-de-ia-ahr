# ia-ecom-031
Projeto final da disciplina de Inteligência Artificial 2020.1

A proposta desse projeto será a construção de um sistema especialista dotado da capacidade de diagnosticar o desempenho de um aluno ao cursar disciplinas de Português ou Matemática em duas escolas do ensino médio português.

# Construção da base de conhecimento
Primeiramente, foi realizada uma análise inicial do DataSet para construção de uma base de conhecimento, onde por meio desses dados, serão extraidas regras necessárias para o desenvolvimento do agente conversacional. A ideia é utilizar essas regras para construir estruturas do tipo "se->então".

A análise inicial pode ser consultada no arquivo data-exploration.ipynb.
Como resultado preliminar, pode-se concluir que os atributos que causam maior impacto nas notas dos alunos são:
- sex
- age
- Medu (nível de educação da mãe)
- Fedu (nível de educação do pai)
- studytime
- failures (número de reprovações anteriores)
- schoolsup (suporte escolar)
- famsup (suporte familiar)
- internet
- freetime
- goout
- Walc (consumo de álcool no fim de semana)
- health

# Construção do motor de inferência

A construção do motor de inferência se dará com o uso do pacote `backward` que implementa a técnica de inferência do encadeamento para trás. No _fork_ do repositório foi implementado algumas funcionalidades adicionais.

> https://github.com/hugotallys/backward

# Instruções de execução da aplicação

```console

$ pip install -r requirements.txt
$ git clone https://github.com/hugotallys/backward.git
$ pip install -r backward/requirements.txt
$ python main.py

```
