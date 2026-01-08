# Teamprosjekt &nbsp;&nbsp;&nbsp; <span style="font-size: 16px;">[ELMED219 / BMED365]</span>
## _Presisjonsmedisin og kvantitativ bildebehandling ved glioblastom_

> **Merk:** Dette er et fellesprosjekt mellom ELMED219 og BMED365. **Prosjektrapporten skal skrives på engelsk** (se [LaTeX-malen](./latex-template/)).

---

## Teamorganisering

I år har vi **14 søkere fra BMED365** og **14 søkere fra ELMED219**. Vi vil etablere **5 tverrfaglige team**, hver med en balansert blanding av studenter fra begge programmene:

<!--
| Team | BMED365-studenter | ELMED219-studenter | Totalt |
|------|------------------|-------------------|-------|
| Team 1 | 3 (b01*, b02, b03) | 3 (e01*, e02*, e03*)| 6 |
| Team 2 | 3 (b04*, b05, b06) | 3 (e04, e05*, e06*)| 6 |
| Team 3 | 3 (b07*, b08, b09*) | 3 (e07, e08, e09*)| 6 |
| Team 4 | 3 (b10*, b11*, b12)| 2 (e10*, e11*)| 5 |
| Team 5 | 2 (b13*, b14*, b15*) | 3 (e12, e13, e14*)| 6 |

*) Tilstede Dag 1 (2026-01-05)
-->

Pr. 2026-01-08:

| Team | BMED365-studenter   | ELMED219-studenter      | Totalt |
|------|---------------------|------------------------|-------|
| Team 1 | 2 (b01, b02)      | 3 (e01, e02, e03)      | 5     |
| Team 2 | 4 (b04, b05, b06, b16) | 2 (e05, e06)      | 6     |
| Team 3 | 3 (b07, b08, b09) | 3 (e08, e09 e17)       | 6    |
| Team 4 | 2 (b10, b11)      | 3 (e10, e11, e15)      | 5     |
| Team 5 | 4 (b12, b13, b14, b15) | 2 (e12, e14)      | 6     |

Denne tverrfaglige sammensetningen reflekterer virkelige forskergrupper der medisinsk ekspertise møter beregnings- og tekniske ferdigheter.

### Målgruppe

- **ELMED219**: Medisinstudenter i 2. til 5. studieår
- **BMED365**: Masterstudenter i biomedisin, inkludert spesialiseringer i bioinformatikk, medisinsk fysikk, molekylærbiologi, medisinsk teknologi og relaterte felt. Noen studenter har nylig fullført sin bachelorgrad.

Prosjektet er utformet for å imøtekomme dette mangfoldet av bakgrunner samtidig som det oppmuntrer til samarbeid og gjensidig læring.

---



## Presentasjon av teamprosjekt (holdes på engelsk)

**Tirsdag 27.01.2026, 08:15-10** (20 min per team, alle teammedlemmer deltar)

## Innlevering av teamprosjektrapport (skrives på engelsk)

**Frist: Torsdag 29.01.2026, 16:00** - Ett medlem leverer teamrapporten (som PDF-fil) til Mitt-UiB på vegne av teamet

---

## Læringsmål

Etter fullført prosjekt skal studentene kunne:

- **Beskrive** relevante bildeteknologier og modaliteter som brukes i diagnostikk og overvåking av glioblastom
- **Identifisere** egnede maskinlæringsmetoder for segmentering og klassifisering av medisinske bilder
- **Integrere** kunnskap fra ulike felt (bildebehandling, beregning, klinisk medisin) til et sammenhengende forskningsforslag
- **Gjenkjenne** sentrale etiske hensyn i AI-basert medisinsk bildebehandling, inkludert personvern, databeskyttelse og rettferdighet
- **Skissere** en grunnleggende databehandlingsplan etter FAIR-prinsippene
- **Samarbeide** effektivt i et tverrfaglig team for å produsere et felles skriftlig dokument

---

## Prosjektmotivasjon

### Hvorfor et forskningsforslag i stedet for dataanalyse?

Dette prosjektet ber deg om å skrive en forskningsplan (skisse til søknad om forskningsmidler) i stedet for å utføre faktisk dataanalyse. Dette designet er pedagogisk motivert:

1. **Konseptuell forståelse**: Å skrive en forskningsplan krever at du demonstrerer forståelse av feltet uten å gå seg vill i teknisk feilsøking eller implementeringsdetaljer.

2. **Virkelighetsnær praksis**: Forskere bruker betydelig tid på å utforme søknader før datainnsamling. Dette gjenspeiler autentisk akademisk praksis.

3. **Integrerende tenkning**: Du må bringe sammen kunnskap på tvers av bildebehandling, maskinlæring, etikk og kliniske domener, som er den typen integrerende tenkning som er essensiell for translasjonsforskning.

4. **Samarbeidsskriving**: Gruppesamarbeid om et skriftlig dokument er mer håndterbart enn å koordinere kode på tvers av ulike ferdighetsnivåer og datamiljøer.

5. **Utjevning av spillefeltet**: Studenter med ulik teknisk bakgrunn kan bidra meningsfullt. Medisinstudenter bidrar med klinisk innsikt; biomedisinske/tekniske studenter bidrar med metodologisk kunnskap.

### Hvorfor glioblastom?

Glioblastom (GBM) representerer et godt case-studie for presisjonsmedisin og kvantitativ bildebehandling:

- **Godt karakterisert**: Omfattende litteratur og etablerte bildeprotokoller (BraTS-utfordringen gir utmerkede benchmarks)
- **Klinisk betydning**: Dårlig prognose (median overlevelse rundt 15 måneder) skaper et genuint behov for forbedrede diagnostiske og terapeutiske tilnærminger
- **Molekylære markører**: Viktige biomarkører (IDH-mutasjonsstatus, MGMT-metylering) eksemplifiserer presisjonsmedisinske tilnærminger
- **Multimodal bildebehandling**: Standard kliniske protokoller inkluderer flere MR-sekvenser (T1, T1+Gd, T2, FLAIR), med fremvoksende roller for avanserte teknikker
- **Aktivt forskningsmiljø**: Årlige utfordringer, åpne datasett og reproduserbare metoder letter læring

---

## Prosjektbeskrivelse

Forestill deg at du er del av en gruppe etablerte, vellykkede forskere som skal samarbeide om en viktig biomedisinsk og medisinsk utfordring. En åpen utlysning for forskningsprosjekter er annonsert under et nytt paraplyprogram med tittelen **«Kunstig intelligens og beregningsbasert (bio)medisin»**. Din tverrfaglige gruppe sikter mot et prosjekt om **«Presisjonsmedisin og kvantitativ bildebehandling i glioblastom: En multiskala-tilnærming»**.

> **Viktig:** Oppgaven er å **skrive en forskningsplan** (en skisse til søknad om forskningsmidler) for et hypotetisk prosjekt, **ikke** å faktisk gjennomføre prosjektet med dataanalyse eller koding. Du skal beskrive *hva* du ville gjort, *hvordan* og *hvorfor*, men ikke utføre selve analysen.

### Fokusområder

1. **Bildeteknologier og modaliteter**: muligens på ulike skalaer (makro: MR/PET; mikro: histopatologi; molekylært: genomikk/proteomikk)
2. **Bildeavledede biomarkører** for diagnostikk, prognose og behandlingsrespons ved glioblastom
3. **Maskinlæringsteknikker** for segmentering, klassifisering og prediksjon
4. **Grafteori og pasientlikhetssnettverk** for å oppdage pasientundergrupper og støtte presisjonsmedisinske tilnærminger *(valgfri alternativ eller komplementær tilnærming)*
5. **Relevans og potensiell effekt** av din foreslåtte tilnærming
6. **Etikk og databehandling**: inkludert personvernhensyn, GDPR-bevissthet og planer for datadeling

---

## Rapportorganisering

### Forskningsplan
**(3 til 5 sider inkludert figurer og referanseliste)**

| Seksjon | Innhold | Spørsmål å vurdere |
|---------|---------|-------------------|
| **Bakgrunn** | Kort introduksjon til feltet | Hva er det kliniske problemet? Hva er nåværende tilnærminger? |
| **Mål** | Målsettinger og forventede resultater | Hva ønsker du å oppnå? Hvorfor er det relevant? |
| **Materialer** | Datakilder, pasientkohorter | Hvilke datasett ville du brukt? Hvilken type bilder? |
| **Metoder** | Bildeanalyse, ML-tilnærminger | Hvordan ville du behandlet bilder? Hvilke metoder ville du anvendt? |
| **Evaluering** | Hvordan vurdere resultater | Hvordan ville du visst om tilnærmingen din fungerer? |

#### Veiledning om metoder og evaluering

Din metodeseksjon bør beskrive (på et konseptuelt nivå):

- **Forbehandling**: Hva må skje med bilder før analyse? (f.eks. registrering til et felles rom, intensitetsnormalisering). Du trenger ikke spesifisere eksakte programvarekommandoer, men bør forstå hvorfor forbehandling er viktig.

- **Segmenterings- eller klassifiseringstilnærming**: Hvilken type metode ville du brukt? (f.eks. et konvolusjonelt nevralt nettverk som U-Net for segmentering, eller en klassifikator for å predikere tumortype). Beskriv den generelle tilnærmingen og hvorfor den er egnet for oppgaven.

- **Trening og validering**: Hvor ville treningsdata komme fra? Hvordan ville du sjekke at modellen fungerer på nye data den ikke har sett før? (f.eks. deling av data i trenings- og testsett, eller bruk av data fra ulike sykehus).

- **Ytelsesmetrikker**: Hvordan ville du målt suksess? For segmentering måler metrikker som Dice-score overlapp mellom predikerte og sanne tumorregioner. For klassifisering er nøyaktighet eller areal under ROC-kurven (AUROC) vanlige.

> **Merknad for studenter**: Du forventes ikke å implementere disse metodene eller kjenne alle tekniske detaljer. Målet er å vise at du forstår den generelle arbeidsflyten og kan beskrive den tydelig. Bruk litteraturen og ressursene som er gitt for å lære om vanlige tilnærminger.

### Databehandlingsplan og etiske hensyn
**(1,5 til 2,5 sider inkludert grafikk eller lenker)**

| Seksjon | Innhold |
|---------|---------|
| **Databeskrivelse** | Typer data du ville brukt, formater, omtrentlig volum |
| **Data- og kodedeling** | Hvor ville du lagret og delt data/kode? |
| **FAIR-prinsipper** | Hvordan ville du gjort data Finnbare, Tilgjengelige, Interoperable, Gjenbrukbare? |
| **Etiske hensyn** | Pasientsamtykke, personvernbeskyttelse, potensielle skjevheter |

#### Sentrale etiske hensyn for AI i medisinsk bildebehandling

Din etikkseksjon bør adressere:

- **Pasientsamtykke og personvern**: Hvordan beskyttes pasientdata? Hva betyr anonymisering?
- **Databeskyttelsesregelverk**: Bevissthet om GDPR og dets implikasjoner for medisinske data
- **Rettferdighet og skjevhet**: Kan AI-systemet fungere ulikt for ulike pasientgrupper? Hvorfor kan dette skje?
- **Transparens**: Kan klinikere forstå og stole på AI-systemets resultater?

> **Merknad**: Du trenger ikke være juridisk ekspert. Målet er å demonstrere bevissthet om disse problemstillingene og vise at du har tenkt gjennom dem i konteksten av ditt foreslåtte prosjekt.

---

## Vurderingskriterier

| Komponent | Vekt | Hva vi ser etter |
|-----------|------|------------------|
| **Bakgrunn og mål** | 20% | Tydelig beskrivelse av problemet, veldefinerte mål, forståelse av klinisk relevans |
| **Materialer og metoder** | 30% | Passende valg av data og metoder, logisk arbeidsflyt, demonstrasjon av forståelse |
| **Relevans og effekt** | 20% | Hvorfor dette prosjektet betyr noe, potensielle fordeler, realistisk omfang |
| **Etikk og databehandling** | 20% | Bevissthet om personvern og etiske problemstillinger, grunnleggende databehandlingsplan, FAIR-prinsipper |
| **Skrivekvalitet** | 10% | Tydelig struktur, passende bruk av referanser, lesbare figurer, godt språk |

> **Merknad**: Vi forventer ikke at du foreslår noe helt nytt eller har dyp teknisk ekspertise. Vi ser etter bevis på at du forstår feltet, kan beskrive en rimelig tilnærming og har tenkt nøye gjennom de etiske dimensjonene.

---

## Forberedelsesguide

### Gjør deg kjent med LaTeX og rapportmalen

Vi bruker den nettbaserte, samarbeidsbaserte LaTeX-editoren [Overleaf](https://www.overleaf.com) for å skrive rapporten.

**LaTeX-ressurser:**
- [Hva er LaTeX?](https://en.wikipedia.org/wiki/LaTeX)
- [Hvorfor bruke LaTeX til vitenskapelig skriving?](https://mildopinions.wordpress.com/2008/07/07/why-i-use-latex-in-biology)
- [Beste praksis for LaTeX](https://www.tug.org/pracjourn/2007-4/senthil/senthil.pdf)
- [Maler for akademiske tidsskrifter](https://www.overleaf.com/latex/templates/tagged/academic-journal)

**Prosjektmal:**
- LaTeX-kilde: [[ELMED219_BMED365_2026_project_team_k.tex](./latex-template/ELMED219_BMED365_2026_project_team_k.tex)]
- Eksempelfigur: [[elmed219_bmed365_dummy_fig.png](./latex-template/elmed219_bmed365_dummy_fig.png)]
- Kompilert PDF: [[ELMED219_BMED365_2026_project_team_k.pdf](./latex-template/ELMED219_BMED365_2026_project_team_k.pdf)]

**Eksempel på forventet detaljnivå:**
- Seili Summer School 2019 prosjektrapport (Prostatakreft-tema):
  - Overleaf-prosjekt: [[vis](https://www.overleaf.com/read/xwjxwcnpzhqv)]
  - Kildefiler: [[main.tex](./latex-template/Seili_2020_example/main.tex)], [[Fig1](./latex-template/Seili_2020_example/Fig1_The_process_of_autoEncoder.png)], [[Fig2](./latex-template/Seili_2020_example/Fig2_Overview_of_the_process.png)]
  - Kompilert PDF: [[Seili_2020_project_template.pdf](./latex-template/Seili_2020_example/Seili_2020_project_template.pdf)]

---

## Informasjonskilder

### Bakgrunnskunnskap

#### Hjernebiologi og patologi
- Coursera: [Medical Neuroscience](https://www.coursera.org/learn/neurobiology), spesielt forelesningen om [hjernesvulster](https://www.coursera.org/lecture/neurobiology/brain-tumors-fUcn4)
- The Human Protein Atlas: [Brain Atlas](https://www.proteinatlas.org/humanproteome/brain)

#### WHOs klassifisering av CNS-svulster

> **Viktig:** WHO 2021-klassifiseringen introduserer betydelige endringer. Diagnosen «Glioblastom, IDH-villtype» *krever* nå molekylær analyse for å bekrefte IDH-villtype-status.

- Louis DN et al. **The 2021 WHO Classification of Tumors of the Central Nervous System: a summary.** Neuro-Oncology 2021;23(8):1231-1251. [[lenke](https://academic.oup.com/neuro-oncology/article/23/8/1231/6311214)]

- Louis DN et al. The 2016 World Health Organization Classification of Tumors of the Central Nervous System: A Summary. Acta Neuropathol 2016;131(6):803-820. [[lenke](https://link.springer.com/article/10.1007/s00401-016-1545-1)]

- Aldape K et al. Challenges to curing primary brain tumors. Nat Rev Clin Oncol 2019;16:509-520. [[lenke](https://www.nature.com/articles/s41571-019-0177-5)]

---

### Hjernesvulster og nevroavbildning

#### Oversiktsartikler

- Abd-Ellah MK et al. A review on brain tumor diagnosis from MRI images: Practical implications, key achievements, and lessons learned. Magnetic Resonance Imaging 2019;61:300-318. [[lenke](https://www.sciencedirect.com/science/article/pii/S0730725X18304302)]

- Stable O et al. Brain tumor segmentation and classification from magnetic resonance images: Review of selected methods from 2014 to 2019. Pattern Recognition Letters 2020;131:244-260. [[lenke](https://www.sciencedirect.com/science/article/pii/S016786551930340X)]

- Nadeem MW et al. Brain Tumor Analysis Empowered with Deep Learning: A Review, Taxonomy, and Future Challenges. Brain Sci 2020;10(2):118. [[lenke](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7071415)]

- Lohmann P et al. PET/MRI Radiomics in Patients With Brain Metastases. Front. Neurol. 2020. [[lenke](https://www.frontiersin.org/articles/10.3389/fneur.2020.00001/full)]

#### BraTS-utfordringen (Brain Tumor Segmentation)

**BraTS-utfordringen** er en årlig internasjonal konkurranse med fokus på segmentering av hjernesvulster fra MR. Siden 2023 er den organisert via Synapse-plattformen og har utvidet seg til å inkludere flere delutfordringer.

- **BraTS 2024 Challenge**: [[synapse.org/brats](https://www.synapse.org/brats)]
  - Delutfordringer inkluderer: Adult Glioma (GLI), Post-treatment Glioma, Meningioma (MEN), Brain Metastases (MET), Pediatric Tumors (PED), Sub-Saharan Africa (SSA)

- Menze BH et al. The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS). IEEE Trans Med Imaging 2015;34(10):1993-2024. [[lenke](https://ieeexplore.ieee.org/document/6975210)]

- Bakas S et al. Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features. Scientific Data 2017;4:170117. [[lenke](https://www.nature.com/articles/sdata2017117)]

- Correia de Verdier M et al. **The 2024 Brain Tumor Segmentation (BraTS) Challenge: Glioma Segmentation on Post-treatment MRI.** arXiv 2024. [[lenke](https://arxiv.org/abs/2405.18368)]
  - *2024-utfordringen introduserte post-behandlings gliom-segmentering, inkludert reseksjonskaviteten som en ny region.*

---

### Kunstig intelligens i nevro-onkologi

#### Grunnleggende artikler

- Lundervold AS, Lundervold A. **An overview of deep learning in medical imaging focusing on MRI.** Zeitschrift für Medizinische Physik 2019;29(2):102-127. [[lenke](https://www.sciencedirect.com/science/article/pii/S0939388918301181)]

- Rudie JD et al. **Emerging Applications of Artificial Intelligence in Neuro-Oncology.** Radiology 2019;290(3):607-618. [[lenke](https://pubs.rsna.org/doi/10.1148/radiol.2019181928)]

#### Kliniske applikasjoner

- Hollon TC et al. Near Real-Time Intraoperative Brain Tumor Diagnosis Using Stimulated Raman Histology and Deep Neural Networks. Nature Medicine 2020;26(1):52-58. [[lenke](https://www.nature.com/articles/s41591-019-0715-9)] [[GitHub](https://github.com/toddhollon/srh_cnn)]

- Yogananda CGB et al. A novel fully automated MRI-based deep-learning method for classification of IDH mutation status in brain gliomas. Neuro-Oncology 2020;22(3):402-411. [[lenke](https://academic.oup.com/neuro-oncology/article/22/3/402/5584591)]

- Kickingereder P et al. Automated quantitative tumour response assessment of MRI in neuro-oncology with artificial neural networks. The Lancet Oncology 2019;20(5):728-740. [[lenke](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(19)30098-1/fulltext)]

#### Nyere fremskritt (2022-2025)

- Pati S et al. **Federated learning enables big data for rare cancer boundary detection.** Nature Communications 2022;13:7346. [[lenke](https://www.nature.com/articles/s41467-022-33407-5)]
  - *Beskriver FeTS (Federated Tumor Segmentation)-initiativet som muliggjør multiinstitusjonelt samarbeid uten å dele sensitive pasientdata.*

- Kofler F et al. **BraTS Toolkit: Translating BraTS Brain Tumor Segmentation Algorithms Into Clinical and Scientific Practice.** Frontiers in Neuroscience 2020;14:125. [[lenke](https://www.frontiersin.org/articles/10.3389/fnins.2020.00125)]

- Ghadimi N et al. **Deep Learning-Based Techniques in Glioma Brain Tumor Segmentation Using Multi-Parametric MRI: A Review on Clinical Applications and Future Outlooks.** Journal of Magnetic Resonance Imaging 2025;61(1):52-69. [[lenke](https://onlinelibrary.wiley.com/doi/10.1002/jmri.29543)]
  - *Omfattende 2025-oversikt som dekker CNN-arkitekturer, oppmerksomhetsmekanismer og transformer-modeller for gliom-segmentering.*

- Booth TC et al. **A review of deep learning for brain tumor analysis in MRI.** npj Precision Oncology 2025;9:2. [[lenke](https://www.nature.com/articles/s41698-024-00789-2)]
  - *Nylig oversikt som utforsker dyplæringsapplikasjoner i tumorsegmentering, klassifisering og overlevelsespredik­sjon.*

- Karniadakis D et al. **A Review on Deep Learning Methods for Glioma Segmentation, Limitations, and Future Perspectives.** Cancers 2025. [[lenke](https://pmc.ncbi.nlm.nih.gov/articles/PMC12387613/)]
  - *Evaluerer over 80 state-of-the-art-modeller, sammenligner CNN-baserte, Transformer- og hybridarkitekturer.*

- Kim S et al. **Deep learning-driven brain tumor classification and segmentation using non-contrast MRI.** Scientific Reports 2025;15:26799. [[lenke](https://www.nature.com/articles/s41598-025-13591-2)]
  - *Demonstrerer høy nøyaktighet for tumorklassifisering og segmentering ved bruk av ikke-kontrast T1w og T2w MR.*

- Kabir T et al. **A Bayesian deep segmentation framework for glioblastoma tumor segmentation using follow-up MRIs.** Frontiers in Neuroimaging 2025. [[lenke](https://www.frontiersin.org/journals/neuroimaging/articles/10.3389/fnimg.2025.1630245/full)]
  - *Introduserer usikkerhetsestimering i dyplæring for mer pålitelig klinisk segmentering.*

- White NS et al. **Deep Learning Segmentation of Infiltrative and Enhancing Cellular Tumor at Pre- and Posttreatment Multishell Diffusion MRI of Glioblastoma.** Radiology 2024;312(3):e240424. [[lenke](https://pubmed.ncbi.nlm.nih.gov/39166970/)]
  - *Demonstrerer dyplæring for segmentering av cellulær tumor fra avansert diffusjons-MR, predikerer overlevelse.*

---

### Grunnlagsmodeller for medisinsk bildebehandling

En ny utvikling innen medisinsk bildeanalyse involverer **grunnlagsmodeller** (foundation models): store modeller forhåndstrent på diverse datasett som kan tilpasses spesifikke oppgaver. Disse er verdt å kjenne til, selv om detaljert forståelse ikke er påkrevd.

#### Segment Anything Model (SAM) og medisinske tilpasninger

- Ma J et al. **Segment Anything in Medical Images.** Nature Communications 2024;15:654. [[lenke](https://www.nature.com/articles/s41467-024-44824-z)] [[GitHub](https://github.com/bowang-lab/MedSAM)]
  - MedSAM: Finjustert på 1,5M+ medisinske bilde-maske-par på tvers av 10 modaliteter
  - Oppnår sterk ytelse på gliom-segmenteringsoppgaver

- Nguyen et al. **Necessity and impact of specialization of large foundation model for medical segmentation tasks.** Medical Physics 2025. [[lenke](https://aapm.onlinelibrary.wiley.com/doi/full/10.1002/mp.17470)]
  - *Viser at grunnlagsmodeller ofte trenger oppgavespesifikk finjustering for best klinisk ytelse.*

> **For din forskningsplan:** Du kan nevne grunnlagsmodeller som en fremvoksende tilnærming, men tradisjonelle metoder som U-Net eller nnU-Net er like gyldige valg. Fokuser på å beskrive din valgte tilnærming tydelig fremfor å bruke den mest avanserte metoden.

---

### Grafteori og pasientlikhetsnettverk

> **Merknad:** Dette er en *valgfri alternativ eller komplementær* tilnærming til dyplæringsmetoder. Team kan velge å inkorporere nettverksbasert analyse sammen med eller i stedet for tradisjonelle ML-tilnærminger.

#### Konsept og motivasjon

Pasientlikhetsnettverk (PSN) representerer pasienter som noder i en graf, med kanter som forbinder pasienter som er like basert på kliniske, bilde- eller molekylære egenskaper. Denne tilnærmingen muliggjør:
- **Pasientstratifisering**: Oppdage naturlige undergrupper (f.eks. glioblastom-subtyper med ulik prognose)
- **Presisjonsmedisin**: Identifisere lignende pasienter for å informere behandlingsbeslutninger
- **Multimodal integrasjon**: Kombinere bildeegenskaper, molekylære markører og kliniske variabler i et enhetlig rammeverk

#### Grunnleggende artikler

- Pai S, Bader GD. **Patient Similarity Networks for Precision Medicine.** Journal of Molecular Biology 2018;430(18):2924-2938. [[lenke](https://www.sciencedirect.com/science/article/pii/S0022283618308489)]
  - *Omfattende oversikt over PSN-metoder, likhetsmetrikker og applikasjoner i presisjonsmedisin.*

- Ruan P et al. **Using Association Signal Annotations to Boost Similarity Network Fusion.** Bioinformatics 2019;35(19):3718-3726. [[lenke](https://academic.oup.com/bioinformatics/article/35/19/3718/5368011)]

- Wang B et al. **Similarity network fusion for aggregating data types on a genomic scale.** Nature Methods 2014;11:333-337. [[lenke](https://www.nature.com/articles/nmeth.2810)]
  - *Grunnleggende metode for å kombinere flere datatyper ved bruk av pasientlikhetsnettverk.*

#### Applikasjoner i nevro-onkologi og klinisk forskning

- Lundervold A et al. **Brain Structure, Cognition, and Fatigue in IBS Assessed Through a Patient Similarity Network.** Diagnostics 2025;15(4):470. [[lenke](https://doi.org/10.3390/diagnostics15040470)]
  - *Eksempel på PSN-metodologi anvendt på nevroavbildning og kognitive data.*

- Forskningsgrupper har anvendt PSN til:
  - Stratifisering av gliompasienter basert på radiomiske egenskaper
  - Identifisering av molekylære subtyper fra multimodale data
  - Prediksjon av behandlingsrespons i hjernesvulstkohorter

#### Kursressurser

Se [Lab 1: Nettverksvitenskap og pasientlikhetsnettverk](../Lab1-NetworkSci-PSN/) for praktiske eksempler inkludert:
- Introduksjon til grafteori og nettverksvitenskap
- Bygging av PSN fra kliniske data
- Fellesskapsdeteksjon for pasientstratifisering

> **For din forskningsplan:** Du kan foreslå en PSN-basert tilnærming for pasientstratifisering, enten som hovedmetode eller som en komplementær analyse til dyplæringssegmentering. Vurder hvordan nettverksbasert analyse kan hjelpe med å identifisere glioblastom-subtyper eller predikere utfall basert på multimodal pasientlikhet.

---

### Programvare og verktøy

Selv om du ikke skal kjøre kode selv, er det nyttig å vite hvilke verktøy som finnes slik at du kan beskrive realistiske metoder i din forskningsplan.

#### Dyplæringsrammeverk for medisinsk bildebehandling

| Verktøy | Beskrivelse | Lenke |
|---------|-------------|-------|
| **nnU-Net** | Selvkonfigurerende segmenteringsmetode; vinner ofte BraTS-utfordringer | [[GitHub](https://github.com/MIC-DKFZ/nnUNet)] |
| **MONAI** | PyTorch-basert rammeverk for medisinsk bildeanalyse | [[monai.io](https://monai.io/)] |
| **MedSAM** | Grunnlagsmodell for medisinsk bildesegmentering | [[GitHub](https://github.com/bowang-lab/MedSAM)] |
| **3DUnetCNN** | 3D U-Net-implementering med BraTS-veiledning | [[GitHub](https://github.com/ellisdg/3DUnetCNN)] |
| **DeepNeuro** | Åpen kildekode dyplæringsverktøykasse for nevroavbildning | [[GitHub](https://github.com/QTIM-Lab/DeepNeuro)] |
| **NetworkX** | Python-bibliotek for nettverks-/grafanalyse og pasientlikhetsnettverk | [[networkx.org](https://networkx.org/)] |
| **SNFtool** | R-pakke for Similarity Network Fusion | [[CRAN](https://cran.r-project.org/package=SNFtool)] |

#### Fellesskapsressurser

- **Papers With Code**: Brain Tumor Segmentation [[paperswithcode.com](https://paperswithcode.com/task/brain-tumor-segmentation)]
- **BraTS Toolkit**: Verktøy for å anvende BraTS-algoritmer [[GitHub](https://github.com/neuronflow/BraTS-Toolkit)]

#### Forhåndstrente modeller

- 3DUnetCNN forhåndstrente modeller for BraTS: [[Zenodo](https://zenodo.org/record/4289225)]

![Illustrasjon av hjernesvulstsegmentering](https://github.com/ellisdg/3DUnetCNN/raw/master/legacy/doc/tumor_segmentation_illusatration.gif)
*Eksempel på hjernesvulstsegmentering fra 3DUnetCNN BraTS-veiledningen*

---

### Datasamlinger

| Datasett | Beskrivelse | Lenke |
|----------|-------------|-------|
| **BraTS Challenge Data** | Multimodal MR med ekspertsegmenteringer | [[synapse.org/brats](https://www.synapse.org/brats)] |
| **TCGA-GBM** | The Cancer Genome Atlas Glioblastoma-samling | [[TCIA](https://wiki.cancerimagingarchive.net/display/Public/TCGA-GBM)] |
| **UCSF-PDGM** | Preoperativ diffust gliom MR (500 pasienter) | [[TCIA](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=119705830)] |
| **The Cancer Imaging Archive** | Generelt repositorium for kreftbildedata | [[cancerimagingarchive.net](https://www.cancerimagingarchive.net/)] |

**Referanse for UCSF-PDGM:**
- Calabrese E et al. The University of California San Francisco Preoperative Diffuse Glioma MRI Dataset. Radiology: Artificial Intelligence 2022;4(6):e220058. [[lenke](https://pubs.rsna.org/doi/10.1148/ryai.220058)]

---

### Etikk i AI og helsevesen

#### Generelle ressurser

- Morley J et al. **The ethics of AI in health care: A mapping review.** Social Science & Medicine 2020;260:113172. [[lenke](https://www.sciencedirect.com/science/article/pii/S0277953620303919)]

- Vollmer S et al. **Machine learning and artificial intelligence research for patient benefit: 20 critical questions on transparency, replicability, ethics, and effectiveness.** BMJ 2020;368:l6927. [[lenke](https://www.bmj.com/content/368/bmj.l6927)]

- Rigby MJ. **Ethical Dimensions of Using Artificial Intelligence in Health Care.** AMA Journal of Ethics 2019. [[lenke](https://journalofethics.ama-assn.org/article/ethical-dimensions-using-artificial-intelligence-health-care/2019-02)]

- Stanford Encyclopedia of Philosophy: **Ethics of Artificial Intelligence and Robotics** [[lenke](https://plato.stanford.edu/entries/ethics-ai)]

#### Rettferdighet og skjevhet i medisinsk AI

- Gichoya JW et al. **AI recognition of patient race in medical imaging: a modelling study.** Lancet Digital Health 2022;4(6):e406-e414. [[lenke](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(22)00063-2/fulltext)]
  - *Demonstrerer at AI-modeller kan kode demografisk informasjon fra medisinske bilder, noe som reiser rettferdighetshensyn.*

- Chen RJ et al. **Algorithm fairness in artificial intelligence for medicine and healthcare.** Nature Biomedical Engineering 2023;7:719-742. [[lenke](https://pmc.ncbi.nlm.nih.gov/articles/PMC10632090/)]
  - *Gjennomgår rettferdighetsproblemer og avbøtningsstrategier i helsevesenets AI.*

- Park SH et al. **Fairness of artificial intelligence in healthcare: review and recommendations.** Japanese Journal of Radiology 2024;42:3-15. [[lenke](https://pmc.ncbi.nlm.nih.gov/articles/PMC10764412/)]
  - *Introduserer FAIR (Fairness of AI Recommendations)-erklæringen for beste praksis.*

- Defined N et al. **Bias in artificial intelligence for medical imaging: fundamentals, detection, avoidance, mitigation, challenges, ethics, and prospects.** Diagnostic and Interventional Radiology 2025;31(2):101-117. [[lenke](https://pmc.ncbi.nlm.nih.gov/articles/PMC11880872/)]
  - *Omfattende 2025-oversikt som dekker skjevhetsdeteksjon, avbøtningsstrategier og etiske prinsipper.*

- Ali S et al. **Ethical framework for responsible foundational models in medical imaging.** Frontiers in Radiology 2025. [[lenke](https://pmc.ncbi.nlm.nih.gov/articles/PMC12128638/)]
  - *Foreslår etisk rammeverk som integrerer personvern, rettferdighet og forklarbarhet for AI i medisinsk bildebehandling.*

#### Regulatorisk rammeverk

- **EU AI Act** (2024): Verdens første omfattende AI-regulering. Medisinsk AI klassifiseres typisk som «høyrisiko».
  - EU AI Act-oversikt: [[digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)]

- **Ethics of AI in Radiology**: European and North American Multisociety Statement 2019 [[pdf](https://www.acr.org/-/media/ACR/Files/Informatics/Ethics-of-AI-in-Radiology-European-and-North-American-Multisociety-Statement--6-13-2019.pdf)]

---

### Planlegging av databehandling

#### FAIR-prinsipper

Din databehandlingsplan bør adressere hvordan prosjektet ditt ville sikre at data og kode er:
- **F**innbare (Findable): vedvarende identifikatorer, beskrivende metadata
- **T**ilgjengelige (Accessible): klare tilgangsprotokoller, dokumentasjon
- **I**nteroperable: standardformater (NIfTI, DICOM), felles terminologi
- **G**jenbrukbare (Reusable): klare lisenser, proveniensdokumentasjon

**Ressurser:**
- FAIR-prinsipper: [[go-fair.org](https://www.go-fair.org/fair-principles/)]
- Science Europe: Practical Guide to Research Data Management [[lenke](https://scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/)]

#### Foreslåtte repositorier

| Type | Repositorium | Bruksområde |
|------|--------------|-------------|
| Kode | GitHub/GitLab | Versjonskontroll, samarbeid |
| Modeller | Zenodo, Hugging Face | Trente modellvekter med DOI |
| Data | TCIA, Synapse | Deling av medisinsk bildedata |
| Preprints | arXiv, medRxiv | Rask formidling |

---

### AI-verktøy for skriving

Disse verktøyene kan hjelpe med litteratursøk, skriving og forståelse av komplekse konsepter:

| Verktøy | Bruksområde | Lenke |
|---------|-------------|-------|
| **Claude** | Tekstanalyse, akademisk skriving, forklaring av konsepter | [claude.ai](https://claude.ai) |
| **ChatGPT** | Generell AI-assistent, idémyldring | [chat.openai.com](https://chat.openai.com) |
| **NotebookLM** | Dokumentanalyse og syntese | [notebooklm.google.com](https://notebooklm.google.com) |
| **Elicit** | AI-drevet litteratursøk | [elicit.com](https://elicit.com) |
| **Connected Papers** | Visualisering av sitasjonsnettverk | [connectedpapers.com](https://www.connectedpapers.com) |
| **Semantic Scholar** | Akademisk søk med AI-funksjoner | [semanticscholar.org](https://www.semanticscholar.org) |

> **Merknad:** Verifiser alltid AI-generert innhold mot primærkilder. Bruk disse verktøyene til å hjelpe arbeidet ditt, ikke til å erstatte kritisk tenkning.

---

## Teamsjekkliste

Før dere starter, sørg for at alle på teamet har fullført disse oppgavene:

### Individuell forberedelse
- [ ] Opprettet en gratis [Overleaf](https://www.overleaf.com)-konto (helst med din Mitt-UiB innloggings-ID)
- [ ] Tilgang til LaTeX-malen og forstått dens struktur
- [ ] Lest minst én bakgrunnsartikkel om glioblastom og dets bildebehandling
- [ ] Gjort deg kjent med WHO 2021-klassifiseringen av CNS-svulster
- [ ] Utforsket relevante datasett (BraTS, TCGA-GBM) for å forstå tilgjengelige data
- [ ] Sett på minst ett programvareverktøy eller rammeverk (nnU-Net, MONAI, MedSAM)

### Teamorganisering
- [ ] Etablert en kommunikasjonskanal ([Discord](https://support.discord.com)-kanal _Team k_ - med din Mitt-UiB innloggings-ID som brukernavn)
- [ ] Tildelt roller og ansvarsområder for ulike seksjoner
- [ ] Opprettet et delt Overleaf-prosjekt fra malen
- [ ] Satt opp en tidslinje med milepæler og interne frister
- [ ] Blitt enige om hvordan referanser skal håndteres (BibTeX-fil)

### Før innlevering
- [ ] Alle teammedlemmer har gjennomgått det komplette dokumentet
- [ ] Referanser er komplette og riktig formatert
- [ ] Figurer er tydelige og har passende bildetekster
- [ ] Dokumentet kompilerer uten feil
- [ ] Sidebegrensningene er respektert (3 til 5 sider forskningsplan + 1,5 til 2,5 sider DMP/etikk)

### Innleveringsfrist
- [ ] Torsdag 29.01.2026, 16:00 - Ett medlem leverer teamrapporten (som PDF-fil) til Mitt-UiB på vegne av teamet

---

## Ofte stilte spørsmål

**Sp: Må vi skrive kode eller analysere data?**

Sv: Nei. Dette er en forskningsplan som beskriver hva du *ville* gjort. Fokuser på metodologi og resonnement, ikke implementering.

**Sp: Hvor teknisk bør metodeseksjonen være?**

Sv: Teknisk nok til å vise at du forstår de generelle tilnærmingene, men tilgjengelig for teamkameratene dine med ulik bakgrunn. Forklar *hvorfor* du velger spesifikke metoder, ikke bare *hva* de er.

**Sp: Jeg er medisinstudent med begrenset teknisk bakgrunn. Hvordan kan jeg bidra?**

Sv: Din kliniske kunnskap er essensiell. Du kan bidra til bakgrunnsseksjonen (klinisk relevans, pasientperspektiv), hjelpe til med å sikre at den foreslåtte tilnærmingen gir klinisk mening, og lede etikkdiskusjonen. Den tverrfaglige naturen til teamene betyr at alle har noe verdifullt å tilby.

**Sp: Jeg er BMED365-student som nettopp fullførte bachelorgraden min. Er dette prosjektet for avansert?**

Sv: Prosjektet er designet for å være tilgjengelig. Du forventes ikke å ha tidligere ekspertise innen hjernesvulstbildebehandling eller dyplæring. Bruk de tilgjengelige ressursene til å lære, og husk at å beskrive metoder tydelig er viktigere enn å foreslå den mest avanserte tilnærmingen.

**Sp: Kan vi foreslå å bruke metoder vi ikke har lært i undervisningen?**

Sv: Ja, så lenge du kan forklare dem tilstrekkelig og begrunne hvorfor de er passende. Litteraturgjennomgangen er en del av læringsprosessen.

**Sp: Hvor mange referanser bør vi inkludere?**

Sv: Kvalitet over kvantitet. Typisk demonstrerer 15 til 25 velvalgte referanser god faglighet uten unødvendig fylde.

**Sp: Bør vi fokusere på ett spesifikt aspekt eller dekke alt bredt?**

Sv: Finn en balanse. Du trenger bredde for å vise forståelse av den overordnede arbeidsflyten, men du kan gå dypere på ett eller to aspekter som interesserer teamet ditt.

**Sp: Kan vi bruke grafteori og pasientlikhetsnettverk i stedet for dyplæring?**

Sv: Ja. Du kan foreslå en PSN-basert tilnærming for pasientstratifisering, eller kombinere nettverksanalyse med bildemetoder. For eksempel kan du trekke ut radiomiske egenskaper fra segmenterte svulster, deretter bruke PSN for å identifisere pasientundergrupper med ulik prognose. Se [Lab 1](../Lab1-NetworkSci-PSN/) for praktiske eksempler og bakgrunnsmateriale.

**Sp: Hvordan fordeler vi arbeidet i et tverrfaglig team?**

Sv: Vurder å fordele etter ekspertise: medisinstudenter kan lede på klinisk bakgrunn og etikk, mens tekniske studenter leder på metoder. Imidlertid bør alle bidra til alle seksjoner. Sluttproduktet bør være sammenhengende, ikke en samling av separate deler.

---

## Kontakt og støtte

- Kursrepositorium: [https://github.com/arvidl/ELMED219-2026](https://github.com/arvidl/ELMED219-2026)<br>
og [https://github.com/arvidl/BMED365-2026](https://github.com/arvidl/BMED365-2026)
- For tekniske spørsmål om LaTeX/Overleaf, se [Overleaf-dokumentasjonen](https://www.overleaf.com/learn)
- For spørsmål om prosjektet, kontakt kursansvarlige

---

_Sist oppdatert: Januar 2026_

---

<details>
<summary><b>Versjonshistorikk</b></summary>

| Dato | Endringer |
|------|-----------|
| Januar 2026 | Lagt til grafteori og pasientlikhetsnettverk (PSN) som valgfri metodologisk tilnærming; lagt til ny PSN-seksjon med grunnleggende artikler og kursressurser; oppdatert programvareverktøy med NetworkX og SNFtool; lagt til FAQ-innlegg for PSN-baserte tilnærminger |
| Januar 2026 | Lagt til teamorganisering for 28 studenter i 5 team; oppdaterte referanser til å inkludere 2025-publikasjoner; justerte læringsmål og vurderingskriterier for blandet studentpublikum; utvidet veiledning for studenter med ulik bakgrunn; fjernet M-bindestreker |
| Desember 2024 | Første versjon |

</details>
