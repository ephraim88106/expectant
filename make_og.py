#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OG 이미지(1200x630) 템플릿 HTML 생성. Playwright로 스크린샷을 찍어 assets/og/*.png 로 저장한다.

사용:
    python3 make_og.py          # /tmp/og/*.html 생성
    node make_og.js             # 위 HTML을 PNG로 렌더 (별도 스크립트)
"""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = "/tmp/og"

CARDS = [
    ("default", "임신 · 출산 정보 가이드",
     "혹시… 임신일까요?", "가장 먼저 확인해야 할 것들", "#F9D6D9", "#E6F0E9"),
    ("pregnancy-test", "임신 확인",
     "임테기부터", "피검사 · 초음파까지", "#FDEBEC", "#F9D6D9"),
    ("symptoms", "주차별 증상",
     "지금 내 몸에", "일어나는 일", "#E6F0E9", "#CDE0D3"),
    ("tools", "임신 계산기",
     "날짜만 넣으면", "계산이 끝나요", "#EFEBF7", "#C6BBE3"),
    ("guide", "임신 · 출산 가이드",
     "임신 준비부터", "산후 회복까지", "#F7ECE5", "#EADFD7"),
]

TPL = """<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    width:1200px; height:630px; overflow:hidden; position:relative;
    font-family:'Pretendard Variable',Pretendard,-apple-system,sans-serif;
    background:#FFFCFA; display:flex; align-items:center;
    letter-spacing:-.035em; word-break:keep-all;
  }}
  .blob {{ position:absolute; border-radius:50%; filter:blur(90px); }}
  .b1 {{ width:620px; height:620px; background:{c1}; top:-220px; right:-140px; opacity:.85; }}
  .b2 {{ width:520px; height:520px; background:{c2}; bottom:-250px; left:-120px; opacity:.7; }}
  .b3 {{ width:380px; height:380px; background:#EFEBF7; top:44%; left:46%; opacity:.6; }}
  .inner {{ position:relative; padding:0 84px; width:100%; }}
  .brand {{ display:flex; align-items:center; gap:14px; margin-bottom:44px; }}
  .mark {{
    width:60px; height:60px; border-radius:20px;
    background:linear-gradient(140deg,#F2B9BF,#D4808B 60%,#C6BBE3);
    display:grid; place-items:center;
    box-shadow:0 8px 22px rgba(212,128,139,.32);
  }}
  .mark svg {{ width:32px; height:32px; }}
  .wordmark {{ font-size:38px; font-weight:800; color:#33272A; letter-spacing:-.05em; }}
  .wordmark em {{ font-style:normal; color:#D4808B; }}
  .eyebrow {{
    display:inline-block; font-size:22px; font-weight:700; letter-spacing:.09em;
    color:#B96874; background:#FDEBEC; padding:11px 26px; border-radius:999px;
    margin-bottom:30px;
  }}
  h1 {{ font-size:82px; line-height:1.22; font-weight:800; color:#33272A; }}
  h1 em {{ font-style:normal; color:#D4808B; }}
  .url {{
    position:absolute; bottom:52px; left:84px;
    font-size:25px; font-weight:600; color:#9A8B90; letter-spacing:-.01em;
  }}
</style></head>
<body>
  <span class="blob b1"></span><span class="blob b2"></span><span class="blob b3"></span>
  <div class="inner">
    <div class="brand">
      <span class="mark"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.9"
        stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 6.6a5.1 5.1 0 0 0-7.2 0L12 8.2l-1.6-1.6a5.1 5.1 0 1 0-7.2 7.2L12 22l8.8-8.2a5.1 5.1 0 0 0 0-7.2z"/></svg></span>
      <span class="wordmark">expect<em>ant</em></span>
    </div>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{l1}<br><em>{l2}</em></h1>
  </div>
  <div class="url">expectant.ephseed.com</div>
</body></html>
"""

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    names = []
    for name, eyebrow, l1, l2, c1, c2 in CARDS:
        html = TPL.format(eyebrow=eyebrow, l1=l1, l2=l2, c1=c1, c2=c2)
        with open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
        names.append(name)
    with open(os.path.join(OUT, "list.json"), "w") as f:
        json.dump(names, f)
    print("템플릿 %d개 생성: %s" % (len(names), ", ".join(names)))
