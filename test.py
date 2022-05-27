import pandas as pd
import requests

openai_api_key = 'XXXXX'
openai_model = 'davinci:ft-personal-XXXXX'

dataframe = pd.read_csv('pulled_data.csv')

input_column_names = ['NE01_AHU7_RESET_POLL_TL', 'NE01_AHU7_HCV_POLL_TL', 'NE01_AHU7_HC_SWT_POLL_TL', 'NE01_AHU7_HC_RWT_POLL_TL', 'NE01_AHU7_MAD_FB_POLL_TL',
                      'NE01_AHU7_HC_SAT_POLL_TL', 'NE01_AHU7_MAT_POLL_TL', 'NE01_AHU7_RAT_POLL_TL', 'NE01_AHU7_SF_SPD_POLL_TL', 'NE01_AHU7_EF_SPD_POLL_TL', 'NE01_AHU5_OAT_GV_POLL_TL']
output_column_names = ['VAV4_1_RT_TL', 'VAV4_2_RT_TL', 'VAV4_3_RT_TL',
                       'VAV4_4_RT_TL', 'VAV4_5_RT_TL', 'VAV4_6_RT_TL', 'VAV4_7_RT_TL']

sampled_dataframe = dataframe.sample(n=10)

for index, row in sampled_dataframe.iterrows():
    print('\n', index)
    inputs_str = ','.join(
        map(str, row[input_column_names].values.tolist()))
    outputs_floats = row[output_column_names].values.tolist()
    outputs_str = ','.join(
        map(str, outputs_floats))
    print('Real inputs:', inputs_str)
    print('Real outputs:', outputs_floats)
    data = requests.post('https://api.openai.com/v1/completions', json={
        'prompt': inputs_str,
        'model': openai_model,
        'max_tokens': 50
    }, headers={
        'Authorization': f'Bearer {openai_api_key}'
    }).json()
    prediction = data['choices'][0]['text']
    parts = prediction.split(',')[:len(output_column_names)]
    prediction_floats = [float(x) for x in parts]
    print('Prediction:', prediction_floats)
    absolute_errors = [abs(x - y)
                       for x, y in zip(prediction_floats, outputs_floats)]
    print('Errors:', absolute_errors)
    average_error = sum(absolute_errors) / len(absolute_errors)
    print('Average error:', average_error)
