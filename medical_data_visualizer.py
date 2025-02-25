import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2)

df['overweight'] = (df['overweight'] > 25).astype(int)

# 3
df['cholesterol'] = df['cholesterol'].replace({1: 0, 2: 1, 3: 1})

df['gluc'] = df['gluc'].replace({1: 0, 2: 1, 3: 1})

# df['active'] = df['active'].replace({1: 0, 0: 1})

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = pd.melt(df,id_vars=['cardio'] , value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.sort_values(by = 'variable')
    ordered_vars = sorted(df_cat["variable"].unique())
    df_cat = df_cat.value_counts().reset_index(name = 'total')
    
    df_cat.columns = ['cardio', 'variable', 'value', 'total']

    # 7
    sns.catplot(x = "variable", y = "total", data = df_cat, hue = "value", col = "cardio", kind = "bar", errorbar = None, order = ordered_vars)


    # 8
    graph = sns.catplot(x = "variable", y = "total", data = df_cat, hue = "value", col = "cardio", kind = "bar", errorbar = None, order = ordered_vars) # fig = -> graph = 
    fig = graph.figure # fallback to graph.fig in case of incompatibility

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & \
             (df['height'] >= df['height'].quantile(0.025)) & \
             (df['height'] <= df['height'].quantile(0.975)) & \
             (df['weight'] >= df['weight'].quantile(0.025) )& \
             (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()
    # corr = corr.round(1)

    # 13
    mask = np.triu(np.ones_like(corr, dtype = bool))


    # 14
    fig, ax = plt.subplots(figsize=(12, 6))

    # 15

    sns.heatmap(corr, mask = mask, annot = True, square = True, ax = ax, fmt = '.1f', annot_kws = {"size": 12})

    # 16
    fig.savefig('heatmap.png')
    return fig
