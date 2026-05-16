import os
import glob
from PIL import Image

def compress_and_convert(folder):
    png_files = glob.glob(os.path.join(folder, "*.png"))
    for filepath in png_files:
        try:
            img = Image.open(filepath)
            # WebP supports alpha channel, so we can convert directly
            webp_path = filepath.replace('.png', '.webp')
            img.save(webp_path, 'WEBP', quality=75, method=6)
            os.remove(filepath)
            print(f"Converted {filepath} -> {webp_path}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

# Process both folders
compress_and_convert('Beneficiary_App/screenshots')
compress_and_convert('Researcher_App/screenshots')

def update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace .png with .webp in image sources
    new_content = content.replace('.png"', '.webp"')
    new_content = new_content.replace('.png)', '.webp)')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated HTML references in {filepath}")

update_html('Beneficiary_App/beneficiary_presentation.html')
update_html('Researcher_App/researcher_presentation.html')
