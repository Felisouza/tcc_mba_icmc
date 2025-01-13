import json
import matplotlib.patheffects as PathEffects
import matplotlib.patches as patches
import seaborn as sns 
import matplotlib.pyplot as plt

with open(r"../reports/paleta_cores.json") as f:
    data = json.load(f)
    paleta = data['colors']['dataColors']
    BadPalette = data['colors']['dataColorsBadVariation']
    GoodPalette = data['colors']['dataColorsGoodVariation']
    PrincipalPallete = data['colors']['dataColorsPrincipalVariation']

def grafico_classes(df, titulo):
    class_counts = df['target'].value_counts(normalize=True) * 100 
    class_counts = class_counts.round(1)
    class_counts = class_counts.reset_index() 
    class_counts.columns = ['target', 'percentual'] 
    class_counts['target'] = class_counts['target'].map({0:'Não', 1:'Sim'})

    # Criando o gráfico de barras com a paleta personalizada 
    fig, ax = plt.subplots(figsize=(8, 6))
    # Adicionando rótulos e título
    plt.xlabel('Inadimplente?')
    plt.ylabel('Quantidade de Inadimplência')
    plt.title(titulo)

    # Limite do eixo y
    plt.ylim(0, 110)

    # Adicionando uma borda ao redor do gráfico 
    rect = patches.FancyBboxPatch(
        (0, 0), 1, 1, 
        boxstyle="round,pad=0.15", edgecolor='#000000', linewidth=1.5, transform=ax.transAxes, clip_on=False,
        facecolor='#ffffff') 
    ax.add_patch(rect)
    sns.barplot(x='target', y='percentual', data=class_counts, palette=paleta[:2], ax=ax)

    # Adicionando os valores nas barras 
    for p in ax.patches[-2:]: 
        ax.annotate(
            f'{p.get_height()}%', 
            (p.get_x() + p.get_width() / 2., p.get_height()), 
            ha='center', 
            va='baseline', 
            fontsize=10, color='black', xytext=(0, 5), textcoords='offset points')

    # # Alterando a cor de fundo do gráfico 
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor("#fff8ed")
    fig.patch.set_alpha(0.7)

    # Mostrando o gráfico
    return plt.show()