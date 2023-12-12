# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Project organization](#project-organization)
- [Report](#project-organization)

## About <a name = "about"></a>

A movie recommendation engine based on collaborative filtering

## Getting Started <a name = "getting_started"></a>
`
git clone https://github.com/bert4geng/recommender.git

`
go to browser: http://localhost:8501/

### Prerequisites
dependencies list in requirements.txt 

### Installing

```
conda create -n recommender python=3.10
pip install -r requirements.txt
pip install -e . 
```

## Usage and deployment <a name = "usage"></a>

```
docker-compose up --build
```

Project organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io



Project report

Data Analysis Report -> notebooks/data_analysis_report.ipynb

Modeling and Evaluation Report -> notebooks/user_based_collaborative_filtering.ipynb

Business Evaluation Report: reports/Business_Evaluation_Report.pdf

Additional Recommendations: -> reports/Additional_Recommendations.pdf

Bonus: Provide factors influencing each movie recommendation -> notebooks/data_analysis_report.ipynb

Community Recommendation Engine Experiment: -> reports/2_Community_Recommendation_Engine Experiment.pdf

--------