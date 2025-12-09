# Lab 3: Generativ AI og Store Språkmodeller (LLM)

Denne laben introduserer generativ AI og store språkmodeller (LLM) med fokus på biomedisinske anvendelser. Vi dekker alt fra grunnleggende konsepter til etiske problemstillinger og fremtidige retninger som nevrosymbolsk AI.

## Læringsmål

Etter å ha fullført denne laben skal du kunne:

- Forstå grunnprinsippene bak generativ AI og transformer-arkitekturen
- Forklare hvordan store språkmodeller (LLM) fungerer
- Anvende prompt engineering-teknikker for medisinske oppgaver
- Vurdere forklarbarhet (XAI) og pålitelighet i AI-systemer
- Reflektere over etiske aspekter ved AI i helsevesenet
- Kjenne til nevrosymbolske tilnærminger og deres potensial

---

## Prioriteringsguide

### Kjerne (obligatorisk) - ca. 4-5 timer
Disse notebooks dekker det essensielle og bør gjennomgås av alle:

| # | Notebook | Beskrivelse | Tid |
|---|----------|-------------|-----|
| 01 | [Introduksjon til Generativ AI](notebooks/01-introduksjon-genai.ipynb) | Oversikt, historie og medisinsk relevans | ~45 min |
| 02 | [Transformer-arkitekturen](notebooks/02-transformer-arkitektur.ipynb) | Self-attention og grunnlaget for moderne AI | ~60 min |
| 03 | [LLM Grunnleggende](notebooks/03-llm-grunnleggende.ipynb) | Tokens, temperature og kontekstvindu | ~45 min |
| 04 | [Prompt Engineering](notebooks/04-prompt-engineering.ipynb) | Teknikker for effektiv kommunikasjon med AI | ~90 min |

### Viktig (anbefalt) - ca. 2-3 timer
Disse notebooks gir viktig kontekst for ansvarlig bruk av AI i helsevesenet:

| # | Notebook | Beskrivelse | Tid |
|---|----------|-------------|-----|
| 05 | [Forklarbar AI (XAI)](notebooks/05-xai-forklarbar-ai.ipynb) | SHAP, LIME og klinisk tolkbarhet | ~60 min |
| 06 | [AI-etikk i medisin](notebooks/06-ai-etikk-medisin.ipynb) | Bias, personvern og regulering | ~60 min |

### Utdypende (valgfritt) - ca. 2-3 timer
For deg som vil gå dypere inn i spesialtemaer:

| # | Notebook | Beskrivelse | Tid |
|---|----------|-------------|-----|
| 07 | [Trustworthy AI](notebooks/07-trustworthy-ai.ipynb) | Pålitelighet, robusthet og human-in-the-loop | ~60 min |
| 08 | [Nevrosymbolsk AI](notebooks/08-nevrosymbolsk-ai.ipynb) | Hybrid AI og kunnskapsgrafer | ~60 min |
| 09 | [ChatGPT/Claude API](notebooks/09-chatgpt-claude-api.ipynb) | Programmatisk bruk av LLM-APIer | ~60 min |

### Teknisk supplement
| # | Notebook | Beskrivelse |
|---|----------|-------------|
| 00 | [Test LLM lokalt](00-test-llm.ipynb) | Kjøring av lokale modeller med Ollama |

---

## Forutsetninger

- Gjennomført Lab 0 (Python grunnleggende)
- Kjennskap til grunnleggende maskinlæring (Lab 1-2)
- Google-konto for Colab (anbefalt)

## Mappestruktur

```
Lab3-GenAI-LLM/
├── README.md                 # Denne filen
├── notebooks/                # Alle notebooks (01-09)
├── prompts/                  # Eksempel-prompts for helsefaglige oppgaver
│   ├── kliniske_notater.txt
│   ├── pasientsamtale.txt
│   └── journalsammendrag.txt
├── ressurser/               # Figurer og referanser
└── 00-test-llm.ipynb        # Teknisk supplement
```

## Ressurser og verktøy

### AI-assistenter
- [Medical AI Assistant (GPT)](https://chatgpt.com/g/g-d90dfN17H-medical-ai-assistant-uibmed-elmed219-bmed365) - Tilpasset for ELMED219/BMED365
- [NotebookLM](https://notebooklm.google.com/) - Google's AI for dokumentanalyse
- [Claude](https://claude.ai/) - Anthropics AI-assistent
- [ChatGPT](https://chat.openai.com/) - OpenAIs AI-assistent

### Utviklingsverktøy
- [Google Colab](https://colab.research.google.com/) - Kjør notebooks i nettleseren
- [Cursor AI](https://cursor.sh/) - AI-drevet kodeeditor

### Videre lesning
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Original transformer-artikkel
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [EU AI Act](https://artificialintelligenceact.eu/) - Europeisk AI-regulering

---

## Refleksjonsoppgave

Etter å ha gjennomgått materialet, skriv en kort refleksjon (300-500 ord) som adresserer:

1. **Muligheter**: Hvordan kan generativ AI forbedre klinisk praksis eller biomedisinsk forskning?
2. **Begrensninger**: Hvilke situasjoner er AI-assistenter IKKE egnet for?
3. **Ansvar**: Hvem har ansvar når AI gir feilaktige anbefalinger?
4. **Fremtid**: Hvordan tror du AI vil påvirke din fremtidige yrkespraksis?

---

## Viktige påminnelser

> **AI erstatter ikke klinisk vurdering.** Alle AI-genererte forslag må valideres av kvalifisert helsepersonell.

> **Personvern først.** Aldri del reelle pasientdata med AI-tjenester uten godkjent databehandleravtale.

> **Kritisk tenkning.** AI kan "hallusinere" - vær alltid kritisk til output og verifiser fakta.

---

*Sist oppdatert: 2025*
