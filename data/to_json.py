import pandas as pd
import argparse
import warnings
import os
warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser()
parser.add_argument('task', choices=['poster', 'talk', 'participant'])
args = parser.parse_args()


if args.task == 'poster':
    df = pd.read_csv('posters.tsv', delimiter='\t', header=0)
    print(df)
    df = df.drop(columns='No.')
    json_data = df.to_json(orient='records')
    print(json_data)

    # df = df.sample(frac=1, random_state=4).reset_index(drop=True)
    # txt = ''
    # for i, row in df.iterrows():
    #     txt += f'  <li><b>{row["Poster Title"]}</b><br>{row["Presenter"]} ({row["Affiliation"]})</li>\n'
    #     # txt += f'  <tr><td>{i}</td><td>\n    {row["Poster Title"]}<br>{row["Presenter"]} ({row["Affiliation"]})</td></tr>\n'
    #     # if i == 0:
    #     #     txt += f'''  <tr><th>{row[0]}</th>\n    <th>{row[1]}</th>\n    <th>{row[2]}</th></tr>\n'''
    #     # else:
    #     #     txt += f'''  <tr><td>{row[0]}</td>\n    <td>{row[1]}</td>\n    <td>{row[2]}</td></tr>\n'''

    with open('posters.json', 'w') as f:
        f.write(json_data)


elif args.task == 'talk':
    df = pd.read_csv('talks.tsv', delimiter='\t', header=0, engine='python')
    df['Pic'] = df['Pic'].apply(lambda x: x if os.path.isfile(f'../images/{x}') else 'placeholder.jpg')
    print(df)
    json_data = df.to_json(orient='records')

    # txt = ''
    # for i, row in df.iterrows():
    #     txt += f'.. container:: talk{i}\n\n' \
    #            f'    .. image:: /images/placeholder.jpg\n' \
    #            f'       :width: 200px\n' \
    #            f'       :align: left\n' \
    #            f'       :class: pic\n\n' \
    #            f'    **{row["Title"]}**\n\n' \
    #            f'    {row["Name"]} ({row["Affiliation"]})\n\n' \
    #            f'    {row["Abstract"]}\n\n' \

    with open('talks.json', 'w') as f:
        f.write(json_data)

