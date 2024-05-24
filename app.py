import streamlit as st
import joblib
import sklearn
import numpy as np

# Definindo Cabeçalho de nossa aplicação
st.set_page_config(layout='wide')
st.image('assets/boot-ia.png', width = 200)
st.title('Previsão de Doença Hepática')
st.subheader('Tem aumentado de forma contínua o número de pacientes com doença hepática devido ao consumo excessivo de álcool, inalação de gases nocivos, ingestão de alimentos contaminados e uso de drogas e anabolizantes.')
st.markdown('Neste projeto construí um modelo de Machine Learning capaz de prever se um paciente vai ou não desenvolver uma doença hepática com base em diversas características do paciente. Esse modelo pode ajudar médicos, hospitais ou governos a planejar melhor o orçamento de gastos de saúde ou mesmo criar políticas de prevenção.')


# Iniciando Formulário
with st.form('Prever Resultado'):
    idade = st.number_input('Idade', min_value = 1.00, max_value = 100.00, help = 'Permitido valores de 1 a 100.')
    genero = st.selectbox('Gênero', ['Masculino', 'Feminino'])
    bilirrubina = st.number_input('Bilirrubina', min_value = 0.4, max_value = 80.0, help = 'Permitido valores de 0,4 a 80.')
    fosfatase_alcalina = st.number_input('Fosfatase Alcalina', min_value = 50.00, max_value = 2200.00, help = 'Permitido valores de 50 a 2.200.')
    alanina_aminotransferase = st.number_input('Alanina Aminotransferase', min_value = 5.00, max_value = 2100.00, help = 'Permitido valores de 5 a 2.100.')
    transaminase_glutanico = st.number_input('Transaminase Glutâmico-Oxalacética', min_value = 5.00, max_value = 5000.00, help = 'Permitido valores de 5 a 5.000.')
    total_proteina = st.number_input('Total de Proteína', min_value = 1.00, max_value = 15.00, help = 'Permitido valores de 1 a 15.')
    albumina = st.number_input('Albumina', min_value = 0.1, max_value = 10.0, help = 'Permitido valores de 0,1 a 10.')
    globulina = st.number_input('Globulina', min_value = 0.1, max_value = 5.0, help = 'Permitido valores de 0,1 a 5.')
    submit_button = st.form_submit_button('Prever Resultado')

    if submit_button:

        if genero == 'Masculino':
            genero = 1
        else:
            genero = 0

        novo_resultado = [idade, 
                          genero, 
                          bilirrubina, 
                          fosfatase_alcalina, 
                          alanina_aminotransferase,
                          transaminase_glutanico,
                          total_proteina,
                          albumina,
                          globulina]
        
        arr_novo_resultado = np.array(novo_resultado)

        # Média de cada feature de nosso conjunto de treinamento
        treino_mean = np.array([43.166113,
                       0.209302,
                       2.658923,
                       269.340532,
                       62.877076,
                       77.333887,
                       6.557594,
                       3.262168,
                       0.996274])
        # Desvio Padrão de cada feature de nosso conjunto de treinamento
        treino_std = np.array([16.443590,
                      0.407149,
                      5.564827,
                      222.340744,
                      140.002596,
                      144.133119,
                      1.010545,
                      0.760875,
                      0.308245])
        
        # Usamos média e desvio de treino para padronizar novos dados
        arr_paciente = (arr_novo_resultado - treino_mean) / treino_std
        arr_paciente = np.array(arr_paciente)

        # Carragendao modelo e transformando-o em um objeto Python

        meu_modelo = joblib.load('modelo_v2.pkl')

        # Antes de fazer uma previsão, é importante garantir que os dados do paciente estejam no formato correto.
        # A função reshape é usada para ajustar a forma dos dados. Nesse caso, reshape(1, -1) está sendo usado para garantir que os dados sejam tratados 
        # como uma única amostra (um único paciente) e que o número de características seja determinado automaticamente (-1) 
        # com base no tamanho do vetor de entrada. Isso é necessário para que o modelo de machine learning possa fazer previsões corretas.

        # Previsões de classe
        # reshape, tornando o array unidimensional
        resultado = meu_modelo.predict(arr_paciente.reshape(1, -1))


        if resultado == 1:
            # Texto para pacientes com doença hepática (vermelho)
            texto_hepatica = "<span style='color:#f36f22; font-size: 36px;'>Este paciente deve apresentar doença hepática!</span>"
            st.markdown('Este paciente deve apresentar doença hepática!') #, divider='rainbow')
        else:
            # Texto para pacientes sem doença hepática (azul)
            texto_nao_hepatica = "<span style='color:#1f3d51; font-size: 36px;'>Este paciente não deve apresentar doença hepática!</span>"
            st.markdown('Este paciente não deve apresentar doença hepática!')


       