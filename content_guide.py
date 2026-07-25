#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
가이드 카테고리 — 4개 허브 + 매일 자동 발행되는 개별 글

개별 글은 guide_articles/<slug와 동일하되 하이픈을 밑줄로>.py 에 한 파일씩 둔다.
각 모듈이 반드시 정의해야 하는 것:

    CATEGORY = "preparation"      # preparation | health | birth | postpartum
    SLUG     = "ovulation-day"    # URL 조각 (하이픈)
    TITLE    = "<title> 태그 문구"
    H1       = "페이지 제목"
    DESC     = "메타 설명 (한 문장)"
    KEYWORDS = "쉼표로 구분한 키워드"
    READING  = "7"                # 예상 읽기 분
    RELATED  = [("표시명", "설명", "경로.html"), ...]   # 3개 권장
    def body(H):  return "...HTML..."   # H = 헬퍼 모음 dict

발행 순서와 상태는 _content-queue.json 이 관리한다.
"""

import os, re, json, glob, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))

CATS = {
    "preparation": {
        "name": "임신 준비",
        "icon": "leaf",
        "cls": "i-sage",
        "lead": "임신을 계획하는 시기에 몸과 생활을 준비하는 방법을 안내합니다. "
                "배란일 계산부터 엽산, 임신 전 검사까지 미리 챙기면 좋은 것들입니다.",
    },
    "health": {
        "name": "임신 중 건강",
        "icon": "heart",
        "cls": "i-rose",
        "lead": "임신 기간 동안 무엇을 먹고, 어떤 약을 쓸 수 있고, 어떻게 몸을 돌봐야 하는지. "
                "가장 자주 묻는 건강 질문들을 정리했습니다.",
    },
    "birth": {
        "name": "출산 준비",
        "icon": "bag",
        "cls": "i-cream",
        "lead": "출산이 가까워지면 준비해야 할 것들과 분만 과정에 대한 이해. "
                "미리 알아두면 그날이 훨씬 덜 두렵습니다.",
    },
    "postpartum": {
        "name": "산후 회복",
        "icon": "moon",
        "cls": "i-lav",
        "lead": "출산 후의 몸과 마음을 돌보는 시간. 회복 과정에서 무엇이 정상이고 "
                "언제 도움을 요청해야 하는지 알려드립니다.",
    },
}
CAT_ORDER = ["preparation", "health", "birth", "postpartum"]


def load_queue():
    p = os.path.join(ROOT, "_content-queue.json")
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as f:
        return json.load(f).get("items", [])


def load_articles():
    """guide_articles/*.py 를 모두 읽어 모듈 리스트로 반환"""
    mods = []
    for path in sorted(glob.glob(os.path.join(ROOT, "guide_articles", "*.py"))):
        name = os.path.basename(path)[:-3]
        if name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location("guide_art_" + name, path)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        if getattr(m, "CATEGORY", None) in CATS and getattr(m, "SLUG", None):
            mods.append(m)
    return mods


def build(G):
    layout = G["layout"]; add = G["add"]; entry = G["entry"]
    I = G["I"]; link = G["link"]; callout = G["callout"]
    breadcrumb = G["breadcrumb"]; article_page = G["article_page"]

    helpers = {k: G[k] for k in
               ("I", "callout", "keypoints", "table", "faq", "steps", "link")}

    queue = load_queue()
    arts = load_articles()
    by_slug = {m.SLUG: m for m in arts}

    # 큐 순서를 따르되, 큐에 없는 글도 뒤에 붙인다
    ordered, seen = [], set()
    for q in sorted(queue, key=lambda x: x.get("order", 999)):
        m = by_slug.get(q["slug"])
        if m:
            ordered.append((m, q)); seen.add(m.SLUG)
    for m in arts:
        if m.SLUG not in seen:
            ordered.append((m, None))

    pub_by_cat = {c: [] for c in CATS}
    for m, q in ordered:
        pub_by_cat[m.CATEGORY].append((m, q))

    pending_by_cat = {c: [] for c in CATS}
    for q in sorted(queue, key=lambda x: x.get("order", 999)):
        if q["slug"] not in by_slug and q["category"] in CATS:
            pending_by_cat[q["category"]].append(q)

    # ---------------------------------------------------------- 개별 글
    for m, q in ordered:
        cat = CATS[m.CATEGORY]
        path = "guide/%s/%s.html" % (m.CATEGORY, m.SLUG)
        trail = [("가이드", "guide/index.html"),
                 (cat["name"], "guide/%s/index.html" % m.CATEGORY),
                 (m.H1, None)]

        # 같은 카테고리의 앞뒤 글로 이전/다음 연결
        sibs = pub_by_cat[m.CATEGORY]
        i = [s[0].SLUG for s in sibs].index(m.SLUG)
        prev = (sibs[i - 1][0].H1, "guide/%s/%s.html" % (m.CATEGORY, sibs[i - 1][0].SLUG)) if i > 0 else None
        nxt = (sibs[i + 1][0].H1, "guide/%s/%s.html" % (m.CATEGORY, sibs[i + 1][0].SLUG)) if i < len(sibs) - 1 else None

        rel_items = getattr(m, "RELATED", None) or [
            ("임신 확인 방법", "임테기·피검사·초음파 비교", "pregnancy-test/index.html"),
            ("주차별 증상", "시기마다 달라지는 몸의 변화", "symptoms/index.html"),
            ("임신 계산기", "예정일·주수·검사시기", "tools/index.html"),
        ]

        article_page(path, m.TITLE, m.H1, m.DESC, m.KEYWORDS, trail,
                     m.body(helpers), rel_items, prev=prev, nxt=nxt,
                     reading=getattr(m, "READING", "7"))

    # ---------------------------------------------------------- 카테고리 허브
    for slug in CAT_ORDER:
        cat = CATS[slug]
        path = "guide/%s/index.html" % slug
        pubs = pub_by_cat[slug]
        pends = pending_by_cat[slug]

        if pubs:
            items = "".join(
                '<a class="list-item reveal" href="%s"><span class="list-item__no">%02d</span>'
                '<div><b>%s</b><p>%s</p></div></a>'
                % (link("guide/%s/%s.html" % (slug, m.SLUG)), i + 1, m.H1, m.DESC)
                for i, (m, q) in enumerate(pubs))
            published_block = ('<div class="section-head" style="margin-top:8px"><h2>발행된 글</h2></div>'
                               '<div class="list-grid">%s</div>' % items)
        else:
            published_block = callout(
                "info", "첫 글을 준비하고 있어요",
                "이 카테고리의 글은 매일 밤 한 편씩 순차적으로 공개됩니다. 아래 예정 목록을 참고해 주세요.")

        if pends:
            upcoming = ('<div class="section-head" style="margin-top:56px"><h2>발행 예정</h2>'
                        '<p>매일 밤 9시에 한 편씩 공개됩니다.</p></div>'
                        '<div class="steps">%s</div>'
                        % "".join('<div class="step"><div><b>%s</b><p>공개 예정</p></div></div>' % q["title"]
                                  for q in pends))
        else:
            upcoming = ""

        body = """
<section class="hub-hero">
  <div class="hero__bg" aria-hidden="true"><span class="blob blob--2"></span><span class="blob blob--3"></span></div>
  <div class="wrap">
    {crumb}
    <span class="eyebrow">{icon} 가이드</span>
    <h1>{name}</h1>
    <p>{lead}</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    {published}
    {upcoming}
    <div class="cta-band" style="margin-top:60px">
      <h2>먼저 확인할 수 있는 내용</h2>
      <p>임신 확인 방법과 주차별 증상은 이미 자세히 정리되어 있어요.</p>
      <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:24px">
        <a class="btn btn--primary" href="/pregnancy-test/">임신 확인 방법</a>
        <a class="btn btn--ghost" href="/symptoms/">주차별 증상</a>
      </div>
    </div>
  </div>
</section>
""".format(crumb=breadcrumb(path, [("가이드", "guide/index.html"), (cat["name"], None)]),
           icon=I[cat["icon"]], name=cat["name"], lead=cat["lead"],
           published=published_block, upcoming=upcoming)

        add(path,
            layout(path, "%s — 임신·출산 가이드 | Expectant" % cat["name"], cat["lead"],
                   body, ",".join([cat["name"]] + [m.SLUG for m, _ in pubs])),
            entry(path, cat["name"], cat["lead"][:60], "가이드", cat["name"]))

    # ---------------------------------------------------------- 가이드 전체 허브
    cards = "".join(
        '<a class="card reveal" href="{href}"><span class="card__icon {cls}">{ic}</span>'
        '<h3>{n}</h3><p>{d}</p><div class="card__links">{chips}</div>'
        '<span class="card__more">{cnt} {arrow}</span></a>'.format(
            href=link("guide/%s/index.html" % s), cls=CATS[s]["cls"], ic=I[CATS[s]["icon"]],
            n=CATS[s]["name"], d=CATS[s]["lead"],
            chips="".join('<span class="chip">%s</span>' % m.H1 for m, _ in pub_by_cat[s][:2])
                  or '<span class="chip">준비 중</span>',
            cnt=("%d편 보기" % len(pub_by_cat[s])) if pub_by_cat[s] else "예정 목록 보기",
            arrow=I["arrow"])
        for s in CAT_ORDER)

    total = sum(len(v) for v in pub_by_cat.values())
    remaining = sum(len(v) for v in pending_by_cat.values())

    guide_body = """
<section class="hub-hero">
  <div class="hero__bg" aria-hidden="true"><span class="blob blob--1"></span></div>
  <div class="wrap">
    {crumb}
    <span class="eyebrow">{book} 가이드</span>
    <h1>임신 준비부터 산후까지</h1>
    <p>임신을 계획하는 순간부터 출산 후 회복까지, 시기마다 필요한 정보를 모았습니다.
       현재 <b>{total}편</b>이 공개되어 있고 <b>{remaining}편</b>이 매일 밤 순차적으로 추가됩니다.</p>
  </div>
</section>
<section class="section">
  <div class="wrap"><div class="cards">{cards}</div></div>
</section>
""".format(crumb=breadcrumb("guide/index.html", [("가이드", None)]), book=I["book"],
           total=total, remaining=remaining, cards=cards)

    add("guide/index.html",
        layout("guide/index.html", "임신·출산 가이드 — 준비부터 산후까지 | Expectant",
               "임신 준비, 임신 중 건강, 출산 준비, 산후 회복. 임신의 전 과정에서 필요한 정보를 "
               "카테고리별로 정리한 가이드입니다.",
               guide_body, "임신 준비,임신 중 건강,출산 준비,산후조리,임신 가이드"),
        entry("guide/index.html", "임신·출산 가이드", "준비·건강·출산·산후 전 과정", "가이드", "가이드"))
