# Lab 2: Dyplæring (DL)

I denne labben utforsker vi konsepter og anvendelser av **dyplæring** (deep learning) i medisin og biomedisinsk forskning.

---

## Læringsmål

Etter å ha gjennomført denne labben skal du kunne:

| Tema | Læringsmål |
|------|-----------|
| **Nevrale nettverk** | Forklare hva et nevralt nettverk er, sammenligne biologiske og kunstige nevroner |
| **Læring** | Forstå backpropagation, gradient descent og treningsprosessen |
| **MLP** | Bygge og trene et multilags perseptron for klassifisering |
| **CNN** | Forklare hvordan konvolusjonelle nevrale nettverk fungerer for bildeanalyse |
| **PyTorch** | Bruke PyTorch til å bygge og trene nevrale nettverk |
| **Medisinsk AI** | Anvende dyplæring på medisinske data (hjertesykdom, EKG, MR) |
| **Forklarbar AI** | Bruke Grad-CAM for å forstå modellbeslutninger |

---

## Prioriteringsguide

Notebooks er organisert i **6 deler (A-F)** med tydelig prioritering. **Start med kjerne-materialet** og gå videre etter tid og interesse.

### Anbefalt læringssti for medisinstudenter

```
1. Start med Del B (NN-teori) → Grunnleggende forståelse
2. Fortsett med Del A kjerne → Praktisk hands-on med MNIST
3. Deretter Del C og D → CNN i praksis og medisinsk bildeanalyse
4. Valgfritt: Del E og F etter interesse
```

---

## Oversikt over notebooks

### DEL A: MNIST-grunnlaget (fra ELMED219)

| Prioritet | Notebook | Beskrivelse | Colab |
|:---------:|:---------|:------------|:------|
| **1** | [A1-CNN-intro](notebooks/A1-CNN-intro.ipynb) | Konseptuell intro til CNN med medisinske analogier | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/A1-CNN-intro.ipynb) |
| 3 | [A2-PyTorch-Lightning](notebooks/A2-PyTorch-Lightning.ipynb) | Introduksjon til PyTorch og Lightning | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/A2-PyTorch-Lightning.ipynb) |
| 3 | [A3-MNIST-datasamling](notebooks/A3-MNIST-datasamling.ipynb) | Datainnsamling og organisering | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/A3-MNIST-datasamling.ipynb) |
| 3 | [A4-MNIST-Random-Forest](notebooks/A4-MNIST-Random-Forest.ipynb) | ML baseline med Random Forest | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/A4-MNIST-Random-Forest.ipynb) |
| **1** | [A5-MNIST-MLP](notebooks/A5-MNIST-MLP.ipynb) | Din første dyplæringsmodell (MLP) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/A5-MNIST-MLP.ipynb) |
| **1** | [A6-MNIST-CNN](notebooks/A6-MNIST-CNN.ipynb) | MNIST med CNN | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/A6-MNIST-CNN.ipynb) |

### DEL B: Nevrale nettverk – Teori og medisinsk anvendelse

| Prioritet | Notebook | Beskrivelse | Colab |
|:---------:|:---------|:------------|:------|
| **1** | [B1-nn-intro](notebooks/B1-nn-intro.ipynb) | Nevrale nettverk i menneske og maskin | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/B1-nn-intro.ipynb) |
| **1** | [B2-læring-i-nn](notebooks/B2-læring-i-nn.ipynb) | Hvordan nevrale nettverk lærer | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/B2-læring-i-nn.ipynb) |
| **1** | [B3-hjertesykdom-klassifikasjon](notebooks/B3-hjertesykdom-klassifikasjon.ipynb) | Klassifisering av hjertesykdom (UCI) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/B3-hjertesykdom-klassifikasjon.ipynb) |
| **1** | [B4-EKG-arytmi-CNN](notebooks/B4-EKG-arytmi-CNN.ipynb) | EKG arytmi-klassifikasjon med CNN | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/B4-EKG-arytmi-CNN.ipynb) |

### DEL C: CNN Bildeklassifikasjon

| Prioritet | Notebook | Beskrivelse | Colab |
|:---------:|:---------|:------------|:------|
| **2** | [C1-cnn-miljø-arkitektur](notebooks/C1-cnn-miljø-arkitektur.ipynb) | Miljøoppsett og CNN-arkitektur | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/C1-cnn-miljø-arkitektur.ipynb) |
| **2** | [C2-cnn-trening](notebooks/C2-cnn-trening.ipynb) | Trening og lagring av modell | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/C2-cnn-trening.ipynb) |
| **2** | [C3-cnn-testing-gradcam](notebooks/C3-cnn-testing-gradcam.ipynb) | Testing, evaluering og Grad-CAM | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/C3-cnn-testing-gradcam.ipynb) |
| **2** | [C4-cnn-konklusjon](notebooks/C4-cnn-konklusjon.ipynb) | Oppsummering og veien videre | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/C4-cnn-konklusjon.ipynb) |
| 📝 | [C4a-cnn-konklusjon-losninger](notebooks/C4a-cnn-konklusjon-losninger.ipynb) | **Løsningsforslag** med MedMNIST, ViT og etikk | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/C4a-cnn-konklusjon-losninger.ipynb) |

### DEL D: Medisinsk bildeanalyse

| Prioritet | Notebook | Beskrivelse | Colab |
|:---------:|:---------|:------------|:------|
| **2** | [D1-MR-demens-klassifikasjon](notebooks/D1-MR-demens-klassifikasjon.ipynb) | MRI-bildeanalyse for demens-deteksjon | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/D1-MR-demens-klassifikasjon.ipynb) |

### DEL E: Emosjonsanalyse

| Prioritet | Notebook | Beskrivelse | Colab |
|:---------:|:---------|:------------|:------|
| 3 | [E1-emosjoner-bygging](notebooks/E1-emosjoner-bygging.ipynb) | Emosjonsklassifikasjon del 1 (bygging) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/E1-emosjoner-bygging.ipynb) |
| 3 | [E2-emosjoner-trening](notebooks/E2-emosjoner-trening.ipynb) | Emosjonsklassifikasjon del 2 (trening) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/E2-emosjoner-trening.ipynb) |
| 3 | [E3-emosjoner-evaluering](notebooks/E3-emosjoner-evaluering.ipynb) | Emosjonsklassifikasjon del 3 (evaluering) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/E3-emosjoner-evaluering.ipynb) |

### DEL F: TabPFN – Dyplæring på tabelldata (avansert)

| Prioritet | Notebook | Beskrivelse | Colab |
|:---------:|:---------|:------------|:------|
| 4 | [F1-TabPFN-intro](notebooks/F1-TabPFN-intro.ipynb) | Utforskning av TabPFN | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/F1-TabPFN-intro.ipynb) |
| 4 | [F2-TabPFN-neuro](notebooks/F2-TabPFN-neuro.ipynb) | TabPFN i nevrovitenskap | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/arvidl/ELMED219-2026/blob/main/Lab2-DL/notebooks/F2-TabPFN-neuro.ipynb) |

---

## Prioritetsnivåer

| Prioritet | Beskrivelse | Estimert tid |
|:---------:|:------------|:------------:|
| **1 (kjerne)** | Essensielt for læringsmålene – alle bør gjennomføre | 4-5 timer |
| **2 (anbefalt)** | Viktig utdyping, spesielt CNN og medisinsk bildeanalyse | 3-4 timer |
| **3 (valgfri)** | Supplerende materiale etter interesse | 2-3 timer |
| **4 (avansert)** | For de som vil gå dypere inn i moderne metoder | 1-2 timer |

---

## Kom i gang

### Google Colab (anbefalt)

1. Klikk på Colab-badgen ved notebooken du vil kjøre
2. Logg inn med Google-konto
3. Kjør cellene med `Shift+Enter`

**Merk:** Data lastes ned automatisk ved kjøring av notebooks.

### Lokal kjøring

```bash
conda env create -f environment.yml
conda activate elmed219
jupyter notebook
```

---

## Læringsressurser

### Videoer (sortert etter varighet)

| Video | Forfatter | Varighet |
|:------|:----------|:--------:|
| [What is Deep Learning?](https://youtu.be/6M5VXKLf4D4) | Simplilearn | 6 min |
| [But what is a neural network?](https://youtu.be/aircAruvnKk) | 3Blue1Brown | 19 min |
| [What is backpropagation?](https://youtu.be/Ilg3gGewQ5U) | 3Blue1Brown | 13 min |
| [Building micrograd](https://youtu.be/VMj-3S1tku0) | Andrej Karpathy | 2.5 t |

### Kurs og ressurser

- [MIT 6.S191: Introduction to Deep Learning](http://introtodeeplearning.com)
- [Stanford CS231n: CNNs for Visual Recognition](http://vision.stanford.edu/teaching/cs231n)
- [Learn PyTorch](https://learnpytorch.io)
- [fastMONAI](https://fastmonai.no) – Bergen-basert medisinsk AI

---

## Struktur

```
Lab2-DL/
├── README.md
├── assets/           # Slides og illustrasjoner
├── data/             # Eksempelbilder
├── ressurser/        # Figurer og illustrasjoner
└── notebooks/
    ├── A1-A6         # MNIST-grunnlaget
    ├── B1-B4         # NN-teori og medisinsk anvendelse
    ├── C1-C4(a)      # CNN bildeklassifikasjon + løsninger
    ├── D1            # Medisinsk MR-analyse
    ├── E1-E3         # Emosjonsanalyse
    └── F1-F2         # TabPFN (avansert)
```

---

Utviklet av Arvid Lundervold, Universitetet i Bergen.
