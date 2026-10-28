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
        im.save(full, "WEBP", quality=92)
    print(f"Generated: {rel_path}")

def draw_cyber_base(w=1280, h=720, primary="#3b82f6", title="SYSTEM DASHBOARD", category="AI INFERENCE ENGINE", status="VERIFIED PRODUCTION"):
    im = Image.new("RGB", (w, h), "#060913")
    draw = ImageDraw.Draw(im)

    # Grid
    grid_spacing = 40
    for x in range(0, w, grid_spacing):
        draw.line([(x, 0), (x, h)], fill="#0c162d", width=1)
    for y in range(0, h, grid_spacing):
        draw.line([(0, y), (w, y)], fill="#0c162d", width=1)

    # Outer decorative frame line & corner brackets
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
    f_brand = get_font(13, bold=True)
    f_sub = get_font(11, bold=False)
    draw.text((48, 28), "AJAY VISHWAKARMA // AI & FULL-STACK", fill="#94a3b8", font=f_brand)
    draw.text((48, 44), f"{category} • REAL-TIME DEPLOYMENT", fill="#475569", font=f_sub)

    # Center title pill
    f_pill = get_font(13, bold=True)
    draw.rounded_rectangle([w // 2 - 210, 22, w // 2 + 210, 52], radius=6, fill="#111c35", outline="#2563eb", width=1)
    draw.text((w // 2, 37), title, fill="#60a5fa", font=f_pill, anchor="mm")

    # Right indicator
    f_mono = get_font(11, bold=True)
    draw.text((w - 200, 37), status, fill="#10b981", font=f_mono, anchor="rm")

    # Footer Bar
    draw.rectangle([12, h - 46, w - 13, h - 13], fill="#0a1020", outline="#1e293b", width=1)
    f_foot = get_font(11, bold=False)
    draw.text((30, h - 30), "STATUS: LIVE IN PRODUCTION | LATENCY: < 35ms | ZERO-ERROR PIPELINE", fill="#64748b", font=f_foot)
    draw.text((w - 30, h - 30), "CLOUD HOSTED • SECURE DEPLOYMENT", fill="#94a3b8", font=f_foot, anchor="rm")

    return im, draw

print("Helper base defined!")
