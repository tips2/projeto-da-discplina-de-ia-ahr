# ia-ecom-031
# Projeto final da disciplina de Inteligência Artificial 2020.1

A proposta desse projeto foi a construção de um sistema especialista dotado da capacidade de diagnosticar o desempenho de um aluno ao cursar disciplinas de Português ou Matemática em duas escolas do ensino médio português. O trabalho apresentado foi inspirado na leitura deste artigo [\[1\]][1], onde são apresentados com detalhes a estrutura do problema, bem como os dados utilizados na construção do modelo. O projeto é dividido em dois módulos fundamentais: o da __construção da base de conhecimento__ e o do __motor de inferência__, como está explicado nas seções abaixo. Uma terceira componente, mais simples, está presente na interação com o usuário através do próprio terminal.

# Instruções de execução da aplicação

É necessário baixar e instalar o `Python` e `git` para rodar a aplicação. Para mais informações de como instalar no seu sistema acesse:

> https://www.python.org/downloads/

> https://git-scm.com/downloads

Em seguida basta executar no terminal:

```console

$ pip install -r requirements.txt
$ git clone https://github.com/hugotallys/backward.git
$ pip install -r backward/requirements.txt
$ python main.py

```

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

Para construir o motor de inferência utilizamos uma implementação já presente na linguagem de programação Python. No link abaxio é possível ter acesso ao repositório bifurcado:

> https://github.com/hugotallys/backward

O módulo implementa a técnica de inferência do encadeamento para trás. Adicionamos a funcionalidade de que, sempre que o valor de uma variável é desconhecido, na execução do próprio algoritmo é solicitado que o usuário informe o valor da variável em questão. Por se tratar de um motor de inferência **bivalorado** (um fato sempre é verdadeiro ou falso) as perguntas sempre são feitas esepreando-se uma resposta do tipo _sim ou não_.

# Referências

1. [Cortez, P., & Silva, A.M. (2008). Using data mining to predict secondary school student performance.][1].

[1]:https://www.semanticscholar.org/paper/Using-data-mining-to-predict-secondary-school-Cortez-Silva/61d468d5254730bbecf822c6b60d7d6595d9889c
