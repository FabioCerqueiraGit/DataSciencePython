# Dashboard de Lead Scoring com Machine Learning no Power BI

## Introdução
Projeto de Criação de um dashboard de lead scoring com o Power BI. Usaremos um conjunto de dados com 1000 leads e construiremos um modelo de machine learning com o PyCaret para prever a probabilidade de um lead se converter em cliente. Em seguida, usaremos o modelo para pontuar os leads, armazenar o novo conjunto de dados de leads em um banco de dados PostgreSQL e visualizar os resultados no Power BI.

## O que é Lead Scoring?
Lead scoring é um processo de atribuição de uma pontuação a um lead com base em seu comportamento e perfil. A pontuação é usada para determinar a probabilidade de um lead se converter em cliente. Lead scoring é uma prática comum na indústria de marketing e é usada para priorizar leads para as equipes de vendas.

Normalmente, o lead scoring é feito manualmente pelas equipes de vendas. No entanto, é um processo demorado e pode estar sujeito a erros. Machine learning pode ser usado para automatizar o processo e torná-lo mais eficiente.

## Tecnologias Utilizadas

- Jupyter Notebook para construir o modelo de machine learning com o PyCaret.

- Power BI para visualizar os resultados e criar o dashboard com os dados do banco de dados PostgreSQL.

- PostgreSQL para armazenar o novo conjunto de dados de leads com as pontuações e probabilidades previstas pelo modelo de machine learning.

- PyCaret para construir o modelo de machine learning, prever as pontuações dos leads e as probabilidades.

### Passo 1: Preparação e Limpeza dos Dados
O primeiro passo é importar as bibliotecas necessárias e carregar o conjunto de dados em um dataframe do pandas. Em seguida, verificaremos a forma (shape) do conjunto de dados e as primeiras 5 linhas para obter uma melhor compreensão dos dados. Também verificaremos os tipos de dados das colunas e o número de valores ausentes em cada coluna.

Aplicaremos uma limpeza básica para remover as colunas que não são relevantes para a análise e remover as linhas com valores ausentes. Também verificaremos a presença de duplicatas e as removeremos, se necessário. Por fim, aplicaremos uma Análise Exploratória de Dados (EDA) básica para obter uma melhor compreensão dos dados.

### Passo 2: Construção do Modelo usando PyCaret
Agora que limpamos o conjunto de dados, podemos passar para o próximo passo: construir o modelo usando PyCaret. O trecho de código abaixo mostra como carregar o conjunto de dados limpo em um dataframe do pandas e, em seguida, como construir o modelo usando PyCaret.

### Passo 3: Criar uma Nova Coluna com a Pontuação de Lead Quente ou Lead Frio com Base no Tempo Gasto no Site
O trecho de código abaixo mostra como criar uma nova coluna com a pontuação de Lead Quente ou Lead Frio com base no tempo gasto no site. Usaremos a função numpy.where. A função numpy.where retornará um dataframe do pandas com uma coluna chamada Lead_Score.

### Passo 4: Armazenar os Dados em um Banco de Dados PostgreSQL
Agora, vamos armazenar os dados em um banco de dados SQL. Se você quiser saber mais sobre como instalar e configurar o PostgreSQL, pode conferir o seguinte artigo. O código completo está disponível no meu repositório GitHub.

Primeiro, vamos carregar o arquivo Excel em um dataframe do pandas. Em seguida, criaremos uma conexão com o banco de dados. Depois, criaremos um cursor e executaremos a consulta SQL para criar a tabela.

### Passo 5: Conectar o PostgreSQL com a Tabela e Criar o Dashboard no Power BI
Agora vamos conectar o PostgreSQL com a tabela e criar o dashboard no Power BI. Se você quiser saber mais sobre como instalar e configurar o Power BI, pode conferir o seguinte artigo. O arquivo do Power BI está disponível no meu repositório GitHub.

Para conectar a tabela do PostgreSQL ao Power BI, seguiremos os passos abaixo:

1) Crie uma nova fonte de dados.
2) Selecione o banco de dados PostgreSQL.
3) Selecione a tabela que queremos conectar.
4) Selecione as colunas que queremos conectar.
5) Selecione o tipo de dados das colunas.
6) Selecione o modo de conexão.
7) Selecione o modo de autenticação.
8) Selecione o nome do servidor.
9) Selecione o nome do banco de dados, nome de usuário, senha e o número da porta.

Após seguir os passos acima, os novos dados de leads serão conectados ao dashboard do Power BI e aparecerão conforme mostrado na seção de tabelas.

### Direitos Autorais
Esse estudo e experimento é baseado na publicação realizada em fevereiro de 2023 no Geek Culture por Marcello Dichiera.