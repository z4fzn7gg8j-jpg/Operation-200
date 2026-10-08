from pathlib import Path

html = Path('index.html')
s = html.read_text()
old = '<div class="op20-hero"><div class="nums"><span class="n20">20</span><span class="sep">·</span><span>160</span><span class="sep">·</span><span class="n3">3</span></div></div>'
new = '<div class="op20-hero op20-strength-banner"><img src="assets/140 Barbell Strength Banner.png" alt="20 · 140 · 3 strength banner"></div>'
if new not in s:
    if old not in s:
        raise SystemExit('Operation 20 hero target not found')
    s = s.replace(old, new, 1)
    html.write_text(s)

css = Path('assets/css/app.css')
c = css.read_text()
marker = '/* Operation 20 strength banner crop */'
block = '''

/* Operation 20 strength banner crop */
.op20-hero.op20-strength-banner{
  position:relative;
  width:100%;
  aspect-ratio:2020 / 569;
  min-height:0 !important;
  height:auto !important;
  padding:0 !important;
  overflow:hidden;
  background:none !important;
  border:0 !important;
  border-radius:28px;
}
.op20-hero.op20-strength-banner::before,
.op20-hero.op20-strength-banner::after{display:none !important;}
.op20-hero.op20-strength-banner img{
  position:absolute;
  display:block;
  max-width:none;
  width:101.386%;
  height:auto;
  left:-0.693%;
  top:-5.10%;
  margin:0;
  pointer-events:none;
  user-select:none;
}
'''
if marker not in c:
    css.write_text(c + block)
