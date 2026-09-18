with open('/Users/nisaalkan/.gemini/antigravity/scratch/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_tag = '<style>'
end_tag = '</style>'
start_idx = html.find(start_tag) + len(start_tag)
end_idx = html.find(end_tag)

css_content = html[start_idx:end_idx].strip()

with open('/Users/nisaalkan/.gemini/antigravity/scratch/site/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("style.css synced.")
