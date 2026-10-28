import os
import math
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
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

def save_both(im, rel_path):
    for root in ["work", "public/work"]:
        full = os.path.join(root, rel_path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        im.save(full, "WEBP", quality=94)
    print(f"Generated: {rel_path}")

def draw_cyber_base(w=1280, h=720, primary="#3b82f6", title="SYSTEM DASHBOARD", category="AI RESEARCH", status="VERIFIED PRODUCTION"):
    im = Image.new("RGB", (w, h), "#060913")
    draw = ImageDraw.Draw(im)

    # Grid
    grid_spacing = 40
    for x in range(0, w, grid_spacing):
        draw.line([(x, 0), (x, h)], fill="#0c162d", width=1)
    for y in range(0, h, grid_spacing):
        draw.line([(0, y), (w, y)], fill="#0c162d", width=1)

    # Corner glow accents
    for r in range(260, 0, -25):
        alpha = int(14 * (1 - r / 260))
        draw.ellipse([w - r, -r, w + r, r], outline=f"#1e3a8a{alpha:02x}", width=10)

    # Frame line & corner brackets
    draw.rectangle([12, 12, w - 13, h - 13], outline="#1e293b", width=1)
    c_len = 24
    for cx, cy in [(12, 12), (w - 13, 12), (12, h - 13), (w - 13, h - 13)]:
        dx = c_len if cx == 12 else -c_len
        dy = c_len if cy == 12 else -c_len
        draw.line([(cx, cy), (cx + dx, cy)], fill=primary, width=2)
        draw.line([(cx, cy), (cx, cy + dy)], fill=primary, width=2)

    # Header Bar
    draw.rectangle([12, 12, w - 13, 62], fill="#0a1020", outline="#1e293b", width=1)
    draw.ellipse([30, 32, 40, 42], fill="#10b981")
    draw.text((48, 28), "AJAY VISHWAKARMA // AI & FULL-STACK", fill="#94a3b8", font=get_font(13, bold=True))
    draw.text((48, 44), f"{category} • LIVE PRODUCTION", fill="#475569", font=get_font(11))

    # Center title pill
    draw.rounded_rectangle([w // 2 - 220, 22, w // 2 + 220, 52], radius=6, fill="#111c35", outline="#2563eb", width=1)
    draw.text((w // 2, 37), title, fill="#60a5fa", font=get_font(13, bold=True), anchor="mm")

    # Right indicator
    draw.text((w - 200, 37), status, fill="#10b981", font=get_font(11, bold=True), anchor="rm")

    # Footer Bar
    draw.rectangle([12, h - 46, w - 13, h - 13], fill="#0a1020", outline="#1e293b", width=1)
    draw.text((30, h - 30), "PRODUCTION SYSTEM // DEPLOYED LIVE // ZERO LATENCY INFERENCE", fill="#64748b", font=get_font(11))
    draw.text((w - 30, h - 30), "HTTPS ENCRYPTED • VERIFIED PIPELINE", fill="#94a3b8", font=get_font(11), anchor="rm")

    return im, draw

# =========================================================================
# 01. BRAIN TUMOR DETECTION (deepfake)
# =========================================================================
def gen_brain_tumor():
    im, draw = draw_cyber_base(title="BRAIN TUMOR DETECTION & CLASSIFICATION", category="MEDICAL AI • TENSORFLOW 2.16")
    
    # Left: Axial T2 MRI Scan
    draw.rounded_rectangle([32, 82, 450, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((50, 100), "AXIAL T2-WEIGHTED MRI SCAN", fill="#38bdf8", font=get_font(14, bold=True))
    draw.text((50, 122), "Input: brain_scan_04.png | Resolution: 512x512", fill="#64748b", font=get_font(11))
    
    bx, by = 241, 350
    draw.ellipse([bx - 140, by - 160, bx + 140, by + 160], fill="#070c18", outline="#334155", width=3)
    draw.ellipse([bx - 120, by - 140, bx - 5, by + 140], fill="#111c33", outline="#1e293b", width=2)
    draw.ellipse([bx + 5, by - 140, bx + 120, by + 140], fill="#111c33", outline="#1e293b", width=2)
    draw.ellipse([bx - 35, by - 40, bx - 10, by + 40], fill="#070c18")
    draw.ellipse([bx + 10, by - 40, bx + 35, by + 40], fill="#070c18")
    
    # Tumor hotspot
    tx, ty = bx + 55, by - 45
    for r in range(45, 0, -5):
        alpha = int(45 * (1 - r / 45))
        draw.ellipse([tx - r, ty - r, tx + r, ty + r], fill=f"#ef4444{alpha:02x}")
    draw.ellipse([tx - 12, ty - 12, tx + 12, ty + 12], fill="#ef4444", outline="#ffffff", width=2)
    draw.line([(tx + 15, ty - 15), (tx + 70, ty - 50)], fill="#ef4444", width=2)
    draw.text((tx + 75, ty - 60), "GLIOMA LESION DETECTED", fill="#f87171", font=get_font(10, bold=True))

    # Right: Classification results & Plotly charts
    draw.rounded_rectangle([470, 82, 1248, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((495, 100), "CNN MULTI-CLASS INFERENCE RESULTS", fill="#60a5fa", font=get_font(14, bold=True))
    draw.text((495, 122), "Keras Transfer Learning Model • Accuracy 92.4% validated on BraTS dataset", fill="#64748b", font=get_font(11))
    
    # Diagnosis alert box
    draw.rounded_rectangle([495, 150, 1220, 225], radius=8, fill="#2a1215", outline="#ef4444", width=1)
    draw.text((515, 165), "PRIMARY DIAGNOSIS RESULT:", fill="#fca5a5", font=get_font(11))
    draw.text((515, 185), "Glioma Tumor Detected", fill="#ef4444", font=get_font(20, bold=True))
    draw.text((1050, 185), "CONFIDENCE: 96.4%", fill="#fca5a5", font=get_font(14, bold=True))

    # Probability bars
    probs = [
        ("Glioma Tumor", 96.4, "#ef4444"),
        ("Meningioma Tumor", 2.1, "#f59e0b"),
        ("No Tumor (Normal)", 0.9, "#10b981"),
        ("Pituitary Tumor", 0.6, "#64748b")
    ]
    draw.text((495, 250), "MULTI-CLASS PROBABILITY DISTRIBUTION (PLOTLY INTERACTIVE)", fill="#94a3b8", font=get_font(11, bold=True))
    for i, (name, pct, col) in enumerate(probs):
        py = 280 + i * 50
        draw.text((495, py), name, fill="#cbd5e1", font=get_font(12))
        draw.text((720, py), f"{pct}%", fill=col, font=get_font(12, bold=True))
        # Bar track
        draw.rounded_rectangle([780, py + 2, 1200, py + 18], radius=4, fill="#111c33")
        # Bar fill
        fw = int(420 * (pct / 100))
        if fw > 0:
            draw.rounded_rectangle([780, py + 2, 780 + max(fw, 6), py + 18], radius=4, fill=col)

    # Bottom model specs
    draw.rounded_rectangle([495, 500, 1220, 625], radius=8, fill="#080e1d", outline="#1e293b", width=1)
    draw.text((515, 515), "MODEL SPECS & TECH STACK", fill="#60a5fa", font=get_font(11, bold=True))
    specs = [
        "Architecture: Custom CNN + ResNet50 Transfer Learning",
        "Frameworks: TensorFlow 2.16, Keras, OpenCV, NumPy",
        "Frontend: Streamlit Cloud with real-time Plotly charts",
        "Preprocessing: Normalization, Contrast Enhancement, Augmentation"
    ]
    for s_i, s_txt in enumerate(specs):
        draw.text((515, 540 + s_i * 20), "• " + s_txt, fill="#94a3b8", font=get_font(11))

    save_both(im, "kt-ai-station/deepfake/start.webp")

# =========================================================================
# 02. EDUTECH AI LEARNING SAAS (fakenews)
# =========================================================================
def gen_edutech():
    im, draw = draw_cyber_base(title="EDUTECH AI // INTERACTIVE SAAS PLATFORM", category="FULL STACK EDTECH • GROQ LLM")
    
    # Left: Course Room & Playlist Importer
    draw.rounded_rectangle([32, 82, 450, 650], radius=10, fill="#0d1424", outline="#a855f7", width=1)
    draw.text((50, 100), "YOUTUBE PLAYLIST TO VIRTUAL CLASSROOM", fill="#c084fc", font=get_font(13, bold=True))
    draw.text((50, 122), "500+ Video Lectures Ingested // Automated Chapters", fill="#64748b", font=get_font(11))
    
    # Active video frame
    draw.rounded_rectangle([50, 150, 430, 360], radius=8, fill="#17112c", outline="#7c3aed", width=1)
    draw.rectangle([50, 150, 430, 310], fill="#0f0b1d")
    # Play icon
    draw.ellipse([215, 205, 265, 255], fill="#7c3aed")
    draw.polygon([(233, 220), (253, 230), (233, 240)], fill="#ffffff")
    draw.text((65, 325), "Lecture 14: Neural Attention Mechanisms (Llama 3.1)", fill="#ffffff", font=get_font(11, bold=True))
    draw.text((65, 342), "Playlist: Deep Learning Complete Curriculum • 42 mins", fill="#94a3b8", font=get_font(10))

    # Focus Pomodoro Room Card
    draw.rounded_rectangle([50, 380, 430, 490], radius=8, fill="#121829", outline="#1e293b", width=1)
    draw.text((65, 395), "POMODORO FOCUS ROOM", fill="#f59e0b", font=get_font(11, bold=True))
    draw.text((65, 420), "24:52", fill="#ffffff", font=get_font(32, bold=True))
    draw.text((170, 435), "Session #3 of 4 • Deep Work Mode", fill="#94a3b8", font=get_font(11))
    
    # Certificate Generator Card
    draw.rounded_rectangle([50, 510, 430, 625], radius=8, fill="#0a1526", outline="#10b981", width=1)
    draw.text((65, 525), "DYNAMIC PDF CERTIFICATE VERIFICATION", fill="#34d399", font=get_font(11, bold=True))
    draw.text((65, 545), "Course Progress: 88% Complete [12/14 Modules Passed]", fill="#94a3b8", font=get_font(10))
    draw.rounded_rectangle([65, 565, 415, 575], radius=3, fill="#1e293b")
    draw.rounded_rectangle([65, 565, 370, 575], radius=3, fill="#10b981")
    draw.text((65, 585), "Razorpay Gateway & Firebase Auth Active", fill="#64748b", font=get_font(10))

    # Right: Groq Llama 3.1 Hinglish AI Tutor
    draw.rounded_rectangle([470, 82, 1248, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((495, 100), "GROQ LLM HINGLISH AI TUTOR (LLAMA 3.1 8B)", fill="#60a5fa", font=get_font(14, bold=True))
    draw.text((495, 122), "Sub-second token streaming with real-time video timestamp references", fill="#64748b", font=get_font(11))
    
    # Chat conversation container
    draw.rounded_rectangle([495, 150, 1220, 625], radius=8, fill="#090e1c", outline="#1e293b", width=1)
    
    # Student message
    draw.rounded_rectangle([680, 175, 1200, 245], radius=8, fill="#1e293b", outline="#334155", width=1)
    draw.text((700, 188), "Student (Hinglish):", fill="#38bdf8", font=get_font(11, bold=True))
    draw.text((700, 208), "\"Sir, Self-Attention mechanism ka simple intuition samjha do with matrix Q, K, V?\"", fill="#ffffff", font=get_font(11))

    # AI Tutor message
    draw.rounded_rectangle([515, 260, 1150, 510], radius=8, fill="#121e38", outline="#2563eb", width=1)
    draw.text((535, 275), "Groq Llama 3.1 AI Tutor (Response in 0.32s):", fill="#34d399", font=get_font(11, bold=True))
    lines = [
        "Bilkul! Self-Attention ko ek library ki tarah samjhein:",
        "1. Query (Q): Wo sawal jo aap dhoondh rahe hain.",
        "2. Key (K): Library me books ke labels/tags jisse match kiya jata hai.",
        "3. Value (V): Actual content/knowledge jo book ke andar hai.",
        "",
        "Formula: Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V",
        "Video me timestamp 14:32 par professor ne iska matrix multiplication diagram dikhaya hai!",
        "Kya aap ispar ek quick 2-minute practice quiz attempt karna chahte hain?"
    ]
    for l_i, l_t in enumerate(lines):
        draw.text((535, 305 + l_i * 22), l_t, fill="#e2e8f0" if l_i!=5 else "#38bdf8", font=get_font(11, bold=(l_i==5)))

    # Action buttons at bottom of chat
    draw.rounded_rectangle([515, 535, 690, 575], radius=6, fill="#2563eb")
    draw.text((602, 555), "Take Practice Quiz", fill="#ffffff", font=get_font(11, bold=True), anchor="mm")
    draw.rounded_rectangle([710, 535, 890, 575], radius=6, fill="#1e293b", outline="#334155")
    draw.text((800, 555), "Jump to 14:32 in Video", fill="#94a3b8", font=get_font(11), anchor="mm")

    save_both(im, "kt-ai-station/fakenews/start.webp")

# =========================================================================
# 03. SKILLPROOF LIVE MONACO CODE EVALUATOR (dcti)
# =========================================================================
def gen_skillproof():
    im, draw = draw_cyber_base(title="SKILLPROOF // LIVE CODE EVALUATOR & PORTFOLIO", category="DEVELOPER TOOLS • MONACO IDE")
    
    # Left: Monaco Editor UI
    draw.rounded_rectangle([32, 82, 700, 650], radius=10, fill="#1e1e1e", outline="#334155", width=1)
    # Editor tab bar
    draw.rectangle([32, 82, 700, 118], fill="#252526")
    draw.rectangle([32, 82, 170, 118], fill="#1e1e1e")
    draw.text((45, 95), "solution.py", fill="#ffffff", font=get_font(11, bold=True))
    draw.text((180, 95), "tests.py", fill="#64748b", font=get_font(11))
    
    code_lines = [
        ("1", "class Solution:", "#4ec9b0"),
        ("2", "    def maxPathSum(self, root: Optional[TreeNode]) -> int:", "#569cd6"),
        ("3", "        self.max_sum = float('-inf')", "#9cdcfe"),
        ("4", "        ", "#d4d4d4"),
        ("5", "        def get_max_gain(node):", "#569cd6"),
        ("6", "            if not node: return 0", "#c586c0"),
        ("7", "            left = max(get_max_gain(node.left), 0)", "#d4d4d4"),
        ("8", "            right = max(get_max_gain(node.right), 0)", "#d4d4d4"),
        ("9", "            price_newpath = node.val + left + right", "#9cdcfe"),
        ("10", "            self.max_sum = max(self.max_sum, price_newpath)", "#9cdcfe"),
        ("11", "            return node.val + max(left, right)", "#c586c0"),
        ("12", "            ", "#d4d4d4"),
        ("13", "        get_max_gain(root)", "#dcdcaa"),
        ("14", "        return self.max_sum", "#c586c0")
    ]
    for num, txt, col in code_lines:
        cy = 135 + int(num) * 23
        draw.text((45, cy), num, fill="#5a5a5a", font=get_font(11))
        draw.text((80, cy), txt, fill=col, font=get_font(11))

    # Terminal / Sandbox Execution Output
    draw.rounded_rectangle([45, 500, 685, 635], radius=6, fill="#0c1017", outline="#30363d", width=1)
    draw.text((60, 512), "SANDBOX RUNNER CONSOLE // DOCKER ISOLATED", fill="#8b949e", font=get_font(10, bold=True))
    draw.text((60, 535), "[TEST 1/5] root = [1,2,3] -> Expected: 6, Got: 6 [PASSED]", fill="#3fb950", font=get_font(10))
    draw.text((60, 555), "[TEST 2/5] root = [-10,9,20,null,null,15,7] -> Expected: 42, Got: 42 [PASSED]", fill="#3fb950", font=get_font(10))
    draw.text((60, 575), "[TEST 3/5] Large Balanced Tree (N=10,000) -> Runtime: 4ms [PASSED]", fill="#3fb950", font=get_font(10))
    draw.text((60, 595), "ALL 5/5 TEST CASES RESOLVED // RUNTIME: BEATS 98.4%", fill="#58a6ff", font=get_font(10, bold=True))

    # Right: Real-time Evaluation & Candidate Scorecard
    draw.rounded_rectangle([720, 82, 1248, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((745, 100), "CANDIDATE CODE INTELLIGENCE SCORECARD", fill="#60a5fa", font=get_font(14, bold=True))
    draw.text((745, 122), "AST Real-Time Syntax & Complexity Evaluation Engine", fill="#64748b", font=get_font(11))
    
    # Score circle
    draw.rounded_rectangle([745, 150, 1220, 250], radius=8, fill="#111c35", outline="#1e293b", width=1)
    draw.text((765, 170), "OVERALL VERIFIED SCORE", fill="#94a3b8", font=get_font(11))
    draw.text((765, 192), "96.8 / 100", fill="#10b981", font=get_font(28, bold=True))
    draw.text((950, 185), "TIME COMPLEXITY: O(N) Optimal", fill="#38bdf8", font=get_font(11, bold=True))
    draw.text((950, 205), "SPACE COMPLEXITY: O(H) Optimal", fill="#38bdf8", font=get_font(11, bold=True))

    metrics = [
        ("Algorithmic Correctness", "100%", "#10b981"),
        ("Clean Code & PEP8 Formatting", "94%", "#34d399"),
        ("Edge Case Resilience", "96%", "#38bdf8"),
        ("Security & Sandbox Isolation", "100%", "#10b981")
    ]
    for i, (m_t, m_v, m_c) in enumerate(metrics):
        my = 275 + i * 55
        draw.rounded_rectangle([745, my, 1220, my + 46], radius=6, fill="#0c1222", outline="#1e293b", width=1)
        draw.text((765, my + 14), m_t, fill="#cbd5e1", font=get_font(11))
        draw.text((1140, my + 14), m_v, fill=m_c, font=get_font(12, bold=True), anchor="rm")

    # Dynamic student portfolio generator card
    draw.rounded_rectangle([745, 510, 1220, 625], radius=8, fill="#080e1d", outline="#2563eb", width=1)
    draw.text((765, 525), "DYNAMIC STUDENT PORTFOLIO LINK GENERATED", fill="#60a5fa", font=get_font(11, bold=True))
    draw.text((765, 550), "URL: https://skillproof-eight.vercel.app/portfolio/ajay-vishwakarma", fill="#38bdf8", font=get_font(11))
    draw.text((765, 575), "Verifiable on-chain cryptographic badge + employer report PDF ready", fill="#94a3b8", font=get_font(10))

    save_both(im, "kt-ai-station/dcti/start.webp")

# =========================================================================
# 04. AI TUTOR (aitutor)
# =========================================================================
def gen_aitutor():
    im, draw = draw_cyber_base(title="AI TUTOR // INTERACTIVE STEM LEARNING", category="CONVERSATIONAL EDTECH • GROQ LLM")
    
    # Left: STEM Curriculum Topic Tree
    draw.rounded_rectangle([32, 82, 450, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((50, 100), "CLASS 5-12 ADAPTIVE CURRICULUM", fill="#38bdf8", font=get_font(14, bold=True))
    draw.text((50, 122), "CBSE / ICSE STEM Learning Pathway Engine", fill="#64748b", font=get_font(11))
    
    topics = [
        ("Physics: Laws of Motion & Friction", "100% Completed", "#10b981"),
        ("Chemistry: Atomic Structure & Bonding", "85% In Progress", "#38bdf8"),
        ("Mathematics: Quadratic Equations", "92% In Progress", "#38bdf8"),
        ("Biology: Cell Division & Genetics", "70% In Progress", "#f59e0b"),
        ("Computer Science: Data Structures", "100% Mastered", "#10b981")
    ]
    for i, (t_name, t_stat, t_col) in enumerate(topics):
        ty = 160 + i * 65
        draw.rounded_rectangle([50, ty, 430, ty + 52], radius=6, fill="#111c33", outline="#1e293b", width=1)
        draw.text((64, ty + 10), t_name, fill="#ffffff", font=get_font(11, bold=True))
        draw.text((64, ty + 30), t_stat, fill=t_col, font=get_font(10))

    # Adaptive IQ meter
    draw.rounded_rectangle([50, 500, 430, 625], radius=8, fill="#0a1226", outline="#3b82f6", width=1)
    draw.text((64, 515), "LEARNING VELOCITY METRICS", fill="#60a5fa", font=get_font(11, bold=True))
    draw.text((64, 540), "Concept Retention Rate: 94.2%", fill="#34d399", font=get_font(11))
    draw.text((64, 565), "Avg Problem Solving Speed: 42s / question", fill="#cbd5e1", font=get_font(10))
    draw.text((64, 590), "Hugging Face Spaces Cloud Deployed", fill="#64748b", font=get_font(10))

    # Right: Interactive AI Tutor Chat
    draw.rounded_rectangle([470, 82, 1248, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((495, 100), "LIVE GROQ LLM STEM ASSISTANT", fill="#60a5fa", font=get_font(14, bold=True))
    draw.text((495, 122), "Real-time step-by-step mathematical & scientific reasoning", fill="#64748b", font=get_font(11))
    
    # Chat container
    draw.rounded_rectangle([495, 150, 1220, 625], radius=8, fill="#080e1d", outline="#1e293b", width=1)
    
    # Student query
    draw.rounded_rectangle([700, 175, 1200, 245], radius=8, fill="#1e293b", outline="#334155", width=1)
    draw.text((720, 188), "Student (Class 10 Physics):", fill="#38bdf8", font=get_font(11, bold=True))
    draw.text((720, 208), "\"A ball is thrown upward with velocity 20 m/s. Max height kitni hogi?\"", fill="#ffffff", font=get_font(11))

    # AI response
    draw.rounded_rectangle([515, 260, 1160, 520], radius=8, fill="#111f3d", outline="#2563eb", width=1)
    draw.text((535, 275), "AI Tutor (Instant Step-by-Step Derivation):", fill="#34d399", font=get_font(11, bold=True))
    sol_lines = [
        "Chaliye 3rd equation of motion use karte hain: v^2 = u^2 - 2gh",
        "• Initial velocity (u) = 20 m/s",
        "• At max height, final velocity (v) = 0 m/s",
        "• Acceleration due to gravity (g) = 9.8 m/s^2 (or approx 10 m/s^2)",
        "",
        "Calculation: 0 = (20)^2 - 2 * 10 * h",
        "=> 20 * h = 400",
        "=> h = 400 / 20 = 20 meters!",
        "Answer: Ball 20 meters ki maximum height achieve karegi!"
    ]
    for s_i, s_t in enumerate(sol_lines):
        draw.text((535, 305 + s_i * 22), s_t, fill="#e2e8f0" if "=>" not in s_t else "#38bdf8", font=get_font(11, bold=("Answer" in s_t or "=>" in s_t)))

    save_both(im, "kt-ai-station/aitutor/start.webp")
    save_both(im, "kt-ai-station/fakenews/opening.webp")

# =========================================================================
# 05. HEALTHCARE DIAGNOSIS & PATIENT TRIAGE (healthcare)
# =========================================================================
def gen_healthcare_screen():
    im, draw = draw_cyber_base(title="HEALTHCARE DIAGNOSIS & PATIENT TRIAGE", category="CLINICAL AI & TRIAGE")
    
    # Left: Patient Vitals Card
    draw.rounded_rectangle([32, 82, 420, 650], radius=10, fill="#0d1424", outline="#10b981", width=1)
    draw.text((50, 100), "PATIENT CLINICAL TRIAGE CARD", fill="#34d399", font=get_font(14, bold=True))
    draw.text((50, 122), "MRN #9028-H | Level 2 Urgent | Age: 42", fill="#64748b", font=get_font(11))
    
    vitals = [
        ("Heart Rate", "88 bpm", "#38bdf8"),
        ("Blood Pressure", "124/82 mmHg", "#34d399"),
        ("SpO2 Level", "98% (Normal)", "#38bdf8"),
        ("Triage Score", "ESI-2 (Priority)", "#f59e0b")
    ]
    for i, (k, v, col) in enumerate(vitals):
        vy = 160 + i * 55
        draw.rounded_rectangle([50, vy, 400, vy + 46], radius=6, fill="#111c33", outline="#1e293b", width=1)
        draw.text((64, vy + 8), k, fill="#94a3b8", font=get_font(11))
        draw.text((64, vy + 24), v, fill=col, font=get_font(13, bold=True))
        
    draw.rounded_rectangle([50, 400, 400, 630], radius=8, fill="#0a1226", outline="#2563eb", width=1)
    draw.text((64, 415), "CONNECTED PHYSICIAN", fill="#60a5fa", font=get_font(12, bold=True))
    draw.text((64, 435), "Dr. Sarah Chen, MD (Emergency Medicine)", fill="#cbd5e1", font=get_font(11))
    draw.text((64, 455), "Status: Virtual Tele-triage Active", fill="#10b981", font=get_font(11, bold=True))
    
    draw.rounded_rectangle([64, 490, 386, 610], radius=6, fill="#111f3d", outline="#3b82f6", width=1)
    draw.text((76, 502), "NEAREST EMERGENCY FACILITY", fill="#38bdf8", font=get_font(11, bold=True))
    draw.text((76, 524), "Apollo Multi-Specialty Hospital (1.4 km)", fill="#ffffff", font=get_font(12, bold=True))
    draw.text((76, 545), "Estimated Ambulance Routing: 4.2 mins", fill="#34d399", font=get_font(11))
    draw.text((76, 570), "OpenStreetMap Geo-Routing: OPTIMAL", fill="#94a3b8", font=get_font(10))

    # Right: Symptom Diagnostics & Queue
    draw.rounded_rectangle([440, 82, 1248, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((465, 100), "CLINICAL TRIAGE & SYMPTOM INFERENCE ENGINE", fill="#60a5fa", font=get_font(14, bold=True))
    draw.text((465, 122), "Django + MongoDB Encrypted EHR Pipeline • Zero-Trust Access Protocol", fill="#64748b", font=get_font(11))
    
    m_data = [
        ("TRIAGE ACCURACY", "96.4%", "#10b981"),
        ("DISPATCH LATENCY", "1.8 sec", "#38bdf8"),
        ("CONNECTED HOSPITALS", "148 Facilities", "#a855f7")
    ]
    for i, (m_t, m_v, m_c) in enumerate(m_data):
        mx = 465 + i * 255
        draw.rounded_rectangle([mx, 155, mx + 240, 235], radius=8, fill="#111c35", outline="#1e293b", width=1)
        draw.text((mx + 16, 170), m_t, fill="#64748b", font=get_font(10, bold=True))
        draw.text((mx + 16, 192), m_v, fill=m_c, font=get_font(20, bold=True))

    draw.rounded_rectangle([465, 255, 1223, 625], radius=8, fill="#080e1d", outline="#1e293b", width=1)
    draw.text((485, 272), "LIVE PATIENT INGESTION & EMERGENCY DISPATCH QUEUE", fill="#94a3b8", font=get_font(11, bold=True))
    
    rows = [
        ("T-1029", "Acute Respiratory Distress", "ESI-1 Critical", "ICU Bed #4 Reserved", "DISPATCHED"),
        ("T-1030", "Chest Pain & Left Arm Radiation", "ESI-2 High", "Cardiology Team Alerted", "TRANSIT"),
        ("T-1031", "Pediatric Febrile Convulsion", "ESI-2 High", "Pediatric Emergency Ready", "PREPPED"),
        ("T-1032", "Deep Laceration / Hemorrhage", "ESI-3 Moderate", "Trauma Bay #2 Assigned", "STABLE"),
        ("T-1033", "Closed Fracture Right Tibia", "ESI-4 Low", "Orthopedic Fast-Track", "TRIAGED")
    ]
    for r_i, (tid, sym, sev, act, st) in enumerate(rows):
        ry = 305 + r_i * 60
        draw.rectangle([485, ry, 1205, ry + 50], fill="#0f192e" if r_i % 2 == 0 else "#0a1122", outline="#1e293b", width=1)
        draw.text((500, ry + 16), tid, fill="#38bdf8", font=get_font(11, bold=True))
        draw.text((580, ry + 16), sym, fill="#ffffff", font=get_font(11, bold=True))
        draw.text((820, ry + 16), sev, fill="#f59e0b" if "High" in sev or "Critical" in sev else "#34d399", font=get_font(11))
        draw.text((960, ry + 16), act, fill="#94a3b8", font=get_font(10))
        draw.rounded_rectangle([1110, ry + 12, 1195, ry + 38], radius=4, fill="#059669" if st=="DISPATCHED" else "#1e3a8a")
        draw.text((1152, ry + 25), st, fill="#ffffff", font=get_font(10, bold=True), anchor="mm")

    save_both(im, "kt-ai-station/healthcare/start.webp")

# =========================================================================
# 06. ESTATEAI - HOUSE PRICE PREDICTION (estateai)
# =========================================================================
def gen_estateai():
    im, draw = draw_cyber_base(title="ESTATEAI // REAL ESTATE VALUATION ENGINE", category="MACHINE LEARNING • SCIKIT-LEARN")
    
    # Left: 12 Property Feature Inputs
    draw.rounded_rectangle([32, 82, 450, 650], radius=10, fill="#0d1424", outline="#3b82f6", width=1)
    draw.text((50, 100), "PROPERTY ATTRIBUTES (12 VARIABLES)", fill="#38bdf8", font=get_font(14, bold=True))
    draw.text((50, 122), "Trained on 1,000+ Verified Residential Sales Records", fill="#64748b", font=get_font(11))
    
    feats = [
        ("Total Living Area", "2,450 sq.ft.", "#38bdf8"),
        ("Bedrooms & Bathrooms", "3 BHK, 3 Baths", "#cbd5e1"),
        ("Locality / Sector", "Sector 14, Prime Metro Corridor", "#ffffff"),
        ("Property Age", "2 Years (Newly Built)", "#34d399"),
        ("Floor Level", "8th Floor (of 22 Floors)", "#cbd5e1"),
        ("Covered Parking", "2 Dedicated Bays", "#34d399"),
        ("Amenities Score", "9.4 / 10 (Club, Pool, Gym)", "#f59e0b")
    ]
    for i, (k, v, col) in enumerate(feats):
        fy = 155 + i * 50
        draw.rounded_rectangle([50, fy, 430, fy + 44], radius=6, fill="#111c33", outline="#1e293b", width=1)
        draw.text((64, fy + 6), k, fill="#94a3b8", font=get_font(10))
        draw.text((64, fy + 22), v, fill=col, font=get_font(12, bold=True))

    draw.rounded_rectangle([50, 520, 430, 625], radius=8, fill="#0a1226", outline="#2563eb", width=1)
    draw.text((64, 535), "REGRESSION BENCHMARKS", fill="#60a5fa", font=get_font(11, bold=True))
    draw.text((64, 560), "Random Forest Regressor: R² = 0.941", fill="#10b981", font=get_font(11, bold=True))
    draw.text((64, 580), "Ridge Regression: R² = 0.918 | RMSE: ±3.1%", fill="#94a3b8", font=get_font(10))
    draw.text((64, 600), "Linear Regression Baseline: R² = 0.884", fill="#64748b", font=get_font(10))

    # Right: Valuation Output & Groq AI Insights
    draw.rounded_rectangle([470, 82, 1248, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((495, 100), "PREDICTIVE VALUATION & MARKET INTELLIGENCE", fill="#60a5fa", font=get_font(14, bold=True))
    draw.text((495, 122), "Real-time regression inference with Groq LLM market trend reasoning", fill="#64748b", font=get_font(11))
    
    # Big Price Card
    draw.rounded_rectangle([495, 150, 1220, 270], radius=8, fill="#0f231a", outline="#10b981", width=1)
    draw.text((520, 170), "ESTIMATED FAIR MARKET VALUE:", fill="#6ee7b7", font=get_font(12, bold=True))
    draw.text((520, 195), "₹ 1,42,80,000", fill="#10b981", font=get_font(36, bold=True))
    draw.text((860, 205), "~ $ 172,500 USD", fill="#a7f3d0", font=get_font(18, bold=True))
    draw.text((520, 245), "Confidence Interval: ₹1.38 Cr — ₹1.47 Cr (95% Probability)", fill="#6ee7b7", font=get_font(11))

    # Groq AI Market Analysis
    draw.rounded_rectangle([495, 290, 1220, 625], radius=8, fill="#090e1c", outline="#1e293b", width=1)
    draw.text((520, 310), "GROQ AI REAL ESTATE MARKET ANALYSIS:", fill="#38bdf8", font=get_font(12, bold=True))
    
    ai_points = [
        ("• Capital Appreciation Potential:", "High (+12.8% YoY projected due to metro station completion in 2026)."),
        ("• Rental Yield Estimate:", "Estimated ₹48,000/month (4.03% annual gross yield), beating city average of 3.2%."),
        ("• Price per Sq. Ft. Analysis:", "₹5,828/sq.ft. vs Sector average of ₹6,100/sq.ft. — Currently trading at attractive value."),
        ("• Demand Velocity Index:", "9.2/10 — High liquidity zone with avg time on market under 38 days.")
    ]
    for p_i, (head, body) in enumerate(ai_points):
        draw.text((520, 345 + p_i * 65), head, fill="#60a5fa", font=get_font(11, bold=True))
        draw.text((520, 365 + p_i * 65), body, fill="#cbd5e1", font=get_font(11))

    save_both(im, "jimssalabium/start.webp")
    save_both(im, "jimssalabium/scan.webp")

# =========================================================================
# 07. CAMPAIGNIQ - CAMPAIGN PERFORMANCE (campaigniq)
# =========================================================================
def gen_campaigniq():
    im, draw = draw_cyber_base(title="CAMPAIGNIQ // MARKETING BI & FUNNEL ANALYTICS", category="DATA ANALYTICS • PANDAS & PLOTLY")
    
    # Left: Automated Pandas Ingestion & Validation
    draw.rounded_rectangle([32, 82, 450, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((50, 100), "AUTOMATED PANDAS DATA PIPELINE", fill="#38bdf8", font=get_font(14, bold=True))
    draw.text((50, 122), "ETL Cleaning • Anomaly Detection • Schema Validation", fill="#64748b", font=get_font(11))
    
    kpis = [
        ("Total Ad Spend", "$48,250.00", "+14.2% YoY", "#38bdf8"),
        ("Direct Conversions", "3,842", "+22.8% vs Target", "#10b981"),
        ("Return on Ad Spend (ROAS)", "4.65x", "Target: 3.50x", "#10b981"),
        ("Avg Cost Per Click (CPC)", "$0.58", "-12.4% Cost Saved", "#34d399"),
        ("Click-Through Rate (CTR)", "4.28%", "Benchmark: 2.80%", "#38bdf8")
    ]
    for i, (k, v, chg, col) in enumerate(kpis):
        ky = 155 + i * 75
        draw.rounded_rectangle([50, ky, 430, ky + 65], radius=6, fill="#111c33", outline="#1e293b", width=1)
        draw.text((64, ky + 8), k, fill="#94a3b8", font=get_font(11))
        draw.text((64, ky + 26), v, fill=col, font=get_font(18, bold=True))
        draw.text((280, ky + 30), chg, fill="#10b981", font=get_font(10, bold=True))

    draw.rounded_rectangle([50, 545, 430, 625], radius=6, fill="#080e1d", outline="#1e293b", width=1)
    draw.text((64, 558), "PANDAS DATASET QUALITY SCORE: 100%", fill="#34d399", font=get_font(10, bold=True))
    draw.text((64, 578), "48,200 records parsed | 0 nulls | 14 KPI aggregates", fill="#64748b", font=get_font(10))
    draw.text((64, 598), "Streamlit Cloud Live Ingestion Active", fill="#94a3b8", font=get_font(10))

    # Right: Plotly Interactive Funnel & AI Recommendations
    draw.rounded_rectangle([470, 82, 1248, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((495, 100), "CONVERSION FUNNEL & MARKETING AI COPILOT", fill="#60a5fa", font=get_font(14, bold=True))
    draw.text((495, 122), "Interactive Plotly Visualizations & Statistical Attribution Model", fill="#64748b", font=get_font(11))
    
    # Funnel stages
    funnel = [
        ("Impressions", "1,240,000", 1.0, "#2563eb"),
        ("Ad Clicks", "53,072", 0.72, "#3b82f6"),
        ("Landing Page Views", "38,210", 0.52, "#0284c7"),
        ("Added to Cart", "12,450", 0.35, "#059669"),
        ("Purchases Completed", "3,842", 0.22, "#10b981")
    ]
    draw.text((495, 155), "MULTI-STAGE CONVERSION FUNNEL (PLOTLY ENGINE):", fill="#94a3b8", font=get_font(11, bold=True))
    for i, (stage, count, ratio, col) in enumerate(funnel):
        fy = 185 + i * 48
        draw.text((495, fy + 4), stage, fill="#cbd5e1", font=get_font(11))
        draw.text((680, fy + 4), count, fill="#ffffff", font=get_font(11, bold=True))
        # Funnel bar
        bw = int(480 * ratio)
        draw.rounded_rectangle([780, fy, 780 + max(bw, 10), fy + 24], radius=4, fill=col)
        draw.text((790 + bw + 10, fy + 4), f"{int(ratio*100)}%", fill=col, font=get_font(10, bold=True))

    # Groq Llama 3.1 AI Copilot
    draw.rounded_rectangle([495, 450, 1220, 625], radius=8, fill="#090e1c", outline="#2563eb", width=1)
    draw.text((515, 468), "GROQ LLAMA 3.1 AI MARKETING COPILOT RECOMMENDATION:", fill="#38bdf8", font=get_font(11, bold=True))
    recs = [
        "1. Funnel drop-off between Cart (12.4k) and Purchase (3.8k) is 69% (industry benchmark: 70%).",
        "2. Action: Deploy automated 1-hour abandoned-cart SMS/WhatsApp trigger to recover estimated +840 orders.",
        "3. High-performing creative: Video Ad #03 has 5.82% CTR and $0.42 CPC. Reallocate $4,000 to this ad set.",
        "4. Projected Revenue Impact: +$34,200 incremental GMV over next 14 billing days."
    ]
    for r_i, r_t in enumerate(recs):
        draw.text((515, 498 + r_i * 26), r_t, fill="#e2e8f0" if r_i!=3 else "#34d399", font=get_font(11, bold=(r_i==3)))

    save_both(im, "millie-genre-me/start.webp")
    save_both(im, "millie-genre-me/test.webp")

# =========================================================================
# 08. PAISA MITRA - SMART EXPENSE COACH (expensecoach)
# =========================================================================
def gen_paisa_mitra():
    im, draw = draw_cyber_base(title="PAISA MITRA // SMART EXPENSE COACH WHATSAPP BOT", category="FINTECH • BAILEYS & GROQ LLM")
    
    # Left: Smartphone Frame with WhatsApp Chat
    draw.rounded_rectangle([32, 82, 480, 650], radius=16, fill="#0b141a", outline="#25d366", width=2)
    
    # WhatsApp Header
    draw.rectangle([32, 82, 480, 140], fill="#202c33")
    draw.ellipse([50, 95, 85, 130], fill="#25d366")
    draw.text((68, 112), "₹", fill="#ffffff", font=get_font(16, bold=True), anchor="mm")
    draw.text((95, 98), "Paisa Mitra AI 🤖", fill="#ffffff", font=get_font(13, bold=True))
    draw.text((95, 118), "WhatsApp Bot • Groq Llama 3.1 Active", fill="#25d366", font=get_font(10))

    # User message 1
    draw.rounded_rectangle([140, 160, 460, 225], radius=8, fill="#005c4b")
    draw.text((155, 172), "User (Hindi/Hinglish):", fill="#8696a0", font=get_font(10))
    draw.text((155, 190), "\"Bhai kal doston ke saath cafe me", fill="#e9edef", font=get_font(11))
    draw.text((155, 206), "dinner kiya 1200 aur auto 150 ka tha\"", fill="#e9edef", font=get_font(11))

    # Bot message 1
    draw.rounded_rectangle([50, 240, 440, 395], radius=8, fill="#202c33")
    draw.text((65, 252), "Paisa Mitra Bot (0.18s):", fill="#25d366", font=get_font(10, bold=True))
    bot_lines = [
        "✅ 2 Expenses Automatically Logged!",
        "🍽️ Dining: ₹1,200 (Cafe dinner)",
        "🛺 Transport: ₹150 (Auto fare)",
        "--------------------------------------",
        "📊 Monthly Budget: ₹18,450 / ₹30,000",
        "💡 You have ₹11,550 left for 8 days.",
        "👉 Daily recommended limit: ₹1,440"
    ]
    for b_i, b_t in enumerate(bot_lines):
        draw.text((65, 272 + b_i * 17), b_t, fill="#e9edef" if b_i!=0 and b_i!=4 else "#25d366", font=get_font(10, bold=(b_i==0 or b_i==4)))

    # User message 2
    draw.rounded_rectangle([180, 410, 460, 465], radius=8, fill="#005c4b")
    draw.text((195, 422), "\"Is mahine dining pe kitna kharch hua?\"", fill="#e9edef", font=get_font(11))

    # Bot message 2
    draw.rounded_rectangle([50, 480, 440, 620], radius=8, fill="#202c33")
    draw.text((65, 492), "Paisa Mitra Bot:", fill="#25d366", font=get_font(10, bold=True))
    bot_lines2 = [
        "🍕 Total Dining Spend: ₹6,840 (37% of budget)",
        "Top outlets: Swiggy (₹3,200), Cafe (₹2,100)",
        "⚠️ Alert: Dining budget 85% consumed!",
        "Suggest: Home cooked meals next 4 days."
    ]
    for b_i, b_t in enumerate(bot_lines2):
        draw.text((65, 515 + b_i * 22), b_t, fill="#e9edef" if "Alert" not in b_t else "#f59e0b", font=get_font(10, bold=("Alert" in b_t)))

    # Right: Expense Analytics Dashboard
    draw.rounded_rectangle([500, 82, 1248, 650], radius=10, fill="#0d1424", outline="#25d366", width=1)
    draw.text((525, 100), "REAL-TIME EXPENSE ANALYTICS & CATEGORY BREAKDOWN", fill="#25d366", font=get_font(14, bold=True))
    draw.text((525, 122), "Django REST Framework + PostgreSQL Ingestion Pipeline", fill="#64748b", font=get_font(11))
    
    # Category cards
    cats = [
        ("Dining & Food", "₹ 6,840", "37.1%", "#ef4444"),
        ("Transport & Fuel", "₹ 3,250", "17.6%", "#3b82f6"),
        ("Utilities & Bills", "₹ 4,500", "24.4%", "#f59e0b"),
        ("Shopping & Leisure", "₹ 3,860", "20.9%", "#a855f7")
    ]
    for i, (c_name, c_amt, c_pct, c_col) in enumerate(cats):
        cx = 525 + (i % 2) * 355
        cy = 160 + (i // 2) * 105
        draw.rounded_rectangle([cx, cy, cx + 335, cy + 90], radius=8, fill="#111c33", outline="#1e293b", width=1)
        draw.text((cx + 16, cy + 14), c_name, fill="#94a3b8", font=get_font(11))
        draw.text((cx + 16, cy + 36), c_amt, fill="#ffffff", font=get_font(18, bold=True))
        draw.text((cx + 250, cy + 40), c_pct, fill=c_col, font=get_font(14, bold=True))
        # mini bar
        draw.rounded_rectangle([cx + 16, cy + 68, cx + 315, cy + 74], radius=3, fill="#1e293b")
        draw.rounded_rectangle([cx + 16, cy + 68, cx + 16 + int(3.0 * float(c_pct.replace('%',''))), cy + 74], radius=3, fill=c_col)

    # Tech Architecture & NLP Parsing
    draw.rounded_rectangle([525, 390, 1220, 625], radius=8, fill="#080e1d", outline="#1e293b", width=1)
    draw.text((545, 410), "NLP TEXT PARSING & AI ARCHITECTURE:", fill="#60a5fa", font=get_font(12, bold=True))
    
    paisa_specs = [
        ("• WhatsApp Gateway:", "Baileys WhatsApp Web API / Webhook (Node.js engine) with multi-device session."),
        ("• Natural Language Pipeline:", "Groq Llama 3.1 8B fine-tuned prompt extracting Amount, Merchant, Category from Hindi/Hinglish."),
        ("• Database & Ledger:", "Django REST Framework with PostgreSQL ACID transactional balance consistency."),
        ("• Production Status:", "Live on Render (https://expense-coach-prxm.onrender.com) with 99.9% webhook uptime.")
    ]
    for p_i, (head, body) in enumerate(paisa_specs):
        draw.text((545, 440 + p_i * 45), head, fill="#25d366", font=get_font(11, bold=True))
        draw.text((545, 458 + p_i * 45), body, fill="#cbd5e1", font=get_font(11))

    save_both(im, "todays-picnic/destination.webp")
    save_both(im, "todays-picnic/intro.webp")

# =========================================================================
# 09. DIGITAL TWIN (digitaltwin)
# =========================================================================
def gen_digital_twin():
    im, draw = draw_cyber_base(title="DIGITAL TWIN PLATFORM // CONVERSATIONAL AI PERSONA", category="PERSONAL AI • HUGGING FACE SPACES")
    
    # Left: Neural Persona Avatar & Interactive Chat
    draw.rounded_rectangle([32, 82, 480, 650], radius=10, fill="#0d1424", outline="#a855f7", width=1)
    draw.text((50, 100), "AJAY VISHWAKARMA // DIGITAL CLONE v3.2", fill="#c084fc", font=get_font(13, bold=True))
    draw.text((50, 122), "Trained on personal behavioral corpus & technical writing", fill="#64748b", font=get_font(11))
    
    # Avatar badge
    draw.rounded_rectangle([50, 150, 460, 235], radius=8, fill="#19112e", outline="#7c3aed", width=1)
    draw.ellipse([65, 165, 120, 220], fill="#7c3aed")
    draw.text((92, 192), "AV", fill="#ffffff", font=get_font(18, bold=True), anchor="mm")
    draw.text((135, 172), "Ajay AI Persona (Online)", fill="#ffffff", font=get_font(13, bold=True))
    draw.text((135, 192), "Neural Latent Dimension: 256 | Temp: 0.7", fill="#a855f7", font=get_font(10))
    draw.text((135, 210), "Status: Conversational reasoning active", fill="#10b981", font=get_font(10))

    # Conversation
    draw.rounded_rectangle([50, 250, 460, 320], radius=8, fill="#1e293b")
    draw.text((65, 262), "Recruiter / Visitor Query:", fill="#38bdf8", font=get_font(10, bold=True))
    draw.text((65, 282), "\"Ajay, what is your experience with Dockerized", fill="#ffffff", font=get_font(11))
    draw.text((65, 298), "code execution sandboxes in SkillProof?\"", fill="#ffffff", font=get_font(11))

    draw.rounded_rectangle([50, 335, 460, 490], radius=8, fill="#17112c", outline="#7c3aed", width=1)
    draw.text((65, 348), "Ajay Digital Twin (Persona Response):", fill="#c084fc", font=get_font(10, bold=True))
    twin_resp = [
        "\"In SkillProof, security was paramount. I designed",
        "ephemeral Docker containers with read-only root filesystems,",
        "capped memory at 128MB, and strictly disabled network egress.",
        "This allowed students to run untrusted code safely",
        "with sub-second return latency.\""
    ]
    for t_i, t_line in enumerate(twin_resp):
        draw.text((65, 372 + t_i * 20), t_line, fill="#e9edef", font=get_font(11))

    # Live voice / text status
    draw.rounded_rectangle([50, 510, 460, 625], radius=8, fill="#080e1d", outline="#1e293b", width=1)
    draw.text((65, 525), "PERSONA TELEMETRY & MEMORY PIPELINE", fill="#60a5fa", font=get_font(11, bold=True))
    draw.text((65, 550), "• Vector Store: FAISS with MiniLM embeddings", fill="#94a3b8", font=get_font(10))
    draw.text((65, 570), "• Core Architecture: Django + Hugging Face Spaces", fill="#94a3b8", font=get_font(10))
    draw.text((65, 590), "• Response Latency: 240ms end-to-end", fill="#10b981", font=get_font(10, bold=True))

    # Right: 5 Daily Habit Tracking Matrix
    draw.rounded_rectangle([500, 82, 1248, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((525, 100), "5 DAILY HABIT TRACKERS & PRODUCTIVITY PREDICTOR", fill="#60a5fa", font=get_font(14, bold=True))
    draw.text((525, 122), "Predictive behavioral analytics driving sustained peak engineering performance", fill="#64748b", font=get_font(11))
    
    habits = [
        ("Deep Work & Architecture", "5.4 hrs", "Target: 4.5 hrs", "120%", "#10b981"),
        ("Code Commits & Implementation", "4.8 hrs", "Target: 4.0 hrs", "120%", "#10b981"),
        ("Physical Training & Fitness", "45 mins", "Target: 45 mins", "100%", "#34d399"),
        ("AI Research & Paper Reading", "1.5 hrs", "Target: 1.0 hr", "150%", "#a855f7"),
        ("Sleep Optimization & Recovery", "7.8 hrs", "Target: 7.5 hrs", "104%", "#38bdf8")
    ]
    for i, (h_name, h_val, h_tgt, h_pct, h_col) in enumerate(habits):
        hy = 160 + i * 72
        draw.rounded_rectangle([525, hy, 1220, hy + 60], radius=8, fill="#111c33", outline="#1e293b", width=1)
        draw.text((545, hy + 12), h_name, fill="#ffffff", font=get_font(12, bold=True))
        draw.text((545, hy + 34), h_tgt, fill="#64748b", font=get_font(10))
        draw.text((850, hy + 18), h_val, fill=h_col, font=get_font(16, bold=True))
        draw.text((1150, hy + 18), h_pct, fill=h_col, font=get_font(16, bold=True), anchor="rm")
        # bar
        draw.rounded_rectangle([950, hy + 24, 1080, hy + 32], radius=4, fill="#1e293b")
        draw.rounded_rectangle([950, hy + 24, 950 + min(130, int(130 * (float(h_pct.replace('%','')) / 100))), hy + 32], radius=4, fill=h_col)

    # Productivity forecast
    draw.rounded_rectangle([525, 540, 1220, 625], radius=8, fill="#080e1d", outline="#10b981", width=1)
    draw.text((545, 555), "PREDICTIVE PRODUCTIVITY SCORE: 97.4% (PEAK EFFICIENCY)", fill="#10b981", font=get_font(12, bold=True))
    draw.text((545, 580), "Live on Hugging Face Spaces: https://ajay160380-digital-twin.hf.space", fill="#38bdf8", font=get_font(11))

    save_both(im, "i-am-solo/start.webp")
    save_both(im, "i-am-solo/profile.webp")

# =========================================================================
# 10. ANUVAD - BOOK TRANSLATION PLATFORM (anuvad)
# =========================================================================
def gen_anuvad():
    im, draw = draw_cyber_base(title="ANUVAD // SIDE-BY-SIDE BOOK TRANSLATION", category="NLP LOCALIZATION • GROQ LLAMA 3")
    
    # Left: Original English Text (Dual Column 1)
    draw.rounded_rectangle([32, 82, 620, 650], radius=10, fill="#0e1726", outline="#3b82f6", width=1)
    draw.rectangle([32, 82, 620, 122], fill="#111c33")
    draw.text((50, 96), "ORIGINAL ENGLISH SOURCE DOCUMENT // PAGE 42", fill="#60a5fa", font=get_font(12, bold=True))
    draw.text((520, 96), "LAYOUT: 100%", fill="#10b981", font=get_font(11, bold=True))
    
    en_paragraphs = [
        "Chapter 4: The Geometry of Deep Learning",
        "In modern artificial intelligence, high-dimensional manifolds form the bedrock of representation learning. When deep networks process raw data, they project inputs through successive affine transformations and non-linear activations.",
        "Gradient descent acts as an optimization trajectory navigating this complex loss landscape. By computing partial derivatives via backpropagation, weights update iteratively toward lower empirical risk.",
        "The mathematical beauty lies in how complex semantic concepts emerge naturally from simple matrix multiplications across hundreds of layers."
    ]
    ey = 145
    for p_i, p_txt in enumerate(en_paragraphs):
        draw.text((50, ey), p_txt if p_i==0 else f"§ {p_i}  " + p_txt[:55], fill="#ffffff" if p_i==0 else "#93c5fd", font=get_font(12 if p_i==0 else 11, bold=(p_i==0)))
        if p_i > 0:
            draw.text((70, ey + 22), p_txt[55:120], fill="#cbd5e1", font=get_font(11))
            draw.text((70, ey + 42), p_txt[120:], fill="#cbd5e1", font=get_font(11))
            ey += 75
        else:
            ey += 35

    # Right: Dual Column 2 - Hindi/Hinglish Translation & Vocabulary Vault
    draw.rounded_rectangle([640, 82, 1248, 650], radius=10, fill="#0e1726", outline="#10b981", width=1)
    draw.rectangle([640, 82, 1248, 122], fill="#0f291e")
    draw.text((660, 96), "HINDI / HINGLISH TRANSLATION (ORIGINAL FORMAT PRESERVED)", fill="#34d399", font=get_font(12, bold=True))
    draw.text((1150, 96), "GROQ LLAMA 3", fill="#34d399", font=get_font(11, bold=True))

    hi_paragraphs = [
        "अध्याय 4: डीप लर्निंग की ज्यामिति (Geometry)",
        "आधुनिक आर्टिफिशियल इंटेलिजेंस में, उच्च-आयामी मैनिफोल्ड्स (high-dimensional manifolds) रिप्रजेंटेशन लर्निंग की नींव बनाते हैं। जब गहरे नेटवर्क रॉ डेटा को प्रोसेस करते हैं, तो वे क्रमिक ट्रांसफॉर्मेशन द्वारा इनपुट्स को प्रोजेक्ट करते हैं।",
        "ग्रेडिएंट डिसेंट (Gradient Descent) इस जटिल लॉस लैंडस्केप में नेविगेट करने वाले ऑप्टिमाइज़ेशन प्रक्षेपवक्र (trajectory) के रूप में कार्य करता है। बैकप्रॉपैगैशन द्वारा आंशिक डेरिवेटिव्स की गणना करके वेट्स अपडेट होते हैं।"
    ]
    hy = 145
    for p_i, p_txt in enumerate(hi_paragraphs):
        draw.text((660, hy), p_txt if p_i==0 else f"§ {p_i}  " + p_txt[:55], fill="#ffffff" if p_i==0 else "#86efac", font=get_font(12 if p_i==0 else 11, bold=(p_i==0)))
        if p_i > 0:
            draw.text((680, hy + 22), p_txt[55:120], fill="#cbd5e1", font=get_font(11))
            draw.text((680, hy + 42), p_txt[120:], fill="#cbd5e1", font=get_font(11))
            hy += 75
        else:
            hy += 35

    # Vocabulary Vault Card
    draw.rounded_rectangle([660, 420, 1228, 625], radius=8, fill="#081424", outline="#2563eb", width=1)
    draw.text((680, 435), "VOCABULARY VAULT & INTERACTIVE CHAT-WITH-BOOK AI", fill="#60a5fa", font=get_font(11, bold=True))
    vocab = [
        ("Gradient Descent", "ढाल अवरोहण (Gradient Descent)", "ऑप्टिमाइज़ेशन कलन विधि"),
        ("Backpropagation", "पश्च-प्रसार (Backpropagation)", "त्रुटि गणना प्रक्रिया"),
        ("Loss Function", "हानि फलन (Loss Function)", "मॉडल त्रुटि का पैमाना")
    ]
    for v_i, (en_w, hi_w, desc) in enumerate(vocab):
        vy = 465 + v_i * 48
        draw.text((680, vy), "• " + en_w, fill="#38bdf8", font=get_font(11, bold=True))
        draw.text((850, vy), "-> " + hi_w, fill="#34d399", font=get_font(11))
        draw.text((1060, vy), desc, fill="#94a3b8", font=get_font(10))

    save_both(im, "booking-system/admin-dashboard.webp")
    save_both(im, "booking-system/admin-reservations.webp")

# =========================================================================
# 11. SMART WOMEN'S SAFETY DEVICE (safetysystem)
# =========================================================================
def gen_safety_system():
    im, draw = draw_cyber_base(title="SMART WOMEN'S SAFETY DEVICE // IOT HARDWARE", category="EMBEDDED ENGINEERING • ESP32", status="BBDU TECH EXPO'26 AWARD")
    
    # Award Banner at Top
    draw.rounded_rectangle([32, 75, 1248, 125], radius=8, fill="#1c1204", outline="#f59e0b", width=1)
    draw.text((50, 92), "🏆 BABU BANARASI DAS UNIVERSITY TECH EXPO'26 — INNOVATOR APPRECIATION AWARD WINNER", fill="#fbbf24", font=get_font(13, bold=True))
    draw.text((1050, 92), "VERIFIED INNOVATION", fill="#f59e0b", font=get_font(11, bold=True))

    # Left: Hardware Telemetry & Microcontroller Stats
    draw.rounded_rectangle([32, 140, 520, 650], radius=10, fill="#0d1424", outline="#3b82f6", width=1)
    draw.text((50, 158), "EMBEDDED HARDWARE ARCHITECTURE", fill="#38bdf8", font=get_font(13, bold=True))
    draw.text((50, 180), "Dual-Core ESP32 @ 240MHz + Multi-Sensor Alert Grid", fill="#64748b", font=get_font(11))
    
    hw_specs = [
        ("Microcontroller", "ESP32 Tensilica Dual-Core 240MHz", "ONLINE", "#10b981"),
        ("Cellular Transceiver", "GSM SIM800L Quad-Band", "SIGNAL: 94%", "#10b981"),
        ("Satellite Positioning", "Neo-6M GPS Module", "9 SATELLITES LOCKED", "#10b981"),
        ("Inertial Sensor", "MPU6050 6-DOF (Accel + Gyro)", "CALIBRATED", "#38bdf8"),
        ("Emergency SOS Trigger", "Hardware Push-Button + Fall Sensor", "ARMED", "#f59e0b"),
        ("Power Management", "3.7V Li-Po Battery (1200mAh)", "BATTERY: 92%", "#34d399")
    ]
    for i, (comp, desc, stat, col) in enumerate(hw_specs):
        sy = 210 + i * 58
        draw.rounded_rectangle([50, sy, 500, sy + 50], radius=6, fill="#111c33", outline="#1e293b", width=1)
        draw.text((64, sy + 8), comp, fill="#94a3b8", font=get_font(10))
        draw.text((64, sy + 26), desc, fill="#ffffff", font=get_font(11, bold=True))
        draw.text((485, sy + 26), stat, fill=col, font=get_font(10, bold=True), anchor="rm")

    draw.rounded_rectangle([50, 570, 500, 635], radius=6, fill="#0a1226", outline="#2563eb", width=1)
    draw.text((64, 582), "FIRMWARE: C++ / Arduino RTOS Core", fill="#60a5fa", font=get_font(10, bold=True))
    draw.text((64, 604), "SMS Geolocation payload latency: < 2.4s via GSM Network", fill="#34d399", font=get_font(10))

    # Right: Live GPS Map Coordinates & Accelerometer Shock Velocity
    draw.rounded_rectangle([540, 140, 1248, 650], radius=10, fill="#0d1424", outline="#2563eb", width=1)
    draw.text((565, 158), "LIVE GPS COORDINATES & DISTRESS EVENT TELEMETRY", fill="#60a5fa", font=get_font(13, bold=True))
    draw.text((565, 180), "Real-Time Latitude/Longitude Transmission & SMS Alert Payload", fill="#64748b", font=get_font(11))
    
    # GPS Coordinate Card
    draw.rounded_rectangle([565, 205, 1220, 290], radius=8, fill="#091428", outline="#10b981", width=1)
    draw.text((585, 220), "CURRENT SATELLITE GEOLOCATION LOCK:", fill="#34d399", font=get_font(11, bold=True))
    draw.text((585, 242), "LAT: 26.8924° N   |   LON: 81.0612° E", fill="#ffffff", font=get_font(18, bold=True))
    draw.text((585, 268), "Location: BBD University Campus Corridor, Lucknow, UP | Accuracy: ±1.8m", fill="#94a3b8", font=get_font(10))
    draw.rounded_rectangle([1060, 225, 1200, 270], radius=6, fill="#059669")
    draw.text((1130, 248), "GPS LOCKED", fill="#ffffff", font=get_font(11, bold=True), anchor="mm")

    # MPU6050 Shock / Fall Accelerometer Graph
    draw.rounded_rectangle([565, 305, 1220, 485], radius=8, fill="#090e1c", outline="#1e293b", width=1)
    draw.text((585, 320), "MPU6050 ACCELEROMETER TELEMETRY (SHOCK & FALL VELOCITY):", fill="#94a3b8", font=get_font(10, bold=True))
    
    # Graph area
    gx0, gy0, gx1, gy1 = 585, 345, 1200, 470
    draw.rectangle([gx0, gy0, gx1, gy1], fill="#060a14", outline="#1e293b")
    # Grid lines
    for gy in range(gy0 + 25, gy1, 25):
        draw.line([(gx0, gy), (gx1, gy)], fill="#0f192e", width=1)
    # Signal curve with shock spike
    pts = []
    mid_y = (gy0 + gy1) // 2
    for x in range(gx0, gx1, 6):
        if 850 < x < 950:
            # Spike
            spike = math.sin((x - 850) / 100 * math.pi) * 55
            pts.append((x, mid_y - int(spike)))
        else:
            noise = math.sin(x * 0.08) * 6
            pts.append((x, mid_y + int(noise)))
    draw.line(pts, fill="#ef4444", width=2)
    draw.text((880, gy0 + 10), "⚠️ 3.4G IMPACT SPIKE DETECTED", fill="#f87171", font=get_font(10, bold=True))
    draw.text((880, gy0 + 26), "Triggered Emergency SMS Dispatch", fill="#f87171", font=get_font(9))

    # Automatic Emergency Dispatch Log
    draw.rounded_rectangle([565, 500, 1220, 635], radius=8, fill="#1c0e12", outline="#ef4444", width=1)
    draw.text((585, 515), "AUTOMATED EMERGENCY SMS & CALL DISPATCH LOG:", fill="#fca5a5", font=get_font(11, bold=True))
    draw.text((585, 538), "1. Emergency Contact 1 (+91-98xxxxxx12): SMS Dispatched with Google Maps link [DELIVERED]", fill="#e2e8f0", font=get_font(10))
    draw.text((585, 558), "2. Emergency Contact 2 (+91-94xxxxxx45): SMS Dispatched + Voice Call Initiated [CONNECTED]", fill="#e2e8f0", font=get_font(10))
    draw.text((585, 578), "3. Police Distress Hotline (112): Geolocation broadcast transmitted [ACKNOWLEDGED]", fill="#e2e8f0", font=get_font(10))
    draw.text((585, 602), "Award Verification Link: https://i.ibb.co/B5Lm5YD0/Tech-Expo.png", fill="#38bdf8", font=get_font(10))

    save_both(im, "wis-2026/site.webp")
    save_both(im, "wis-2026/settings.webp")

print("Executing all screen generators...")
gen_brain_tumor()
gen_edutech()
gen_skillproof()
gen_aitutor()
gen_healthcare_screen()
gen_estateai()
gen_campaigniq()
gen_paisa_mitra()
gen_digital_twin()
gen_anuvad()
gen_safety_system()
print("ALL 11 AUTHENTIC CYBER UI SCREENS GENERATED SUCCESSFULLY!")
