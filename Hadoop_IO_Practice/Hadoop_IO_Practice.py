import pandas as pd
import numpy as np
import os
import re
import datetime

def indexToDate(INPUT_PATH, OUTPUT_PATH, year):
    pd.set_option('mode.chained_assignment', None)
    print(f'input_path: {INPUT_PATH}')
    ori = sorted(os.listdir(INPUT_PATH))
    filter = []
    for filename in ori:
        if filename.startswith(f'{year}'):
            filter.append(filename)

    total_count = len(filter)
    print(f'{year}년 데이터 수: {total_count}')
    count = 0

    for file in filter:
        target = pd.read_csv(f'{INPUT_PATH}/{file}', delimiter='\t', header=None)
        target.columns = ['date', 'value']
        date = file.replace('.dat', '')

        for i in range(len(target)):
            tmp = f'{year}'
            tmp += str(datetime.timedelta(seconds=i)).replace(':', '')
            target['date'][i] = tmp

        target.to_csv(f'{OUTPUT_PATH}/{date}.csv', index=False)

        print(f'{count + 1} / {total_count} 완료..')
        count += 1

indexToDate('M_WT.WT01.P/','2016_result' ,2016)