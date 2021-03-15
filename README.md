# House Rocket Project 
<img src = "https://cdn.pixabay.com/photo/2015/03/26/10/04/new-york-690868_960_720.jpg" height = "350" width="800">


Este é um projeto fictício. A empresa, o contexto e as perguntas de negócios não são reais. Este portfólio está seguindo as recomendações do blog [Seja um Data Scientist](https://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/) 

# Descrição 
*House Rocket* é uma empresa que trabalha com a compra e venda de imóveis. O Cientista de dados da empresa deverá ajudar a encontrar as melhores oportunidades de negócio, ou seja, maximizar a receita. A melhor estratégia é a compra de casas em ótimas condições por baixos preços e a venda desses imóveis por um preço superior. Os atributos das casas as tornam mais ou menos atrativas, influenciando a atratividade dos imóveis e, consequentemente, o seu preço. As questões a serem respondidas são:

**1**. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?

**2.** Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?

**3.** A House Rocket deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças? Qual o incremento no preço dado por cada opção de reforma? 


# Atributos 

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



# 2. Premissas do Negócio

- As seguintes premissas foram consideradas para esse projeto:
- Os valores iguais a zero em **yr_renovated** são casas que nunca foram reformadas.
- O valor igual a 33 na coluna **bathroom** foi considerada um erro e por isso foi delatada das análises
- A coluna **price** significa o preço que a casa foi / será comprada pela empresa House Rocket
- Valores duplicados em ID foram removidos e considerados somente a compra mais recente



# 3. Estratégia de solução



# 4. Top Insights

Imóveis renovados recentemente são 35% mais caros

Falso: Imóveis antigos e atuais possuem uma faixa de preço equivalente.

Imóveis em más condições, mas com uma boa vista são 10% mais caros.

Falso: Imóveis em más condições e com vista ruim são mais caros.

Crescimento do preço mês após mês em 2014 é de 10%

Falso: O preço dos imóveis são mais caros entre o mês 3 e 6.



# 5. Tradução para o negócio

O as análises das hipóteses dizem sobre o negócio

| Hipótese | Resultado | Tradução para negócio |
| -------- | --------- | --------------------- |
| H1 -     |           |                       |
|          |           |                       |
|          |           |                       |
|          |           |                       |
|          |           |                       |
|          |           |                       |
|          |           |                       |
|          |           |                       |
|          |           |                       |

