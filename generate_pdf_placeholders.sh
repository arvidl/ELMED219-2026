#!/bin/bash

# Function to generate a placeholder PDF
generate_pdf() {
    path=$1
    filename=$2
    title=$3
    prompt=$4
    
    mkdir -p "$path"
    
    texfile="$path/$filename.tex"
    
    echo "\documentclass[border=2pt]{standalone}" > "$texfile"
    echo "\usepackage[utf8]{inputenc}" >> "$texfile"
    echo "\usepackage{tikz}" >> "$texfile"
    echo "\begin{document}" >> "$texfile"
    echo "\begin{tikzpicture}" >> "$texfile"
    echo "  \node[draw, fill=blue!10, minimum width=16cm, minimum height=9cm, align=center] {" >> "$texfile"
    echo "    \textbf{\huge NANO BANANA PRO} \\\\" >> "$texfile"
    echo "    \textit{\Large $title} \\\\" >> "$texfile"
    echo "    \small Prompt: $prompt" >> "$texfile"
    echo "  };" >> "$texfile"
    echo "\end{tikzpicture}" >> "$texfile"
    echo "\end{document}" >> "$texfile"
    
    # Compile
    cd "$path"
    pdflatex -interaction=nonstopmode "$filename.tex" > /dev/null
    rm "$filename.log" "$filename.aux" "$filename.tex"
    cd - > /dev/null
    echo "Generated placeholder: $path/$filename.pdf"
}

# Lab Lynkurs
generate_pdf "Lab-Lynkurs/Beamer/images" "python_medisin" "Python + Medicine" "A friendly, stylized python snake wrapped around a medical cross"
generate_pdf "Lab-Lynkurs/Beamer/images" "coding_interface" "Coding Interface" "Futuristic coding interface with medical data visualization"

# Lab 0
generate_pdf "Lab0-ML/Beamer/images" "ml_pipeline" "ML Pipeline" "A clean, horizontal flowchart illustration of the ML pipeline"
generate_pdf "Lab0-ML/Beamer/images" "class_vs_reg" "Classification vs Regression" "Split screen scientific illustration"

# Lab 1
generate_pdf "Lab1-NetworkSci-PSN/Beamer/images" "psn_graph" "PSN Graph" "A complex network graph visualization representing a PSN"
generate_pdf "Lab1-NetworkSci-PSN/Beamer/images/psn_graph" "brain_connectome" "Brain Connectome" "A glowing, translucent human brain viewed from the side"

# Lab 2
generate_pdf "Lab2-DL/Beamer/images" "cnn_architecture" "CNN Architecture" "Isometric visualization of a CNN"
generate_pdf "Lab2-DL/Beamer/images" "mri_analysis" "MRI Analysis" "Futuristic medical interface showing MRI scan"

# Lab 3
generate_pdf "Lab3-GenAI-LLM/Beamer/images" "transformer_attention" "Transformer Attention" "Abstract representation of Attention mechanism"
generate_pdf "Lab3-GenAI-LLM/Beamer/images" "doctor_ai_team" "Human-AI Team" "Doctor and AI assistant collaborating"
generate_pdf "Lab3-GenAI-LLM/Beamer/images" "xai_blackbox" "XAI Black Box" "Black Box cube cracked open revealing logic"

