import re

def generate_html():
    with open('extracted_links.txt', 'r') as f:
        content = f.read()

    # Regex to find URLs
    urls = re.findall(r'href="(https://[^"]+)"', content)
    
    # Dedup urls while preserving order
    seen = set()
    unique_urls = []
    for url in urls:
        if url not in seen:
            unique_urls.append(url)
            seen.add(url)

    print('<option value="" disabled selected>Выберите версию</option>')
    
    for url in unique_urls:
        # Extract version from filename
        # Pattern: CapCut_X_X_X_XXXX_... or CapCut_split_X_X_X_XXXX_...
        match = re.search(r'CapCut(?:_split)?_(\d+_\d+_\d+_\d+)', url)
        if match:
            version_str = match.group(1).replace('_', '.')
        else:
            # Fallback for shorter versions like 2.5.3.801 which might match, but try generic
            match_generic = re.search(r'CapCut(?:_split)?_([0-9_]+)', url)
            if match_generic:
                version_str = match_generic.group(1).replace('_', '.')
            else:
                version_str = "Unknown Version"
        
        # HTML Option
        print(f'<option value="{url}">Версия {version_str}</option>')

if __name__ == '__main__':
    generate_html()
