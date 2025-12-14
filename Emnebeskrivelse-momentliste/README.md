# Emnebeskrivelse og Momentliste

Denne mappen inneholder en utfyllende emnebeskrivelse og momentliste for ELMED219 (Kunstig intelligens og beregningsorientert medisin).

## Filer

| Fil | Beskrivelse |
|-----|-------------|
| `emnebeskrivelse-og-momentliste.tex` | LaTeX-kildefil |
| `referanser.bib` | BibTeX-referanser |
| `emnebeskrivelse-og-momentliste.pdf` | Kompilert PDF (16 sider) |

## Innhold

Dokumentet dekker:

1. **Innledning og motivasjon** – Hvorfor AI i medisin?
2. **Kursstruktur og innhold** – Oversikt over alle Labs og Teamprosjekt
3. **Detaljert momentliste** – Ca. 100 momenter organisert etter tema
4. **Verktøy og ressurser** – Programvare, AI-assistenter, anbefalt lesning
5. **Vurdering og eksamen** – Eksamensformat og emner
6. **Timeplan** – Foreløpig timeplan for januar 2026
7. **Appendiks** – Illustrasjoner (TikZ-figurer)

## Kompilering

For å kompilere dokumentet lokalt (krever LaTeX-installasjon):

```bash
cd Emnebeskrivelse-momentliste
pdflatex emnebeskrivelse-og-momentliste.tex
bibtex emnebeskrivelse-og-momentliste
pdflatex emnebeskrivelse-og-momentliste.tex
pdflatex emnebeskrivelse-og-momentliste.tex
```

Eller bruk en LaTeX-editor som TeXShop (macOS), TeXworks, eller Overleaf.

## Figurer

Mappen `figs/` er reservert for eventuelle figurer i 300 dpi kvalitet. Foreløpig genereres alle illustrasjoner med TikZ direkte i LaTeX-dokumentet.

---

*Sist oppdatert: Desember 2025*









