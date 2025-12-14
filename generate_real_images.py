import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as mlines
import numpy as np
import networkx as nx
import seaborn as sns
import os
from matplotlib.path import Path

# Set style for professional look
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_context("talk")
# Use a standard font available everywhere to avoid box issues
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_plot(path):
    ensure_dir(path)
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Generated: {path}")

# --- Helper Functions for Drawing Icons ---

def draw_database(ax, x, y, size, color='#90caf9'):
    w = size
    h = size * 1.2
    ellipse_h = h * 0.2
    ax.add_patch(patches.Ellipse((x, y - h/2 + ellipse_h/2), w, ellipse_h, facecolor=color, edgecolor='black'))
    ax.add_patch(patches.Rectangle((x - w/2, y - h/2 + ellipse_h/2), w, h - ellipse_h, facecolor=color, edgecolor='none'))
    ax.plot([x - w/2, x - w/2], [y - h/2 + ellipse_h/2, y + h/2 - ellipse_h/2], 'k-', lw=1)
    ax.plot([x + w/2, x + w/2], [y - h/2 + ellipse_h/2, y + h/2 - ellipse_h/2], 'k-', lw=1)
    ax.add_patch(patches.Ellipse((x, y + h/2 - ellipse_h/2), w, ellipse_h, facecolor=color, edgecolor='black'))
    ax.add_patch(patches.Arc((x, y), w, ellipse_h, theta1=180, theta2=360, color='black'))
    ax.add_patch(patches.Arc((x, y - h/4), w, ellipse_h, theta1=180, theta2=360, color='black'))

def draw_gear(ax, x, y, size, color='#b0bec5'):
    radius = size * 0.5
    circle = patches.Circle((x, y), radius*0.8, facecolor=color, edgecolor='black')
    ax.add_patch(circle)
    ax.add_patch(patches.Circle((x, y), radius*0.3, facecolor='white', edgecolor='black'))
    for angle in range(0, 360, 45):
        rad = np.radians(angle)
        tx = x + radius * 0.8 * np.cos(rad)
        ty = y + radius * 0.8 * np.sin(rad)
        rect = patches.Rectangle((tx-radius*0.1, ty-radius*0.1), radius*0.2, radius*0.2, 
                               angle=angle, facecolor=color, edgecolor='black')
        ax.add_patch(rect)

def draw_brain_icon(ax, x, y, size, color='#f48fb1'):
    ax.add_patch(patches.Ellipse((x-size*0.2, y), size*0.8, size, angle=-10, facecolor=color, edgecolor='black', alpha=0.9))
    ax.add_patch(patches.Ellipse((x+size*0.2, y), size*0.8, size, angle=10, facecolor=color, edgecolor='black', alpha=0.9))
    t = np.linspace(0, 1, 100)
    sx = x + size*0.3 * np.sin(10*t)
    sy = y - size*0.3 + size*0.6*t
    ax.plot(sx, sy, 'k-', alpha=0.3)

def draw_magnifying_glass(ax, x, y, size, color='#e1f5fe'):
    ax.add_patch(patches.Circle((x-size*0.2, y+size*0.2), size*0.4, facecolor=color, edgecolor='black', lw=2))
    ax.plot([x-size*0.2 + size*0.3, x+size*0.5], [y+size*0.2 - size*0.3, y-size*0.5], 'k-', lw=4)

def draw_cloud(ax, x, y, size, color='#e3f2fd'):
    centers = [(0,0), (-0.3, -0.1), (0.3, -0.1), (-0.15, 0.2), (0.15, 0.2)]
    for cx, cy in centers:
        ax.add_patch(patches.Circle((x+cx*size, y+cy*size), size*0.25, facecolor=color, edgecolor='none'))
    for cx, cy in centers:
        ax.add_patch(patches.Arc((x+cx*size, y+cy*size), size*0.5, size*0.5, theta1=0, theta2=180, lw=1))

def draw_robot_head(ax, x, y, size):
    ax.add_patch(patches.Rectangle((x-size/2, y-size/2), size, size, facecolor='#cfd8dc', edgecolor='black'))
    ax.add_patch(patches.Circle((x-size*0.2, y+size*0.1), size*0.1, facecolor='#64ffda'))
    ax.add_patch(patches.Circle((x+size*0.2, y+size*0.1), size*0.1, facecolor='#64ffda'))
    ax.plot([x, x], [y+size/2, y+size*0.8], 'k-')
    ax.add_patch(patches.Circle((x, y+size*0.8), size*0.1, facecolor='red'))
    ax.plot([x-size*0.2, x+size*0.2], [y-size*0.2, y-size*0.2], 'k-', lw=1)

def draw_doctor_icon(ax, x, y, size):
    ax.add_patch(patches.Circle((x, y+size*0.3), size*0.25, facecolor='#ffe0b2', edgecolor='black'))
    path = Path([(x, y+size*0.1), (x-size*0.4, y-size*0.5), (x+size*0.4, y-size*0.5), (x, y+size*0.1)],
                [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY])
    patch = patches.PathPatch(path, facecolor='white', edgecolor='black')
    ax.add_patch(patch)
    ax.plot([x-size*0.2, x-size*0.2, x+size*0.2, x+size*0.2], [y-size*0.1, y+size*0.05, y+size*0.05, y-size*0.1], 'k-', lw=1)
    ax.add_patch(patches.Circle((x, y-size*0.2), size*0.05, color='gray'))

# --- LAB 0: Machine Learning ---

def plot_ml_pipeline(path):
    fig, ax = plt.subplots(figsize=(16, 5)) # Wider, shorter
    ax.set_axis_off()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3) # Reduced height
    
    steps = [
        ("Rådata", "Samle inn\ndata", draw_database),
        ("Prosessering", "Rense &\nNormalisere", draw_gear),
        ("Trening", "Lære\nmønstre", draw_brain_icon),
        ("Evaluering", "Teste\nnøyaktighet", draw_magnifying_glass),
        ("Utrulling", "Ta i bruk\nmodellen", draw_cloud)
    ]
    
    x_positions = np.linspace(1, 9, len(steps))
    y_center = 1.5
    box_w, box_h = 1.6, 2.2
    
    for i, (title, desc, draw_func) in enumerate(steps):
        x = x_positions[i]
        rect = patches.FancyBboxPatch((x - box_w/2, y_center - box_h/2), box_w, box_h, 
                                    boxstyle="round,pad=0.1", 
                                    fc='white', ec='#0277bd', lw=2, alpha=0.9)
        ax.add_patch(rect)
        ax.text(x, y_center + box_h*0.35, title, ha='center', va='center', fontsize=12, fontweight='bold', color='#01579b')
        draw_func(ax, x, y_center, 0.7) 
        ax.text(x, y_center - box_h*0.35, desc, ha='center', va='center', fontsize=10, color='#455a64', style='italic')
        
        if i < len(steps) - 1:
            next_x = x_positions[i+1]
            ax.arrow(x + box_w/2 + 0.1, y_center, (next_x - x) - box_w - 0.2, 0, 
                     head_width=0.15, head_length=0.15, fc='#cfd8dc', ec='#b0bec5', lw=3)
            
    plt.title("Maskinlæring Pipeline", fontsize=20, color='#37474f', pad=10)
    save_plot(path)

def plot_class_vs_reg(path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6)) # Reduced height
    
    # Classification
    np.random.seed(42)
    n_samples = 30
    c1 = np.random.randn(n_samples, 2) * 0.5 + [1, 3]
    c2 = np.random.randn(n_samples, 2) * 0.5 + [3, 1]
    
    ax1.scatter(c1[:, 0], c1[:, 1], c='#e57373', label='Syk', s=100, edgecolor='white')
    ax1.scatter(c2[:, 0], c2[:, 1], c='#64b5f6', label='Frisk', s=100, edgecolor='white')
    ax1.plot([0, 4], [4, 0], '--', color='#546e7a', linewidth=3, label='Grense')
    
    ax1.set_title("Klassifikasjon", fontsize=18, fontweight='bold')
    ax1.set_xlabel("F1", fontsize=10)
    ax1.set_ylabel("F2", fontsize=10)
    ax1.legend(loc='upper right', fontsize=10)
    ax1.text(0.5, 3.5, "Skille kategorier", fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
    
    # Regression
    X_reg = np.linspace(0, 10, 20)
    y_true = 0.5 * X_reg + 2
    y_noise = y_true + np.random.randn(20) * 0.5
    
    ax2.scatter(X_reg, y_noise, c='#81c784', s=100, edgecolor='white')
    ax2.plot(X_reg, y_true, '-', color='#2e7d32', linewidth=3, label='Trend')
    
    for i in range(len(X_reg)):
        ax2.plot([X_reg[i], X_reg[i]], [y_noise[i], y_true[i]], 'k-', alpha=0.2)
        
    ax2.set_title("Regresjon", fontsize=18, fontweight='bold')
    ax2.set_xlabel("Dose", fontsize=10)
    ax2.set_ylabel("Verdi", fontsize=10)
    ax2.text(1, 6, "Predikere verdi", fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
    
    save_plot(path)


# --- LAB 1: Network Science ---

def plot_psn_graph(path):
    np.random.seed(42)
    G = nx.newman_watts_strogatz_graph(20, 3, 0.3)
    plt.figure(figsize=(16, 6)) # Wider
    
    pos = nx.spring_layout(G, k=0.5, seed=42) # Spring layout spreads better
    
    communities = [0]*7 + [1]*7 + [2]*6
    colors = ['#ffab91' if c==0 else '#80deea' if c==1 else '#c5e1a5' for c in communities]
    node_sizes = [300 + 100 * G.degree(n) for n in G.nodes]
    
    nx.draw_networkx_edges(G, pos, edge_color='#b0bec5', alpha=0.4, width=2)
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=node_sizes, edgecolors='white', linewidths=2)
    labels = {i: f"P{i+1}" for i in G.nodes}
    nx.draw_networkx_labels(G, pos, labels, font_size=9, font_weight='bold', font_color='#37474f')
    
    legend_elements = [
        mlines.Line2D([0], [0], marker='o', color='w', label='Type A', markerfacecolor='#ffab91', markersize=12),
        mlines.Line2D([0], [0], marker='o', color='w', label='Type B', markerfacecolor='#80deea', markersize=12),
        mlines.Line2D([0], [0], marker='o', color='w', label='Type C', markerfacecolor='#c5e1a5', markersize=12)
    ]
    plt.legend(handles=legend_elements, loc='upper right', title="Subtyper", fontsize=10)
    
    plt.title("Pasient-Likhetsnettverk (PSN)", fontsize=20, fontweight='bold')
    plt.axis('off')
    
    # Text annotation
    plt.text(min(x for x,y in pos.values()), min(y for x,y in pos.values())-0.1, 
             "Noder = Pasienter | Kanter = Likhet", fontsize=12, 
             bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.9))
             
    save_plot(path)

def plot_brain_connectome(path):
    plt.figure(figsize=(16, 6), facecolor='black') # Much wider
    ax = plt.gca()
    ax.set_facecolor('black')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.2, 1.2)
    
    # Draw brain outline (top view approx) - slightly flattened for wide aspect
    t = np.linspace(0, 2*np.pi, 100)
    x_outline = 1.5 * np.cos(t) # Wider
    y_outline = 1.0 * np.sin(t) * (1 + 0.2*np.cos(t))
    ax.plot(x_outline, y_outline, color='#4dd0e1', alpha=0.3, lw=2)
    
    np.random.seed(10)
    n_nodes = 50
    nodes_x, nodes_y = [], []
    while len(nodes_x) < n_nodes:
        x, y = np.random.uniform(-1.5, 1.5), np.random.uniform(-1.2, 1.2)
        if (x/1.5)**2 + (y/(1.0*(1 + 0.2*x)))**2 < 0.9: 
            nodes_x.append(x)
            nodes_y.append(y)
            
    for i in range(n_nodes):
        for j in range(i+1, n_nodes):
            dist = np.sqrt(((nodes_x[i]-nodes_x[j])/1.5)**2 + (nodes_y[i]-nodes_y[j])**2)
            if dist < 0.3:
                alpha = 1 - (dist/0.3)
                ax.plot([nodes_x[i], nodes_x[j]], [nodes_y[i], nodes_y[j]], 
                        color='#ffd700', alpha=alpha*0.6, lw=1)

    ax.scatter(nodes_x, nodes_y, c='#00bcd4', s=80, alpha=0.9, edgecolors='white', zorder=10)
    
    plt.title("Hjerne-Connectome Modell", color='white', fontsize=20, pad=10)
    plt.axis('off')
    save_plot(path)


# --- LAB 2: Deep Learning ---

def plot_cnn_architecture(path):
    fig, ax = plt.subplots(figsize=(16, 5)) # Shorter
    ax.set_axis_off()
    ax.set_xlim(0, 12)
    ax.set_ylim(1, 4) # Focused vertical range
    
    def draw_feature_map(ax, x, y, h, w, d, label, color):
        ax.add_patch(patches.Rectangle((x, y-h/2), w, h, fc=color, ec='k', alpha=0.8))
        poly = np.array([[x+w, y-h/2], [x+w+d, y-h/2+d], [x+w+d, y+h/2+d], [x+w, y+h/2]])
        ax.add_patch(patches.Polygon(poly, fc=color, ec='k', alpha=0.6))
        poly_top = np.array([[x, y+h/2], [x+d, y+h/2+d], [x+w+d, y+h/2+d], [x+w, y+h/2]])
        ax.add_patch(patches.Polygon(poly_top, fc=color, ec='k', alpha=0.5))
        ax.text(x+w/2, y-h/2-0.4, label, ha='center', fontsize=10)
        
    draw_feature_map(ax, 1, 2.5, 2.5, 0.2, 0, "Input\n(28x28)", '#e0e0e0')
    ax.arrow(1.5, 2.5, 0.8, 0, head_width=0.2, fc='k')
    draw_feature_map(ax, 2.5, 2.5, 2.3, 0.5, 0.5, "Conv\n(26x26)", '#90caf9')
    ax.arrow(3.5, 2.5, 0.8, 0, head_width=0.2, fc='k')
    draw_feature_map(ax, 4.5, 2.5, 1.2, 0.5, 0.5, "Pool\n(13x13)", '#ef9a9a')
    ax.arrow(5.5, 2.5, 0.8, 0, head_width=0.2, fc='k')
    draw_feature_map(ax, 6.5, 2.5, 1.0, 0.8, 0.8, "Conv\n(11x11)", '#90caf9')
    ax.arrow(8, 2.5, 0.8, 0, head_width=0.2, fc='k')
    ax.add_patch(patches.Rectangle((9, 1.5), 0.3, 2, fc='#a5d6a7', ec='k'))
    ax.text(9.15, 1.1, "Dense", ha='center', fontsize=10)
    ax.arrow(9.5, 2.5, 0.8, 0, head_width=0.2, fc='k')
    ax.add_patch(patches.Rectangle((10.5, 2), 0.2, 1, fc='#fff59d', ec='k'))
    ax.text(10.6, 1.6, "Out", ha='center', fontsize=10)
    
    plt.title("CNN Arkitektur", fontsize=18)
    save_plot(path)

def plot_mri_analysis(path):
    fig, ax = plt.subplots(figsize=(14, 6)) # Wider
    
    img_size = 200
    x = np.linspace(-1, 1, img_size)
    y = np.linspace(-1, 1, img_size)
    X, Y = np.meshgrid(x, y)
    
    mask = (X**2 + Y**2*0.8 < 0.6)
    mri_data = np.zeros((img_size, img_size))
    mri_data[mask] = 0.5 + 0.1*np.random.randn(np.sum(mask)) 
    ventricles = (np.abs(X) < 0.15) & (np.abs(Y) < 0.2)
    mri_data[mask & ventricles] = 0.1 
    
    ax.imshow(mri_data, cmap='gray', extent=[-1, 1, -1, 1], aspect='auto') # Fit to box
    
    heatmap = np.exp(-((X-0.3)**2 + (Y-0.3)**2)/0.05)
    heatmap[~mask] = 0
    im = ax.imshow(heatmap, cmap='jet', alpha=0.4, extent=[-1, 1, -1, 1], aspect='auto')
    
    cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label('AI Oppmerksomhet', rotation=270, labelpad=15)
    
    ax.annotate('Tumor funnet', xy=(0.3, 0.3), xytext=(0.6, 0.6),
                arrowprops=dict(facecolor='white', shrink=0.05),
                fontsize=12, color='white', fontweight='bold',
                bbox=dict(boxstyle="round", fc="red", ec="none", alpha=0.7))
    
    ax.set_title("AI-Analyse av MRI", fontsize=18)
    ax.axis('off')
    save_plot(path)


# --- LAB 3: GenAI ---

def plot_transformer_attention(path):
    fig, ax = plt.subplots(figsize=(16, 5))
    ax.set_axis_off()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    
    words = ["Legen", "stilte", "pasientens", "diagnose"]
    x_pos = np.linspace(1, 9, len(words))
    
    for i, (x, word) in enumerate(zip(x_pos, words)):
        ax.text(x, 1, word, ha='center', fontsize=14, fontweight='bold', 
                bbox=dict(boxstyle="round,pad=0.3", fc="#e3f2fd", ec="#2196f3"))
        ax.text(x, 4, word, ha='center', fontsize=14, fontweight='bold', 
                bbox=dict(boxstyle="round,pad=0.3", fc="#e8f5e9", ec="#4caf50"))

    ax.annotate("", xy=(x_pos[0], 1.5), xytext=(x_pos[3], 3.5),
                arrowprops=dict(arrowstyle="-", color="#f44336", lw=4, alpha=0.6, connectionstyle="arc3,rad=0.2"))
    ax.annotate("", xy=(x_pos[2], 1.5), xytext=(x_pos[3], 3.5),
                arrowprops=dict(arrowstyle="-", color="#f44336", lw=6, alpha=0.8, connectionstyle="arc3,rad=-0.1"))
    ax.plot([x_pos[1], x_pos[1]], [1.5, 3.5], 'k-', alpha=0.1)
    
    ax.text(5, 2.5, "Attention Weights (Vekter)", ha='center', fontsize=12, 
            bbox=dict(facecolor='white', edgecolor='none'))
            
    plt.title("Transformer Self-Attention", fontsize=18)
    save_plot(path)

def plot_doctor_ai(path):
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_axis_off()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    
    draw_doctor_icon(ax, 2.5, 3, 2.0)
    ax.text(2.5, 0.5, "Lege\n(Skjønn)", ha='center', fontsize=14)
    
    draw_robot_head(ax, 7.5, 3.2, 1.8)
    ax.text(7.5, 0.5, "AI\n(Data)", ha='center', fontsize=14)
    
    ax.annotate("", xy=(3.8, 3), xytext=(6.2, 3),
                arrowprops=dict(arrowstyle="<->", lw=5, color="#ff9800"))
    ax.text(5, 3.5, "Samarbeid", ha='center', fontsize=14, fontweight='bold', color="#e65100")
    
    ax.add_patch(patches.Rectangle((4.5, 4), 1, 1.5, fc='#e1f5fe', ec='#0288d1', alpha=0.7))
    ax.plot([4.6, 4.9, 5.2, 5.4], [4.2, 4.8, 4.5, 5.2], 'b-')
    
    plt.title("Menneske + AI", fontsize=22)
    save_plot(path)

def plot_xai_blackbox(path):
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.set_axis_off()
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    
    rect = patches.Rectangle((4, 2), 2, 2, fc='black', ec='none')
    ax.add_patch(rect)
    ax.text(5, 3, "Black\nBox", ha='center', va='center', color='white', fontsize=14, fontweight='bold')
    
    ax.arrow(1, 3, 2.5, 0, head_width=0.3, fc='k', ec='k', lw=2)
    ax.text(2, 3.5, "Input Data", ha='center', fontsize=12)
    
    ax.arrow(6.5, 3, 2, 0, head_width=0.3, fc='k', ec='k', lw=2)
    ax.text(9.5, 3.5, "Prediksjon", ha='center', fontsize=12, fontweight='bold')
    
    callout_path = Path([(5, 4), (5, 5), (8, 5)], [Path.MOVETO, Path.LINETO, Path.LINETO])
    ax.add_patch(patches.PathPatch(callout_path, fill=False, edgecolor='#ffc107', lw=3, ls='--'))
    
    ax.add_patch(patches.FancyBboxPatch((8, 4), 4, 1.8, boxstyle="round,pad=0.1", fc='#fff9c4', ec='#fbc02d'))
    features = ['BP', 'Alder', 'Røyk']
    vals = [0.8, 0.5, 0.3]
    for i, (f, v) in enumerate(zip(features, vals)):
        y_pos = 5.2 - i*0.5
        ax.text(8.2, y_pos, f, fontsize=10)
        ax.add_patch(patches.Rectangle((9, y_pos-0.1), v*3, 0.3, fc='#ff9800'))
        
    ax.text(10, 5.9, "Forklaring", ha='center', fontsize=11, fontweight='bold', color='#f57f17')
    
    plt.title("Forklarbar AI (XAI)", fontsize=20)
    save_plot(path)

# --- Lab Lynkurs ---

def plot_python_med(path):
    fig, ax = plt.subplots(figsize=(12, 6)) # Wide
    ax.set_axis_off()
    ax.set_xlim(0, 12)
    ax.set_ylim(2, 8)
    
    cx, cy = 6, 5
    size = 2
    ax.add_patch(patches.Rectangle((cx-size/2, cy-size*1.5), size, size*3, fc='#e53935', ec='none'))
    ax.add_patch(patches.Rectangle((cx-size*1.5, cy-size/2), size*3, size, fc='#e53935', ec='none'))
    
    t = np.linspace(-np.pi, np.pi, 100)
    s_x = cx + 3.0 * np.sin(t)
    s_y = cy + 2.5 * np.sin(0.5*t)
    
    ax.plot(s_x, s_y, color='#1e88e5', lw=15, solid_capstyle='round', alpha=0.9)
    ax.plot(s_x, s_y, color='#ffe082', lw=5, alpha=1.0)
    
    head_x, head_y = s_x[-1], s_y[-1]
    ax.add_patch(patches.Circle((head_x, head_y), 0.6, fc='#1e88e5'))
    ax.add_patch(patches.Circle((head_x+0.2, head_y+0.2), 0.1, fc='white'))
    
    plt.title("Python i Medisin", fontsize=24)
    save_plot(path)

def plot_coding_interface(path):
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_axis_off()
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    
    ax.add_patch(patches.FancyBboxPatch((1, 0.5), 12, 5, boxstyle="round,pad=0.1", fc='#263238', ec='#37474f'))
    ax.add_patch(patches.Rectangle((1, 0.5), 2.5, 5, fc='#37474f', ec='none'))
    
    for i in range(8):
        y = 4.5 - i*0.5
        width = np.random.uniform(2, 6)
        color = np.random.choice(['#ef5350', '#42a5f5', '#66bb6a', '#ffca28'])
        ax.plot([4, 4+width], [y, y], lw=4, color=color, solid_capstyle='round')
        
    ax.add_patch(patches.Rectangle((8, 1.5), 4, 3, fc='white', ec='none'))
    tx = np.linspace(8.2, 11.8, 50)
    ty = 3 + np.sin(10*(tx-8))*1.0
    ax.plot(tx, ty, 'b-')
    
    ax.text(7, 5.8, "Jupyter Notebook", ha='center', fontsize=16, fontweight='bold')
    save_plot(path)


# Execution
print("Genererer Lab Lynkurs bilder...")
plot_python_med("Lab-Lynkurs/Beamer/images/python_medisin.pdf")
plot_coding_interface("Lab-Lynkurs/Beamer/images/coding_interface.pdf")

print("Genererer Lab 0 bilder...")
plot_ml_pipeline("Lab0-ML/Beamer/images/ml_pipeline.pdf")
plot_class_vs_reg("Lab0-ML/Beamer/images/class_vs_reg.pdf")

print("Genererer Lab 1 bilder...")
plot_psn_graph("Lab1-NetworkSci-PSN/Beamer/images/psn_graph.pdf")
plot_brain_connectome("Lab1-NetworkSci-PSN/Beamer/images/brain_connectome.pdf")

print("Genererer Lab 2 bilder...")
plot_cnn_architecture("Lab2-DL/Beamer/images/cnn_architecture.pdf")
plot_mri_analysis("Lab2-DL/Beamer/images/mri_analysis.pdf")

print("Genererer Lab 3 bilder...")
plot_transformer_attention("Lab3-GenAI-LLM/Beamer/images/transformer_attention.pdf")
plot_doctor_ai("Lab3-GenAI-LLM/Beamer/images/doctor_ai_team.pdf")
plot_xai_blackbox("Lab3-GenAI-LLM/Beamer/images/xai_blackbox.pdf")

print("Ferdig! Alle bilder generert med Wide Format.")






