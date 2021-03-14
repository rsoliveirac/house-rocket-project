import streamlit as st
import pandas as pd
import folium
import numpy as np
from streamlit_folium import folium_static
import plotly.express as px


st.set_page_config( layout = 'wide')

@st.cache( allow_output_mutation=True )
def get_data(path):
    df = pd.read_csv(path)

    return df

path = 'projeto-insight/kc_house_data.csv'
df = get_data(path)

#=========================================
# ========== Remover duplicatas ==========
#==========================================
def remove_duplicates (df):
    df = df.drop_duplicates(subset = ['id'], keep = 'last')
    return df

#=========================================
# ========== Remover valor erroneo ==========
#==========================================
def remove_value (df):
    df = df.drop(15870)
    return df

def data_overview(df):
    if st.checkbox('Mostre o dataset'):
     st.write(df.head(50))

data_overview(df)

st.sidebar.title('Projeto House Hocket')
st.sidebar.write('House Rocket é uma empresa que trabalha com a compra e venda de imóveis. '
                     'O Cientista de dados da empresa deverá ajudar a encontrar as melhores '
                     'oportunidades de negócio.')
st.sidebar.write("Para mais informações sobre o projeto, acesse: "
         "[GitHub](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
#=========================================
# ========== Métricas ==========
#==========================================
#Incluindo somente variáveis numéricas
st.markdown("<h1 style='text-align: center; color: black;'> Análise Descritiva</h1>", unsafe_allow_html=True)
atri_num = df.select_dtypes(include = ['int64', 'float64'])
#deletando a coluna 'ID'
atri_num = atri_num.iloc[:, 1: ]
#medidas de tendencia central
df_mean =  pd.DataFrame(atri_num.apply(np.mean)).T
df_median = pd.DataFrame(atri_num.apply(np.median)).T

#medidas de dispersão
df_std = pd.DataFrame(atri_num.apply(np.std)).T
df_min = pd.DataFrame(atri_num.apply(np.min)).T
df_max = pd.DataFrame(atri_num.apply(np.max)).T

#concatenando
est = pd.concat( [df_mean, df_median,  df_std, df_min, df_max ] ).T.reset_index()



#alterando o nome das colunas
est.columns = [ 'atributos','media', 'mediana', 'std', 'min', 'max']

st.dataframe(est, width = 1000)

#=========================================
# ========== H1 ==========
#==========================================
st.markdown("<h1 style='text-align: center; color: black;'>Testando Hipóteses de Negócio</h1>", unsafe_allow_html=True)

c1,c2 = st.beta_columns(2)

c1.subheader('Hipótese 1:  Imóveis com vista para a água são em média 30% mais caros')
h1 = df[['price', 'waterfront']].groupby('waterfront').mean().reset_index()
h1['waterfront'] = h1['waterfront'].astype(str)
fig = px.bar(h1, x='waterfront', y = 'price', color = 'waterfront',  labels={"waterfront": "Visão para água",
                                                                             "price": "Preço"},
                                                                              template= 'simple_white')

fig.update_layout(showlegend = False)
c1.plotly_chart(fig, use_container_width= True)

#=========================================
# ========== H2 ==========
#==========================================
c2.subheader('Hipótese 2: Imóveis com data de construção menor que 1955 são em média 50% mais baratos')
df['construcao'] = df['yr_built'].apply(lambda x: '> 1955' if x > 1955
                                                               else '< 1955')

h2 = df[['construcao', 'price']].groupby('construcao').mean().reset_index()

fig2 = px.bar(h2, x='construcao', y = 'price', color = 'construcao', labels = {"contrucao":"Ano da Construção",
                                                                               'price': 'Preço'},
                                                                                template='simple_white')




fig2.update_layout(showlegend = False)

c2.plotly_chart(fig2, use_container_width= True)

#=========================================
# ========== H3 ==========
#==========================================
c3,c4 = st.beta_columns(2)

c3.subheader('Hipótese 3: Imóveis sem porão com maior área total são 40% mais caros do que imóveis com porão')
df['porao'] = df['sqft_basement'].apply(lambda x: 'nao' if x == 0
                                                  else 'sim')

h3 = df[['porao', 'sqft_lot', 'price']].groupby('porao').sum().reset_index()
fig3 = px.bar(h3, x='porao', y = 'price', color = 'porao', labels = {'price': 'Preço',
                                                                         'sqft_lot': 'Área Total'},
                                                                        template= 'simple_white')
fig3.update_layout(showlegend = False)
c3.plotly_chart(fig3, use_container_width= True)

#=========================================
# ========== H4 ==========
#==========================================
c4.subheader('Hipótese 4: Imóveis que nunca foram reformadas são em média 20% mais baratos')
df['renovacao'] = df['yr_renovated'].apply(lambda x: 'sim' if x > 0 else
                                                     'nao'   )

h6 = df[['price', 'renovacao']].groupby('renovacao').mean().reset_index()
fig4 = px.bar(h6, x='renovacao', y = 'price', color = 'renovacao', labels = {'renovacao':'Renovação',
                                        'price': 'Preço'}, template = 'simple_white')
fig4.update_layout(showlegend = False)
c4.plotly_chart(fig4, use_container_width= True)

#=========================================
# ========== H5 ==========
#==========================================
c5, c6 = st.beta_columns(2)

c5.subheader('Hipótese 5: Imóveis em más condições mas com boa vista são 10% mais caros')
h71 = df[df['condition'] == 1]
h7 = h71[['price', 'view']].groupby('view').sum().reset_index()

fig5 = px.bar(h7, x= 'view', y = 'price', color = 'view',  labels = {'price':'Preço','view': 'Qualidade da Vista'},
                                                    template = 'simple_white')
fig5.update_layout(coloraxis_showscale=False)
c5.plotly_chart(fig5, use_container_width= True)



#=========================================
# ========== H4 ==========
#==========================================

c6.subheader('Hipótse 6: Imóveis antigos e não renovados são 40% mais baratos')
df['renovacao'] =  df['yr_renovated'].apply(lambda  x: 'sim' if x > 0 else
                                                        'nao')

df['contrucao'] = df['yr_built'].apply(lambda x: 'antigo' if (x < 1951) else
                                               'atual')
h8 = df[df['renovacao'] == 1]
h8 = df[['contrucao', 'price']].groupby('contrucao').sum().reset_index()
fig6 = px.bar(h8, x ='contrucao', y = 'price', color = 'contrucao', labels = {'price':'Preço','contrucao': 'Tempo de Imóveis não renovados'} ,
                                                                                template= 'simple_white')

fig6.update_layout(showlegend = False)
c6.plotly_chart(fig6, use_container_width= True)


#=========================================
# ========== H7 ==========
#==========================================
c7, c8 = st.beta_columns(2)

c7.subheader('Hipótese 7: Imóveis com mais banheiros são em média 5% mais caros')
df['banheiro'] =  df['bathrooms'].apply(lambda x: '0-3' if (x > 0 ) & (x < 3) else
                                                   '3-5' if (x > 3) & (x < 5) else
                                                   '5-8')

h9 = df[['banheiro', 'price', 'sqft_lot']].groupby('banheiro').mean().reset_index()

fig7 = px.bar(h9, x = 'banheiro', y = 'price', color = 'banheiro', labels = {'price':'Preço','banheiro':
                                                                            'Quantidade de banheiros'},
                                                                            template= 'simple_white')


fig7.update_layout(showlegend = False)
c7.plotly_chart(fig7, use_container_width= True)


#=========================================
# ========== H8 ==========
#==========================================
c8.subheader('Hipótese 8: Imóveis renovados recentemente são 35% mais caros')
df['contrucao'] = df['yr_built'].apply(lambda x: 'antigo' if (x < 1951) else
                                               'atual')

h10 = df[['contrucao', 'price']].groupby('contrucao').mean().reset_index()

fig8 = px.bar(h10, x = 'contrucao', y = 'price', color =  'contrucao', labels = {'price':'Preço', 'contrucao': 'Tempo de renovação'},
                                                                                    template = 'simple_white')
fig8.update_layout(showlegend = False)
c8.plotly_chart(fig8, use_container_width= True)

#=========================================
# ========== H9 ==========
#==========================================
st.subheader('Hipótese 9: O crescimento do preço dos imóveis mês após mês no ano de 2014 é de 10% ')
df['date'] = pd.to_datetime(df['date'])

df['mes'] = df['date'].dt.month
df['ano'] = df['date'].dt.year

year_df = df[df['ano'] == 2014]


h41 = year_df[['mes', 'price']].groupby('mes').sum().reset_index()
fig41 = px.line(h41, x='mes', y = 'price', color_discrete_sequence= ['teal'], template = 'simple_white',
                labels={'mes':'Mês', 'price': 'Preço'})

st.plotly_chart(fig41, use_container_width= True)
#=========================================
# ========== 10==========
#==========================================
st.subheader('Hipótese 10: Imóveis com 3 banheiros tem um crescimento mês após mês de 15 %')
h5 = df[(df['bathrooms'] == 3)]

h5 = h5[['mes', 'price']].groupby('mes').sum().reset_index()


fig5 = px.line(h5, x = 'mes', y = 'price', color_discrete_sequence= ['teal'], template = 'simple_white',
               labels= {'mes':'Mês', 'price': 'Preço'})

st.plotly_chart(fig5, x='mes', y='price', use_container_width= True)
#=========================================
# ========== FIM DAS HIPÓTESES==========
#==========================================


st.markdown("<h1 style='text-align: center; color: black;'> Questões de Negócio</h1>", unsafe_allow_html=True)
st.subheader('1. Quais são os imóveis que a House Rocket deveria comprar e por qual preço?')
#Respondendo
a = df[['zipcode', 'price']].groupby('zipcode').median().reset_index()
df2 = pd.merge(a, df, on='zipcode', how = 'inner')
df2 = df2.rename(columns = {'price_y' : 'price', 'price_x' : 'price_median'} ) #alterando nome das colunas
#criando coluna
for i, row in df2.iterrows():
    if (row['price_median'] >= row['price']) & (row['condition'] < 3):
        df2.loc[i,'pay'] =  'sim'
    else:
        df2.loc[i, 'pay'] = 'nao'



####################
#TMAPA
####################
#criar coluna com cor
for i, row in df2.iterrows():
    if (row['pay'] == 'sim'):
        df2.loc[i,'marker_color'] = 'green'
    else:
        df2.loc[i, 'marker_color'] = 'red'
############################################
st.markdown('Mapa - Quais imóveis devem ser comprados?')
st.markdown("""
<style>
.big-font {
    font-size:14px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font"> Em verde os imóveis indicados '
            'para compra  <br> Em vermelho os imóveis não indicados para compra </p>', unsafe_allow_html=True)

mapa = folium.Map(width = 600, height = 300,
                  location = [df['lat'].mean(),df[ 'long'].mean()],
                  default_zoom_start=30)
features = {}
for row in pd.unique(df2['marker_color']):
    features[row] = folium.FeatureGroup(name=row)

for index, row in df2.head(10000).iterrows():
    circ = folium.Circle([row['lat'], row['long']],
            radius=150, color=row['marker_color'], fill_color=row['marker_color'],
            fill_opacity = 1, popup= 'Compra: {0}, Preço: {1}'.format(row['pay'],
                              row['price']))
    circ.add_to(features[row['marker_color']])

for row in pd.unique(df2["marker_color"]):
    features[row].add_to(mapa)

folium.LayerControl().add_to(mapa)
folium_static(mapa)

############
# QUESTÃO 2 #
############

st.subheader('2. Uma vez comprado, qual é o melhor momento para vendê-lo e por qual preço?')
df3 = df2.copy()

df3['season'] = df3['mes'].apply(lambda x: 'summer' if (x > 5) & (x < 8) else
                                           'spring' if (x > 2) & (x < 5) else
                                           'fall' if (x > 8) & (x < 12) else
                                           'winter')

df3 = df3[df3['pay'] == 'sim']

df4 = df3[['season', 'zipcode', 'price']].groupby(['zipcode', 'season']).median().reset_index()

df4 = df4.rename(columns = {'price' : 'price_medi_season', 'season': 'season_median'} )

df5 = pd.merge(df3, df4, on='zipcode', how = 'inner')

for i, row in df5.iterrows():
    if (row['price_medi_season'] > row['price']):
        df5.loc[i, 'sale'] =  row['price'] * 0.1
    else:
        df5.loc[i, 'sale'] = row['price'] * 0.3


df5= df5[['price_medi_season', 'price', 'sale', 'price_median', 'season', 'zipcode']]


fig11 = px.bar(df5, x = 'season', y = 'sale', color = 'season', labels={'season':'Estação do Ano', 'sale': 'Preço de Venda'},
                                                                    template = 'simple_white')
fig11.update_layout(showlegend = False)
st.plotly_chart(fig11, x='season', y='sale', use_container_width= True)


st.markdown("<h1 style='text-align: center; color: black;'> Resumo sobre as Hipóteses </h1>", unsafe_allow_html=True)
hipoteses = pd.DataFrame({
'.': ['Verdadeira', 'Falsa', 'Verdadeira', 'Verdadeira', 'Falsa', 'Verdadeira', 'Falsa', 'Falsa',
    'Falsa', 'Falsa']}, index=['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10'])
hipoteses = hipoteses.style.set_table_styles([dict(selector='th', props=[('text-align', 'center')])])
hipoteses.set_properties(**{'text-align': 'center'}).hide_index()
st.table(hipoteses)

