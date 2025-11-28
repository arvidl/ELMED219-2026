# ELMED219-2026: Lab 0 - Enkle ML-eksempler
## Slide-innhold for Google Slides

---

## Slide 1: Tittelside
**Tittel:** ELMED219: Kunstig intelligens og beregningsorientert medisin

**Undertittel:** Lab 0: Introduksjon til maskinlæring med Python

**Detaljer:**
- Institutt for biomedisin, UiB
- Januar 2026

---

## Slide 2: Læringsmål

**Tittel:** Hva skal vi lære i dag?

**Punkter:**
- ✅ Forstå hva maskinlæring er
- ✅ Utforske medisinske datasett
- ✅ Trene en klassifikasjonsmodell (Random Forest)
- ✅ Evaluere modellens ytelse
- ✅ Forstå Explainable AI (XAI)
- ✅ Bygge en interaktiv webapp

---

## Slide 3: Hva er maskinlæring?

**Tittel:** Maskinlæring - Definisjon

**Innhold:**
> "Maskinlæring er en gren av kunstig intelligens der datamaskiner lærer mønstre fra data, uten å bli eksplisitt programmert."

**Eksempel:**
- Tradisjonell programmering: `if blodsukker > 126: return "diabetes"`
- Maskinlæring: Modellen *lærer* terskelen fra data!

---

## Slide 4: ML i medisin

**Tittel:** Hvorfor maskinlæring i medisin?

**Punkter:**
- 🏥 Diagnostikk (bildediagnostikk, patologi)
- 💊 Behandlingsvalg (prediksjon av respons)
- ⚠️ Risikovurdering (diabetes, hjertesykdom)
- 🔬 Legemiddelutvikling
- 📊 Pasientmonitorering

**Bilde:** Illustrasjon av AI i helsevesenet

---

## Slide 5: Arbeidsflyt i ML

**Tittel:** Fra data til prediksjon

**Diagram (flowchart):**
```
Data → Preprosessering → Trening → Evaluering → Deployment
         ↓                  ↓           ↓
    Rensing, splitting   Algoritme   Accuracy, F1
```

---

## Slide 6: Iris-datasettet

**Tittel:** Vårt første datasett: Iris-blomster

**Innhold:**
- 🌸 150 blomster, 3 arter
- 📏 4 egenskaper: sepal/petal lengde og bredde
- 🎯 Klassisk benchmark-datasett (Fisher, 1936)

**Bilde:** Foto av de tre iris-artene

---

## Slide 7: Visualisering av Iris

**Tittel:** Scatter plot: Kan vi skille artene?

**Bilde:** Scatter plot med sepal length vs petal length, fargekodet etter art

**Observasjon:**
- Setosa er tydelig separert
- Versicolor og Virginica overlapper noe

---

## Slide 8: Random Forest - Intuisjon

**Tittel:** Random Forest: Mange trær gir bedre svar

**Innhold:**
- 🌳 Ensemble av beslutningstrær
- 🎲 Hvert tre trenes på tilfeldig utvalg
- 🗳️ Flertallsavstemning for prediksjon

**Analogi:**
> "Som å spørre 100 eksperter og følge flertallet"

---

## Slide 9: Hvordan lærer Random Forest?

**Tittel:** Trening av modellen

**Diagram:**
```
                    ┌─── Tre 1: Hvis petal > 2.5 → ...
Treningsdata ──────├─── Tre 2: Hvis sepal < 5.0 → ...
                    ├─── Tre 3: ...
                    └─── ... (100 trær)
```

**Nøkkelpunkt:** Modellen lagrer regler, ikke data!

---

## Slide 10: Train/Test Split

**Tittel:** Hvorfor dele data i trening og test?

**Innhold:**
- 🎓 **Treningsdata (75%):** Modellen lærer
- 🧪 **Testdata (25%):** Vi evaluerer på *usett* data

**Advarsel:**
> ⚠️ Aldri evaluer på treningsdata! Det gir falsk optimisme.

---

## Slide 11: Overfitting

**Tittel:** Overfitting: Modellen husker, men forstår ikke

**Diagram:**
| | Treningsdata | Testdata |
|--|--------------|----------|
| God modell | 85% | 82% |
| Overfittet | 99% | 65% |

**Medisinsk konsekvens:** Modellen fungerer på "gamle" pasienter, men feiler på nye!

---

## Slide 12: Resultater på Iris

**Tittel:** Random Forest på Iris: 100% accuracy!

**Konfusjonsmatrise:**
```
              Predikert
           Set  Ver  Vir
Faktisk Set  12   0    0
        Ver   0  13    0
        Vir   0   0   13
```

**Tolkning:** Perfekt klassifisering på testdata

---

## Slide 13: Diabetes-datasettet

**Tittel:** Et mer realistisk eksempel: Diabetes-prediksjon

**Innhold:**
- 👩 768 kvinner fra Pima-indianerstammen
- 📅 Data fra 1988
- 🎯 Mål: Predikere diabetes basert på 8 egenskaper

**Egenskaper:** Graviditeter, glukose, blodtrykk, BMI, alder, ...

---

## Slide 14: Utfordringer med reelle data

**Tittel:** Diabetes er vanskeligere enn Iris!

**Punkter:**
- ⚖️ Ubalanserte klasser (65% friske, 35% diabetikere)
- ❓ Manglende verdier (0 = missing for glucose, BMI)
- 🔀 Overlappende klasser
- 📉 Støy i målingene

---

## Slide 15: Accuracy er ikke nok

**Tittel:** Evaluering: Mer enn bare "prosent riktig"

**Metrikker:**
| Metrikk | Definisjon | Diabetes-modell |
|---------|------------|-----------------|
| Accuracy | Andel korrekte | 74% |
| Precision | Av de vi sa JA, hvor mange var syke? | 65% |
| Recall | Av de syke, hvor mange fant vi? | 58% |
| F1 | Balanse mellom precision og recall | 61% |

---

## Slide 16: Konfusjonsmatrise

**Tittel:** Konfusjonsmatrise: Hvor feiler modellen?

**Matrise med forklaring:**
```
                 Predikert
              Frisk    Syk
Faktisk Frisk  TN=98   FP=22   ← Falske positive
        Syk    FN=29   TP=43   ← Falske negative
```

**Medisinsk perspektiv:**
- FP: Unødvendig bekymring og testing
- FN: **Farlig!** Oversett sykdom

---

## Slide 17: Precision vs Recall

**Tittel:** Trade-off: Precision vs Recall

**Diagram:** Precision-Recall kurve

**Klinisk valg:**
- **Screening:** Prioriter høy recall (fange alle syke)
- **Bekreftende test:** Prioriter høy precision (unngå falske positive)

---

## Slide 18: Explainable AI (XAI)

**Tittel:** XAI: Hvorfor ga modellen dette svaret?

**Motivasjon:**
> "En lege kan ikke stole på en 'black box' som sier 'du har diabetes' uten forklaring."

**XAI-metoder:**
- Feature Importance
- Partial Dependence Plots
- SHAP / LIME

---

## Slide 19: Feature Importance

**Tittel:** Hvilke egenskaper er viktigst?

**Stolpediagram:**
```
glucose       ████████████████████ (0.25)
bmi           ██████████████ (0.18)
age           ██████████ (0.13)
dpf           ████████ (0.10)
...
```

**Innsikt:** Glukosenivå er klart viktigst for diabetes-prediksjon

---

## Slide 20: Partial Dependence Plot

**Tittel:** PDP: Hvordan påvirker glucose risikoen?

**Graf:** PDP-kurve for glucose (120-200)

**Tolkning:**
- Lav glucose (< 100): Lav risiko
- Høy glucose (> 140): Risiko øker dramatisk

---

## Slide 21: Trustworthy AI

**Tittel:** Pålitelig AI i medisin: Sjekkliste

**6 pilarer:**
1. ✅ **Nøyaktighet:** Fungerer modellen godt nok?
2. 🔍 **Forklarbarhet:** Kan vi forstå beslutningene?
3. ⚖️ **Rettferdighet:** Fungerer den likt for alle grupper?
4. 🛡️ **Robusthet:** Tåler den støy og angrep?
5. 🔒 **Personvern:** Er pasientdata beskyttet?
6. 📋 **Ansvarlighet:** Hvem har ansvaret?

---

## Slide 22: Etiske utfordringer

**Tittel:** Etikk i medisinsk AI

**Diskusjonspunkter:**
- 🌍 **Populasjonsbias:** Pima-data → norske pasienter?
- ⏰ **Historisk bias:** 1988-data → 2026-pasienter?
- 👫 **Kjønnsbias:** Kun kvinner i datasettet
- 📜 **Informert samtykke:** Bør pasienten vite om AI?

---

## Slide 23: Interaktiv webapp

**Tittel:** Fra notebook til webapp med Gradio

**Skjermbilde:** Gradio-appen med sliders og output

**Kode (forenklet):**
```python
gr.Interface(
    fn=predict_diabetes,
    inputs=[Slider("Alder"), Slider("BMI"), Slider("Glukose")],
    outputs=Textbox("Prediksjon")
).launch()
```

---

## Slide 24: Oppsummering

**Tittel:** Hva har vi lært?

**Sjekkliste:**
- ✅ ML lærer mønstre fra data
- ✅ Random Forest: Ensemble av beslutningstrær
- ✅ Evaluering: Accuracy, precision, recall, F1
- ✅ XAI: Feature importance, PDP
- ✅ Trustworthy AI: 6 pilarer
- ✅ Etiske utfordringer i medisinsk AI

---

## Slide 25: Neste steg

**Tittel:** Videre læring

**Ressurser:**
- 📘 Molnar: *Interpretable Machine Learning* (gratis online)
- 📘 James et al.: *ISLP* (gratis online)
- 🔗 scikit-learn.org
- 🔗 gradio.app

**Neste lab:**
- Lab 1: Nettverksvitenskap og PSN
- Lab 2: Dyp læring

---

## Slide-design tips

**Fargepalett:**
- Primær: UiB blå (#003A70)
- Sekundær: Hvit, lysgrå
- Aksent: Oransje for viktige punkter

**Font:**
- Titler: Bold, 36-44pt
- Brødtekst: 24-28pt
- Kode: Monospace (Consolas, Monaco)

**Bilder å inkludere:**
1. Iris-blomster (slide 6)
2. Scatter plots fra notebook (slide 7)
3. Konfusjonsmatrise heatmap (slide 16)
4. Feature importance barplot (slide 19)
5. PDP-kurve (slide 20)
6. Gradio-skjermbilde (slide 23)

---

*Generert fra: 01-Enkle_eksempler.ipynb*
*ELMED219-2026, UiB*



