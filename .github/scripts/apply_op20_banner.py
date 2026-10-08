from pathlib import Path
import re

p = Path('index.html')
s = p.read_text()

css_marker = '/* Operation 20 opening banner */'
css_block = '''/* Operation 20 opening banner */
#box-phase.op20-strength-banner-shell{
  position:relative;
  overflow:visible !important;
  min-height:0 !important;
  padding:0 !important;
  background:none !important;
  border:none !important;
  border-radius:0 !important;
}
#box-phase.op20-strength-banner-shell::before,
#box-phase.op20-strength-banner-shell::after{ display:none !important; }
.op20-strength-banner-frame{
  position:relative;
  width:100%;
  aspect-ratio:2020 / 569;
  overflow:hidden;
  border-radius:28px;
  line-height:0;
}
.op20-strength-banner-frame img{
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

if css_marker not in s:
    anchor = '/* Achievement banner */'
    if anchor not in s:
        raise SystemExit('CSS anchor not found')
    s = s.replace(anchor, css_block + '\n' + anchor, 1)

new_box = '''<div id="box-phase" class="op20-strength-banner-shell" onclick="tapBox('box-phase'); openModal('modal-phase')" aria-label="Operation 20 banner">
  <div class="op20-strength-banner-frame">
    <img src="assets/140 Barbell Strength Banner.png" alt="20 · 140 · 3 strength banner" />
  </div>
</div>

'''

if 'assets/140 Barbell Strength Banner.png' not in s:
    pattern = r'<div id="box-phase"[\s\S]*?(?=<!-- BOX 2: LOGGING STREAK \+ ROADMAP / PHASE REPORTS -->)'
    s, n = re.subn(pattern, new_box, s, count=1)
    if n != 1:
        raise SystemExit('Phase banner block not found')

p.write_text(s)
