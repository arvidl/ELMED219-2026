# Lab 0: Introduksjon til teori og verktøy for maskinlæring

I denne første laben får vi en introduksjon til **maskinlæring**: hva det er og hva det brukes til. Vår tilnærming vil være praktisk, ved bruk av Python og scikit-learn-biblioteket.

---

## 🎯 Læringsmål

Etter å ha gjennomført denne labben skal du kunne:

| Tema | Læringsmål |
|------|-----------|
| **ML-konsepter** | Definere sentrale maskinlæringsbegreper (features, labels, trening, testing) og skille mellom veiledet (supervised)og ikke-veiledet (unsupervised) læring |
| **Klassifisering** | Forstå klassifiseringsoppgaven og hvordan den skiller seg fra regresjon |
| **Dataoppdeling** | Forklare hvorfor vi deler data i trenings- og testsett, og bruke `train_test_split` |
| **Modelltrening** | Trene enkle klassifikasjonsmodeller (beslutningstre, logistisk regresjon, k-NN) med scikit-learn |
| **Evaluering** | Beregne og tolke evalueringsmetrikker som nøyaktighet (accuracy), presisjon, sensitivitet (recall) og F1-score |
| **Forvirringsmatrise** | Lese og tolke en forvirringsmatrise (confusion matrix) for å forstå modellens feil |
| **ROC-kurve** | Forstå ROC-kurven og AUC som mål på modellkvalitet |
| **Kryssvalidering** | Bruke kryssvalidering for mer robust evaluering av modeller |
| **AutoML** | Bruke PyCaret for rask prototyping og modellsammenligning |
| **Medisinsk kontekst** | Forstå spesielle hensyn ved bruk av ML i medisin (TRIPOD, overtilpasning, generaliserbarhet) |

---

## 🐍 Ny til Python?

Hvis du har lite eller ingen erfaring med Python-programmering, anbefaler vi at du først gjennomfører [**Lynkurs i AI-assistert Python-programmering**](../Lab-Lynkurs/README.md). Dette lynkurset gir deg:

- Praktisk introduksjon til Python og Google Colab
- Grunnleggende Python-syntaks (variabler, datatyper, lister)
- Erfaring med å bruke AI-verktøy (Gemini/ChatGPT) som programmeringspartner
- Smakebiter fra både Lab 0 og Lab 1

Lynkurset er spesielt designet for medisinstudenter uten programmeringserfaring.

---

## Ressurser

### Lysbilder:

| Fil | Beskrivelse |
|:----|:------------|
| [01-Enkle_eksempler-slides.pptx](slides/ELMED219-2026_Lab0-ML_01-Enkle_eksempler-slides.pptx) | Introduksjon til maskinlæring |

### Notebooks:

| Notebook | Beskrivelse | Colab |
|:---------|:------------|:------|
| [01-Enkle_eksempler.ipynb](notebooks/01-Enkle_eksempler.ipynb) | Bygger prediktive modeller basert på enkle datasett. Praktisk introduksjon til grunnleggende ML. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab0-ML/notebooks/01-Enkle_eksempler.ipynb) |
| [02-Binaer_klassifikasjon.ipynb](notebooks/02-Binaer_klassifikasjon.ipynb) | Sentrale konsepter innen binær klassifikasjon: evaluering, metrikker, validering. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab0-ML/notebooks/02-Binaer_klassifikasjon.ipynb) |
| [03-PyCaret_hurtigguide.ipynb](notebooks/03-PyCaret_hurtigguide.ipynb) | AutoML med PyCaret – hurtig prototyping med advarsler for medisinsk bruk. | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab0-ML/notebooks/03-PyCaret_hurtigguide.ipynb) |

### Løsningsnotebooks:

| Notebook | Beskrivelse |
|:---------|:------------|
| [01a-Enkle_eksempler_losninger.ipynb](notebooks/01a-Enkle_eksempler_losninger.ipynb) | Løsninger og drøftinger til oppgavene i notebook 01 |
| [02a-Binaer_klassifikasjon_losninger.ipynb](notebooks/02a-Binaer_klassifikasjon_losninger.ipynb) | Løsninger til oppgavene i notebook 02, inkl. ROC, modellsammenligning, TRIPOD |
| [03a-PyCaret_hurtigguide_losninger.ipynb](notebooks/03a-PyCaret_hurtigguide_losninger.ipynb) | Løsninger til oppgavene i notebook 03, inkl. Iris, Breast Cancer, feature selection, hyperparameter-tuning, modellkalibrering |


## Maskinlæring i Python

Vi bruker Python, det mest populære programmeringsspråket for maskinlæring. Det praktiske innholdet er hovedsakelig basert på [Jupyter Notebooks](https://jupyter.org/), som lar oss blande kode, tekst, resultater og dokumentasjon i ett enkelt dokument. Vi bruker også standard datavitenskap- og maskinlæringsbiblioteker i Python, som [Pandas](https://pandas.pydata.org/) og [scikit-learn](https://scikit-learn.org/stable/).

### Conda-miljøer

**Hovedmiljø:** Bruk `environment.yml` i rot-katalogen for notebook 01 og 02.

**PyCaret-miljø:** Notebook 03 krever PyCaret, som har avhengigheter som kan være i konflikt med TensorFlow/PyTorch. Vi anbefaler et separat miljø:

```bash
# Opprett PyCaret-miljø
conda env create -f pycaret-environment.yml
conda activate pycaret-elmed219

# Start Jupyter
jupyter notebook
```

**Alternativ: Google Colab** – Alle notebooks kan kjøres i Colab uten lokal installasjon. PyCaret installeres automatisk ved kjøring.


## Eksterne ressurser

### Maskinlæring

* [Introduction to Machine Learning](https://developers.google.com/machine-learning/intro-to-ml) (Nybegynner, 20 min) - Googles introduksjon til grunnleggende ML-konsepter.
* [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) (Nybegynner, 3 timer) - Kaggles hands-on introduksjon til maskinlæring.
* [Supervised Learning with scikit-learn](https://app.datacamp.com/learn/courses/supervised-learning-with-scikit-learn) (Middels, 4 timer) - Interaktiv introduksjon til ML ved bruk av scikit-learn.
* [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) (Middels, 15 timer) - Googles praktiske introduksjon til maskinlæring.
* [Problem Framing](https://developers.google.com/machine-learning/problem-framing) (Middels, 45 min) - Hvordan avgjøre om ML er en god løsning og hvordan skissere en ML-løsning.

### Forklarbar AI (XAI)

* [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/) - Christoph Molnars omfattende bok om tolkbar ML (gratis online).
* [SHAP Documentation](https://shap.readthedocs.io/) - Offisiell dokumentasjon for SHAP-biblioteket.

### Python for datavitenskap

* [Intermediate Python](https://app.datacamp.com/learn/courses/intermediate-python-for-data-science) (Nybegynner, 4 timer) - DataCamps datavitenskapsorienterte introduksjon til Python.
* [Pandas](https://www.kaggle.com/learn/pandas) (Nybegynner, 4 timer) - Kaggles introduksjon til Pandas.
* [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) - Offisiell dokumentasjon med eksempler og tutorials.

### Jupyter Notebooks

* [Jupyter Notebook 101](https://www.kaggle.com/code/jhoward/jupyter-notebook-101) - Jeremy Howards introduksjon til Jupyter.
* [How to Use Jupyter Notebooks: The Ultimate Guide](https://www.datacamp.com/tutorial/tutorial-jupyter-notebook) - DataCamps grundige guide.

### Medisinsk ML

* [Machine Learning for Healthcare](https://ocw.mit.edu/courses/6-s897-machine-learning-for-healthcare-spring-2019/) - MIT OpenCourseWare kurs om ML i helsevesenet.
* [TRIPOD Statement](https://www.tripod-statement.org/) - Retningslinjer for rapportering av prediktive modeller i medisin.
