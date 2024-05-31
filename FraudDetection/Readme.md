## Detecção de Fraude na Empresa Enron Corporation.
Projeto de Ciência de Dados realizado por Fábio Cerqueira

## Contexto
O projeto visa explorar o conjunto de dados de e-mails (de comunicações internas) da Enron Corporation, mundialmente conhecida por um grande esquema de fraude corporativa que levou à falência da empresa. A exploração consistirá em encontrar padrões e classificar e-mails na tentativa de detectar e-mails fraudulentos.

## Conjunto de Dados
O conjunto de dados pertence ao Enron Corpus, um banco de dados massivo com mais de 600.000 e-mails pertencentes aos funcionários da Enron Corp.

## Metodologia Utilizada
CRISP-DM (Cross-Industry Standard Process for Data Mining)

<h3>1. Compreensão do Negócio (Business Understanding)</h3>

<h4>Objetivo:</h4>

- Entender o contexto e os objetivos do projeto.
- Definir o problema: explorar a comunicação interna da Enron em busca de fraudes.

<h3>2. Compreensão dos Dados (Data Understanding)</h3>

<h4>Atividades:</h4>

- Coletar os datasets disponíveis.
- Explorar e verificar a qualidade dos dados.
- Entender as principais características e variáveis dos datasets.

<h4>Ações:</h4>

- Carregamento dos datasets fornecidos.
- Análise exploratória inicial para verificar a estrutura e o conteúdo dos dados.

<h3>3. Preparação dos Dados (Data Preparation)</h3>

<h4>Atividades:</h4>

- Limpeza e transformação dos dados.
- Integração de múltiplas fontes de dados.
- Seleção das variáveis relevantes para análise.

<h4>Ações:</h4>

- Remoção de valores ausentes e limpeza dos textos.
- Normalização dos dados textuais.
- Preparação dos dados para análise de texto e modelagem.

<h3>4. Modelagem (Modeling)</h3>

<h4>Atividades:</h4>

- Seleção e aplicação de técnicas de modelagem apropriadas.
- Treinamento e validação dos modelos.

<h4>Ações:</h4>

- Utilização de modelos de detecção de anomalias (Isolation Forest) para identificar fraudes.
- Feature engineering para criar variáveis relevantes para a modelagem.

<h3>5. Avaliação (Evaluation)</h3>

<h4>Atividades:</h4>

- Avaliação dos resultados dos modelos.
- Verificação da performance e validação das suposições.

<h4>Ações:</h4>

- Análise dos scores e anomalias detectadas pelo modelo.
- Interpretação dos resultados para verificar a eficácia do modelo.

<h3>6. Implementação (Deployment)</h3>

<h4>Atividades:</h4>

- Implementação prática dos modelos e das análises.
- Comunicação dos resultados aos stakeholders.

<h4>Ações:</h4>

- Geração de visualizações e relatórios claros e informativos.
- Salvamento dos modelos para futuras análises.
