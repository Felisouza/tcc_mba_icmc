from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import seaborn as sns 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def matriz_confusao(y, y_pred, palete, titulo):
    # Calcular a matriz de confusão
    conf_matrix2 = confusion_matrix(y, y_pred)

    # Plotar a matriz de confusão usando Seaborn
    fig, ax =  plt.subplots(figsize=(8, 6))
    
    rect = patches.FancyBboxPatch(
        (0, 0), 1, 1, 
        boxstyle="round,pad=0.25", edgecolor='#000000', linewidth=1.5, transform=ax.transAxes, clip_on=False,
        facecolor='#ffffff') 
    ax.add_patch(rect)
    sns.heatmap(conf_matrix2, annot=True, fmt='d', cmap=palete, xticklabels=['NÃO', 'SIM'], yticklabels=['NÃO', 'SIM'], ax=ax)

    plt.title(titulo)
    plt.xlabel('Previsto')
    plt.ylabel('Verdadeiro')
    

    # # Alterando a cor de fundo do gráfico 
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor("#fff8ed")
    fig.patch.set_alpha(0.7)
    return plt.show()

def matriz_confusao_porcentagem(y, y_pred, palete, titulo):
    # Calcular a matriz de confusão
    cm = confusion_matrix(y_test, y_test_pred)

    # Convertendo a matriz de confusão para porcentagens
    cm_percentage = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100

    # Plotar a matriz de confusão usando Seaborn
    fig, ax =  plt.subplots(figsize=(8, 6))
    
    rect = patches.FancyBboxPatch(
        (0, 0), 1, 1, 
        boxstyle="round,pad=0.25", edgecolor='#000000', linewidth=1.5, transform=ax.transAxes, clip_on=False,
        facecolor='#ffffff') 
    ax.add_patch(rect)
    sns.heatmap(cm_percentage, annot=True, fmt='d', cmap=palete, xticklabels=['NÃO', 'SIM'], yticklabels=['NÃO', 'SIM'], ax=ax)

    plt.title(titulo)
    plt.xlabel('Previsto')
    plt.ylabel('Verdadeiro')
    

    # # Alterando a cor de fundo do gráfico 
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor("#fff8ed")
    fig.patch.set_alpha(0.7)
    return plt.show()