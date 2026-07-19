import os, re

files = ['hr-solutions.html','real-estate.html','ceo-reset.html','finance-audit.html']

for fname in files:
    path = fname
    with open(path, 'r') as f:
        content = f.read()
    
    # Insert click-fix after .skill-card::before rule closing brace
    old = """.skill-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--brass);opacity:0;transition:opacity 0.2s}
.skill-card:hover::before{opacity:1}
.skill-card:hover{transform:translateY(-2px);box-shadow:0 12px 40px rgba(11,46,41,0.06)}"""
    
    new = """.skill-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--brass);opacity:0;transition:opacity 0.2s}
.skill-card::after{content:'';position:absolute;inset:0;z-index:10}
.skill-card:hover::before{opacity:1}
.skill-card:hover{transform:translateY(-2px);box-shadow:0 12px 40px rgba(11,46,41,0.06)}"""
    
    content = content.replace(old, new)
    
    # Make child elements non-interactive so overlay captures clicks
    old2 = ".skill-badge{display:inline-block;background:var(--porcelain);color:var(--muted);font-family:var(--font-mono);font-size:11px;padding:4px 12px;border-radius:100px;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.5px}"
    new2 = ".skill-badge{display:inline-block;background:var(--porcelain);color:var(--muted);font-family:var(--font-mono);font-size:11px;padding:4px 12px;border-radius:100px;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.5px;position:relative;z-index:5;pointer-events:none}"
    content = content.replace(old2, new2)
    
    old3 = ".skill-card h3{font-family:var(--font-display);font-size:22px;margin-bottom:8px;color:var(--ink)}"
    new3 = ".skill-card h3{font-family:var(--font-display);font-size:22px;margin-bottom:8px;color:var(--ink);position:relative;z-index:5;pointer-events:none}"
    content = content.replace(old3, new3)
    
    old4 = ".skill-card p{color:var(--muted);font-size:14px;margin-bottom:16px;min-height:60px}"
    new4 = ".skill-card p{color:var(--muted);font-size:14px;margin-bottom:16px;min-height:60px;position:relative;z-index:5;pointer-events:none}"
    content = content.replace(old4, new4)
    
    old5 = ".skill-meta{display:flex;justify-content:space-between;align-items:center}"
    new5 = ".skill-meta{display:flex;justify-content:space-between;align-items:center;position:relative;z-index:5;pointer-events:none}"
    content = content.replace(old5, new5)
    
    with open(path, 'w') as f:
        f.write(content)
    print(f"Fixed {fname}")

print("Done.")
