# Open Source e Inteligência Artificial: O Casamento que Pode Salvar Vidas em Hospitais

![image](https://github.com/CllsPy/Generative_AI/assets/96326019/2868c040-9606-4d52-ba9b-69dd07983b48)

Na medicina, a formação e as ferramentas disponíveis ao profissional servem a um objetivo em comum: tomar a decisão correta. Qual tratamento utilizar, qual medicação recomendar – essas são decisões que precisam ser rápidas e eficientes, pois vidas dependem delas. Como seria possível construir uma estrutura que pudesse auxiliar os médicos em tarefas repetitivas e extenuantes, como a tomada de decisões baseadas em documentos extensos, como o RSE (Relatório de Saúde Eletrônico)?



O objetivo deste artigo é mostrar a implementação de um LLM na utilização da técnica de sumarização. O modelo escolhido será o Llma 2b, em um processo que vai desde o "business problem" até o deployment do modelo com a ferramenta de prototipagem Gradio.



Llma 2b: é uma geração de modelos open source desenvolvidos pela Meta, que, como o nome sugere, possui uma rede neural de 2 bilhões de parâmetros.
Gradio: é um pacote open source criado com base em Python usado para prototipagem de modelos de machine learning e APIs.
LLMs: é a sigla para Large Language Models. São modelos treinados com uma grande quantidade de dados obtidos de toda a internet. No geral, eles podem executar tarefas como classificação de sentimentos, reconhecimento de diálogo tóxico e, o nosso foco neste artigo, sumarização.
Sumarização: é a habilidade que um LLM tem de "resumir" uma certa quantidade de informações, que podem vir de documentos, texto ou áudio.


Keys: Llma-2b, GenerativeAI, ML, Medicina, Decision Making AI, Open Source



1. Etapas
Primeiro vamos definir quais os passos para a implementação da solução proposta.



1. Definir o problema

2. Escolher dados para o problema

3. Escolher modelo

4. Instalar e importar recursos necessários

5. Solicitar acesso ao modelo via Hugging Face Token

6. Definir características do modelo

7. Definir o padrão de resposta e direcionamento

8. Definir qual texto será sumarizado

9. Solicitar sumarização

10. Observar respostas

11. Construir Interface

12. Avaliar resultados



1.1 Requisitos
Todo o código escrito durante este processo foi feito com base na linguagem dinâmica Python.



A IDE escolhida fica a critério de preferência, mas recomendo o uso de ambientes virtuais onde é possível utilizar acesso a GPU, o que torna o treinamento mais veloz.



1.2 Pacotes
Para que seja possível seguir, é necessário que as seguintes ferramentas estejam presentes:



- torch

- transformers

- langchain 

- gradio



2. Definir problema
No contexto apresentado, a aplicação de IA para sumarização de RSE (Registro de Saúde Eletrônico) parece ser justificada e relevante. Aqui estão alguns pontos que sustentam essa afirmação:



1. Complexidade dos Dados: Os registros de saúde eletrônicos podem conter uma grande quantidade de informações, incluindo histórico médico, resultados de exames, prescrições e notas de saúde. A análise manual desses dados pode ser demorada e propensa a erros, enquanto a IA pode ajudar a extrair e resumir as informações mais relevantes de forma eficiente.



2. Necessidade de Tomada de Decisão Rápida: Os profissionais de saúde muitas vezes precisam tomar decisões rápidas e precisas durante as consultas. Ter um resumo conciso e relevante do histórico médico do paciente pode ajudar os profissionais a entender rapidamente a situação do paciente e tomar decisões informadas.



3. Otimização do Tempo: Com a ajuda da IA para sumarização de RSE, os profissionais de saúde podem economizar tempo valioso entre as consultas, pois não precisam passar por todo o registro do paciente para obter as informações necessárias.



Portanto, considerando a complexidade dos dados de RSE , a necessidade de tomada de decisão rápida e a otimização do tempo dos profissionais de saúde, a aplicação de IA para sumarização de RSE parece ser justificada e benéfica.



2.1 Código
Os passos que se seguem envolvem código e, por este motivo, não vou detalhar no notebook. Apresentarei um diagrama de como o processo será feito e vou disponibilizar acesso ao código no meu Github para quem quiser conferir.

