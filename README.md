# Cours ML II - modèles linéaires pour l'économétrie

*Repo partagé entre MA & MS, maintenu par Thomas Milcent et Basile Desjuzeur*

## Comment utiliser ce repo

Vous pouvez cloner ce repo sur votre machine avec `git clone https://github.com/basile-desjuzeur/albert_school_ml2`.

Pour le mettre à jour au fur et à mesure du cours : `git pull`

## Contenu

Ce repo contient des notebooks et des slides de support de cours. La table de matières ci-dessous n'est pas exhaustive.

### [0.Git & Github](./0.%20Git%20&%20Github/)

#### [0.1. Exercice Pull Request](./0.%20Git%20&%20Github/albert_school_pr/)

#### [0.2. Exercice navigation dans un repo](0.%20Git%20&%20Github/albert-school-intro-to-git/)

### [1. ML workflow](./1.%20ML%20pipeline/)

#### [1.1. Demo sklearn](./1.%20ML%20pipeline/1.demo_sklearn.ipynb)

Notebook fait en cours qui montre les principales fonctionnalités de skleanr

- estimateur
- pipeline
- dummyregressor

#### [1.2. Cross validation](1.%20ML%20pipeline/2.cross_validation.ipynb)

Pourquoi et comment fait on de la cross-validation ?

- besoin d'estimer la capacité de généralisation d'un modèle
- KFold
- TimeSeriesSplit

#### [1.3. Grid search](./1.%20ML%20pipeline/3.grid_search.ipynb)

Pourquoi et comment chercher les meilleurs hyperparamètres d'un modèle avec une GridSearch ?

[Notebook](1.%20ML%20pipeline/3.grid_search.ipynb) et [corrigé](./1.%20ML%20pipeline/3.grid_search_corrige.ipynb).

#### [1.4. Bias variance trade off](./1.%20ML%20pipeline/4.bias_variance.ipynb)

Cours & exemples du compromis biais-variance.

#### [1.5. Encodings](./1.%20ML%20pipeline/5.encodings.ipynb)

Introduction aux encoders avec sklearn. Corrigé de la session du 09/12/25 MS.

- OneHotEncoder, OrdinalEncoder
- StandardScaler, KbinsDiscretizer
- combiner les encoders avec ColumnTransformer
- corrigé de l'exercice

### [2. Linear Models](./2.%20Linear%20Reg/)

#### [2.1. Lasso, ridge, elasticnet](./2.%20Linear%20Reg/1.lasso_ridge_elasticnet.ipynb)

Fonctionnement de Lasso, Ridge, Elasticnet.

#### [2.2. Exercices]
