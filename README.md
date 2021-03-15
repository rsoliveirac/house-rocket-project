# House Rocket Project 

<img src="https://user-images.githubusercontent.com/71949871/111184181-78e4a500-858f-11eb-9ed8-9888964ed06d.png" alt="logo" style="zoom:100%;" />

Este é um projeto fictício. A empresa, o contexto e as perguntas de negócios não são reais. Este portfólio está seguindo as recomendações do blog [Seja um Data Scientist](https://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/) 

​																																								*A logo criada é ficticia.* 

# 1. Descrição 

*House Rocket* é uma empresa que trabalha com a compra e venda de imóveis. O Cientista de dados da empresa deverá ajudar a encontrar as melhores oportunidades de negócio, ou seja, maximizar a receita. A melhor estratégia é a compra de casas em ótimas condições por baixos preços e a venda desses imóveis por um preço superior. Os atributos das casas as tornam mais ou menos atrativas, influenciando a atratividade dos imóveis e, consequentemente, o seu preço. As questões a serem respondidas são:

**1**. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?

**2.** Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?

 


# 2. Atributos 

Os dados para este projeto podem ser encontrados em: https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885 . Abaixo segue a definição para cada um dos 21 atributos:


|    Atributos    |                         Significado                          |
| :-------------: | :----------------------------------------------------------: |
|       id        |       Numeração única de identificação de cada imóvel        |
|      date       |                    Data da venda da casa                     |
|      price      |    Preço que a casa está sendo vendida pelo proprietário     |
|    bedrooms     |                      Número de quartos                       |
|    bathrooms    | Número de banheiros (0.5 = banheiro em um quarto, mas sem chuveiro) |
|   sqft_living   | Medida (em pés quadrado) do espaço interior dos apartamentos |
|    sqft_lot     |     Medida (em pés quadrado)quadrada do espaço terrestre     |
|     floors      |                 Número de andares do imóvel                  |
|   waterfront    | Variável que indica a presença ou não de vista para água (0 = não e 1 = sim) |
|      view       | Um índice de 0 a 4 que indica a qualidade da vista da propriedade. Varia de 0 a 4, onde: 0 = baixa  4 = alta |
|    condition    | Um índice de 1 a 5 que indica a condição da casa. Varia de 1 a 5, onde: 1 = baixo \|-\| 5 = alta |
|      grade      | Um índice de 1 a 13 que indica a construção e o design do edifício. Varia de 1 a 13, onde: 1-3 = baixo, 7 = médio e 11-13 = alta |
|  sqft_basement  | A metragem quadrada do espaço habitacional interior acima do nível do solo |
|    yr_built     |               Ano de construção de cada imóvel               |
|  yr_renovated   |                Ano de reforma de cada imóvel                 |
|     zipcode     |                         CEP da casa                          |
|       lat       |                           Latitude                           |
|      long       |                          Longitude                           |
| sqft_livining15 | Medida (em pés quadrado) do espaço interno de habitação para os 15 vizinhos mais próximo |
|   sqft_lot15    | Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo |



# 3. Premissas do Negócio

Quais premissas foram adotadas para este projeto:

- As seguintes premissas foram consideradas para esse projeto:
- Os valores iguais a zero em **yr_renovated** são casas que nunca foram reformadas.
- O valor igual a 33 na coluna **bathroom** foi considerada um erro e por isso foi delatada das análises
- A coluna **price** significa o preço que a casa foi / será comprada pela empresa House Rocket
- Valores duplicados em ID foram removidos e considerados somente a compra mais recente
- A localidade e a condição do imóvel foram características decisivas na compra ou não do imóvel
- A estação do ano foi a característica decisiva para a época da venda do imóvel



# 4. Estratégia de solução

Quais foram as etapas para solucionar o problema de negócio:

1. Coleta de dados via Kaggle
2. Entendimento de negócio
3. Tratamento de dados 

- ​	Tranformação de variaveis 
- ​	Limpeza 
- ​	Entendimento

4. Exploração de dados
[link para app no Heroku](https://house-rocket-project.herokuapp.com/)
5. Responder problemas do negócio

6. Resultados para o negócio

7. Conclusão

# 5. Top Insights

Insights mais relevantes para o projeto:

Imóveis renovados recentemente são 35% mais caros

**Falso**: Imóveis antigos e atuais possuem uma faixa de preço equivalente.

Imóveis em más condições, mas com uma boa vista são 10% mais caros.

**Falso**: Imóveis em más condições e com vista ruim são mais caros.

Crescimento do preço mês após mês em 2014 é de 10%.

**Falso**: O preço dos imóveis são mais caros entre o mês 3 e 6.



# 6. Tradução para o negócio

O as análises das hipóteses dizem sobre o negócio

| Hipótese                                                     | Resultado  | Tradução para negócio                                        |
| ------------------------------------------------------------ | ---------- | ------------------------------------------------------------ |
| **H1** -Imóveis com vista para a água são em média 30% mais caros | Verdadeira | Investir em imóveis com vista para água                      |
| **H2** - Imóveis com data de construção menor que 1955 são em média 50% mais baratos | Falsa      | Investir em imóveis independente da data de construção       |
| **H3** - Imóveis sem porão com maior área total são 40% mais caros | Verdadeira | Investir em imóveis sem porão                                |
| **H4** - Imóveis que nunca foram reformados são em média 20% mais baratos | Verdadeira | Investir em imóveis não reformados e reformá-los para venda  |
| **H5** - Imóveis em más condições, mas com boa vista são 10% mais caros | Falsa      | Não investir em imóveis em más condições                     |
| **H6** - Imóveis antigos e não renovados são 40% mais baratos | Verdadeira | Investir em imóveis antigos e não renovados e reformalos para venda |
| **H7** - Imóveis com mais banheiros são em média 5% mais caros | Falsa      | Investir em imóveis de 3-5 banheiros                         |
| **H8** - Imóveis renovados recentemente são 35% mais caros   | Falsa      | Investir em imóveis independente da reforma                  |
| **H9** - O crescimento do preço dos imóveis mês após mês no ano de 2014 é de 10% | Falsa      | Investir em imóveis nos meses de menor custo                 |
| **H10** - Imóveis com 3 banheiros tem um crescimento mês após mês de 15% | Falsa      | Investir em imóveis nos meses de menor custo                 |

O valor total de lucro (preço de compra - preço de venda) dos imóveis é de: **22.623.548,20**



# 7. Conclusão

O objetivo final desse projeto era responder a duas questões principais:

**1**. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?

**2.** Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?

Os objetivos foram alcançados.  Os imóveis foram agrupados por região (zipcode). Considerando o preço do imóvel e a condição (1 - 5)  foi calculado a mediana do preço. Imóveis abaixo do preço da mediana e com melhores condições foram sugeridos para compra (Total de 151 imóveis). Os imóveis aptos para compra foram agrupados pela localidade e a estação do ano. A mediana foi calculada e imóveis com preço abaixo da mediana teve um acréscimo de 10% em seu valor, enquanto imóveis com preço acima da mediana teve um acréscimo de 30% acima do seu valor.  O melhor momento da venda dos imóveis é na primavera, uma vez que o preço é maior nessa época. 

Como próximo passo, seria interessante a análise de quais apartamentos deveriam sofrer reformas, uma vez que imóveis antigos e não reformados são mais baratos, enquanto imóveis renovados recentemente são mais caros.  Também é de interesse prever a valorização do imóvel, pois pode permitir reter a venda da habitação até esta estar mais valorizada no mercado. 



