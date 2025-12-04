# Teamprosjekt &nbsp;&nbsp;&nbsp; <span style="font-size: 16px;">[ELMED219 / BMED365]</span>
## _Presisjonsmedisin og kvantitativ avbildning ved glioblastom_

> **Merk:** Dette er et felles prosjekt mellom ELMED219 og BMED365. Siden BMED365-2026 gjennomføres på engelsk, skal selve **prosjektrapporten skrives på engelsk** (se [LaTeX-malen](./latex-template/)). Denne README-filen gir informasjon om prosjektet på norsk for ELMED219-studentene.

---

## Beskrivelse

Forestill deg at du er del av en gruppe etablerte, suksessrike forskere som skal samarbeide om en viktig biomedisinsk og medisinsk utfordring. Det er utlyst en åpen søknadsrunde for forskningsprosjekter under et nytt paraplyprogram med tittelen «Kunstig intelligens og beregningsorientert (bio)medisin». Din tverrfaglige gruppe sikter mot et prosjekt om «Presisjonsmedisin og kvantitativ avbildning ved glioblastom – en multiskala-tilnærming».

> **Viktig:** Oppgaven går ut på å **skrive en forskningsplan** (en søknadsskisse) for et tenkt prosjekt – **ikke** å faktisk gjennomføre prosjektet med dataanalyse eller koding. Dere skal beskrive *hva* dere ville gjort, *hvordan* og *hvorfor*, men ikke utføre selve analysen.

Fokuset for oppgaven er:

1. Beskrivelse av relevante bildeteknologier og modaliteter – muligens på ulike skalaer
2. Forslag til bildeavledede biomarkører for glioblastom
3. Maskinlæringsteknikker for segmentering, klassifisering, behandlingsstratifisering og prediksjon
4. Nyhetsverdien og forventet effekt av tilnærmingen din
5. Evaluering av etikken i prosjektet ditt, sammen med en datahåndteringsplan (og ikke så mye den grunnleggende vitenskapen om hjernesvulster i seg selv)


## Organisering av rapporten

### Forskningsplan
(3-5 sider inkl. figurer og referanseliste)
- En kort bakgrunn til feltet
- Mål og forventet effekt
- Materiale og metoder
- Evaluering

### Datahåndteringsplan og etiske betraktninger
(1½-2½ sider inkl. grafikk / lenker)
- Beskrivelse av innsamlede/genererte data og kode
- Deling av data og kode
- Etiske betraktninger

---

## *Forbered deg og din datamaskin for teamprosjektet*

### *Sett deg inn i materialet for gruppeprosjektet og hvordan du bruker [LaTeX](https://www.latex-project.org) for å skrive rapporten*

- Vi bruker den nettbaserte, samarbeidsorienterte LaTeX-editoren [Overleaf](https://www.overleaf.com) (for mer informasjon om LaTeX, se [her](https://en.wikipedia.org/wiki/LaTeX), [her](https://www.tug.org/pracjourn/2007-4/senthil/senthil.pdf) og [her](https://mildopinions.wordpress.com/2008/07/07/why-i-use-latex-in-biology), og for LaTeX-maler, se f.eks. [her](https://www.overleaf.com/latex/templates/template-for-submissions-to-molecular-systems-biology/kyxgttpbzhht) og [her](https://www.overleaf.com/latex/templates/tagged/academic-journal))

- **LaTeX-mal for rapporten** finnes [[her](./latex-template/ELMED219_2026_project_team_k.tex)] med en eksempelfigur [[her](./latex-template/elmed219_dummy_fig.png)], som resulterer i følgende eksempelrapport [[pdf](./latex-template/ELMED219_2026_project_team_k.pdf)].

- **Forventet detaljnivå** illustreres med en [prosjektrapport](https://www.overleaf.com/read/xwjxwcnpzhqv) fra sommerskolen på Seili i 2019 (der *Prostatakreft* var temaet). Den finnes på Overleaf [[her](https://www.overleaf.com/project/5ec71af71aca320001385354)] og i dette repoet som [[main.tex](./latex-template/Seili_2020_example/main.tex)], [[fig1](./latex-template/Seili_2020_example/Fig1_The_process_of_autoEncoder.png)], [[fig2](./latex-template/Seili_2020_example/Fig2_Overview_of_the_process.png)], som gir [[pdf](./latex-template/Seili_2020_example/Seili_2020_project_template.pdf)].


---

## Informasjonskilder (hjernesvulster – nevroavbildning – KI – programvare og data)

### Forkunnskaper og bakgrunnslesning

- For de av dere som har begrenset kunnskap om biologi og patologi i hjernen eller ønsker å friske opp kunnskapen, anbefaler vi det gratis Coursera-kurset [https://www.coursera.org/learn/neurobiology](https://www.coursera.org/learn/neurobiology), spesielt forelesningen om [hjernesvulster](https://www.coursera.org/lecture/neurobiology/brain-tumors-fUcn4).

- The Brain Atlas: [https://www.proteinatlas.org/humanproteome/brain](https://www.proteinatlas.org/humanproteome/brain)

#### WHO-klassifikasjon av CNS-svulster (oppdatert 2021)

- Louis DN et al. **The 2021 WHO Classification of Tumors of the Central Nervous System: a summary.** Neuro-Oncology 2021;23(8):1231-1251. [[lenke](https://academic.oup.com/neuro-oncology/article/23/8/1231/6311214)]
  - *Merk: WHO 2021-klassifikasjonen innfører viktige endringer, inkludert at diagnosen «Glioblastom, IDH-villtype» nå krever IDH-mutasjonsanalyse.*

- Louis DN et al. The 2016 World Health Organization Classification of Tumors of the Central Nervous System: A Summary. Acta Neuropathol 2016;131(6):803-820. [[lenke](https://link.springer.com/article/10.1007/s00401-016-1545-1)]

- Aldape K et al. Challenges to curing primary brain tumors. Nat Rev Clin Oncol 2019;16:509-520. [[lenke](https://www.nature.com/articles/s41571-019-0177-5)]

---

### Hjernesvulster og nevroavbildning (noen pekere)

- Abd-Ellah MK et al. A review on brain tumor diagnosis from MRI images: Practical implications, key achievements, and lessons learned. Magnetic Resonance Imaging 2019;61:300-318. [[lenke](https://www.sciencedirect.com/science/article/pii/S0730725X18304302)]

- Hamid MAA, Khan NA. Investigation and Classification of MRI Brain Tumors Using Feature Extraction Technique. Journal of Medical and Biological Engineering 2020;40:307–317. [[lenke](https://link.springer.com/article/10.1007/s40846-020-00510-1)]

- Lohmann P et al. PET/MRI Radiomics in Patients With Brain Metastases. Front. Neurol., 07 February 2020. [[lenke](https://www.frontiersin.org/articles/10.3389/fneur.2020.00001/full)]

- Tiwari A et al. Brain tumor segmentation and classification from magnetic resonance images: Review of selected methods from 2014 to 2019. Pattern Recognition Letters 2020;131:244-260. [[lenke](https://www.sciencedirect.com/science/article/pii/S016786551930340X)]

- Nadeem MW et al. Brain Tumor Analysis Empowered with Deep Learning: A Review, Taxonomy, and Future Challenges. Brain Sci 2020;10(2):118. [[lenke](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7071415)]

#### BraTS Challenge (Brain Tumor Segmentation)

- **BraTS Challenge** er en årlig internasjonal konkurranse som fokuserer på segmentering av hjernesvulster fra MR-bilder. Fra 2023 arrangeres konkurransen via Synapse-plattformen.

- BraTS 2023/2024 Challenge: [[synapse.org/brats](https://www.synapse.org/brats)]

- Menze BH et al. The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS). IEEE Trans Med Imaging 2015;34(10):1993-2024. [[lenke](https://ieeexplore.ieee.org/document/6975210)]

- Bakas S et al. Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features. Scientific Data 2017;4:170117. [[lenke](https://www.nature.com/articles/sdata2017117)]

---

### Hjernesvulster og kunstig intelligens (noen pekere)

- NCI: Artificial Intelligence Expedites Brain Tumor Diagnosis during Surgery. 2020 Feb 12. [[lenke](https://www.cancer.gov/news-events/cancer-currents-blog/2020/artificial-intelligence-brain-tumor-diagnosis-surgery)]

- Hollon TC et al. Near Real-Time Intraoperative Brain Tumor Diagnosis Using Stimulated Raman Histology and Deep Neural Networks. Nature Medicine 2020;26(1):52-58. [[lenke](https://www.nature.com/articles/s41591-019-0715-9)] [[GitHub](https://github.com/toddhollon/srh_cnn)] [[video](https://labblog.uofmhealth.org/health-tech/artificial-intelligence-improves-brain-tumor-diagnosis)]

- Yogananda CGB et al. A novel fully automated MRI-based deep-learning method for classification of IDH mutation status in brain gliomas. Neuro-Oncology 2020;22(3):402–411. [[lenke](https://academic.oup.com/neuro-oncology/article/22/3/402/5584591)]

- Kickinereer P et al. Automated quantitative tumour response assessment of MRI in neuro-oncology with artificial neural networks: a multicentre, retrospective study. The Lancet Oncology 2019;20(5):728-740. [[lenke](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(19)30098-1/fulltext)]

- Eitel F et al. Patch individual filter layers in CNNs to harness the spatial homogeneity of neuroimaging data. Scientific Reports 2021;11:24447. [[lenke](https://www.nature.com/articles/s41598-021-03785-9)]

#### Nyere AI-artikler om hjernesvulster (2022-2024)

- Rudie JD et al. **Emerging Applications of Artificial Intelligence in Neuro-Oncology.** Radiology 2019;290(3):607-618. [[lenke](https://pubs.rsna.org/doi/10.1148/radiol.2019181928)]

- Pati S et al. **Federated learning enables big data for rare cancer boundary detection.** Nature Communications 2022;13:7346. [[lenke](https://www.nature.com/articles/s41467-022-33407-5)]
  - *Beskriver FeTS (Federated Tumor Segmentation) initiativet som muliggjør samarbeid mellom institusjoner uten å dele sensitive pasientdata.*

- Kofler F et al. **BraTS Toolkit: Translating BraTS Brain Tumor Segmentation Algorithms Into Clinical and Scientific Practice.** Frontiers in Neuroscience 2020;14:125. [[lenke](https://www.frontiersin.org/articles/10.3389/fnins.2020.00125)]

---

### Programvare og data (ressurser å beskrive i forskningsplanen)

Selv om dere ikke skal kjøre kode eller analysere data selv, er det viktig å kjenne til hvilke verktøy og datasett som finnes – slik at dere kan beskrive dem realistisk i forskningsplanen.

#### Papers With Code og GitHub-ressurser

- Brain Tumor Segmentation | Papers With Code: [[paperswithcode.com/task/brain-tumor-segmentation](https://paperswithcode.com/task/brain-tumor-segmentation)]

- Akshay Kumaar M. Brain Tumor Classification (using ResNet50 and Google Colab): [[GitHub](https://github.com/aksh-ai/brain_tumor_classification)]

- Joohyun Lee. BraTs (Brain Tumor Segmentation): [[GitHub](https://github.com/cv-lee/BraTs)]

- Ellis DG. **3DUnetCNN**: [[GitHub](https://github.com/ellisdg/3DUnetCNN)]
  - Inkluderer BraTS tutorial og pretrenerte modeller
  - Pretrained models: [[zenodo](https://zenodo.org/record/4289225)]

#### Datasamlinger

- **TCGA-GBM**: The Cancer Genome Atlas Glioblastoma Multiforme Collection [[lenke](https://wiki.cancerimagingarchive.net/display/Public/TCGA-GBM)]

- **UCSF-PDGM**: University of California San Francisco Preoperative Diffuse Glioma MRI [[lenke](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=119705830)]
  - Calabrese E et al. The University of California San Francisco Preoperative Diffuse Glioma MRI Dataset. Radiology: Artificial Intelligence 2022;4(6):e220058. [[lenke](https://pubs.rsna.org/doi/10.1148/ryai.220058)]

- **The Cancer Imaging Archive (TCIA)**: [[cancerimagingarchive.net](https://www.cancerimagingarchive.net/)]

#### Verktøy for medisinsk bildebehandling

- **DeepNeuro**: An open-source deep learning toolbox for neuroimaging [[GitHub](https://github.com/QTIM-Lab/DeepNeuro)]
  - Beers A et al. DeepNeuro: an open-source deep learning toolbox for neuroimaging. Neuroinformatics 2020. [[lenke](https://link.springer.com/article/10.1007/s12021-020-09477-5)]

- **MONAI**: Medical Open Network for Artificial Intelligence [[monai.io](https://monai.io/)]
  - Moderne PyTorch-basert rammeverk for medisinsk bildeanalyse

- **nnU-Net**: Self-configuring Method for Deep Learning-based Biomedical Image Segmentation [[GitHub](https://github.com/MIC-DKFZ/nnUNet)]
  - State-of-the-art segmenteringsmetode som ofte brukes i BraTS-utfordringen

#### Oversiktsartikkel

- Lundervold AS, Lundervold A. **An overview of deep learning in medical imaging focusing on MRI.** Zeitschrift für Medizinische Physik 2019;29(2):102-127. [[lenke](https://www.sciencedirect.com/science/article/pii/S0939388918301181)]


David G. Ellis [BraTS 2020 Tutorial](https://github.com/ellisdg/3DUnetCNN/tree/master/examples/brats2020) med [3DUNetCNN](https://github.com/ellisdg/3DUnetCNN):

![Brain Tumor Segmentation (BraTS) Tutorial](https://github.com/ellisdg/3DUnetCNN/raw/master/legacy/doc/tumor_segmentation_illusatration.gif)

---

### Etikk innen kunstig intelligens og maskinlæring (noen pekere)

- Wikipedia: Ethics of artificial intelligence [[lenke](https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence)]

- Rigby MJ. **Ethical Dimensions of Using Artificial Intelligence in Health Care.** AMA Journal of Ethics, Feb 2019. [[lenke](https://journalofethics.ama-assn.org/article/ethical-dimensions-using-artificial-intelligence-health-care/2019-02)]

- Morley J et al. **The ethics of AI in health care: A mapping review.** Social Science & Medicine 2020;260:113172. [[lenke](https://www.sciencedirect.com/science/article/pii/S0277953620303919)]

- Bostrom N, Yudkowsky E. The Ethics of Artificial Intelligence. In: Cambridge Handbook of Artificial Intelligence, CUP 2014. [[pdf](https://intelligence.org/files/EthicsofAI.pdf)]

- Ethics of Artificial Intelligence and Robotics. Stanford Encyclopedia of Philosophy. [[lenke](https://plato.stanford.edu/entries/ethics-ai)]

- Vollmer S et al. **Machine learning and artificial intelligence research for patient benefit: 20 critical questions on transparency, replicability, ethics, and effectiveness.** BMJ 2020;368:l6927. [[lenke](https://www.bmj.com/content/368/bmj.l6927)]

- Ethics of AI in Radiology. European and North American Multisociety Statement 2019. [[pdf](https://www.acr.org/-/media/ACR/Files/Informatics/Ethics-of-AI-in-Radiology-European-and-North-American-Multisociety-Statement--6-13-2019.pdf)]

#### EU AI Act og regulering (2024)

- **EU AI Act**: Verdens første omfattende AI-regulering, vedtatt i 2024. Relevant for medisinsk AI som klassifiseres som «høyrisiko».
  - EU AI Act oversikt: [[digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)]

---

### Datahåndteringsplan (DMP)

For å skrive datahåndteringsplanen anbefales det å se på:

- **Science Europe**: Practical Guide to the International Alignment of Research Data Management [[lenke](https://scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/)]

- **NSD/Sikt**: Datahåndteringsplan-verktøy for norske forskere [[sikt.no](https://sikt.no/tjenester/datahndteringsplan)]

- **FAIR-prinsippene**: Findable, Accessible, Interoperable, Reusable [[go-fair.org](https://www.go-fair.org/fair-principles/)]

---

### Nyttige AI-verktøy for å skrive forskningsplanen

For å jobbe effektivt med å skrive forskningsplanen kan følgende AI-verktøy være nyttige:

| Verktøy | Bruksområde | Lenke |
|---------|-------------|-------|
| **ChatGPT** | Generell AI-assistent, kodeforklaringer, litteratursøk | [chat.openai.com](https://chat.openai.com) |
| **Claude** | Tekstanalyse, akademisk skriving | [claude.ai](https://claude.ai) |
| **Gemini** | Integrert i Google Colab for kodehjelp | [gemini.google.com](https://gemini.google.com) |
| **NotebookLM** | Dokumentanalyse og kunnskapssammenstilling | [notebooklm.google.com](https://notebooklm.google.com) |
| **Cursor** | AI-assistert kodeutvikling | [cursor.sh](https://cursor.sh) |
| **Elicit** | AI-drevet litteratursøk | [elicit.com](https://elicit.com) |
| **Connected Papers** | Visualisering av litteraturnettverk | [connectedpapers.com](https://www.connectedpapers.com) |

---

## Sjekkliste for teamet

Før dere starter, sørg for at alle i teamet har:

- [ ] Opprettet en [Overleaf](https://www.overleaf.com)-konto (gratis)
- [ ] Tilgang til LaTeX-malen og forstått strukturen
- [ ] Lest gjennom minst én bakgrunnsartikkel om glioblastom
- [ ] Satt seg inn i WHO 2021-klassifikasjonen av CNS-svulster
- [ ] Utforsket relevante datakilder og programvare (for å kunne beskrive dem i planen)
- [ ] Avtalt kommunikasjonskanal for teamet (f.eks. Teams, Discord, Slack)
- [ ] Fordelt oppgaver og laget en foreløpig plan

---

_Oppdatert: Desember 2025_
