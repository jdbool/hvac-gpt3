import pandas as pd
import json

dataframe = pd.read_csv('pulled_data.csv')

input_column_names = ['NE01_AHU7_RESET_POLL_TL', 'NE01_AHU7_HCV_POLL_TL', 'NE01_AHU7_HC_SWT_POLL_TL', 'NE01_AHU7_HC_RWT_POLL_TL', 'NE01_AHU7_MAD_FB_POLL_TL',
                      'NE01_AHU7_HC_SAT_POLL_TL', 'NE01_AHU7_MAT_POLL_TL', 'NE01_AHU7_RAT_POLL_TL', 'NE01_AHU7_SF_SPD_POLL_TL', 'NE01_AHU7_EF_SPD_POLL_TL', 'NE01_AHU5_OAT_GV_POLL_TL']
output_column_names = ['VAV4_1_RT_TL', 'VAV4_2_RT_TL', 'VAV4_3_RT_TL',
                       'VAV4_4_RT_TL', 'VAV4_5_RT_TL', 'VAV4_6_RT_TL', 'VAV4_7_RT_TL']

with open('test.jsonl', 'w') as f:
    for index, row in dataframe.iterrows():
        inputs_str = ','.join(
            map(str, row[input_column_names].values.tolist()))
        outputs_str = ','.join(
            map(str, row[output_column_names].values.tolist()))
        json_line = json.dumps({
            "prompt": inputs_str,
            "completion": outputs_str
        })
        f.write(f'{json_line}\n')
