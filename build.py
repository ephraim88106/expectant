#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Expectant — static site generator."""

import os, re, json, shutil, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://expectant.ephseed.com"
TODAY = datetime.date.today().isoformat()

# ---------------------------------------------------------------- icons
I = {
"baby":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12h.01M15 12h.01M10 16c.5.6 1.2.9 2 .9s1.5-.3 2-.9"/><circle cx="12" cy="12" r="9"/><path d="M12 3c1.5 1 2 2 2 3"/></svg>',
"test":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="7" width="16" height="10" rx="3"/><path d="M9 10v4M12.5 10v4"/></svg>',
"calendar":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M8 3v4M16 3v4M3 10h18"/></svg>',
"heart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 6.6a5.1 5.1 0 0 0-7.2 0L12 8.2l-1.6-1.6a5.1 5.1 0 1 0-7.2 7.2L12 22l8.8-8.2a5.1 5.1 0 0 0 0-7.2z"/></svg>',
"leaf":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6"/></svg>',
"calc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="3"/><path d="M8 6h8M8 11h.01M12 11h.01M16 11h.01M8 15h.01M12 15h.01M16 15v4M8 19h4"/></svg>',
"stetho":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 3v6a5 5 0 0 0 10 0V3"/><path d="M4 3h2M12 3h2"/><path d="M9 14v2a5 5 0 0 0 10 0v-1"/><circle cx="19" cy="12" r="2.4"/></svg>',
"scan":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/><circle cx="12" cy="12" r="3.2"/></svg>',
"search":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
"menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
"close":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>',
"chev":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
"arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
"caret":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg>',
"plus":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>',
"spark":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/><circle cx="12" cy="12" r="3"/></svg>',
"bulb":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.5.4.9 1 1 1.7l.1.5h5l.1-.5c.1-.7.5-1.3 1-1.7A6 6 0 0 0 12 3z"/></svg>',
"warn":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 9v4M12 17h.01"/><path d="M10.3 3.9 2.4 17.5A2 2 0 0 0 4.1 20.5h15.8a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/></svg>',
"info":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 16v-5M12 8h.01"/></svg>',
"check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 13 4 4L19 7"/></svg>',
"clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
"refresh":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-2.6-6.4"/><path d="M21 4v5h-5"/></svg>',
"book":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5"/></svg>',
"bag":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h16l-1.2 12.2a2 2 0 0 1-2 1.8H7.2a2 2 0 0 1-2-1.8z"/><path d="M9 11V6a3 3 0 0 1 6 0v5"/></svg>',
"moon":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 13.2A9 9 0 1 1 10.8 3a7 7 0 0 0 10.2 10.2z"/></svg>',
}

# ---------------------------------------------------------------- nav
NAV = [
    ("임신 확인", "pregnancy-test/index.html", [
        ("LABEL", "임신 테스트기"),
        ("임테기 사용시기", "pregnancy-test/when-to-test.html"),
        ("얼리 임테기", "pregnancy-test/early-test.html"),
        ("임테기 사용법", "pregnancy-test/how-to-use.html"),
        ("임테기 두 줄 판독", "pregnancy-test/two-lines.html"),
        ("임테기 오류·증발선", "pregnancy-test/errors.html"),
        ("임테기 역전", "pregnancy-test/reversal.html"),
        ("SEP", ""),
        ("LABEL", "병원 검사"),
        ("피검사 (hCG 수치)", "pregnancy-test/blood-test.html"),
        ("초음파 검사", "pregnancy-test/ultrasound.html"),
    ]),
    ("주차별 증상", "symptoms/index.html", [
        ("LABEL", "시기별 가이드"),
        ("임신 극초기 증상", "symptoms/very-early.html"),
        ("임신 초기 증상 (1~13주)", "symptoms/first-trimester.html"),
        ("임신 중기 증상 (14~27주)", "symptoms/second-trimester.html"),
        ("임신 막달 증상 (28~40주)", "symptoms/third-trimester.html"),
        ("SEP", ""),
        ("주차별 전체 타임라인", "symptoms/index.html#timeline"),
    ]),
    ("계산기", "tools/index.html", [
        ("출산 예정일 계산기", "tools/due-date.html"),
        ("임신 주수 계산기", "tools/pregnancy-week.html"),
        ("임테기 검사시기 계산기", "tools/test-timing.html"),
    ]),
    ("더보기", "guide/index.html", [
        ("임신 준비", "guide/preparation/index.html"),
        ("임신 중 건강", "guide/health/index.html"),
        ("출산 준비", "guide/birth/index.html"),
        ("산후 회복", "guide/postpartum/index.html"),
    ]),
]

CATEGORY_LABEL = {
    "pregnancy-test": "임신 확인",
    "symptoms": "주차별 증상",
    "tools": "계산기",
    "guide": "가이드",
    "": "홈",
}

# ---------------------------------------------------------------- helpers
def rel(path):
    """asset prefix — root-absolute so Cloudflare Pages' clean URLs never break it"""
    return "/"

def url_of(path):
    """disk path -> clean public URL (Cloudflare Pages strips the .html extension)"""
    if path == "index.html":
        return "/"
    if path.endswith("/index.html"):
        return "/" + path[:-len("index.html")]
    return "/" + path[:-len(".html")]

def link(path, page_path=None):
    if path.startswith(("http", "#", "mailto:", "data:")):
        return path
    frag = ""
    if "#" in path:
        path, frag = path.split("#", 1)
        frag = "#" + frag
    return url_of(path) + frag

def nav_html(page_path):
    out = []
    for title, hub, items in NAV:
        drop = []
        for a, b in items:
            if a == "LABEL":
                drop.append('<div class="dropdown__label">%s</div>' % b)
            elif a == "SEP":
                drop.append('<div class="dropdown__sep"></div>')
            else:
                drop.append('<a href="%s">%s</a>' % (link(b, page_path), a))
        cur = ' aria-current="page"' if page_path.startswith(hub.split("/")[0] + "/") and "/" in hub else ""
        out.append(
            '<div class="nav__item"><a class="nav__link" href="%s"%s>%s<span class="nav__chev">%s</span></a>'
            '<div class="dropdown">%s</div></div>'
            % (link(hub, page_path), cur, title, I["chev"], "".join(drop))
        )
    return "".join(out)

def drawer_html(page_path):
    out = []
    for i, (title, hub, items) in enumerate(NAV):
        links = "".join(
            '<a href="%s">%s</a>' % (link(b, page_path), a)
            for a, b in items if a not in ("LABEL", "SEP")
        )
        out.append(
            '<div class="drawer__group">'
            '<button class="drawer__toggle" aria-expanded="false">%s%s</button>'
            '<div class="drawer__panel-list"><div><a href="%s"><b>%s 전체보기</b></a>%s</div></div></div>'
            % (title, I["chev"], link(hub, page_path), title, links)
        )
    return "".join(out)

def footer_html(page_path):
    cols = []
    for title, hub, items in NAV[:3]:
        lis = "".join(
            '<li><a href="%s">%s</a></li>' % (link(b, page_path), a)
            for a, b in items if a not in ("LABEL", "SEP")
        )
        cols.append("<div><h4>%s</h4><ul>%s</ul></div>" % (title, lis))
    return """
<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__about">
        <a class="logo" href="%(home)s"><span class="logo__mark">%(mark)s</span>
        <span class="logo__text">expect<em>ant</em></span></a>
        <p>임신을 준비하고, 확인하고, 함께 기다리는 모든 순간을 위한 정보 가이드입니다.</p>
      </div>
      %(cols)s
    </div>

    <section class="biz" aria-labelledby="biz-title">
      <h4 id="biz-title">사업자 정보</h4>
      <dl class="biz__list">
        <div><dt>상호</dt><dd>에브라임 시드 (Ephraim Seed)</dd></div>
        <div><dt>대표자</dt><dd>김남호</dd></div>
        <div><dt>사업자등록번호</dt><dd>359-05-03748</dd></div>
        <div><dt>주소</dt><dd>인천광역시 연수구 아카데미로 446</dd></div>
        <div><dt>이메일</dt><dd><a href="mailto:namho8816@naver.com">namho8816@naver.com</a></dd></div>
        <div><dt>전화</dt><dd><a href="tel:01059440714">010-5944-0714</a></dd></div>
      </dl>
    </section>

    <div class="footer__bottom">
      <span>&copy; <span data-year>2026</span> Ephseed AI. All rights reserved. 의료 조언을 대체하지 않습니다.</span>
      <span>최종 업데이트 %(today)s</span>
    </div>
  </div>
</footer>
""" % dict(home=link("index.html", page_path), mark=I["heart"], cols="".join(cols), today=TODAY)

# ---------------------------------------------------------------- ads (Kakao AdFit)
AD_TOP = """
<div class="ad ad--top" aria-label="광고">
  <div class="ad__pc">
    <ins class="kakao_ad_area" style="display:none;"
         data-ad-unit="DAN-MHSpt9N6WJmbCvFE"
         data-ad-width="728"
         data-ad-height="90"></ins>
  </div>
  <div class="ad__mo">
    <ins class="kakao_ad_area" style="display:none;"
         data-ad-unit="DAN-VthMQex1Zl00SsDa"
         data-ad-width="320"
         data-ad-height="100"></ins>
  </div>
</div>
"""

AD_SIDE = """
<aside class="ad ad--side" aria-label="광고">
  <ins class="kakao_ad_area" style="display:none;"
       data-ad-unit="DAN-81oJa1C0kry2wmSl"
       data-ad-width="160"
       data-ad-height="600"></ins>
</aside>
"""

AD_SCRIPT = '<script type="text/javascript" src="//t1.kakaocdn.net/kas/static/ba.min.js" async></script>'

DISCLAIMER = """
<div class="disclaimer">
  <b>의학 정보 안내</b> — 이 페이지의 내용은 일반적인 건강 정보를 제공할 목적으로 작성되었으며,
  의사의 진단이나 치료를 대신할 수 없습니다. 증상이 걱정되거나 개인적인 상황에 대한 판단이 필요하다면
  반드시 산부인과 전문의와 상담해 주세요. 응급 증상(심한 출혈, 극심한 복통, 실신 등)이 있다면 즉시 의료기관을 방문하세요.
</div>
"""

# ---------------------------------------------------------------- SEO 설정
# 각 검색엔진 웹마스터도구에서 발급받은 소유확인 코드를 넣으면 메타태그가 자동 삽입된다.
# 값이 빈 문자열이면 해당 태그는 출력되지 않는다.
VERIFY = {
    # Google Search Console — "URL 접두어" 속성의 HTML 태그 방식 content 값
    "google":   "prwsKG6JlRxVMzUakGjBY0Nqhqv1Lqbi3nJBZ9NPS8o",
    # 네이버 서치어드바이저 — 웹마스터 도구 HTML 태그 방식 content 값
    "naver":    "c263c4e3eac81eacf5513faee88091648d122793",
    "bing":     "",   # Bing Webmaster        <meta name="msvalidate.01">
}

ORG = {
    "name": "에브라임 시드",
    "alt": "Ephraim Seed",
    "email": "namho8816@naver.com",
    "phone": "+82-10-5944-0714",
    "street": "아카데미로 446",
    "locality": "연수구",
    "region": "인천광역시",
    "country": "KR",
}

# 구조화 데이터 수집 버퍼 — 본문을 만들 때 채워지고 layout()에서 비워진다
_FAQ_BUF = []
_CRUMB_BUF = []


def og_image_for(page_path):
    """페이지 경로 → OG 이미지. 카테고리 전용 이미지가 있으면 그것을, 없으면 기본 이미지."""
    top = page_path.split("/")[0]
    cand = "assets/og/%s.png" % top
    if top and os.path.exists(os.path.join(ROOT, cand)):
        return SITE_URL + "/" + cand
    return SITE_URL + "/assets/og/default.png"


def _schema_graph(page_path, title, desc, article, crumbs, faqs):
    canonical = SITE_URL + url_of(page_path)
    org_id, site_id = SITE_URL + "/#organization", SITE_URL + "/#website"

    org = {
        "@type": "Organization",
        "@id": org_id,
        "name": ORG["name"],
        "alternateName": ORG["alt"],
        "url": SITE_URL + "/",
        "email": ORG["email"],
        "telephone": ORG["phone"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": ORG["street"],
            "addressLocality": ORG["locality"],
            "addressRegion": ORG["region"],
            "addressCountry": ORG["country"],
        },
    }
    website = {
        "@type": "WebSite",
        "@id": site_id,
        "url": SITE_URL + "/",
        "name": "Expectant",
        "description": "임신 확인부터 주차별 증상, 출산 준비까지 안내하는 임신·출산 정보 가이드",
        "inLanguage": "ko-KR",
        "publisher": {"@id": org_id},
        "potentialAction": {
            "@type": "SearchAction",
            "target": {"@type": "EntryPoint", "urlTemplate": SITE_URL + "/?s={search_term_string}"},
            "query-input": "required name=search_term_string",
        },
    }
    graph = [org, website]

    page = {
        "@type": "Article" if article else "WebPage",
        "@id": canonical + "#page",
        "url": canonical,
        "name": title,
        "description": desc,
        "inLanguage": "ko-KR",
        "isPartOf": {"@id": site_id},
        "primaryImageOfPage": og_image_for(page_path),
    }
    if article:
        page.update({
            "headline": title.split(" | ")[0],
            "image": og_image_for(page_path),
            "datePublished": TODAY,
            "dateModified": TODAY,
            "author": {"@id": org_id},
            "publisher": {"@id": org_id},
        })
    graph.append(page)

    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "홈", "item": SITE_URL + "/"}]
        for i, (label, p) in enumerate(crumbs, start=2):
            it = {"@type": "ListItem", "position": i, "name": label}
            if p:
                it["item"] = SITE_URL + url_of(p)
            items.append(it)
        graph.append({"@type": "BreadcrumbList", "@id": canonical + "#breadcrumb", "itemListElement": items})

    if faqs:
        graph.append({
            "@type": "FAQPage",
            "@id": canonical + "#faq",
            "mainEntity": [
                {"@type": "Question", "name": strip_tags(q),
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                for q, a in faqs
            ],
        })

    return {"@context": "https://schema.org", "@graph": graph}


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


# ---------------------------------------------------------------- layout
def layout(page_path, title, desc, body, keywords="", article=False, og_type="website"):
    r = rel(page_path)
    canonical = SITE_URL + url_of(page_path)

    faqs = list(_FAQ_BUF); _FAQ_BUF.clear()
    crumbs = list(_CRUMB_BUF[-1]) if _CRUMB_BUF else []
    _CRUMB_BUF.clear()
    schema = _schema_graph(page_path, title, desc, article, crumbs, faqs)

    verify_tags = "".join(
        '\n<meta name="%s" content="%s">' % (n, v) for n, v in (
            ("google-site-verification", VERIFY["google"]),
            ("naver-site-verification", VERIFY["naver"]),
            ("msvalidate.01", VERIFY["bing"]),
        ) if v
    )
    og_img = og_image_for(page_path)
    og_extra = (
        '<meta property="og:image" content="{img}">\n'
        '<meta property="og:image:width" content="1200">\n'
        '<meta property="og:image:height" content="630">\n'
        '<meta property="og:image:alt" content="{alt}">\n'
        '<meta name="twitter:image" content="{img}">'
    ).format(img=og_img, alt=title.split(" | ")[0].replace('"', "&quot;"))
    if article:
        og_extra += ('\n<meta property="article:published_time" content="%sT00:00:00+09:00">'
                     '\n<meta property="article:modified_time" content="%sT00:00:00+09:00">' % (TODAY, TODAY))

    return """<!DOCTYPE html>
<html lang="ko" data-base="">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{kw}
<link rel="canonical" href="{canonical}">{verify}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Expectant">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="ko_KR">
{og_extra}
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FFFCFA">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='11' fill='%23D4808B'/%3E%3Cpath d='M23.6 11.4a4.4 4.4 0 0 0-6.2 0L16 12.8l-1.4-1.4a4.4 4.4 0 1 0-6.2 6.2L16 25l7.6-7.4a4.4 4.4 0 0 0 0-6.2z' fill='%23fff'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap">
<link rel="stylesheet" href="{r}assets/css/style.css">
<script type="application/ld+json">{schema}</script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VVCGWT08P0"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-VVCGWT08P0');
</script>
</head>
<body>
<a class="sr-only" href="#main">본문 바로가기</a>
{progress}
<header class="header">
  <div class="wrap header__inner">
    <a class="logo" href="{home}">
      <span class="logo__mark">{mark}</span>
      <span class="logo__text">expect<em>ant</em></span>
    </a>
    <nav class="nav" aria-label="주 메뉴">{nav}</nav>
    <div class="header__actions">
      <button class="icon-btn" data-search-open aria-label="검색 열기">{search}</button>
      <button class="icon-btn burger" data-drawer-open aria-label="메뉴 열기">{menu}</button>
    </div>
  </div>
</header>

<div class="drawer" role="dialog" aria-modal="true" aria-label="모바일 메뉴">
  <div class="drawer__scrim"></div>
  <div class="drawer__panel">
    <div class="drawer__head">
      <a class="logo" href="{home}"><span class="logo__mark">{mark}</span><span class="logo__text">expect<em>ant</em></span></a>
      <button class="icon-btn" data-drawer-close aria-label="메뉴 닫기">{close}</button>
    </div>
    {drawer}
  </div>
</div>

<div class="search" role="dialog" aria-modal="true" aria-label="사이트 검색">
  <div class="search__scrim"></div>
  <div class="search__box">
    <div class="search__field">
      {search}
      <input type="search" placeholder="임테기, 초기 증상, 예정일…" aria-label="검색어" autocomplete="off">
      <span class="search__kbd">ESC</span>
    </div>
    <div class="search__results"></div>
  </div>
</div>

{ad_top}
{ad_side}

<main id="main">
{body}
</main>

{footer}
<script src="{r}assets/js/search-index.js" defer></script>
<script src="{r}assets/js/site.js" defer></script>
{ad_script}
</body>
</html>
""".format(
        ad_top=AD_TOP, ad_side=AD_SIDE, ad_script=AD_SCRIPT,
        r=r, title=title, desc=desc, verify=verify_tags, og_extra=og_extra,
        kw=('<meta name="keywords" content="%s">' % keywords) if keywords else "",
        canonical=canonical, og_type=og_type,
        schema=json.dumps(schema, ensure_ascii=False),
        progress='<div class="progress" aria-hidden="true"></div>' if article else "",
        home="/", mark=I["heart"], nav=nav_html(page_path),
        search=I["search"], menu=I["menu"], close=I["close"],
        drawer=drawer_html(page_path), body=body, footer=footer_html(page_path),
    )

# ---------------------------------------------------------------- components
def breadcrumb(page_path, trail):
    """trail: list of (label, path|None)"""
    _CRUMB_BUF.append(list(trail))
    parts = ['<a href="%s">홈</a>' % link("index.html", page_path)]
    for label, p in trail:
        parts.append(I["caret"])
        parts.append('<a href="%s">%s</a>' % (link(p, page_path), label) if p else "<span>%s</span>" % label)
    return '<nav class="breadcrumb" aria-label="현재 위치">%s</nav>' % "".join(parts)

def callout(kind, title, text):
    icon = {"tip": I["bulb"], "warn": I["warn"], "info": I["info"], "alert": I["heart"]}[kind]
    return ('<div class="callout callout--%s"><span class="callout__icon">%s</span>'
            '<div><b>%s</b><p>%s</p></div></div>' % (kind, icon, title, text))

def keypoints(items):
    lis = "".join("<li>%s</li>" % x for x in items)
    return ('<div class="keypoints"><b>%s 핵심 요약</b><ul>%s</ul></div>'
            % (I["spark"], lis))

def faq(items):
    _FAQ_BUF.extend(items)
    out = []
    for q, a in items:
        out.append(
            '<div class="faq__item"><button class="faq__q" aria-expanded="false">'
            '<span>%s</span>%s</button><div class="faq__a"><div><p>%s</p></div></div></div>'
            % (q, I["plus"], a)
        )
    return '<div class="faq">%s</div>' % "".join(out)

def table(headers, rows):
    th = "".join("<th>%s</th>" % h for h in headers)
    tr = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return ('<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            % (th, tr))

def steps(items):
    out = "".join('<div class="step"><div><b>%s</b><p>%s</p></div></div>' % (t, d) for t, d in items)
    return '<div class="steps">%s</div>' % out

def related(page_path, items):
    out = "".join('<a class="related__item" href="%s"><b>%s</b><span>%s</span></a>'
                  % (link(p, page_path), t, d) for t, d, p in items)
    return ('<div class="related"><h3>이어서 읽어보세요</h3><div class="related__grid">%s</div></div>' % out)

def pager(page_path, prev, nxt):
    out = []
    if prev:
        out.append('<a href="%s"><span>이전 글</span><b>%s</b></a>' % (link(prev[1], page_path), prev[0]))
    else:
        out.append("<span></span>")
    if nxt:
        out.append('<a class="next" href="%s"><span>다음 글</span><b>%s</b></a>' % (link(nxt[1], page_path), nxt[0]))
    return '<div class="pager">%s</div>' % "".join(out)

def article_page(path, title, h1, desc, keywords, trail, body, rel_items, prev=None, nxt=None, reading="6"):
    inner = """
<div class="wrap article-layout">
  <article>
    {crumb}
    <header class="article__head">
      <span class="eyebrow">{cat}</span>
      <h1>{h1}</h1>
      <p class="article__desc">{desc}</p>
      <div class="article__meta">
        <span>{ic}약 {reading}분 읽기</span>
        <span>{icc}{today} 업데이트</span>
      </div>
    </header>
    <div class="prose">
      {body}
    </div>
    {disc}
    {rel}
    {pg}
  </article>
  <aside class="toc">
    <div class="toc__title">목차</div>
    <nav class="toc__list"></nav>
    <div class="toc__cta">
      <b>계산기로 확인하기</b>
      <p>예정일·임신 주수·검사 시기를 바로 계산해 보세요.</p>
      <a class="btn btn--primary btn--sm" href="{tools}">계산기 열기</a>
    </div>
  </aside>
</div>
""".format(
        crumb=breadcrumb(path, trail),
        cat=CATEGORY_LABEL.get(path.split("/")[0], "가이드"),
        h1=h1, desc=desc, ic=I["clock"], icc=I["calendar"], reading=reading, today=TODAY,
        body=body, disc=DISCLAIMER,
        rel=related(path, rel_items), pg=pager(path, prev, nxt),
        tools=link("tools/index.html", path),
    )
    html = layout(path, title, desc, inner, keywords, article=True, og_type="article")
    add(path, html, entry(path, h1, desc[:60], CATEGORY_LABEL.get(path.split("/")[0], "가이드"), keywords))
    return html

# ---------------------------------------------------------------- write
PAGES = {}          # path -> html
INDEX_ENTRIES = []  # for search

def add(path, html, idx=None):
    PAGES[path] = html
    if idx:
        INDEX_ENTRIES.append(idx)

def entry(path, title, desc, cat, kw=""):
    return {"u": url_of(path), "t": title, "d": desc, "c": cat, "k": kw}

if __name__ == "__main__":
    import content_pages
    content_pages.build(globals())

    # search index
    js = "window.SITE_INDEX = %s;" % json.dumps(INDEX_ENTRIES, ensure_ascii=False)
    with open(os.path.join(ROOT, "assets/js/search-index.js"), "w", encoding="utf-8") as f:
        f.write(js)

    # sitemap + robots
    urls = "".join(
        "<url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>weekly</changefreq>"
        "<priority>%s</priority></url>"
        % (SITE_URL, url_of(p), TODAY, "1.0" if p == "index.html" else "0.8")
        for p in sorted(PAGES) if p != "404.html"
    )
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>' % urls)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(
            "User-agent: *\n"
            "Allow: /\n\n"
            "# 네이버\n"
            "User-agent: Yeti\n"
            "Allow: /\n\n"
            "# 다음(카카오)\n"
            "User-agent: Daum\n"
            "Allow: /\n\n"
            "User-agent: Daumoa\n"
            "Allow: /\n\n"
            "# 구글\n"
            "User-agent: Googlebot\n"
            "Allow: /\n\n"
            "User-agent: Googlebot-Image\n"
            "Allow: /\n\n"
            "# 빙\n"
            "User-agent: Bingbot\n"
            "Allow: /\n\n"
            "Sitemap: %s/sitemap.xml\n" % SITE_URL
        )

    for path, html in PAGES.items():
        full = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(html)
    print("✓ %d pages, %d index entries" % (len(PAGES), len(INDEX_ENTRIES)))
