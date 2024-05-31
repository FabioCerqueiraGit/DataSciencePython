## Detecção de Fraude na Empresa Enron Corporation
Projeto de Ciência de Dados realizado por Fábio Cerqueira

## Contexto
O projeto visa explorar o conjunto de dados de e-mails (de comunicações internas) da Enron Corporation, mundialmente conhecida por um grande esquema de fraude corporativa que levou à falência da empresa. A exploração consistirá em encontrar padrões e classificar e-mails na tentativa de detectar e-mails fraudulentos.

## Conjunto de Dados
O conjunto de dados pertence ao Enron Corpus, um banco de dados massivo com mais de 600.000 e-mails pertencentes aos funcionários da Enron Corp.

## Metodologia Utilizada
CRISP-DM (Cross-Industry Standard Process for Data Mining)

1. Compreensão do Negócio (Business Understanding)
Objetivo:

- Entender o contexto e os objetivos do projeto.
- Definir o problema: explorar a comunicação interna da Enron em busca de fraudes.

2. Compreensão dos Dados (Data Understanding)

Atividades:

- Coletar os datasets disponíveis.
- Explorar e verificar a qualidade dos dados.
- Entender as principais características e variáveis dos datasets.

Ações:

- Carregamento dos datasets fornecidos.
- Análise exploratória inicial para verificar a estrutura e o conteúdo dos dados.

3. Preparação dos Dados (Data Preparation)

Atividades:

- Limpeza e transformação dos dados.
- Integração de múltiplas fontes de dados.
- Seleção das variáveis relevantes para análise.

Ações:

- Remoção de valores ausentes e limpeza dos textos.
- Normalização dos dados textuais.
- Preparação dos dados para análise de texto e modelagem.

4. Modelagem (Modeling)

Atividades:

- Seleção e aplicação de técnicas de modelagem apropriadas.
- Treinamento e validação dos modelos.

Ações:

- Utilização de modelos de detecção de anomalias (Isolation Forest) para identificar fraudes.
- Feature engineering para criar variáveis relevantes para a modelagem.

5. Avaliação (Evaluation)

Atividades:

- Avaliação dos resultados dos modelos.
- Verificação da performance e validação das suposições.

Ações:

- Análise dos scores e anomalias detectadas pelo modelo.
- Interpretação dos resultados para verificar a eficácia do modelo.

6. Implementação (Deployment)

Atividades:

- Implementação prática dos modelos e das análises.
- Comunicação dos resultados aos stakeholders.

Ações:

- Geração de visualizações e relatórios claros e informativos.
- Salvamento dos modelos para futuras análises.