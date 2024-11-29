#!/usr/bin/env python
# coding: utf-8

# #### **IMPORTANDO AS BIBLIOTECAS**

# In[1]:


# Bibliotecas para tratar os dados
import pandas as pd

# Bibliotecas para EDA
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.offline as py
import folium

# Configurar para não exibir warnings
import warnings
warnings.filterwarnings('ignore')

# Configurar para exibir todas as colunas de um dataframe do Pandas
pd.set_option('display.max_columns',None)


# #### **IMPORTANDO O DATASET**

# In[2]:


airbnb = pd.read_csv('train.csv')
airbnb.head()


# In[3]:


print(f'O dataframe possui {airbnb.shape[0]} linhas e {airbnb.shape[1]} colunas.')


# In[4]:


airbnb.info()


# Temos alguns valores nulos nas colunas name, host_name, last_review e review_per_month. 

# In[5]:


numericas = airbnb.select_dtypes(include='int64')
nao_numericas = airbnb.select_dtypes(exclude='int64')

print(f'Temos {numericas.shape[1]} colunas numéricas e {nao_numericas.shape[1]} colunas não-numéricas.')


# #### **EXPLORANDO OS DADOS**
# Primeiramente, iremos avaliar as distribuições dos tipos de acomodações.

# In[6]:


fig = px.histogram(airbnb, x='room_type', color='room_type',text_auto='.0f')

fig.update_traces(textposition='outside')

fig.update_layout(title='Distribuição dos Tipos de Acomodações',
                  xaxis_title='Tipo',
                  yaxis_title='Quantidade',
                  showlegend=False)

fig.show()


# Como é possível verificar no gráfico acima, dos 48.895 acomodações listadas na plataforma, mais da metade (25.409 - representando 51,97%) são do tipo 'Entire home/apt', seguido por 22.326 do tipo 'Private Room' (45,66%), e apenas 1.160 são do tipo 'Shared room'(2,37%).

# Agora vamos avaliar a distribuição das acomodações nos cinco distritos da cidade de Nova York - Manhattan, Brooklyn, Queens, Bronx e Staten Island.

# In[7]:


contagem = airbnb['neighbourhood_group'].value_counts().values
distritos = airbnb['neighbourhood_group'].value_counts().index

fig = px.bar(
    x=contagem,
    y=distritos,
    orientation='h',
    title='Quantidade de Acomodações por Distritos',
    color=distritos,
    labels={'y': 'Distrito', 'x': 'Quantidade'},
    custom_data=[distritos, contagem])

fig.update_yaxes(autorange='reversed')

fig.update_layout(
    xaxis_title='Quantidade',
    yaxis_title='Distrito',
    showlegend=False
)

fig.update_traces(hovertemplate='Quantidade: %{customdata[1]}')

fig.show()


# O gráfico acima demonstra que Manhattan mais de 85% das acomodações estão localizadas em Manhattan ou no Brooklyn. Staten Island é o distrito com a menor quantidade de imóveis, representando apenas 0,76% das acomodações listadas neste dataframe.

# Além disso, conforme podemos visualizar abaixo, quando analisamos a distruibuição das acomodações por tipo de quarto, reafirmamos o dado de que, majoritariamente, os imóveis são do tipo Entire home/apt ou Private Room. Em Manhattan temos a maior concentração de apartamentos do tipo Entire home/apt, enquanto a maior número de apartamentos do tipo Private room está no Brooklyn.

# In[8]:


pd.crosstab(airbnb['neighbourhood_group'],airbnb['room_type']).sort_values(by='Entire home/apt',ascending=False)


# Visto que já identificamos que a maior quantidade de acomodações está em Manhattan ou no Brooklyn, vamos verificar os bairros destes distritos que possuem a maior distruibuição de imóveis.

# In[9]:


top10_bairros = airbnb.groupby(['neighbourhood','neighbourhood_group']).size().sort_values(ascending=False).reset_index(name='contagem')[:10]
top10_bairros


# In[10]:


top10_bairros.groupby('neighbourhood_group')['contagem'].agg(['sum','count']).reset_index()


# Quando avaliamos os top 10 bairros com mais acomodações listadas, é possível verifcar que embora as duas primeiras posições sejam ocupadas por bairros localizados no distrito do Brooklyn, Manhattan possui cerca cerca de 100 imóveis a mais neste ranking, representando um total de 6 bairros, dois a mais que no Brooklyn.

# Nossas próximas análises estarão relacionadas aos preços das acomodações.
# 
# Conforme podemos verificar na tabela abaixo, o preço médio da diária é de US$ 152.72, com um desvio padrão de US$ 240.15. Este desvio padrão pode ser considerado elevado, indicando que há uma alta dispersão ou variabilidade dos preços em relação à média. Quando avaliamos os quartis, podemos perceber que a maior parte das acomodações possui diária pouco maior que a média e estão nos três primeiros quartis.

# In[11]:


airbnb[['price']].describe().T


# In[12]:


print(f'Adicionalmente, identifica-se que {airbnb.query("price == 0").shape[0]} acomodações possuem preço igual a zero.')


# Vamos excluir do dataframe as acomodações com diárias zeradas, para que possamos visualizar melhor graficamente o preço das diárias médias, máximas e mínimas, por distrito, considerando o tipo de quarto.

# In[13]:


airbnb = airbnb.query('price != 0')
precos = airbnb.groupby(['neighbourhood_group','room_type'])['price'].agg(['mean','median','min','max']).reset_index()

fig1 = px.bar(precos, x="neighbourhood_group", y="mean",
             color='room_type', barmode='group')

fig2 = px.bar(precos, x="neighbourhood_group", y="median",
             color='room_type', barmode='group')

fig3 = px.bar(precos, x="neighbourhood_group", y="max",
             color='room_type', barmode='group')

fig4 = px.bar(precos, x="neighbourhood_group", y="min",
             color='room_type', barmode='group')

fig = make_subplots(rows=2, cols=2, subplot_titles=('Média','Mediana','Preço Máximo', 'Preço Mínimo'))

for trace in fig1.data:
    fig.add_trace(trace, row=1, col=1)

for trace in fig2.data:
    fig.add_trace(trace, row=1, col=2)
    
for trace in fig3.data:
    fig.add_trace(trace, row=2, col=1)

for trace in fig4.data:
    fig.add_trace(trace, row=2, col=2)

fig.update_layout(height=700, width=1100, title='Preço das Diárias por Tipo de Quarto e Distrito',showlegend=False)
fig.update_xaxes(tickangle=-90)
fig.show()


# In[14]:


airbnb.groupby('neighbourhood_group')['price'].agg(['mean','median','std','min','max']).reset_index()


# In[15]:


precos['diff'] = precos['mean'] - precos['median']
precos


# Com base nos gráficos e nas tabelas acima, cabe citar os seguintes pontos:
# * Brooklyn, Manhattan e Queens tem o mesmo preço máximo;
# * Com exceção de Staten Island, demais distritos possuem o mesmo preço mínimo;
# * O maior preço médio de diárias está em Manhattan, e o menor, no Bronx;
# * No Bronx e Queens o tipo de quarto mais caro é o Private Room (e não o Entire home/apt conforme seria esperado);
# * A diária mínima para Staten Island é a maior quando comparada aos demais distrito;
# * A mediana - número central de uma lista de dados organizados de forma crescente, é relativamente inferior a média independentemente do tipo de quarto e distrito. A maior diferença é percebida nos quartos do tipo Entire home/apt em Manhattan e Staten Island (aproximadamente US$ 58 e US$ 74, respectivamente).

# Agora, vamos verificar onde estão localizados as acomodações com as diárias mais caras, e qual o respectivo tipo de quarto.

# In[16]:


airbnb[['id','neighbourhood_group','neighbourhood','room_type','price']].sort_values(by='price',ascending=False)[:10]


# As acomodações mais caras estão no Queens, Brooklyn e Manhattan, sendo que este último distrito, possui a maior quantidade de imóveis dentre os mais caros. Chama a atenção que temos quartos do tipo Private Room entre os mais caros.

# Agora vamos verificar as acomodações com as maiores diárias em cada bairro.

# In[17]:


neighbourhood_group = airbnb['neighbourhood_group'].unique()
for i in neighbourhood_group:
    bairro = airbnb[airbnb.neighbourhood_group == i].reset_index()
    bairro = bairro.groupby(['neighbourhood','room_type'])['price'].max().reset_index(name='max_price').sort_values(by='max_price',ascending=False)[:10]
    print(i)
    display(bairro)


# Esperava-se que somente acomodações do tipo Private room e Entire home/apt estivessem entre as mais caras, no entanto, é possível verificar que no Queens e no Bronx temos acomodações do tipo Shared room entre as mais caras.

# Vamos visualizar em um mapa da cidade de Nova York onde estão localizados as 50 acomodações mais caras.

# In[18]:


# Criando um dataframe com os 50 apartamentos mais caros
top_50 = airbnb.sort_values(by='price',ascending=False)[:50]

# Criando o mapa
mapa = folium.Map(location=[40.7128, -74.0060], zoom_start=11)  

# Adicionando marcadores para cada apartamento
for i in range(0,len(top_50)):
   folium.Marker(
      location=[top_50.iloc[i]['latitude'], top_50.iloc[i]['longitude']],
      popup=f"Name: {top_50.iloc[i]['name']} | District: {top_50.iloc[i]['neighbourhood_group']} | Price: US$ {top_50.iloc[i]['price']:,.2f}",
   ).add_to(mapa)

# Exibindo o mapa
mapa


# Nossas próximas análises estatarão relacionadas ao número mínimo de noites.
# 
# Conforme podemos verificar abaixo, de forma geral, a média do mínimo de noites é 7, com um desvio padrão relativamente alto de 20 noites. Além disso, chama a atenção o máximo de noites relacionado na base, que é de 1250 noites (aproximadamente 42 meses).

# In[19]:


airbnb[['minimum_nights']].describe().T


# Vamos separar o mínimo de noite em alguns intervalos:

# In[20]:


intervalos = [0, 10, 30, 90, 180, 365, float('inf')]
labels = ['até 10 noites', 'maior que 10 até 30 noites', 'mais de 30 até 90 noites','maior que 90 até 180 noites', 'maior que 180 até 365 noites', 'maior que 365 noites']
airbnb['categoria'] = pd.cut(airbnb['minimum_nights'], bins=intervalos, labels=labels)
nights = airbnb.groupby('categoria')['minimum_nights'].count().reset_index(name='qtd')
nights['%_total'] = nights['qtd']/48884
nights


# In[21]:


pivot = airbnb.groupby(['categoria','room_type'])['minimum_nights'].count().reset_index()
pivot = pd.pivot_table(pivot,values='minimum_nights',index='categoria',columns=['room_type']).reset_index()
pivot


# Mais de 98% das acomodações listadas exigem um mínimo de noites de até 30 dias, sendo um percentual superior a 86% para apartamentos com mínimo de noites de até 10 dias. Quando analisamos a distribuiçao do diferentes room_types nas faixas de mínimo de noites, também identificamos uma elevada concentração de acomodações na faixa de até 30 dias.
# 
# Agora vamos avaliar a média, mediana, moda, mínimo e máximo de noites por distrito.

# In[22]:


airbnb.groupby('neighbourhood_group')['minimum_nights'].agg(['mean','median',pd.Series.mode,'min','max']).reset_index()


# Quando olhamos para a média, o Bronx possui a menor média de noites, enquanto Manhattan, a maior. 
# 
# Com relação à Mediana, verifica-se que esta é igual a 2 noites tanto no Brooklyn como em Manhattan, e para os demais distritos, igual a 2.
# 
# Já a Moda (valor que mais se repete num conjunto de valores), é igual a 2 noites no Brooklyn e Staten Island, e a 1 noite nos demais distritos.
# 
# Novamente o máximo de noites chama a atenção, e podemos verificar que a acomodação com o maior número mínimo de noites está localizado em Manhattan. Adicionalmento, no Brooklyn também temos um imóvel com mínimo de noites superior a 1 ano (999 noites - aproximadamente 33 meses), assim como no Queens (500 noites - aproximadamente 17 meses).

# Abaixo podemos visualizar quais são estas acomodações com número mínimo de noite superior a 365 dias e onde estão localizados. Dos 48.895 acomodações listadas na base em análise, apenas 14 possuem o nínimo de noites superior a 365 dias (0,03%). Além disso, é possível verificar que Staten Island e Bronx não possuem imóveis onde o mínimo de noites é maior que um ano.

# In[23]:


max_nights = airbnb.query('minimum_nights > 365').sort_values(by='minimum_nights',ascending=False).reset_index()
max_nights[['name','neighbourhood_group','room_type','price','minimum_nights']]


# Agora vamos verificar qual a média de preços para as acomodações nas diferentes faixas de mínimo de noites.

# In[24]:


airbnb.groupby('categoria')['price'].mean().reset_index()


# Conforme verifica-se acima, as acomodações com mínimo de diárias superior a 365 apresentam a menor média de preços. Chama a atenção que os apartamentos com mínimo de diárias maior que 90 até 180 noites, apresenta média maior que o dobro das demais faixas.

# Por fim, vamos olhar para a quantidade de avaliações dos imóveis listados na base. 
# 
# Quando olhamos apenas para as acomodações que mais receberam avaliações, é possível identificar que estão localizados no Queens, Manhattan e Brooklyn. Não temos imóveis no Bronx e Staten Island entre os que mais receberam avaliações.

# In[25]:


airbnb[['name','neighbourhood_group','room_type','number_of_reviews','reviews_per_month']].sort_values(by='number_of_reviews',ascending=False)[:10]


# Abaixo, relacionamos as acomodações por distrito que mais receberam avaliações e quantas avaliações receberam por mês.

# In[26]:


idx = airbnb.groupby('neighbourhood_group')['number_of_reviews'].idxmax()
top_avaliados = airbnb.loc[idx, ['neighbourhood_group', 'name', 'number_of_reviews','reviews_per_month']].sort_values(by='number_of_reviews',ascending=False)
top_avaliados


# In[27]:


bottom_avaliados = airbnb[airbnb.number_of_reviews == 0]
print(f'Identificamos que um total de {bottom_avaliados.shape[0]} acomodações não receberam nenhuma avaliação.')


# Agora, vamos verificar qual o percentual de acomodações por distrito que não receberam nenhuma avaliação.

# In[28]:


# Criando novo dataframe com o total de imóveis por distrito que não receberam nenhuma avaliação
bottom_avaliados = bottom_avaliados.groupby('neighbourhood_group')['id'].count().reset_index(name='count').sort_values(by='count',ascending=False)

# Criando novo dataframe com o total de imóveis por distrito 
total_aptos = airbnb.groupby('neighbourhood_group')['id'].count().reset_index(name='total_count')

# Realizando o merge dos dataframe de imóveis sem avaliação + total de apartamentos
bottom_avaliados = bottom_avaliados.merge(total_aptos, how='left', on='neighbourhood_group')

# Adicionando nova coluna ao dataframe com o percentual de imóveis por distrito que não recebeu nenhuma avaliação
bottom_avaliados['%_no_review'] = round(((bottom_avaliados['count'] / bottom_avaliados['total_count'])*100),2)

# Visualizando o dataframe criado
bottom_avaliados


# Para finalizar, vamos visualizar as informações acima graficamente.

# In[29]:


distrito = bottom_avaliados['neighbourhood_group'].value_counts().index
total_ap = bottom_avaliados['total_count'].value_counts().index
sem_aval = bottom_avaliados['count'].value_counts().index
percent = bottom_avaliados['%_no_review'].value_counts().index

# Criando o gráfico total
barra_total = go.Bar(x=distrito, y=total_ap,
               name='Total')
           
# Criando o gráfico sem avaliação
barra_zero = go.Bar(x=distrito, y=sem_aval,
               name='Sem Avaliação')

# Adicionando percentuais nas barras 'sem avaliação'
annotations= []
for i in range(len(sem_aval)):
    annotation = dict(
        x=i + 0.25,
        y=sem_aval[i] + 50,
        text=f'{percent[i]}%',
        showarrow=True,
        arrowhead=3,
        ax=0
    )
    annotations.append(annotation)
               
# Definindo o layout
layout = go.Layout(title='Total de Quartos por Distrito x Quartos sem Avaliação (%)',
                   # Configurações do título
                   titlefont= {'family':'Arial', 'size':25, 'color':'#0e78a3'},
                   xaxis={'title':'Distrito'},
                   yaxis={'title':'Quantidade de Quartos'},
                   barmode='group',
                   height=500, width=1000,
                   annotations=annotations)

# Criando a figura
fig = go.Figure(data=[barra_total,barra_zero], layout=layout)

# Plotando o gráfico
py.iplot(fig)


# In[ ]:





# #### **CONCLUSÃO**
# Nova York é uma metrópole globalmente conhecida como centro de negócios e destino turístico vibrante. Está dividida em cinco distritos, sendo eles: Manhattan, Brooklyn, Queens, Bronx e Staten Island.
# 
# Manhattan e Brooklyn são as regiões mais populares e turísticas. Manhattan, mesmo sendo menor em área, possui a maior densidade demográfica, inúmeras atrações turísticas, além de ser o epicentro financeiro da cidade. 
# 
# Enquanto isso, o Brooklyn se destaca como o distrito mais populoso e um verdadeiro caldeirão cultural, com bairros que respiram história e arte.
# 
# O Queens, o maior distrito em extensão, é pouco explorado por turistas, mas está estrategicamente localizado próximo aos principais aeroportos da cidade. Nos últimos anos, passou por um desenvolvimento significativo, com foco na construção e renovação de prédios residenciais, elevando assim os custos de moradia.
# 
# O Bronx, embora seja pouco visitado por turistas pois, infelizmente, muitas vezes é associado à pobreza e criminalidade, possui alguns atrativos relavantes, como o Jardim Zoológico do Bronx e o Yankee Stadium, palco de grandes eventos esportivos.
# 
# Por fim, Staten Island, é o distrito mais meridional e menos conhecido, oferecendo um refúgio tranquilo e uma atmosfera suburbana, contrastando fortemente com a agitação do resto da cidade.
# 
# Nova York é conhecida por seus preços elevados, desde diárias de hotéis até o custo de vida em geral. Quando olhamos para a plataforma AirBnB - plataforma online que permite às pessoas alugar acomodações alternativas aos hotéis tradicionais, onde os anfitriões disponibilizam desde quartos individuais a casas inteiras para viajantes, as acomodações listadas na cidade de Nova York corroboram com as características gerais da cidade, quanto aos custos elevados, distritos mais caros e populares. Após EDA realizada, os principais insights foram:
# 
# * Mais da metade das acomodações listadas são do tipo Entire home/apt inteiros, sendo que somado aos apartamentos do tipo Private, somam mais de 97% dos apartamentos analisados. Pouco mais de 2% dos apartamentos são do tipo Shared room. Esta distribuição dos tipos de apartamento pode refletir tanto a preferência como o orçamento dos visitantes - a diária de apartamentos inteiros ou quartos privados costuma ser mais cara;
# 
# * A popularidade dos distritos de Manhattan e Brooklyn reflete na quantidade de acomodações ofertadas nestas regiões - mais de 85% dos imóveis relacionados no dataset;
# 
# * O Queens possui cerca de 12% das acomodações listadas, o que pode estar somente relacionado somente a sua maior extensão geográfica ou também ao desenvolvimento observado nos últimos anos;
# 
# * Um percentual superior a 98% dos apartamentos exige um mínimo de noites de até 30 dias, independetemente do room_type;
# 
# * Manhattan e Brooklyn, em linha com sua popularidade, possuem as maiores médias de diária. Quando olhamos para o valor máximo de diária, além destes dois distrito, também no Queens observa-se o valor de US$ 10.000. O preço das diárias de uma forma geral reforçam a fama que a cidade de Nova York tem de possuir preços elevados.
# 
# * Chama a atenção a oferta de apartamentos com mínimo de noites superior a 30 dias, o que pode indicar que os imóveis listados na plataforma não são direcionado somente a turistas, mas também a outros públicos, que precisam ficam um prazo superior na cidade por um prazo maior. Os alugueis por mínimo de noite superior a 365 dias tendem a possuir a diária mais barata.
# 
# * Verfica-se um percentual elevado de acomodações sem avaliação, pode-se supor que são apartamentos listados mais recentemente na plataforma e por este motivo ainda não tiveram avaliações.
# 
