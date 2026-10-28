import os
import math
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    # Try system fonts on Mac
    paths = [
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/SFCompactDisplay-Bold.otf" if bold else "/System/Library/Fonts/SFCompactDisplay-Regular.otf",
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf"
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def draw_cyber_base(w=1280, h=720, primary="#3b82f6", title="SYSTEM DASHBOARD", category="AI INFERENCE ENGINE"):
    im = Image.new("RGB", (w, h), "#060913")
    draw = ImageDraw.Draw(im)

    # 1. Subtle Background Grid
    grid_spacing = 40
    for x in range(0, w, grid_spacing):
        draw.line([(x, 0), (x, h)], fill="#0c162d", width=1)
    for y in range(0, h, grid_spacing):
        draw.line([(0, y), (w, y)], fill="#0c162d", width=1)

    # 2. Glowing Radial Accents in corners (simulated)
    # Top-right glow
    for r in range(300, 0, -25):
        alpha = int(18 * (1 - r / 300))
        draw.ellipse([w - r, -r, w + r, r], outline=f"#1e3a8a{alpha:02x}", width=12)
    # Bottom-left glow
    for r in range(250, 0, -25):
        alpha = int(14 * (1 - r / 250))
        draw.ellipse([-r, h - r, r, h + r], outline=f"#0284c7{alpha:02x}", width=12)

    # 3. Outer edge decorative frame line
    draw.rectangle([12, 12, w - 13, h - 13], outline="#1e293b", width=1)
    # Corner brackets
    c_len = 24
    for cx, cy in [(12, 12), (w - 13, 12), (12, h - 13), (w - 13, h - 13)]:
        dx = c_len if cx == 12 else -c_len
        dy = c_len if cy == 12 else -c_len
        draw.line([(cx, cy), (cx + dx, cy)], fill="#3b82f6", width=2)
        draw.line([(cx, cy), (cx, cy + dy)], fill="#3b82f6", width=2)

    # 4. Top Header Bar (Edge to Edge)
    draw.rectangle([12, 12, w - 13, 62], fill="#0a1020", outline="#1e293b", width=1)
    
    # Status Dot + Brand
    draw.ellipse([30, 32, 40, 42], fill="#10b981")
    f_brand = get_font(13, bold=True)
    f_sub = get_font(11, bold=False)
    draw.text((48, 28), "AJAY VISHWAKARMA // AI RESEARCH PLATFORM", fill="#94a3b8", font=f_brand)
    draw.text((48, 44), f"{category} • REAL-TIME INFERENCE (v4.2)", fill="#475569", font=f_sub)

    # Center title pill
    f_pill = get_font(14, bold=True)
    draw.rounded_rectangle([w // 2 - 180, 22, w // 2 + 180, 52], radius=6, fill="#111c35", outline="#2563eb", width=1)
    draw.text((w // 2, 37), title, fill="#60a5fa", font=f_pill, anchor="mm")

    # Right telemetry indicators
    f_mono = get_font(11, bold=True)
    draw.text((w - 240, 30), "GPU: RTX 4090 (98%)", fill="#38bdf8", font=f_mono)
    draw.text((w - 240, 44), "LATENCY: 14ms • ACC: 92.4%", fill="#10b981", font=f_mono)

    # 5. Bottom Status Footer
    draw.rectangle([12, h - 46, w - 13, h - 13], fill="#0a1020", outline="#1e293b", width=1)
    f_foot = get_font(11, bold=False)
    draw.text((30, h - 30), "MODEL: ConvNeXt + EfficientNet-B4 Hybrid | BATCH SIZE: 32 | OPTIMIZER: AdamW (lr=1e-4)", fill="#64748b", font=f_foot)
    draw.text((w - 230, h - 30), "CONFIDENCE THRESHOLD: 85%", fill="#94a3b8", font=f_foot)

    return im, draw

def save_both(im, rel_path):
    for root in ["work", "public/work"]:
        full = os.path.join(root, rel_path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        im.save(full, "WEBP", quality=92)
    print(f"Generated: {rel_path}")

# =========================================================================
# 1. BRAIN TUMOR DETECTION (kt-ai-station/deepfake/*)
# =========================================================================

def gen_deepfake_start():
    # 01 Diagnostic Dashboard
    im, draw = draw_cyber_base(title="DIAGNOSTIC DASHBOARD // MULTI-CLASS MRI CLASSIFIER", category="MEDICAL AI SUITE")
    
    # Left Panel: Scan Visualizer (360x540)
    draw.rounded_rectangle([32, 82, 450, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((50, 100), "AXIAL T2-WEIGHTED MRI SCAN", fill="#38bdf8", font=get_font(14, bold=True))
    draw.text((50, 122), "Patient Anon_90832 | Slice 42/64 | Echo Time: 90ms", fill="#64748b", font=get_font(11))
    
    # Simulated brain cross-section drawing
    bx, by = 241, 350
    # Outer skull
    draw.ellipse([bx - 140, by - 160, bx + 140, by + 160], fill="#070c18", outline="#334155", width=3)
    # Inner brain hemispheres
    draw.ellipse([bx - 120, by - 140, bx - 5, by + 140], fill="#111c33", outline="#1e293b", width=2)
    draw.ellipse([bx + 5, by - 140, bx + 120, by + 140], fill="#111c33", outline="#1e293b", width=2)
    # Ventricles
    draw.ellipse([bx - 35, by - 40, bx - 10, by + 40], fill="#070c18")
    draw.ellipse([bx + 10, by - 40, bx + 35, by + 40], fill="#070c18")
    # Detected Lesion (Tumor highlighted in neon red/orange)
    draw.ellipse([bx - 95, by - 70, bx - 35, by - 10], fill="#7f1d1d", outline="#ef4444", width=3)
    # Bounding box & target reticle
    draw.rectangle([bx - 105, by - 80, bx - 25, by], outline="#f43f5e", width=2)
    draw.line([(bx - 115, by - 40), (bx - 15, by - 40)], fill="#f43f5e", width=1)
    draw.line([(bx - 65, by - 90), (bx - 65, by + 10)], fill="#f43f5e", width=1)
    draw.text((bx - 105, by - 102), "LESION: GLIOMA (94.2%)", fill="#f43f5e", font=get_font(11, bold=True))
    
    # Center-Right Panel: Clinical Predictions
    draw.rounded_rectangle([474, 82, 1248, 380], radius=10, fill="#0d1424", outline="#1e293b", width=1)
    draw.text((498, 102), "MODEL INFERENCE & PROBABILITY SPECTRUM", fill="#f8fafc", font=get_font(16, bold=True))
    draw.text((498, 126), "Softmax distribution across 4 target pathology classes", fill="#64748b", font=get_font(12))

    # Probability bars
    classes = [
        ("Glioma Tumor (Primary Lesion)", 0.942, "#ef4444", "CRITICAL POSITIVE"),
        ("Meningioma", 0.031, "#3b82f6", "LOW RISK"),
        ("Pituitary Tumor", 0.018, "#8b5cf6", "MINIMAL"),
        ("No Tumor (Healthy Tissue)", 0.009, "#10b981", "EXCLUDED")
    ]
    py = 160
    for label, prob, col, status in classes:
        draw.text((498, py), label, fill="#e2e8f0", font=get_font(13, bold=True))
        draw.text((920, py), f"{prob * 100:.1f}%", fill=col, font=get_font(14, bold=True))
        draw.text((1060, py), status, fill=col, font=get_font(11, bold=True))
        # Background bar
        draw.rounded_rectangle([498, py + 22, 1220, py + 38], radius=4, fill="#1e293b")
        # Fill bar
        bar_w = int(722 * prob)
        draw.rounded_rectangle([498, py + 22, 498 + bar_w, py + 38], radius=4, fill=col)
        py += 52

    # Bottom Right Panel: Model Verification Stats (4 cards)
    metrics = [
        ("ACCURACY", "92.4%", "Verified on test set", "#38bdf8"),
        ("PRECISION", "94.2%", "Glioma class", "#10b981"),
        ("RECALL", "93.5%", "Sensitivity rate", "#a855f7"),
        ("F1-SCORE", "0.938", "Harmonic mean", "#f59e0b")
    ]
    mx = 474
    for title_m, val_m, sub_m, col_m in metrics:
        draw.rounded_rectangle([mx, 400, mx + 184, 650], radius=10, fill="#0d1424", outline="#1e293b", width=1)
        draw.text((mx + 16, 424), title_m, fill="#64748b", font=get_font(12, bold=True))
        draw.text((mx + 16, 460), val_m, fill=col_m, font=get_font(28, bold=True))
        draw.text((mx + 16, 510), sub_m, fill="#94a3b8", font=get_font(11))
        # Decorative micro meter
        draw.rounded_rectangle([mx + 16, 560, mx + 168, 568], radius=3, fill="#1e293b")
        draw.rounded_rectangle([mx + 16, 560, mx + 130, 568], radius=3, fill=col_m)
        draw.text((mx + 16, 590), "VERIFIED V4.2", fill="#475569", font=get_font(10, bold=True))
        mx += 194

    save_both(im, "kt-ai-station/deepfake/start.webp")

def gen_deepfake_intro():
    # 02 MRI Scan Upload
    im, draw = draw_cyber_base(title="DICOM / NIFTI SCAN INGESTION & PIPELINE", category="DATA INGESTION")
    
    # Large dropzone area
    draw.rounded_rectangle([80, 100, 1200, 400], radius=16, fill="#0a1226", outline="#3b82f6", width=2)
    # Animated corner borders
    for x1, y1 in [(100, 120), (1180, 120), (100, 380), (1180, 380)]:
        draw.ellipse([x1-10, y1-10, x1+10, y1+10], fill="#3b82f6")
    
    # Cloud upload icon simulated
    cx, cy = 640, 200
    draw.rounded_rectangle([cx - 40, cy - 20, cx + 40, cy + 25], radius=12, fill="#1d4ed8")
    draw.polygon([(cx, cy - 45), (cx - 25, cy - 15), (cx + 25, cy - 15)], fill="#60a5fa")
    
    draw.text((640, 260), "DRAG & DROP BRAIN MRI SCANS (DICOM, NIfTI, .PNG, .JPG)", fill="#f8fafc", font=get_font(18, bold=True), anchor="mm")
    draw.text((640, 290), "Supports multi-slice volumetric tensors up to 512x512x128 voxels with automatic intensity normalization", fill="#94a3b8", font=get_font(13), anchor="mm")
    
    # Uploaded file status pill
    draw.rounded_rectangle([440, 325, 840, 375], radius=8, fill="#1e293b", outline="#10b981", width=1)
    draw.text((460, 340), "● patient_t2_vol_0492.dcm (48.2 MB)", fill="#e2e8f0", font=get_font(13, bold=True))
    draw.text((460, 356), "Normalized • CLAHE contrast applied • Voxel spacing: 0.8x0.8x1.2mm", fill="#10b981", font=get_font(11))
    draw.text((810, 350), "READY ↗", fill="#38bdf8", font=get_font(12, bold=True), anchor="rm")

    # Bottom 3 orthogonal slices preview
    slices = [
        ("AXIAL SLICE (Z=42)", "#38bdf8"),
        ("SAGITTAL SLICE (X=128)", "#818cf8"),
        ("CORONAL SLICE (Y=116)", "#a855f7")
    ]
    sx = 80
    for name_s, col_s in slices:
        draw.rounded_rectangle([sx, 430, sx + 350, 650], radius=10, fill="#0d1424", outline="#1e293b", width=1)
        draw.text((sx + 20, 450), name_s, fill=col_s, font=get_font(13, bold=True))
        # Inner simulated slice viewport
        draw.rectangle([sx + 20, 480, sx + 330, 630], fill="#050811", outline="#334155", width=1)
        # Scan curves
        mid_x, mid_y = sx + 175, 555
        draw.ellipse([mid_x - 70, mid_y - 60, mid_x + 70, mid_y + 60], fill="#111d38", outline="#1e293b")
        draw.ellipse([mid_x - 30, mid_y - 20, mid_x + 30, mid_y + 20], fill="#080e1c")
        draw.line([(mid_x, 480), (mid_x, 630)], fill="#1e3a8a", width=1)
        draw.line([(sx + 20, mid_y), (sx + 330, mid_y)], fill="#1e3a8a", width=1)
        sx += 385

    save_both(im, "kt-ai-station/deepfake/intro.webp")

def gen_deepfake_how():
    # 03 CNN Feature Extraction
    im, draw = draw_cyber_base(title="CNN FEATURE EXTRACTION & GRAD-CAM ACTIVATION", category="DEEP LEARNING ARCHITECTURE")

    # 4 Architecture stages across screen
    stages = [
        ("STAGE 1: INPUT LAYER", "512x512x3 Normalized Tensor", "CLAHE contrast stretching & Gaussian filtering", "#38bdf8"),
        ("STAGE 2: CONV2D BLOCKS", "Conv2D + BatchNorm + Swish", "Edge & gradient boundary tensor activation", "#60a5fa"),
        ("STAGE 3: RESIDUAL DENSE", "Bottleneck DenseBlock (x32)", "Deep pathological feature representations", "#a855f7"),
        ("STAGE 4: GRAD-CAM MAP", "Class Activation Mapping", "Heatmap localization on target tumor region", "#ef4444")
    ]
    st_w = 268
    st_x = 40
    for title_st, sub1_st, sub2_st, col_st in stages:
        draw.rounded_rectangle([st_x, 90, st_x + st_w, 650], radius=12, fill="#0d1424", outline=col_st, width=1)
        draw.text((st_x + 16, 110), title_st, fill=col_st, font=get_font(13, bold=True))
        draw.text((st_x + 16, 132), sub1_st, fill="#e2e8f0", font=get_font(12, bold=True))
        draw.text((st_x + 16, 150), sub2_st, fill="#64748b", font=get_font(10))

        # Graphic representation per stage
        box_y = 190
        if "STAGE 1" in title_st:
            # Raw scan with coordinate grid
            draw.rectangle([st_x + 20, box_y, st_x + st_w - 20, box_y + 240], fill="#070c18", outline="#334155")
            draw.ellipse([st_x + 50, box_y + 30, st_x + st_w - 50, box_y + 210], fill="#15213b")
            draw.text((st_x + 30, box_y + 260), "RGB [0, 255] -> [-1.0, 1.0]", fill="#94a3b8", font=get_font(11))
            draw.text((st_x + 30, box_y + 280), "Resolution: 0.5mm / pixel", fill="#475569", font=get_font(10))
        elif "STAGE 2" in title_st:
            # Feature map grid (4x4 squares)
            draw.rectangle([st_x + 20, box_y, st_x + st_w - 20, box_y + 240], fill="#070c18", outline="#334155")
            for r in range(4):
                for c in range(4):
                    gx = st_x + 32 + c * 52
                    gy = box_y + 16 + r * 52
                    draw.rectangle([gx, gy, gx + 44, gy + 44], fill="#1e293b", outline="#3b82f6")
                    draw.ellipse([gx + 10, gy + 10, gx + 34, gy + 34], fill="#2563eb")
            draw.text((st_x + 30, box_y + 260), "128 Learned Kernel Filters", fill="#94a3b8", font=get_font(11))
            draw.text((st_x + 30, box_y + 280), "Stride: 2 | Padding: Same", fill="#475569", font=get_font(10))
        elif "STAGE 3" in title_st:
            # Dense neural connectivity
            draw.rectangle([st_x + 20, box_y, st_x + st_w - 20, box_y + 240], fill="#070c18", outline="#334155")
            nodes_x = [st_x + 50, st_x + 134, st_x + st_w - 50]
            for col_idx, nx in enumerate(nodes_x):
                for ny in range(box_y + 30, box_y + 220, 36):
                    draw.ellipse([nx - 6, ny - 6, nx + 6, ny + 6], fill="#a855f7")
                    if col_idx < 2:
                        next_nx = nodes_x[col_idx + 1]
                        for nny in range(box_y + 30, box_y + 220, 72):
                            draw.line([(nx, ny), (next_nx, nny)], fill="#4c1d95", width=1)
            draw.text((st_x + 30, box_y + 260), "Residual Skip Connections", fill="#94a3b8", font=get_font(11))
            draw.text((st_x + 30, box_y + 280), "Dense Vector Dim: 2048", fill="#475569", font=get_font(10))
        else:
            # Grad-CAM heatmap visualization
            draw.rectangle([st_x + 20, box_y, st_x + st_w - 20, box_y + 240], fill="#070c18", outline="#334155")
            draw.ellipse([st_x + 50, box_y + 30, st_x + st_w - 50, box_y + 210], fill="#1e3a8a")
            # Glowing heat area
            draw.ellipse([st_x + 70, box_y + 70, st_x + 150, box_y + 150], fill="#f59e0b")
            draw.ellipse([st_x + 85, box_y + 85, st_x + 135, box_y + 135], fill="#ef4444")
            draw.text((st_x + 30, box_y + 260), "Weight Gradient α_k^c", fill="#f43f5e", font=get_font(11, bold=True))
            draw.text((st_x + 30, box_y + 280), "Salient Focus: 94.2% on Tumor", fill="#94a3b8", font=get_font(10))

        # Bottom stats
        draw.rectangle([st_x + 20, 520, st_x + st_w - 20, 620], fill="#0a1020", outline="#1e293b")
        draw.text((st_x + 30, 535), "PARAMETER COUNT", fill="#64748b", font=get_font(10, bold=True))
        draw.text((st_x + 30, 555), "24.8M Tensors", fill="#f8fafc", font=get_font(15, bold=True))
        draw.text((st_x + 30, 585), "Zero vanishing gradient", fill="#10b981", font=get_font(10))

        st_x += st_w + 38

    save_both(im, "kt-ai-station/deepfake/how.webp")

def gen_deepfake_quiz():
    # 04 Probability Analysis
    im, draw = draw_cyber_base(title="CONFIDENCE INTERVALS & SOFTMAX PROBABILITY MATRIX", category="ANALYTICAL METRICS")

    # Left large radar / distribution panel
    draw.rounded_rectangle([40, 90, 620, 650], radius=12, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((64, 115), "MULTI-CLASS PROBABILITY DISTRIBUTION", fill="#f8fafc", font=get_font(16, bold=True))
    draw.text((64, 138), "Bayesian Monte-Carlo dropout uncertainty: ±0.8%", fill="#64748b", font=get_font(12))

    # Graph axes
    draw.line([(100, 520), (560, 520)], fill="#334155", width=2)
    draw.line([(100, 200), (100, 520)], fill="#334155", width=2)
    # Grid lines
    for gy in range(240, 520, 70):
        draw.line([(100, gy), (560, gy)], fill="#1e293b", width=1)

    # Bars on chart
    b_data = [
        ("Glioma", 0.942, "#ef4444"),
        ("Meningioma", 0.031, "#3b82f6"),
        ("Pituitary", 0.018, "#8b5cf6"),
        ("Healthy", 0.009, "#10b981")
    ]
    for i, (name_b, p_val, col_b) in enumerate(b_data):
        bx1 = 140 + i * 105
        bx2 = bx1 + 65
        h_bar = int(300 * p_val)
        by1 = 520 - h_bar
        draw.rounded_rectangle([bx1, by1, bx2, 520], radius=6, fill=col_b)
        draw.text((bx1 + 32, by1 - 20), f"{p_val*100:.1f}%", fill=col_b, font=get_font(13, bold=True), anchor="mm")
        draw.text((bx1 + 32, 538), name_b, fill="#94a3b8", font=get_font(11, bold=True), anchor="mm")

    # Right side detailed telemetry
    draw.rounded_rectangle([660, 90, 1240, 650], radius=12, fill="#0d1424", outline="#1e293b", width=1)
    draw.text((684, 115), "CROSS-ENTROPY LOSS & METRIC PROOFS", fill="#f8fafc", font=get_font(16, bold=True))
    draw.text((684, 138), "1,200 Validation scans tested across 4 major medical hospital datasets", fill="#64748b", font=get_font(12))

    # Stats rows
    telemetry = [
        ("Categorical Cross-Entropy Loss", "0.142", "Lower is better (Baseline: 0.850)", "#10b981"),
        ("Area Under ROC Curve (AUC)", "0.984", "Near-perfect discrimination score", "#38bdf8"),
        ("True Positive Rate (TPR)", "95.1%", "Glioma sensitivity under 0.5 threshold", "#ef4444"),
        ("False Discovery Rate (FDR)", "3.8%", "Extremely low false alarm margin", "#a855f7"),
        ("Softmax Temperature Scale (T)", "1.0", "Calibrated Platt scaling verified", "#f59e0b")
    ]
    ty = 180
    for label_t, val_t, sub_t, col_t in telemetry:
        draw.rounded_rectangle([684, ty, 1216, ty + 70], radius=8, fill="#0a1020", outline="#1e293b")
        draw.text((704, ty + 16), label_t, fill="#e2e8f0", font=get_font(14, bold=True))
        draw.text((704, ty + 40), sub_t, fill="#64748b", font=get_font(11))
        draw.text((1196, ty + 35), val_t, fill=col_t, font=get_font(20, bold=True), anchor="rm")
        ty += 84

    save_both(im, "kt-ai-station/deepfake/quiz.webp")

def gen_deepfake_correct():
    # 05 92.4% Accuracy Validated
    im, draw = draw_cyber_base(title="OFFICIAL BENCHMARK // 92.4% VALIDATED ACCURACY", category="VALIDATION SUMMARY")

    # Big top hero stat box
    draw.rounded_rectangle([40, 90, 1240, 240], radius=14, fill="#0b1329", outline="#10b981", width=2)
    draw.text((70, 120), "OFFICIALLY VALIDATED ACCURACY RATING", fill="#10b981", font=get_font(14, bold=True))
    draw.text((70, 155), "92.4%", fill="#f8fafc", font=get_font(64, bold=True))
    draw.text((320, 175), "Across 4 Distinct Brain Tumor Morphologies\n(Glioma, Meningioma, Pituitary, Normal Brain Scans)", fill="#94a3b8", font=get_font(15))

    # Verification Badge
    draw.rounded_rectangle([920, 120, 1200, 210], radius=10, fill="#064e3b", outline="#10b981", width=1)
    draw.text((1060, 150), "✓ BENCHMARK PASSED", fill="#34d399", font=get_font(15, bold=True), anchor="mm")
    draw.text((1060, 175), "K-Fold Stratified Cross-Validation", fill="#a7f3d0", font=get_font(11), anchor="mm")

    # Bottom left: Confusion Matrix
    draw.rounded_rectangle([40, 270, 620, 650], radius=12, fill="#0d1424", outline="#1e293b", width=1)
    draw.text((64, 295), "CONFUSION MATRIX (N=1,200)", fill="#f8fafc", font=get_font(16, bold=True))
    draw.text((64, 318), "Rows: True Class | Columns: Predicted Class", fill="#64748b", font=get_font(12))

    matrix = [
        ["Glioma", "282", "8", "6", "4"],
        ["Mening.", "7", "275", "11", "7"],
        ["Pituitary", "5", "9", "281", "5"],
        ["Healthy", "2", "3", "4", "291"]
    ]
    # Draw Matrix table
    col_names = ["Class", "Glioma", "Mening.", "Pituit.", "Normal"]
    my = 360
    for ci, cn in enumerate(col_names):
        draw.text((70 + ci * 105, my), cn, fill="#38bdf8", font=get_font(12, bold=True))
    my += 28
    draw.line([(64, my), (600, my)], fill="#334155", width=1)
    my += 14

    for row in matrix:
        for ci, val in enumerate(row):
            is_diag = (ci > 0 and row[0][:4] == col_names[ci][:4])
            color = "#34d399" if is_diag else ("#ef4444" if ci > 0 else "#e2e8f0")
            font_use = get_font(13, bold=True if is_diag else False)
            if is_diag:
                draw.rectangle([60 + ci * 105, my - 6, 140 + ci * 105, my + 22], fill="#064e3b")
            draw.text((70 + ci * 105, my), val, fill=color, font=font_use)
        my += 42

    # Bottom right: Training curves graph
    draw.rounded_rectangle([660, 270, 1240, 650], radius=12, fill="#0d1424", outline="#1e293b", width=1)
    draw.text((684, 295), "ACCURACY & LOSS CONVERGENCE", fill="#f8fafc", font=get_font(16, bold=True))
    draw.text((684, 318), "50 Epochs with Early Stopping & ReduceLROnPlateau", fill="#64748b", font=get_font(12))

    # Graph canvas
    draw.rectangle([700, 360, 1200, 610], fill="#070c18", outline="#334155")
    # Axis
    draw.line([(700, 580), (1200, 580)], fill="#475569", width=2)
    draw.line([(740, 360), (740, 580)], fill="#475569", width=2)
    # Simulated accuracy curve (Blue)
    pts_acc = []
    for ep in range(50):
        gx = 740 + int(ep * 9.2)
        gy = int(570 - 180 * (1 - math.exp(-ep / 8)))
        pts_acc.append((gx, gy))
    draw.line(pts_acc, fill="#38bdf8", width=3)
    draw.text((1120, 380), "● Train Acc (95.1%)", fill="#38bdf8", font=get_font(11, bold=True))

    # Validation accuracy curve (Green)
    pts_val = []
    for ep in range(50):
        gx = 740 + int(ep * 9.2)
        gy = int(570 - 165 * (1 - math.exp(-ep / 9)) + (math.sin(ep) * 4))
        pts_val.append((gx, gy))
    draw.line(pts_val, fill="#34d399", width=3)
    draw.text((1120, 405), "● Val Acc (92.4%)", fill="#34d399", font=get_font(11, bold=True))

    save_both(im, "kt-ai-station/deepfake/correct.webp")

def gen_deepfake_result():
    # 06 Diagnostic Report
    im, draw = draw_cyber_base(title="CLINICAL DIAGNOSTIC REPORT // DISPATCH READY", category="EXPORT CENTER")

    # Document wrapper
    draw.rounded_rectangle([180, 85, 1100, 650], radius=14, fill="#0d1424", outline="#2563eb", width=2)

    # Document Header
    draw.rectangle([182, 87, 1098, 160], fill="#111c33")
    draw.text((220, 105), "NEUROLOGICAL ONCOLOGY AI DIAGNOSIS SUMMARY", fill="#f8fafc", font=get_font(18, bold=True))
    draw.text((220, 134), "BABU BANARASI DAS UNIVERSITY AI RESEARCH INITIATIVE | REPORT ID: #DL-2026-0982", fill="#38bdf8", font=get_font(11, bold=True))

    # Patient info grid
    draw.rectangle([220, 180, 1060, 240], fill="#070c18", outline="#1e293b")
    draw.text((240, 195), "PATIENT IDENTIFIER:", fill="#64748b", font=get_font(11))
    draw.text((240, 215), "ANON_83921 (AGE: 47, M)", fill="#f8fafc", font=get_font(13, bold=True))

    draw.text((500, 195), "SCAN MODALITY:", fill="#64748b", font=get_font(11))
    draw.text((500, 215), "3.0T MRI (Axial T1+C / T2)", fill="#f8fafc", font=get_font(13, bold=True))

    draw.text((780, 195), "DATE OF INFERENCE:", fill="#64748b", font=get_font(11))
    draw.text((780, 215), "OCTOBER 2026 • 22:45 UTC", fill="#f8fafc", font=get_font(13, bold=True))

    # Diagnosis Block (Red critical alert)
    draw.rounded_rectangle([220, 260, 1060, 390], radius=10, fill="#1c0b11", outline="#ef4444", width=2)
    draw.text((250, 280), "PREDICTED DIAGNOSIS: HIGH-GRADE GLIOMA DETECTED", fill="#f43f5e", font=get_font(18, bold=True))
    draw.text((250, 312), "Confidence Level: 94.2%  •  Uncertainty Variance: ±0.8%  •  Severity: Urgent Clinical Evaluation", fill="#fca5a5", font=get_font(13))
    draw.text((250, 342), "Location: Left temporoparietal lobe with noticeable peri-tumoral edema and mass effect.", fill="#cbd5e1", font=get_font(12))

    # Recommendation and physician notes
    draw.rounded_rectangle([220, 410, 1060, 520], radius=8, fill="#070c18", outline="#1e293b")
    draw.text((240, 425), "AI CLINICAL RECOMMENDATION PROTOCOL:", fill="#38bdf8", font=get_font(12, bold=True))
    draw.text((240, 450), "1. Immediate contrast-enhanced MRI spectroscopy validation.", fill="#94a3b8", font=get_font(12))
    draw.text((240, 472), "2. Neurosurgical consultation for stereotactic biopsy evaluation.", fill="#94a3b8", font=get_font(12))
    draw.text((240, 494), "3. Differential review against low-grade astrocytoma sub-types.", fill="#94a3b8", font=get_font(12))

    # Action Buttons
    draw.rounded_rectangle([220, 550, 520, 610], radius=8, fill="#2563eb")
    draw.text((370, 580), "EXPORT OFFICIAL PDF REPORT ↗", fill="#ffffff", font=get_font(13, bold=True), anchor="mm")

    draw.rounded_rectangle([550, 550, 850, 610], radius=8, fill="#0d1424", outline="#3b82f6", width=1)
    draw.text((700, 580), "TRANSFER DICOM TO PACS SERVER", fill="#60a5fa", font=get_font(13, bold=True), anchor="mm")

    draw.text((950, 580), "VERIFIED V4.2 ✓", fill="#10b981", font=get_font(14, bold=True), anchor="mm")

    save_both(im, "kt-ai-station/deepfake/result.webp")

# =========================================================================
# 2. EDUTECH AI (kt-ai-station/fakenews/*)
# =========================================================================

def gen_fakenews_screens():
    # start: Virtual Classroom
    im, draw = draw_cyber_base(title="EDUTECH AI // VIRTUAL CLASSROOM HUD", category="GROQ LLM SAAS")
    # Video HUD
    draw.rounded_rectangle([40, 85, 780, 520], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.rectangle([60, 105, 760, 460], fill="#040711", outline="#334155")
    # Video play button simulated
    draw.ellipse([380, 250, 440, 310], fill="#2563eb")
    draw.polygon([(402, 268), (402, 292), (424, 280)], fill="#ffffff")
    draw.text((410, 335), "YOUTUBE PLAYLIST SYNC // 500+ LECTURES", fill="#94a3b8", font=get_font(13, bold=True), anchor="mm")
    draw.text((60, 485), "▶ [00:42:15 / 01:15:00] Data Structures & Algorithms — Lecture 14", fill="#e2e8f0", font=get_font(12, bold=True))

    # Right side: Real-time AI Note Generator
    draw.rounded_rectangle([810, 85, 1240, 650], radius=10, fill="#0d1424", outline="#1e293b", width=1)
    draw.text((830, 110), "GROQ LLAMA 3.1 REAL-TIME SUMMARY", fill="#38bdf8", font=get_font(14, bold=True))
    draw.text((830, 132), "Generating key concepts at 750 tokens/sec", fill="#64748b", font=get_font(11))
    
    notes = [
        "1. Dynamic Programming Memoization Matrix initialized.",
        "2. Time Complexity reduced from O(2^N) to O(N*W).",
        "3. Space Complexity optimal with 1D row array.",
        "4. Auto-generated Quiz: 5 questions ready."
    ]
    ny = 170
    for n in notes:
        draw.rounded_rectangle([830, ny, 1220, ny + 50], radius=6, fill="#070c18", outline="#1e293b")
        draw.text((845, ny + 15), n, fill="#cbd5e1", font=get_font(11))
        ny += 60

    # Bottom left: Student chat prompt
    draw.rounded_rectangle([40, 545, 780, 650], radius=10, fill="#0d1424", outline="#1e293b", width=1)
    draw.text((60, 565), "ASK HINGLISH AI TUTOR:", fill="#10b981", font=get_font(12, bold=True))
    draw.rounded_rectangle([60, 590, 680, 630], radius=6, fill="#070c18", outline="#334155")
    draw.text((75, 603), "Bhai yeh knapsack problem ka base case ek baar aur explain krdo...", fill="#94a3b8", font=get_font(12))
    draw.rounded_rectangle([700, 590, 760, 630], radius=6, fill="#10b981")
    draw.text((730, 610), "SEND", fill="#000000", font=get_font(11, bold=True), anchor="mm")

    save_both(im, "kt-ai-station/fakenews/start.webp")

    # opening: Groq LLM AI Tutor
    im, draw = draw_cyber_base(title="GROQ LLM AI TUTOR (LLAMA 3.1 8B)", category="STREAMING AI CHAT")
    draw.rounded_rectangle([120, 85, 1160, 650], radius=12, fill="#0d1424", outline="#8b5cf6", width=1)
    # Chat bubbles
    # User message
    draw.rounded_rectangle([600, 120, 1120, 185], radius=10, fill="#1e1b4b", outline="#8b5cf6")
    draw.text((620, 135), "Ajay (Student)", fill="#c084fc", font=get_font(12, bold=True))
    draw.text((620, 155), "Can you write an optimized DP solution for 0/1 Knapsack in Python?", fill="#f8fafc", font=get_font(13))

    # AI Tutor message
    draw.rounded_rectangle([150, 215, 950, 520], radius=10, fill="#070c18", outline="#2563eb")
    draw.text((170, 230), "Groq AI Tutor (Llama 3.1 8B @ 820 tok/sec)", fill="#38bdf8", font=get_font(12, bold=True))
    draw.text((170, 255), "Zaroor! Yeh raha space-optimized O(W) solution:", fill="#cbd5e1", font=get_font(13))
    # Code block
    draw.rectangle([170, 285, 930, 460], fill="#02040a", outline="#334155")
    code = [
        "def knapSack(W, wt, val, n):",
        "    dp = [0] * (W + 1)",
        "    for i in range(n):",
        "        for w in range(W, wt[i] - 1, -1):",
        "            dp[w] = max(dp[w], dp[w - wt[i]] + val[i])",
        "    return dp[W]  # O(N*W) time, O(W) auxiliary space"
    ]
    cy = 298
    for line in code:
        draw.text((190, cy), line, fill="#34d399", font=get_font(12))
        cy += 24
    draw.text((170, 480), "Isme space complexity O(N*W) se reduce hoke sirf O(W) ho gayi!", fill="#94a3b8", font=get_font(12))

    save_both(im, "kt-ai-station/fakenews/opening.webp")

    # intro: Pomodoro Focus Space
    im, draw = draw_cyber_base(title="CYBERPUNK POMODORO FOCUS ROOM", category="PRODUCTIVITY LAB")
    # Circular Timer in center
    cx, cy = 640, 320
    # Outer glowing track
    draw.ellipse([cx - 160, cy - 160, cx + 160, cy + 160], outline="#1e293b", width=14)
    draw.arc([cx - 160, cy - 160, cx + 160, cy + 160], start=-90, end=140, fill="#38bdf8", width=14)
    # Timer text
    draw.text((cx, cy - 30), "24:18", fill="#f8fafc", font=get_font(60, bold=True), anchor="mm")
    draw.text((cx, cy + 35), "FOCUS INTERVAL • STREAK: 4/4", fill="#38bdf8", font=get_font(13, bold=True), anchor="mm")
    draw.text((cx, cy + 60), "Bina distract hue DSA lecture finish karein", fill="#64748b", font=get_font(11), anchor="mm")

    # Audio widget bottom
    draw.rounded_rectangle([340, 520, 940, 620], radius=10, fill="#0d1424", outline="#1e293b")
    draw.text((365, 545), "LO-FI CYBER AMBIENT // BINAURAL BEATS 432Hz", fill="#10b981", font=get_font(13, bold=True))
    draw.text((365, 570), "Volume: 80% • Noise isolation active • Rain soundscape", fill="#64748b", font=get_font(11))
    # Sound waveform bars
    wx = 750
    for h_b in [12, 28, 44, 30, 18, 42, 50, 34, 20, 38, 45, 22]:
        draw.rounded_rectangle([wx, 580 - h_b // 2, wx + 8, 580 + h_b // 2], radius=2, fill="#38bdf8")
        wx += 14

    save_both(im, "kt-ai-station/fakenews/intro.webp")

    # choose: Automated Certificate Engine
    im, draw = draw_cyber_base(title="REPORTLAB DYNAMIC PDF CERTIFICATE GENERATOR", category="CREDENTIAL ENGINE")
    # Certificate mockup sheet
    draw.rounded_rectangle([240, 90, 1040, 640], radius=14, fill="#0a1226", outline="#f59e0b", width=2)
    draw.rectangle([255, 105, 1025, 625], outline="#1e3a8a", width=1)
    draw.text((640, 160), "CERTIFICATE OF ACHIEVEMENT", fill="#f59e0b", font=get_font(24, bold=True), anchor="mm")
    draw.text((640, 200), "THIS IS PROUDLY PRESENTED TO", fill="#64748b", font=get_font(12, bold=True), anchor="mm")
    draw.text((640, 250), "AJAY VISHWAKARMA", fill="#f8fafc", font=get_font(34, bold=True), anchor="mm")
    draw.text((640, 295), "For successfully mastering the Advanced AI & Machine Learning Specialization", fill="#94a3b8", font=get_font(13), anchor="mm")
    draw.text((640, 320), "Covering TensorFlow, Groq LLM pipelines, Django REST, and Neural Architecture Design", fill="#64748b", font=get_font(11), anchor="mm")

    # Verification block
    draw.rectangle([340, 380, 940, 470], fill="#040817", outline="#334155")
    draw.text((360, 400), "CRYPTOGRAPHIC PROOF ID: #CERT-EDUTECH-92841-VERIFIED", fill="#38bdf8", font=get_font(11, bold=True))
    draw.text((360, 422), "SHA-256: 8f2b3e9a1c4d8e7f0b5a6c1e9d2f4a3b7c8e9f0a1b2c3d4e5f6a7b8c9d0e1f2", fill="#475569", font=get_font(10))
    draw.text((360, 444), "VERIFICATION URL: https://edu-tech-ai-vk2e.onrender.com/verify/92841", fill="#10b981", font=get_font(11))

    # Signatures
    draw.line([(340, 560), (540, 560)], fill="#64748b", width=1)
    draw.text((440, 575), "BBD University AI Lab", fill="#94a3b8", font=get_font(11), anchor="mm")
    draw.line([(740, 560), (940, 560)], fill="#64748b", width=1)
    draw.text((840, 575), "Lead Engineering Instructor", fill="#94a3b8", font=get_font(11), anchor="mm")

    save_both(im, "kt-ai-station/fakenews/choose.webp")

# =========================================================================
# 3. SKILLPROOF (kt-ai-station/dcti/*)
# =========================================================================

def gen_dcti_screens():
    # start: Monaco Code Editor
    im, draw = draw_cyber_base(title="MONACO CODE EDITOR // REACT 19 & ZUSTAND", category="DEVELOPER IDE")
    # VS Code dark interface
    draw.rounded_rectangle([40, 85, 1240, 650], radius=10, fill="#0f172a", outline="#334155")
    # Tabs bar
    draw.rectangle([40, 85, 1240, 125], fill="#1e293b")
    draw.rectangle([40, 85, 200, 125], fill="#0f172a")
    draw.text((70, 105), "solution.ts", fill="#38bdf8", font=get_font(12, bold=True))
    draw.text((220, 105), "test_suite.py", fill="#64748b", font=get_font(12))
    draw.text((340, 105), "schema.sql", fill="#64748b", font=get_font(12))

    # Editor area with line numbers
    draw.rectangle([40, 125, 90, 650], fill="#0b0f19")
    for i in range(1, 19):
        draw.text((65, 140 + (i-1)*26), str(i), fill="#475569", font=get_font(12), anchor="mm")

    code_lines = [
        ("import { Engine, Pipeline } from '@skillproof/core';", "#c084fc"),
        ("", "#ffffff"),
        ("export class SystemEvaluator {", "#60a5fa"),
        ("  private cache = new Map<string, ExecutionResult>();", "#e2e8f0"),
        ("", "#ffffff"),
        ("  async benchmark(candidateCode: string): Promise<Report> {", "#60a5fa"),
        ("    const ast = parseAbstractSyntaxTree(candidateCode);", "#e2e8f0"),
        ("    const complexity = calculateCyclomaticComplexity(ast);", "#e2e8f0"),
        ("    const sandbox = await Sandbox.spawn({ timeoutMs: 3000 });", "#38bdf8"),
        ("    const results = await sandbox.runAllUnitTests();", "#34d399"),
        ("    return { score: complexity.score, passed: results.allPassed };", "#f59e0b"),
        ("  }", "#60a5fa"),
        ("}", "#60a5fa")
    ]
    cy = 140
    for line, col in code_lines:
        draw.text((110, cy), line, fill=col, font=get_font(13))
        cy += 26

    # Right execution console
    draw.rectangle([800, 125, 1240, 650], fill="#080c16", outline="#1e293b")
    draw.text((820, 145), "TERMINAL EXECUTION // PASS 12/12", fill="#10b981", font=get_font(13, bold=True))
    terminal_out = [
        "✓ test_basic_input (3ms)",
        "✓ test_boundary_conditions (8ms)",
        "✓ test_large_array_performance (14ms)",
        "✓ test_memory_leak_prevention (11ms)",
        "------------------------------------",
        "ALL 12 TESTS PASSED SUCCESSFULLY",
        "EXECUTION TIME: 42ms | CPU: 2.1%",
        "STATUS: VERIFIED ON-CHAIN PROOF"
    ]
    ty = 180
    for t in terminal_out:
        col = "#34d399" if "✓" in t or "ALL" in t else "#94a3b8"
        draw.text((820, ty), t, fill=col, font=get_font(12))
        ty += 28

    save_both(im, "kt-ai-station/dcti/start.webp")

    # intro: AI Code Analysis
    im, draw = draw_cyber_base(title="ABSTRACT SYNTAX TREE & VULNERABILITY SCANNER", category="CODE INTELLIGENCE")
    # 3 analysis panels
    panes = [
        ("AST SYNTAX TREE", "Tree Depth: 8 | 148 Nodes", [("Program", "#38bdf8"), ("ClassDeclaration", "#60a5fa"), ("MethodDefinition", "#a855f7"), ("BinaryExpression", "#34d399")]),
        ("COMPLEXITY ANALYSIS", "Cyclomatic Index: 4 (Optimal)", [("Cyclomatic Complexity: 4", "#10b981"), ("Cognitive Complexity: 2", "#10b981"), ("Maintainability Index: 92/100", "#38bdf8"), ("Halstead Volume: Low", "#94a3b8")]),
        ("SECURITY SCANNER", "Zero Vulnerabilities Detected", [("SQL Injection Risk: 0%", "#10b981"), ("XSS Vectors: None", "#10b981"), ("Regex ReDoS Safe", "#10b981"), ("Dependency Vulnerabilities: 0", "#10b981")])
    ]
    px = 40
    for p_title, p_sub, items in panes:
        draw.rounded_rectangle([px, 90, px + 380, 650], radius=10, fill="#0d1424", outline="#1e293b")
        draw.text((px + 20, 115), p_title, fill="#f8fafc", font=get_font(15, bold=True))
        draw.text((px + 20, 138), p_sub, fill="#38bdf8", font=get_font(12))
        iy = 180
        for item_t, col in items:
            draw.rounded_rectangle([px + 20, iy, px + 360, iy + 65], radius=6, fill="#070c18", outline="#1e293b")
            draw.text((px + 35, iy + 25), item_t, fill=col, font=get_font(13, bold=True))
            iy += 80
        px += 410

    save_both(im, "kt-ai-station/dcti/intro.webp")

    # user: Student Skill Dashboard
    im, draw = draw_cyber_base(title="STUDENT RADAR SKILL MATRIX // GLOBAL RANK #14", category="TALENT ANALYTICS")
    # Radar chart simulated
    draw.rounded_rectangle([40, 90, 620, 650], radius=10, fill="#0d1424", outline="#2563eb")
    draw.text((64, 115), "COMPETENCY RADAR (6 CORE PILLARS)", fill="#f8fafc", font=get_font(16, bold=True))
    draw.text((64, 138), "Assessed via 80+ dynamic code challenges", fill="#64748b", font=get_font(12))
    # Radar hexagon
    cx, cy = 330, 380
    for r in [200, 150, 100, 50]:
        pts = [(cx + r * math.cos(i * math.pi / 3), cy + r * math.sin(i * math.pi / 3)) for i in range(6)]
        draw.polygon(pts, outline="#1e293b", fill=None)
    # Skill fill polygon
    skill_r = [180, 160, 190, 170, 150, 185]
    s_pts = [(cx + skill_r[i] * math.cos(i * math.pi / 3), cy + skill_r[i] * math.sin(i * math.pi / 3)) for i in range(6)]
    draw.polygon(s_pts, fill="#1d4ed855", outline="#38bdf8", width=2)
    # Labels
    labels = ["Algorithms", "Data Structures", "System Design", "Database", "REST APIs", "Clean Code"]
    for i, l in enumerate(labels):
        lx = cx + 225 * math.cos(i * math.pi / 3)
        ly = cy + 225 * math.sin(i * math.pi / 3)
        draw.text((lx, ly), l, fill="#f8fafc", font=get_font(11, bold=True), anchor="mm")

    # Right side rank & stats
    draw.rounded_rectangle([660, 90, 1240, 650], radius=10, fill="#0d1424", outline="#1e293b")
    draw.text((684, 115), "GLOBAL LEADERBOARD & CREDENTIALS", fill="#f8fafc", font=get_font(16, bold=True))
    draw.text((684, 138), "Top 1% Percentile in Problem Solving & Algorithmic Design", fill="#10b981", font=get_font(12))
    
    leaders = [
        ("#14", "Ajay Vishwakarma", "98.4 Rating", "BBD University"),
        ("#15", "Kavya Sharma", "97.9 Rating", "IIT Delhi"),
        ("#16", "Rohan Mehta", "97.4 Rating", "NIT Trichy"),
        ("#17", "Aarav Patel", "96.8 Rating", "BITS Pilani")
    ]
    ly = 180
    for rank, name_l, rating, clg in leaders:
        is_user = "#14" in rank
        bg = "#1e3a8a" if is_user else "#070c18"
        border = "#38bdf8" if is_user else "#1e293b"
        draw.rounded_rectangle([684, ly, 1216, ly + 65], radius=8, fill=bg, outline=border)
        draw.text((710, ly + 22), rank, fill="#38bdf8", font=get_font(16, bold=True))
        draw.text((770, ly + 15), name_l, fill="#f8fafc", font=get_font(14, bold=True))
        draw.text((770, ly + 36), clg, fill="#94a3b8", font=get_font(11))
        draw.text((1190, ly + 25), rating, fill="#34d399", font=get_font(14, bold=True), anchor="rm")
        ly += 80

    save_both(im, "kt-ai-station/dcti/user.webp")

    # result: Verified Portfolio Output
    im, draw = draw_cyber_base(title="VERIFIED STUDENT PORTFOLIO OUTPUT", category="PUBLIC CREDENTIAL")
    draw.rounded_rectangle([180, 90, 1100, 650], radius=12, fill="#0d1424", outline="#10b981", width=2)
    draw.text((220, 120), "SKILLPROOF VERIFIED DEVELOPER PROFILE", fill="#10b981", font=get_font(18, bold=True))
    draw.text((220, 150), "Permanent Public URL: https://skillproof-eight.vercel.app/p/ajay160380", fill="#38bdf8", font=get_font(13))

    # Grid of verified skills
    skills_v = [
        ("PYTHON & DJANGO ARCHITECTURE", "VERIFIED EXPERT", "#10b981"),
        ("TENSORFLOW & DEEP LEARNING", "VERIFIED ADVANCED", "#38bdf8"),
        ("REACT 19 & TYPESCRIPT FRONTEND", "VERIFIED PROFICIENT", "#a855f7"),
        ("POSTGRESQL & REST API DESIGN", "VERIFIED ADVANCED", "#f59e0b")
    ]
    sy = 200
    for s_name, s_lvl, col in skills_v:
        draw.rounded_rectangle([220, sy, 1060, sy + 65], radius=8, fill="#070c18", outline="#1e293b")
        draw.text((245, sy + 22), s_name, fill="#f8fafc", font=get_font(14, bold=True))
        draw.text((1035, sy + 22), s_lvl, fill=col, font=get_font(12, bold=True), anchor="rm")
        sy += 80

    draw.rounded_rectangle([220, 540, 540, 600], radius=8, fill="#10b981")
    draw.text((380, 570), "OPEN LIVE VERCEL PROFILE ↗", fill="#000000", font=get_font(13, bold=True), anchor="mm")

    save_both(im, "kt-ai-station/dcti/result.webp")

    # type-dca: Live Code Execution
    im, draw = draw_cyber_base(title="REAL-TIME SANDBOX CODE EXECUTION ENGINE", category="SANDBOX RUNNER")
    draw.rounded_rectangle([80, 90, 1200, 650], radius=12, fill="#090d16", outline="#3b82f6")
    draw.text((110, 120), "DOCKER SANDBOX ISOLATION // ZERO NETWORK ESCAPE", fill="#38bdf8", font=get_font(15, bold=True))
    draw.rectangle([110, 150, 1170, 610], fill="#020409", outline="#334155")
    # Terminal text
    logs = [
        "$ skillproof-runner exec --runtime=node20 --memory=128mb --timeout=2000ms",
        "[*] Compiling TypeScript source to JavaScript (ES2022)...",
        "[+] Compilation successful in 18ms.",
        "[*] Spawning microVM jail [ID: 9a8f-28c1-4821]...",
        "[+] microVM ready in 9ms. Memory ceiling: 128MB. Network: disabled.",
        "",
        "RUNNING UNIT TEST SUITE (18 TEST CASES):",
        "----------------------------------------------------------",
        " PASS  test/fibonacci_dp.test.ts",
        "  ✓ calculates F(10) in 0.12ms",
        "  ✓ handles maximum integer overflow gracefully in 0.18ms",
        "  ✓ recursion stack depth remains bounded within O(N)",
        "",
        "TEST RESULTS: 18 passed, 0 failed. Execution time: 41ms.",
        "STATUS: MEMORY USAGE 18.4MB / 128MB ceiling (14.3%)"
    ]
    ly = 170
    for l in logs:
        col = "#34d399" if "✓" in l or "PASS" in l else ("#38bdf8" if "$" in l or "[+]" in l else "#94a3b8")
        draw.text((130, ly), l, fill=col, font=get_font(12))
        ly += 22

    save_both(im, "kt-ai-station/dcti/type-dca.webp")

    # type-dsa: AI Real-time Feedback
    im, draw = draw_cyber_base(title="INLINE CODE REVIEW & TIME COMPLEXITY HINTS", category="AI FEEDBACK")
    draw.rounded_rectangle([100, 90, 1180, 650], radius=12, fill="#0d1424", outline="#8b5cf6")
    draw.text((130, 120), "AI AUTOMATED INLINE CODE REVIEW SUGGESTION", fill="#c084fc", font=get_font(16, bold=True))
    draw.text((130, 145), "Detected O(N^2) nested loop in array filter. Refactoring recommended.", fill="#94a3b8", font=get_font(13))

    # Diff block
    draw.rectangle([130, 180, 1150, 480], fill="#070c18", outline="#334155")
    diffs = [
        ("-  // Suboptimal O(N^2) linear lookup:", "#ef4444"),
        ("-  const matches = items.filter(i => lookupArr.includes(i.id));", "#ef4444"),
        ("", "#ffffff"),
        ("+  // Optimized O(N) hash set lookup:", "#10b981"),
        ("+  const lookupSet = new Set(lookupArr);", "#10b981"),
        ("+  const matches = items.filter(i => lookupSet.has(i.id));", "#10b981"),
        ("", "#ffffff"),
        ("AI SUMMARY: Reduces algorithmic complexity from O(N*M) to O(N+M).", "#38bdf8"),
        ("Performance gain on 100,000 items: ~1,200x faster execution.", "#38bdf8")
    ]
    dy = 200
    for line, col in diffs:
        draw.text((150, dy), line, fill=col, font=get_font(13, bold=True if ("+" in line or "-" in line) else False))
        dy += 26

    # Action pill
    draw.rounded_rectangle([130, 510, 480, 560], radius=8, fill="#8b5cf6")
    draw.text((305, 535), "ACCEPT & APPLY REFACTORING ✓", fill="#ffffff", font=get_font(13, bold=True), anchor="mm")

    save_both(im, "kt-ai-station/dcti/type-dsa.webp")

# =========================================================================
# 4. SITE DEPLOYMENT SCREENS (kt-ai-station/site/*)
# =========================================================================

def gen_site_screens():
    # station: EduTech AI deployed
    im, draw = draw_cyber_base(title="EDUTECH AI // RENDER & HUGGINGFACE LIVE DEPLOYMENT", category="CLOUD INFRASTRUCTURE")
    draw.rounded_rectangle([60, 90, 1220, 650], radius=12, fill="#0d1424", outline="#10b981")
    draw.text((90, 120), "PRODUCTION SYSTEM HEALTH: 100% OPERATIONAL", fill="#10b981", font=get_font(16, bold=True))
    draw.text((90, 145), "Live URL: https://edu-tech-ai-vk2e.onrender.com/  •  HuggingFace Space Active", fill="#38bdf8", font=get_font(13))

    # Cluster metrics
    cards = [
        ("UPTIME", "99.98%", "Last 90 days", "#10b981"),
        ("ACTIVE SESSIONS", "1,420", "Live students", "#38bdf8"),
        ("API LATENCY", "124ms", "P95 response time", "#a855f7"),
        ("DATABASE", "Neon PG", "Serverless connected", "#f59e0b")
    ]
    cx = 90
    for t_c, v_c, s_c, col_c in cards:
        draw.rounded_rectangle([cx, 190, cx + 245, 330], radius=8, fill="#070c18", outline="#1e293b")
        draw.text((cx + 20, 215), t_c, fill="#64748b", font=get_font(12, bold=True))
        draw.text((cx + 20, 245), v_c, fill=col_c, font=get_font(32, bold=True))
        draw.text((cx + 20, 290), s_c, fill="#94a3b8", font=get_font(11))
        cx += 270

    # Traffic Graph
    draw.rounded_rectangle([90, 360, 1190, 610], radius=10, fill="#070c18", outline="#1e293b")
    draw.text((115, 385), "LIVE TRAFFIC THROUGHPUT & GROQ API CALLS (LAST 24 HOURS)", fill="#f8fafc", font=get_font(14, bold=True))
    # Simulated traffic line
    draw.line([(120, 560), (1160, 560)], fill="#334155", width=1)
    pts = []
    for x in range(120, 1160, 20):
        val = math.sin((x - 120) / 70) * 40 + math.cos((x - 120) / 30) * 20
        pts.append((x, int(500 - val)))
    draw.line(pts, fill="#38bdf8", width=3)
    save_both(im, "kt-ai-station/site/station.webp")

    # dcti: SkillProof live on Vercel
    im, draw = draw_cyber_base(title="SKILLPROOF LIVE ON VERCEL EDGE NETWORK", category="FRONTEND EDGE")
    draw.rounded_rectangle([80, 90, 1200, 650], radius=12, fill="#0d1424", outline="#2563eb")
    draw.text((110, 120), "VERCEL EDGE NETWORK DEPLOYMENT", fill="#38bdf8", font=get_font(16, bold=True))
    draw.text((110, 145), "Live URL: https://skillproof-eight.vercel.app  •  Global CDN Active", fill="#94a3b8", font=get_font(13))
    # Vercel deployment card
    draw.rounded_rectangle([110, 190, 1170, 590], radius=10, fill="#070c18", outline="#1e293b")
    draw.text((140, 220), "DEPLOYMENT SUMMARY: production-eight (Ready in 34s)", fill="#f8fafc", font=get_font(15, bold=True))
    draw.text((140, 250), "Git Commit: feat(monaco): add real-time websocket test evaluation", fill="#64748b", font=get_font(12))
    draw.text((140, 280), "Framework: Next.js 14 (App Router) + Tailwind CSS + Monaco Core", fill="#38bdf8", font=get_font(12))
    draw.text((140, 310), "Edge Middleware: Auth verification @ 12ms latency", fill="#10b981", font=get_font(12))
    save_both(im, "kt-ai-station/site/dcti.webp")

    # fakenews: Brain Tumor Detection Streamlit
    im, draw = draw_cyber_base(title="BRAIN TUMOR DETECTION STREAMLIT CLOUD DEPLOYMENT", category="STREAMLIT CLOUD")
    draw.rounded_rectangle([80, 90, 1200, 650], radius=12, fill="#0d1424", outline="#f43f5e")
    draw.text((110, 120), "STREAMLIT CLOUD APPLICATION HOSTING", fill="#f43f5e", font=get_font(16, bold=True))
    draw.text((110, 145), "Live URL: https://neuro-detection.streamlit.app  •  Streamlit Community Cloud", fill="#94a3b8", font=get_font(13))
    # Streamlit app layout
    draw.rounded_rectangle([110, 190, 1170, 590], radius=10, fill="#070c18", outline="#1e293b")
    draw.text((140, 220), "STREAMLIT APP ARCHITECTURE & TENSOR PIPELINE", fill="#f8fafc", font=get_font(15, bold=True))
    draw.text((140, 250), "Python 3.11  •  TensorFlow 2.16  •  OpenCV-headless  •  Plotly Interactive Graphs", fill="#64748b", font=get_font(12))
    draw.text((140, 280), "Instant File Drag-and-Drop  •  Grad-CAM Layer Visualizer  •  Downloadable Clinical PDF", fill="#38bdf8", font=get_font(12))
    draw.text((140, 310), "Active Container Memory: 1.2 GB / 2.0 GB allocated", fill="#10b981", font=get_font(12))
    save_both(im, "kt-ai-station/site/fakenews.webp")

# =========================================================================
# 5. BOOKING SYSTEM & OTHER PROJECTS
# =========================================================================

def gen_booking_screens():
    items = [
        ("booking-system/admin-dashboard.webp", "ENTERPRISE RESERVATION MATRIX", "ADMIN DASHBOARD"),
        ("booking-system/admin-reservations.webp", "REAL-TIME VISITOR BOOKING ROSTER", "RESERVATIONS"),
        ("booking-system/admin-settings.webp", "VENUE CAPACITY & MULTI-SLOT CONFIG", "SYSTEM SETTINGS"),
        ("booking-system/admin-statistics.webp", "HOURLY FOOTFALL & ATTENDANCE ANALYTICS", "METRICS"),
        ("booking-system/visitor-form.webp", "INSTANT MOBILE RESERVATION FORM", "VISITOR FORM"),
        ("booking-system/visitor-times.webp", "LIVE TIME SLOT GRID // REAL-TIME SEATS", "TIME SELECTION"),
        ("booking-system/visitor-titles.webp", "EXHIBITION PROGRAM CATALOG // 3D TOUR", "EXHIBITION"),
        ("booking-system/visitor-done.webp", "DIGITAL NFC PASS WITH CRYPTO QR", "RESERVATION PASS"),
        ("booking-system/loop-poster.webp", "AUTOMATED VENUE MANAGEMENT SYSTEM", "OVERVIEW")
    ]
    for rel_path, title, cat in items:
        im, draw = draw_cyber_base(title=title, category=cat)
        # Content box
        draw.rounded_rectangle([60, 90, 1220, 650], radius=12, fill="#0d1424", outline="#2563eb", width=1)
        draw.text((90, 125), f"{title} // SYSTEM VIEW", fill="#f8fafc", font=get_font(18, bold=True))
        draw.text((90, 155), f"Category: {cat} • Full-bleed verified interface • Responsive 16:9 view", fill="#38bdf8", font=get_font(13))
        # Draw some mock data cards
        for i in range(3):
            cx = 90 + i * 370
            draw.rounded_rectangle([cx, 200, cx + 340, 400], radius=8, fill="#070c18", outline="#1e293b")
            draw.text((cx + 20, 225), f"SECTION {i+1}: {cat}", fill="#94a3b8", font=get_font(12, bold=True))
            draw.text((cx + 20, 260), f"Active Parameter #{i+1}", fill="#f8fafc", font=get_font(16, bold=True))
            draw.text((cx + 20, 290), "Synchronized with PostgreSQL database", fill="#64748b", font=get_font(11))
            draw.rounded_rectangle([cx + 20, 330, cx + 320, 360], radius=4, fill="#1e293b")
            draw.rounded_rectangle([cx + 20, 330, cx + 180 + i * 40, 360], radius=4, fill="#2563eb")
        
        draw.rounded_rectangle([90, 440, 1190, 610], radius=8, fill="#070c18", outline="#1e293b")
        draw.text((115, 470), "LIVE TRANSACTION STREAM // WEBSOCKET FEED", fill="#10b981", font=get_font(13, bold=True))
        draw.text((115, 505), "• [22:42:01] Reservation #BK-9021 confirmed for 4 visitors.", fill="#cbd5e1", font=get_font(12))
        draw.text((115, 535), "• [22:42:14] QR pass generated and dispatched via WhatsApp bot.", fill="#cbd5e1", font=get_font(12))
        draw.text((115, 565), "• [22:42:30] Venue capacity at 78% of maximum safety threshold.", fill="#cbd5e1", font=get_font(12))

        save_both(im, rel_path)

def gen_other_projects():
    others = [
        ("i-am-solo/camera.webp", "AI CAMERA TRACKING // 3D POSE ESTIMATION", "VISION LAB"),
        ("i-am-solo/characters.webp", "CHARACTER RECOGNITION & BIOMETRICS", "BIOMETRICS"),
        ("i-am-solo/gender.webp", "DEMOGRAPHIC & GENDER AI INFERENCE", "CLASSIFIER"),
        ("i-am-solo/performances.webp", "REAL-TIME PERFORMANCE TELEMETRY", "METRICS"),
        ("i-am-solo/profile.webp", "CANDIDATE BIOMETRIC PROFILE", "PROFILE"),
        ("i-am-solo/site.webp", "AI SURVEILLANCE SUITE LIVE", "DEPLOYED"),
        ("i-am-solo/start.webp", "AUTONOMOUS VISION SYSTEM HUD", "VISION"),
        ("jimssalabium/guide.webp", "AUGMENTED REALITY INTERACTIVE GUIDE", "AR LAB"),
        ("jimssalabium/result.webp", "AR SPATIAL LOCALIZATION OUTPUT", "RESULT"),
        ("jimssalabium/scan.webp", "SPATIAL SLAM SCANNER MATRIX", "SLAM"),
        ("jimssalabium/start.webp", "AR DIGITAL ASSISTANT INTERFACE", "AR ASSIST"),
        ("millie-genre-me/book.webp", "NLP LITERARY GENRE CLASSIFIER", "NLP"),
        ("millie-genre-me/site.webp", "BOOK TRANSLATION ENGINE LIVE", "DEPLOYED"),
        ("millie-genre-me/start.webp", "GROQ TRANSLATION PIPELINE", "TRANSLATION"),
        ("millie-genre-me/test.webp", "EVALUATION & BLEU BENCHMARK", "METRICS"),
        ("todays-picnic/destination.webp", "AI TRAVEL DESTINATION RECOMMENDER", "RECOMMENDER"),
        ("todays-picnic/guide.webp", "DYNAMIC WEATHER & ROUTE PLANNER", "ROUTING"),
        ("todays-picnic/intro.webp", "TRAVEL COMPANION INTERFACE", "ASSISTANT"),
        ("todays-picnic/question.webp", "PREFERENCE ELICITATION ENGINE", "PREFERENCES"),
        ("todays-picnic/result-film.webp", "GENERATED ITINERARY COMPILATION", "ITINERARY"),
        ("wis-2026/flow-loop-en.webp", "AUTONOMOUS DRONE SURVEILLANCE", "DRONE AI"),
        ("wis-2026/flow-loop.webp", "REAL-TIME EDGE AI SURVEILLANCE", "EDGE COMPUTING"),
        ("wis-2026/settings.webp", "DRONE MISSION TELEMETRY & CONTROLS", "MISSION CONTROL"),
        ("wis-2026/site.webp", "AUTONOMOUS AI SUITE DEPLOYMENT", "DEPLOYED")
    ]
    for rel_path, title, cat in others:
        im, draw = draw_cyber_base(title=title, category=cat)
        draw.rounded_rectangle([60, 90, 1220, 650], radius=12, fill="#0d1424", outline="#2563eb", width=1)
        draw.text((90, 125), title, fill="#f8fafc", font=get_font(18, bold=True))
        draw.text((90, 155), f"Category: {cat} • Ajay Vishwakarma Core Project • Edge-to-edge frame fit", fill="#38bdf8", font=get_font(13))
        # Draw mock dashboard elements
        draw.rounded_rectangle([90, 200, 620, 610], radius=8, fill="#070c18", outline="#1e293b")
        draw.text((115, 225), "PRIMARY SYSTEM TELEMETRY", fill="#10b981", font=get_font(14, bold=True))
        draw.text((115, 255), "Inference latency: 18ms", fill="#cbd5e1", font=get_font(12))
        draw.text((115, 280), "Model Architecture: ResNet50 + Transformer", fill="#cbd5e1", font=get_font(12))
        draw.text((115, 305), "GPU Utilization: 94.2%", fill="#cbd5e1", font=get_font(12))
        draw.text((115, 330), "Memory allocation: 3.8 GB / 8.0 GB", fill="#cbd5e1", font=get_font(12))

        draw.rounded_rectangle([650, 200, 1190, 610], radius=8, fill="#070c18", outline="#1e293b")
        draw.text((675, 225), "ANALYTICS & CONVERSION CHARTS", fill="#38bdf8", font=get_font(14, bold=True))
        draw.text((675, 255), "Live Production Stream // Zero Dropouts", fill="#94a3b8", font=get_font(12))
        # Simulated chart lines
        draw.line([(680, 560), (1160, 560)], fill="#334155", width=1)
        pts = [(680 + x * 20, int(500 - math.sin(x/3)*40 - math.cos(x/5)*30)) for x in range(24)]
        draw.line(pts, fill="#10b981", width=2)
        save_both(im, rel_path)

if __name__ == "__main__":
    print("Starting generation of all cyber UI screens...")
    gen_deepfake_start()
    gen_deepfake_intro()
    gen_deepfake_how()
    gen_deepfake_quiz()
    gen_deepfake_correct()
    gen_deepfake_result()
    gen_fakenews_screens()
    gen_dcti_screens()
    gen_site_screens()
    gen_booking_screens()
    gen_other_projects()
    print("ALL SCREENS GENERATED SUCCESSFULLY!")
