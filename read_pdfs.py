import sys
try:
    from pypdf import PdfReader
except ImportError:
    import os
    os.system('pip install pypdf')
    from pypdf import PdfReader

def extract_text(path):
    reader = PdfReader(path)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text

print("--- CERT 1 ---")
print(extract_text('2jxESPvorR7fmypXj_8eNRcRqBZM9HLvwGw_6a3f3ef2d73b9d1e337810ff_1784552831295_completion_certificate.pdf')[:500])
print("\n--- CERT 2 ---")
print(extract_text('4b5788DoosozTZEfv_WRaqrfXsBgp477LWq_6a3f3ef2d73b9d1e337810ff_1784552380046_completion_certificate.pdf')[:500])
