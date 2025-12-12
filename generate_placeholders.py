import matplotlib.pyplot as plt
import os
import numpy as np

def create_placeholder_image(path, title, subtitle, color_theme='blue'):
    plt.figure(figsize=(16, 9), dpi=100)
    
    # Background color
    if color_theme == 'dark':
        bg_color = '#1a1a2e'
        text_color = '#e94560'
    else:
        bg_color = '#f0f4f8'
        text_color = '#2d3436'
        
    plt.gca().set_facecolor(bg_color)
    
    # Simple aesthetic elements
    plt.text(0.5, 0.6, "NANO BANANA PRO\nGENERATED ILLUSTRATION", 
             ha='center', va='center', fontsize=30, color=text_color, fontweight='bold')
    
    plt.text(0.5, 0.4, title, 
             ha='center', va='center', fontsize=20, color='#636e72', style='italic')
             
    plt.text(0.5, 0.2, f"Prompt: {subtitle[:50]}...", 
             ha='center', va='center', fontsize=12, color='#b2bec3')

    # Add a border
    plt.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=text_color, linewidth=5)
    
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('off')
    
    plt.savefig(path, bbox_inches='tight', facecolor=bg_color)
    plt.close()
    print(f"Generated: {path}")

# --- Lab Lynkurs ---
create_placeholder_image('Lab-Lynkurs/Beamer/images/python_medisin.png', 
                        'Python Snake Medical', 'A friendly, stylized python snake wrapped around a medical cross')
create_placeholder_image('Lab-Lynkurs/Beamer/images/coding_interface.png', 
                        'Futuristic Coding Interface', 'Futuristic coding interface with medical data visualization')

# --- Lab 0 ---
create_placeholder_image('Lab0-ML/Beamer/images/ml_pipeline.png', 
                        'ML Pipeline Flowchart', 'A clean, horizontal flowchart illustration of the Machine Learning pipeline')
create_placeholder_image('Lab0-ML/Beamer/images/class_vs_reg.png', 
                        'Classification vs Regression', 'Split screen scientific illustration')

# --- Lab 1 ---
create_placeholder_image('Lab1-NetworkSci-PSN/Beamer/images/psn_graph.png', 
                        'Patient Similarity Network', 'A complex network graph visualization representing a PSN')
create_placeholder_image('Lab1-NetworkSci-PSN/Beamer/images/brain_connectome.png', 
                        'Brain Connectome', 'A glowing, translucent human brain viewed from the side', color_theme='dark')

# --- Lab 2 ---
create_placeholder_image('Lab2-DL/Beamer/images/cnn_architecture.png', 
                        'CNN Architecture', 'An isometric visualization of a Convolutional Neural Network')
create_placeholder_image('Lab2-DL/Beamer/images/mri_analysis.png', 
                        'MRI AI Analysis', 'A futuristic medical interface screen showing an MRI scan', color_theme='dark')

# --- Lab 3 ---
create_placeholder_image('Lab3-GenAI-LLM/Beamer/images/transformer_attention.png', 
                        'Transformer Attention', 'An abstract, artistic representation of the Transformer architecture')
create_placeholder_image('Lab3-GenAI-LLM/Beamer/images/doctor_ai_team.png', 
                        'Doctor and AI', 'A doctor in a white coat holding a tablet, standing next to a friendly AI')
create_placeholder_image('Lab3-GenAI-LLM/Beamer/images/xai_blackbox.png', 
                        'Explainable AI Black Box', 'A Black Box cube that is cracked open', color_theme='dark')



