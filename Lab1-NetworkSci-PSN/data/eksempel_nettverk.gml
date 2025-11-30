graph [
  name "Protein-interaksjoner"
  node [
    id 0
    label "1"
    funksjon "Tumorsuppressor"
  ]
  node [
    id 1
    label "2"
    funksjon "Ubiquitin-ligase"
  ]
  node [
    id 2
    label "3"
    funksjon "DNA-reparasjon"
  ]
  edge [
    source 0
    target 1
    interaksjon "binding"
    styrke 0.9
  ]
  edge [
    source 0
    target 2
    interaksjon "samarbeid"
    styrke 0.7
  ]
]
