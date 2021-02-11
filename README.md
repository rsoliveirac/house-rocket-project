# projeto-insights-houses
<img src = "https://cdn.pixabay.com/photo/2015/03/26/10/04/new-york-690868_960_720.jpg" height = "350" width="800">


Este é um projeto fictício. A empresa, o contexto e as perguntas de negócios não são reais. Este portfólio está seguindo as recomendações do blog [Seja um Data Scientist](https://sejaumdatascientist.com/os-5-projetos-de-data-science-que-fara-o-recrutador-olhar-para-voce/) 

# Descrição 
*House Rocket* trabalha com a compra e venda de imóveis. O Cientista de dados da empresa deverá ajudar a encontrar as melhores oportunidades de negócio, ou seja, maximizar a receita. A melhor estratégia é a compra de casas em ótimas condições por baixos preços e a venda desses imóveis por um preço superior. Os atributos das casas as tornam mais ou menos atrativas, influenciando a atratividade dos imóveis e, consequentemente, o seu preço. O cientista de dados da empresa deverá responder:

**1**. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?

**2.** Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?

**3.** A House Rocket deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças? Qual o incremento no preço dado por cada opção de reforma? 


# Atributos 

Os dados para este projeto podem ser encontrados em: https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885 . Abaixo segue a definição para cada um dos 21 atibutos:

* id - Numeração única que identifica cada um dos imóveis 

* date - Data da venda da casa

* price - Preço de venda

* bedrooms - Número de quartos

* bathrooms - Número de banheiros (0.5 = banheiro em um quarto, mas sem chuveiro)

* sqft_living - Medida (em pés quadrado) do espaço interior dos apartamentos

* sqft_lot - Medida (em pés quadrado)quadrada do espaço terrestre

* floors - Número de andares

* waterfront - Variavél ficticia para saber se há visão para água ou não (0 = não e 1 = sim).

* view - Um índice de 0 a 4 que indica a qualidade da vista da propriedade (0 = baixa |-| 4 = alta)

* condition - Um indice de 1 a 5 que indica a condição da casa (1 = baixo |-| 5 = alta)

* grade - Um índice de 1 a 1 que indica a construção e o design do edifício, (1-3 =  baixo, 7 = médio e 11-13 = alta)

* sqft_above - A metragem quadrada do espaço habitacional interior acima do nível do solo

* sqft_basement - A metragem quadrada do espaço interno da habitação que está abaixo do nível do solo 45

* yr_built - Ano de construção de cada casa

* yr_renovated - Ano da última reforma da casa

* zipcode - CEP da casa

* lat -  Latitude

* long - Longitude

* sqft_living15 - Medida (em pés quadrado) do espaço interno de habitação para os 15 vizinhos mais próximos

* sqft_lot15 - Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximos
