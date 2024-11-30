# Análise de Dados do AirBnB em Nova York

**Fonte dos Dados:** [New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data/data)

## Introdução

A base descreve características e métricas relacionadas às acomodações listadas na plataforma AirBnB em Nova York durante o ano de 2019, incluindo informações detalhadas sobre os anfitriões, a disponibilidade geográfica das acomodações, tipo de acomodação, preço, mínimo de noites, dados sobre avaliações, entre outras.

Por meio desta análise exploratória de dados, buscou-se analisar e entender os padrões de oferta, preços e comportamento das listagens de acomodações no Airbnb em Nova York, incluindo informações como:

- Tendências, insights sobre os distritos, e possíveis fatores que influenciam o mercado de aluguel por temporada na cidade;
- Tipos de acomodações mais ofertadas;
- Avaliação dos preços médios e máximos por distrito;
- Padrões no número mínimo de noites exigidas, diferenciando entre turistas de curto prazo e outros públicos de estadia prolongada.

**Acesse a análise completa** [aqui](https://github.com/laissapadilha/Python-NYC_AirBnB/blob/66052aeff4e96553d444741df10692b787c3a4b9/airbnb_nyc.ipynb)

## Exploração dos Dados

### Localização x Tipo de Acomodação

Primeiramente, avaliou-se a distribuição dos diferentes tipos de acomodações.

![image](https://github.com/user-attachments/assets/30163649-3927-4c8e-94f3-7db4809145dc)

Como é possível verificar no gráfico acima, dos 48.895 acomodações listadas na plataforma, mais da metade (25.409 - representando 51,97%) são do tipo 'Entire home/apt', seguido por 22.326 do tipo 'Private Room' (45,66%), e apenas 1.160 são do tipo 'Shared room'(2,37%).

A seguir, avaliou-se a distribuição das acomodações nos cinco distritos da cidade de Nova York - Manhattan, Brooklyn, Queens, Bronx e Staten Island.

![image](https://github.com/user-attachments/assets/773741eb-dc09-43d6-bc66-6aeaa4dcb15e)

O gráfico acima demonstra que Manhattan mais de 85% das acomodações estão localizadas em Manhattan ou no Brooklyn. Staten Island é o distrito com a menor quantidade de imóveis, representando apenas 0,76% das acomodações listadas neste dataframe.

Além disso, conforme é possível visualizar abaixo, quando analisa-se a distruibuição das acomodações por tipo de quarto, reafirma-se o dado de que, majoritariamente, os imóveis são do tipo Entire home/apt ou Private Room. Em Manhattan há a maior concentração de apartamentos do tipo Entire home/apt, enquanto a maior número de apartamentos do tipo Private room está no Brooklyn.

![image](https://github.com/user-attachments/assets/5af7f445-6547-4e90-8f0e-f5d151a7c2c7)

Visto que já foi identificado que a maior quantidade de acomodações está em Manhattan ou no Brooklyn, também foi verificado os bairros destes distritos que possuem a maior distruibuição de imóveis.

![image](https://github.com/user-attachments/assets/d9a28168-f3a9-48b8-99cc-e51df1ab7c67)

Quando avalia-se os top 10 bairros com mais acomodações listadas, é possível verifcar que embora as duas primeiras posições sejam ocupadas por bairros localizados no distrito do Brooklyn, Manhattan possui cerca cerca de 100 imóveis a mais neste ranking, representando um total de 6 bairros, dois a mais que no Brooklyn.

### Preços

Conforme podemos verificar na tabela abaixo, o preço médio da diária é de US$ 152.72, com um desvio padrão de US$ 240.15. Este desvio padrão pode ser considerado elevado, indicando que há uma alta dispersão ou variabilidade dos preços em relação à média. Quando avaliamos os quartis, pode-se perceber que a maior parte das acomodações possui diária pouco maior que a média e estão nos três primeiros quartis.

![image](https://github.com/user-attachments/assets/cca6061c-143b-4043-8acd-3cf2fd38985a)

Com base nos gráficos abaixo, cabe citar os seguintes pontos:

* Brooklyn, Manhattan e Queens tem o mesmo preço máximo;
* Com exceção de Staten Island, demais distritos possuem o mesmo preço mínimo;
* O maior preço médio de diárias está em Manhattan, e o menor, no Bronx;
* No Bronx e Queens o tipo de quarto mais caro é o Private Room (e não o Entire home/apt conforme seria esperado);
* A diária mínima para Staten Island é a maior quando comparada aos demais distrito;
* A mediana - número central de uma lista de dados organizados de forma crescente, é relativamente inferior a média independentemente do tipo de quarto e distrito. A maior diferença é percebida nos quartos do tipo Entire home/apt em Manhattan e Staten Island (aproximadamente US$ 58 e US$ 74, respectivamente).

![image](https://github.com/user-attachments/assets/9914c3bc-6c96-4fb0-925a-9f25f5fbc67a)

### Preço x Tipo de Acomodação

É possível verificar abaixo que as acomodações mais caras estão no Queens, Brooklyn e Manhattan, sendo que este último distrito, possui a maior quantidade de imóveis dentre os mais caros. Chama a atenção que temos quartos do tipo Private Room entre os mais caros, e não somente Entire home/apt.

![image](https://github.com/user-attachments/assets/c8805c54-924f-43d1-ad63-8317e164cec7)

### Mínimo de Noites

Conforme pode ser verificado abaixo, de forma geral, a média do mínimo de noites é 7, com um desvio padrão relativamente alto de 20 noites. Além disso, chama a atenção o máximo de noites relacionado na base, que é de 1250 noites (aproximadamente 42 meses).

![image](https://github.com/user-attachments/assets/dcd4125b-f191-447b-8872-a08f63cc0307)

A seguir, o número mínimo de noite foi separado em alguns intervalos:

![image](https://github.com/user-attachments/assets/630bbafe-520c-4874-847c-6810ca264219)

![image](https://github.com/user-attachments/assets/2e82d5f2-f8c8-4700-91a3-763261b6a4d3)

Conforme verifica-se acima, mais de 98% das acomodações listadas exigem um mínimo de noites de até 30 dias, sendo um percentual superior a 86% para apartamentos com mínimo de noites de até 10 dias. Quando analisamos a distribuiçao do diferentes room_types nas faixas de mínimo de noites, também identificamos uma elevada concentração de acomodações na faixa de até 30 dias.

### Mínimo de Noites x Localização

A seguir, avaliou-se a média, mediana, moda, mínimo e máximo de noites por distrito.

![image](https://github.com/user-attachments/assets/111f73cc-72a1-4fb7-aace-d78e4e77087e)

Quando olhamos para a média, o Bronx possui a menor média de noites, enquanto Manhattan, a maior. 

Com relação à Mediana, verifica-se que esta é igual a 2 noites tanto no Brooklyn como em Manhattan, e para os demais distritos, igual a 2.

Já a Moda (valor que mais se repete num conjunto de valores), é igual a 2 noites no Brooklyn e Staten Island, e a 1 noite nos demais distritos.

Novamente o máximo de noites chama a atenção, e podemos verificar que a acomodação com o maior número mínimo de noites está localizado em Manhattan. Adicionalmento, no Brooklyn também temos um imóvel com mínimo de noites superior a 1 ano (999 noites - aproximadamente 33 meses), assim como no Queens (500 noites - aproximadamente 17 meses).

### Mínimo de Noites x Preço

Conforme verifica-se abaixo, as acomodações com mínimo de diárias superior a 365 apresentam a menor média de preços. Chama a atenção que os apartamentos com mínimo de diárias maior que 90 até 180 noites, apresenta média maior que o dobro das demais faixas.

![image](https://github.com/user-attachments/assets/e47b8371-25ed-4acf-a0f3-bcc76203137f)

### Avaliações

Quando olhamos apenas para as acomodações que mais receberam avaliações, é possível identificar que estão localizados no Queens, Manhattan e Brooklyn. Não temos imóveis no Bronx e Staten Island entre os que mais receberam avaliações.

![image](https://github.com/user-attachments/assets/7c711d0e-f7b1-46c7-b759-ecafc731f3b9)

Adicionalmente, foi possível identificar que um total de 10.051 acomodações não receberam nenhuma avaliação. A partir disso, verificou-se qual o percentual de acomodações por distrito que não receberam nenhuma avaliação. Tais informações estão exibidas no gráfico abaixo.

![image](https://github.com/user-attachments/assets/529e5cb1-8e29-49d1-bc3e-1d5903d9e1a6)


## Considerações Finais
Nova York é uma metrópole globalmente conhecida como centro de negócios e destino turístico vibrante. Está dividida em cinco distritos, sendo eles: Manhattan, Brooklyn, Queens, Bronx e Staten Island.

Manhattan e Brooklyn são as regiões mais populares e turísticas. Manhattan, mesmo sendo menor em área, possui a maior densidade demográfica, inúmeras atrações turísticas, além de ser o epicentro financeiro da cidade. 

Enquanto isso, o Brooklyn se destaca como o distrito mais populoso e um verdadeiro caldeirão cultural, com bairros que respiram história e arte.

O Queens, o maior distrito em extensão, é pouco explorado por turistas, mas está estrategicamente localizado próximo aos principais aeroportos da cidade. Nos últimos anos, passou por um desenvolvimento significativo, com foco na construção e renovação de prédios residenciais, elevando assim os custos de moradia.

O Bronx, embora seja pouco visitado por turistas pois, infelizmente, muitas vezes é associado à pobreza e criminalidade, possui alguns atrativos relavantes, como o Jardim Zoológico do Bronx e o Yankee Stadium, palco de grandes eventos esportivos.

Por fim, Staten Island, é o distrito mais meridional e menos conhecido, oferecendo um refúgio tranquilo e uma atmosfera suburbana, contrastando fortemente com a agitação do resto da cidade.

Nova York é conhecida por seus preços elevados, desde diárias de hotéis até o custo de vida em geral. Quando olhamos para a plataforma AirBnB - plataforma online que permite às pessoas alugar acomodações alternativas aos hotéis tradicionais, onde os anfitriões disponibilizam desde quartos individuais a casas inteiras para viajantes, as acomodações listadas na cidade de Nova York corroboram com as características gerais da cidade, quanto aos custos elevados, distritos mais caros e populares. Após EDA realizada, os principais insights foram:

* Mais da metade das acomodações listadas são do tipo Entire home/apt inteiros, sendo que somado aos apartamentos do tipo Private, somam mais de 97% dos apartamentos analisados. Pouco mais de 2% dos apartamentos são do tipo Shared room. Esta distribuição dos tipos de apartamento pode refletir tanto a preferência como o orçamento dos visitantes - a diária de apartamentos inteiros ou quartos privados costuma ser mais cara;

* A popularidade dos distritos de Manhattan e Brooklyn reflete na quantidade de acomodações ofertadas nestas regiões - mais de 85% dos imóveis relacionados no dataset;

* O Queens possui cerca de 12% das acomodações listadas, o que pode estar somente relacionado somente a sua maior extensão geográfica ou também ao desenvolvimento observado nos últimos anos;

* Um percentual superior a 98% dos apartamentos exige um mínimo de noites de até 30 dias, independetemente do room_type;

* Manhattan e Brooklyn, em linha com sua popularidade, possuem as maiores médias de diária. Quando olhamos para o valor máximo de diária, além destes dois distrito, também no Queens observa-se o valor de US$ 10.000. O preço das diárias de uma forma geral reforçam a fama que a cidade de Nova York tem de possuir preços elevados.

* Chama a atenção a oferta de apartamentos com mínimo de noites superior a 30 dias, o que pode indicar que os imóveis listados na plataforma não são direcionado somente a turistas, mas também a outros públicos, que precisam ficam um prazo superior na cidade por um prazo maior. Os alugueis por mínimo de noite superior a 365 dias tendem a possuir a diária mais barata.

* Verfica-se um percentual elevado de acomodações sem avaliação, pode-se supor que são apartamentos listados mais recentemente na plataforma e por este motivo ainda não tiveram avaliações.
