# Trabalho de conclusão de curso - MBA em ciência de dados ICMC - USP

## 📌 Objetivo
Este trabalho tem como objetivo aplicar técnicas de **estatística** e **machine learning** em dados de uma corretora de seguros para prever a inadimplência em parcelas de seguros no contexto de negócios entre empresas (**B2B**).  

A análise busca fornecer **insights estratégicos** para gestão de risco, apoio na tomada de decisões comerciais e otimização de operações financeiras.

---

## Metodologia
- **Modelos utilizados**:
  - Regressão Logística
  - Random Forest
  - XGBoost  

- **Desafio principal**: desbalanceamento da variável-alvo (inadimplente vs. adimplente).  
- **Técnicas de balanceamento aplicadas**:
  - Oversampling (superamostragem)
  - Undersampling (subamostragem)

---

## Avaliação de Desempenho
Os modelos foram avaliados com base em:
- **Recall**
- **Precisão**
- **F1-score**
- **Matriz de confusão**

### Principais resultados:
- O **XGBoost com oversampling** apresentou o melhor desempenho.
- Maior capacidade de capturar casos de inadimplência.
- Redução significativa de **falsos negativos (FN)**.
- Oversampling mostrou maior robustez e generalização em comparação ao undersampling.

---

## Conclusões
- O modelo **XGBoost + Oversampling** se destacou como a abordagem mais promissora.  
- Apesar dos bons resultados, os modelos **não estão prontos para produção**.  
- O estudo abre caminho para aplicações práticas na **avaliação de inadimplência** e gestão de riscos em corretoras de seguros.

---

## Próximos Passos
Para aprimorar os resultados, recomenda-se:
- Testar técnicas avançadas de balanceamento (ex.: **SMOTE**, **ADASYN**).
- Realizar **fine-tuning de hiperparâmetros**.
- Incorporar **dados mais informativos** (indicadores financeiros, histórico de pagamentos).
- Explorar novas arquiteturas e algoritmos.

---

## Estrutura do Projeto
```
├── data/                # Dataset da corretora de seguros
├── notebooks/           # Jupyter Notebooks com análises e experimentos
├── models/              # Modelos treinados
├── reports/             # Relatórios e resultados
└── README.md            # Documentação do projeto
```

---

## Impacto para o Negócio
Este estudo contribui para:
- **Mensuração de risco** em operações B2B.
- **Decisão estratégica** sobre comercialização de produtos.
- **Gestão de clientes inadimplentes**.
- **Otimização financeira** e redução de perdas.