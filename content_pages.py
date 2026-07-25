#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""홈 · 허브 · 계산기 · 가이드 페이지"""


def build(G):
    layout      = G["layout"];      add    = G["add"];       entry   = G["entry"]
    I           = G["I"];           link   = G["link"];      callout = G["callout"]
    breadcrumb  = G["breadcrumb"];  table  = G["table"];     faq     = G["faq"]
    TODAY       = G["TODAY"]

    # =================================================================== HOME
    home_cards = [
        ("i-rose", I["test"], "임신 확인 방법", "임신 테스트기부터 피검사, 초음파까지. 언제·어떻게 확인해야 정확한지 단계별로 정리했어요.",
         [("임테기 사용시기", "pregnancy-test/when-to-test.html"),
          ("얼리 임테기", "pregnancy-test/early-test.html"),
          ("두 줄 판독", "pregnancy-test/two-lines.html"),
          ("임테기 오류", "pregnancy-test/errors.html")],
         "pregnancy-test/index.html"),
        ("i-sage", I["calendar"], "주차별 증상", "극초기부터 막달까지, 시기마다 몸에 나타나는 변화와 그 이유를 주차별로 안내합니다.",
         [("극초기 증상", "symptoms/very-early.html"),
          ("초기 증상", "symptoms/first-trimester.html"),
          ("중기 증상", "symptoms/second-trimester.html"),
          ("막달 증상", "symptoms/third-trimester.html")],
         "symptoms/index.html"),
        ("i-lav", I["calc"], "임신 계산기", "출산 예정일, 오늘의 임신 주수, 임테기 검사 시기를 날짜만 넣으면 바로 계산해 드려요.",
         [("출산 예정일", "tools/due-date.html"),
          ("임신 주수", "tools/pregnancy-week.html"),
          ("검사 시기", "tools/test-timing.html")],
         "tools/index.html"),
        ("i-sky", I["stetho"], "병원 검사 이해하기", "피검사 hCG 수치는 무엇을 뜻하는지, 초음파에서 아기집은 언제 보이는지 알려드려요.",
         [("hCG 수치표", "pregnancy-test/blood-test.html"),
          ("초음파 일정", "pregnancy-test/ultrasound.html")],
         "pregnancy-test/blood-test.html"),
        ("i-cream", I["leaf"], "임신 준비 · 건강", "엽산, 배란일, 임신 중 먹어도 되는 것들. 몸을 준비하는 시기부터 챙겨야 할 것들.",
         [("임신 준비", "guide/preparation.html"), ("임신 중 건강", "guide/health.html")],
         "guide/index.html"),
        ("i-rose", I["bag"], "출산 · 산후", "출산 신호를 알아채는 법부터 산후조리와 회복까지, 마지막 준비를 함께 합니다.",
         [("출산 준비", "guide/birth.html"), ("산후 회복", "guide/postpartum.html")],
         "guide/index.html"),
    ]

    cards_html = "".join(
        '<a class="card reveal" href="{href}">'
        '<span class="card__icon {ic}">{svg}</span>'
        '<h3>{t}</h3><p>{d}</p>'
        '<div class="card__links">{chips}</div>'
        '<span class="card__more">전체 보기 {arrow}</span></a>'.format(
            href=link(hub, "index.html"), ic=ic, svg=svg, t=t, d=d,
            chips="".join('<span class="chip">%s</span>' % c[0] for c in chips),
            arrow=I["arrow"])
        for ic, svg, t, d, chips, hub in home_cards
    )

    quick_links = [
        ("임테기 두 줄이 희미해요", "pregnancy-test/two-lines.html"),
        ("임테기 언제부터 가능한가요", "pregnancy-test/when-to-test.html"),
        ("임신 극초기 증상", "symptoms/very-early.html"),
        ("증발선 구별하는 법", "pregnancy-test/errors.html"),
        ("hCG 수치가 낮대요", "pregnancy-test/blood-test.html"),
        ("태동은 언제부터?", "symptoms/second-trimester.html"),
    ]

    timeline_data = [
        ("극초기", "0~4주", "아직 증상이 거의 없는 시기",
         "수정란이 나팔관을 따라 이동해 자궁내막에 착상합니다. 착상은 배란 후 6~12일 사이에 일어나고, 이때부터 hCG가 만들어지기 시작해요.",
         "양귀비씨 크기 (약 0.1~1mm)",
         ["대부분 아무 증상이 없어요", "착상혈 — 수정 후 10~14일경 아주 소량의 분홍·갈색 출혈", "가벼운 하복부 콕콕거림",
          "기초체온이 고온기로 유지됨", "평소보다 심한 피로감"],
         "symptoms/very-early.html"),
        ("초기", "5~13주", "입덧과 피로가 가장 심한 시기",
         "아기의 주요 장기가 만들어지는 가장 중요한 시기입니다. hCG가 급격히 상승하면서 몸의 변화도 가장 크게 느껴져요.",
         "블루베리 → 자두 (약 1cm → 7cm)",
         ["입덧 — 보통 임신 5~6주경 시작해 8~11주에 정점", "가슴이 커지고 아프며 유륜이 짙어짐", "잦은 소변",
          "극심한 졸음과 피로", "냄새에 예민해지고 음식 취향이 바뀜", "감정 기복"],
         "symptoms/first-trimester.html"),
        ("중기", "14~27주", "가장 편안한 '황금기'",
         "입덧이 가라앉고 컨디션이 회복됩니다. 배가 눈에 띄게 나오기 시작하고, 처음으로 태동을 느끼는 시기예요.",
         "레몬 → 배추 (약 10cm → 36cm)",
         ["태동 — 초산은 18~20주, 경산은 16~18주경부터", "배가 나오면서 옆구리가 당기는 원인대 통증", "식욕 회복",
          "다리 쥐·부종", "코막힘·잇몸 출혈", "정밀 초음파와 임신성 당뇨 검사 시기"],
         "symptoms/second-trimester.html"),
        ("막달", "28~40주", "출산을 준비하는 마지막 구간",
         "아기가 빠르게 자라며 몸이 무거워집니다. 가진통이 시작되고, 출산 신호를 구분하는 법을 알아둬야 할 때예요.",
         "가지 → 수박 (약 38cm → 50cm)",
         ["브랙스턴 힉스(가진통) — 불규칙하고 자세를 바꾸면 사라짐", "허리·골반 통증과 치골통", "속쓰림과 숨참",
          "손발 부종", "잦은 밤 소변과 불면", "이슬·양막파수 등 출산 임박 신호"],
         "symptoms/third-trimester.html"),
    ]

    tabs = "".join(
        '<button class="timeline__tab%s" role="tab" aria-selected="%s">%s<br><span style="font-size:.76rem;opacity:.8">%s</span></button>'
        % (" is-active" if i == 0 else "", "true" if i == 0 else "false", t[0], t[1])
        for i, t in enumerate(timeline_data)
    )
    panels = "".join(
        '<div class="timeline__panel%s" role="tabpanel">'
        '<div class="tl-card"><div class="tl-card__aside">'
        '<div class="tl-card__week">%s</div><div class="tl-card__sub">%s</div>'
        '<div class="tl-card__size"><b>아기 크기</b><span>%s</span></div>'
        '<a class="btn btn--ghost btn--sm" style="margin-top:18px" href="%s">자세히 보기</a>'
        '</div><div><h4>%s</h4><p style="margin-top:8px;font-size:.93rem;color:var(--text-muted)">%s</p>'
        '<ul class="tl-list">%s</ul></div></div></div>'
        % (" is-active" if i == 0 else "", t[1], t[0] + " · " + t[2], t[4],
           link(t[6], "index.html"), t[2], t[3],
           "".join("<li>%s</li>" % s for s in t[5]))
        for i, t in enumerate(timeline_data)
    )

    home_body = """
<section class="hero">
  <div class="hero__bg" aria-hidden="true">
    <span class="blob blob--1"></span><span class="blob blob--2"></span><span class="blob blob--3"></span>
  </div>
  <div class="wrap hero__grid">
    <div>
      <span class="eyebrow">{spark} 임신 · 출산 정보 가이드</span>
      <h1>혹시… <em>임신일까요?</em><br>가장 먼저 확인해야 할 것들</h1>
      <p class="hero__lead">임신 테스트기를 언제 써야 하는지, 두 줄이 희미하면 어떤 의미인지,
        지금 내 몸의 변화가 정상인지. 근거 있는 정보로 차분하게 안내해 드릴게요.</p>
      <div class="hero__cta">
        <a class="btn btn--primary" href="{when}">임테기 사용시기 보기 {arrow}</a>
        <a class="btn btn--ghost" href="{tools}">{calc} 예정일 계산하기</a>
      </div>
      <div class="hero__stats">
        <div class="hero__stat"><b>99%</b><span>정확한 시기에 쓴 임테기</span></div>
        <div class="hero__stat"><b>10~14일</b><span>수정 후 착상까지</span></div>
        <div class="hero__stat"><b>40주</b><span>표준 임신 기간</span></div>
      </div>
    </div>

    <div class="hero__card">
      <h3>{calc} 출산 예정일 빠른 계산</h3>
      <p class="hint">마지막 생리 시작일만 넣으면 예정일과 현재 주수를 함께 알려드려요.</p>
      <form data-calc="due" novalidate>
        <div class="field">
          <label for="h-lmp">마지막 생리 시작일</label>
          <input type="date" id="h-lmp" name="lmp" required>
        </div>
        <div class="field">
          <label for="h-cycle">평균 생리 주기</label>
          <select id="h-cycle" name="cycle">
            {cycles}
          </select>
        </div>
        <button class="btn btn--primary" type="submit" style="width:100%;margin-top:20px">계산하기</button>
        <div class="result" data-out hidden></div>
      </form>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head section-head--center">
      <span class="eyebrow">Categories</span>
      <h2>무엇이 궁금하신가요?</h2>
      <p>임신 확인부터 주차별 변화, 출산 준비까지. 필요한 주제를 골라 들어가 보세요.</p>
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="section" id="timeline">
  <div class="wrap">
    <div class="section-head section-head--center">
      <span class="eyebrow">Week by Week</span>
      <h2>주차별로 내 몸에 일어나는 일</h2>
      <p>지금 시기를 눌러보세요. 그때 몸에서 무슨 일이 일어나는지 한눈에 정리했어요.</p>
    </div>
    <div class="timeline">
      <div class="timeline__track" role="tablist" aria-label="임신 시기">{tabs}</div>
      <div class="timeline__panels">{panels}</div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="section-head section-head--center">
      <span class="eyebrow">Popular</span>
      <h2>이런 질문을 가장 많이 하세요</h2>
    </div>
    <div class="list-grid">{quick}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta-band">
      <span class="eyebrow">Tools</span>
      <h2 style="margin-top:16px">날짜만 넣으면 계산이 끝나요</h2>
      <p>출산 예정일, 오늘 기준 임신 주수, 임테기를 언제 써야 가장 정확한지까지
         세 가지 계산기를 무료로 제공합니다.</p>
      <a class="btn btn--primary" href="{tools}">계산기 사용하기 {arrow}</a>
    </div>
  </div>
</section>
""".format(
        spark=I["spark"], arrow=I["arrow"], calc=I["calc"],
        when=link("pregnancy-test/when-to-test.html", "index.html"),
        tools=link("tools/index.html", "index.html"),
        cycles="".join('<option value="%d"%s>%d일</option>' % (c, ' selected' if c == 28 else '', c)
                       for c in range(21, 41)),
        cards=cards_html, tabs=tabs, panels=panels,
        quick="".join(
            '<a class="list-item reveal" href="%s"><span class="list-item__no">%02d</span>'
            '<div><b>%s</b><p>바로 답 보러가기</p></div></a>'
            % (link(p, "index.html"), i + 1, t) for i, (t, p) in enumerate(quick_links)),
    )

    add("index.html",
        layout("index.html",
               "Expectant — 임신 테스트기부터 주차별 증상까지, 임신·출산 정보 가이드",
               "임테기 사용시기와 두 줄 판독, 임신 극초기·초기·중기·막달 증상, 출산 예정일 계산기까지. "
               "임신을 확인하고 준비하는 모든 과정을 근거 있는 정보로 안내합니다.",
               home_body,
               "임신테스트기,임테기,임테기 사용시기,얼리임테기,임신 초기증상,임신 극초기 증상,출산예정일 계산기,임신주수 계산기"),
        entry("index.html", "Expectant 홈", "임신·출산 정보 가이드", "홈", "임신 출산 임테기"))

    # =================================================================== HUB : pregnancy-test
    pt_items = [
        ("임테기 사용시기", "언제 검사해야 가장 정확할까요? hCG 상승 곡선과 정확도를 기준으로 알려드려요.", "pregnancy-test/when-to-test.html"),
        ("얼리 임테기", "생리 예정일 전에 쓰는 고민감도 테스트기, 언제부터 얼마나 믿을 수 있을까요.", "pregnancy-test/early-test.html"),
        ("임테기 사용법", "가장 정확한 결과를 얻는 5단계와 흔히 하는 실수 7가지를 정리했어요.", "pregnancy-test/how-to-use.html"),
        ("임테기 두 줄 판독", "진한 두 줄, 희미한 두 줄, 한 줄. 각각 무슨 의미이고 다음에 뭘 해야 하는지.", "pregnancy-test/two-lines.html"),
        ("임테기 오류 · 증발선", "위양성과 위음성이 생기는 이유, 증발선을 진짜 양성과 구별하는 법.", "pregnancy-test/errors.html"),
        ("임테기 역전", "검사선이 대조선보다 진해지는 '역전'은 언제 일어나고 무엇을 뜻할까요.", "pregnancy-test/reversal.html"),
        ("피검사 (hCG 수치)", "정성·정량 검사의 차이와 주차별 hCG 수치표, 수치가 낮거나 높을 때의 의미.", "pregnancy-test/blood-test.html"),
        ("초음파 검사", "아기집·난황·심장박동이 각각 언제 보이는지, 초음파 일정을 정리했어요.", "pregnancy-test/ultrasound.html"),
    ]

    pt_body = """
<section class="hub-hero">
  <div class="hero__bg" aria-hidden="true"><span class="blob blob--1"></span><span class="blob blob--3"></span></div>
  <div class="wrap">
    {crumb}
    <span class="eyebrow">{test} 임신 확인</span>
    <h1>임신, 어떻게 확인하나요?</h1>
    <p>임신 확인에는 세 가지 방법이 있습니다. 집에서 하는 <b>임신 테스트기(소변)</b>,
       병원에서 하는 <b>피검사(혈액 hCG)</b>, 그리고 <b>초음파</b>예요.
       각각 확인할 수 있는 시기와 알 수 있는 정보가 다릅니다.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="compare">
      <div class="compare__col">
        <span class="compare__badge" style="background:var(--rose-100);color:var(--rose-600)">가장 빠르고 간편</span>
        <h4>임신 테스트기</h4>
        <p style="font-size:.87rem;color:var(--text-muted);margin-top:6px">소변 속 hCG 감지</p>
        <ul>
          <li>생리 예정일 이후 검사 시 정확도 약 99%</li>
          <li>얼리 제품은 예정일 3~4일 전부터 가능</li>
          <li>임신 여부만 확인 (수치는 알 수 없음)</li>
        </ul>
      </div>
      <div class="compare__col">
        <span class="compare__badge" style="background:var(--sky-100);color:var(--sky-600)">가장 정확한 수치</span>
        <h4>피검사 (혈액)</h4>
        <p style="font-size:.87rem;color:var(--text-muted);margin-top:6px">혈중 hCG 정량 측정</p>
        <ul>
          <li>수정 후 7~10일부터 감지 가능</li>
          <li>정확한 수치(mIU/mL)를 알 수 있음</li>
          <li>48시간 간격 재검으로 경과 확인</li>
        </ul>
      </div>
      <div class="compare__col">
        <span class="compare__badge" style="background:var(--sage-100);color:var(--sage-600)">눈으로 확인</span>
        <h4>초음파</h4>
        <p style="font-size:.87rem;color:var(--text-muted);margin-top:6px">자궁 내 착상 확인</p>
        <ul>
          <li>아기집은 임신 4~5주경부터</li>
          <li>심장박동은 6~7주경 확인</li>
          <li>자궁외임신 여부를 판별할 수 있음</li>
        </ul>
      </div>
    </div>

    <div class="section-head" style="margin-top:64px">
      <h2>세부 주제 전체보기</h2>
      <p>궁금한 항목을 눌러 자세한 내용을 확인하세요.</p>
    </div>
    <div class="list-grid">{items}</div>
  </div>
</section>
""".format(
        crumb=breadcrumb("pregnancy-test/index.html", [("임신 확인", None)]),
        test=I["test"],
        items="".join(
            '<a class="list-item reveal" href="%s"><span class="list-item__no">%02d</span>'
            '<div><b>%s</b><p>%s</p></div></a>'
            % (link(p, "pregnancy-test/index.html"), i + 1, t, d)
            for i, (t, d, p) in enumerate(pt_items)),
    )

    add("pregnancy-test/index.html",
        layout("pregnancy-test/index.html",
               "임신 확인 방법 총정리 — 임테기 · 피검사 · 초음파 | Expectant",
               "임신을 확인하는 세 가지 방법인 임신 테스트기, 혈액 hCG 피검사, 초음파 검사의 "
               "가능 시기와 정확도를 비교하고 세부 주제를 안내합니다.",
               pt_body, "임신확인방법,임신테스트기,피검사,초음파,hCG"),
        entry("pregnancy-test/index.html", "임신 확인 방법", "임테기·피검사·초음파 비교", "임신 확인", "임신확인 방법"))

    # =================================================================== HUB : symptoms
    sym_items = [
        ("임신 극초기 증상", "0~4주. 아직 임테기도 반응하지 않는 시기에 나타나는 미세한 신호들.", "symptoms/very-early.html"),
        ("임신 초기 증상 (1~13주)", "입덧, 피로, 가슴 통증. 가장 변화가 큰 1분기를 주차별로 안내합니다.", "symptoms/first-trimester.html"),
        ("임신 중기 증상 (14~27주)", "태동이 시작되는 안정기. 몸이 편해지면서 새로 생기는 변화들.", "symptoms/second-trimester.html"),
        ("임신 막달 증상 (28~40주)", "가진통과 출산 신호. 언제 병원에 가야 하는지 구분하는 법.", "symptoms/third-trimester.html"),
    ]

    sym_body = """
<section class="hub-hero">
  <div class="hero__bg" aria-hidden="true"><span class="blob blob--2"></span><span class="blob blob--3"></span></div>
  <div class="wrap">
    {crumb}
    <span class="eyebrow">{cal} 주차별 증상</span>
    <h1>지금 내 몸에 일어나는 일</h1>
    <p>임신 주수는 <b>수정일이 아니라 마지막 생리 시작일</b>부터 셉니다.
       그래서 임신을 확인한 시점에 이미 임신 4~5주인 경우가 많아요.
       시기마다 몸이 어떻게 달라지는지, 그리고 그 변화가 왜 생기는지 정리했습니다.</p>
  </div>
</section>

<section class="section" id="timeline">
  <div class="wrap">
    <div class="timeline">
      <div class="timeline__track" role="tablist" aria-label="임신 시기">{tabs}</div>
      <div class="timeline__panels">{panels}</div>
    </div>

    <div class="section-head" style="margin-top:64px">
      <h2>시기별 상세 가이드</h2>
    </div>
    <div class="list-grid">{items}</div>

    <div style="margin-top:44px">{note}</div>
  </div>
</section>
""".format(
        crumb=breadcrumb("symptoms/index.html", [("주차별 증상", None)]),
        cal=I["calendar"],
        tabs="".join(
            '<button class="timeline__tab%s" role="tab" aria-selected="%s">%s<br>'
            '<span style="font-size:.76rem;opacity:.8">%s</span></button>'
            % (" is-active" if i == 0 else "", "true" if i == 0 else "false", t[0], t[1])
            for i, t in enumerate(timeline_data)),
        panels="".join(
            '<div class="timeline__panel%s" role="tabpanel">'
            '<div class="tl-card"><div class="tl-card__aside">'
            '<div class="tl-card__week">%s</div><div class="tl-card__sub">%s</div>'
            '<div class="tl-card__size"><b>아기 크기</b><span>%s</span></div>'
            '<a class="btn btn--ghost btn--sm" style="margin-top:18px" href="%s">자세히 보기</a>'
            '</div><div><h4>%s</h4><p style="margin-top:8px;font-size:.93rem;color:var(--text-muted)">%s</p>'
            '<ul class="tl-list">%s</ul></div></div></div>'
            % (" is-active" if i == 0 else "", t[1], t[0] + " · " + t[2], t[4],
               link(t[6], "symptoms/index.html"), t[2], t[3],
               "".join("<li>%s</li>" % s for s in t[5]))
            for i, t in enumerate(timeline_data)),
        items="".join(
            '<a class="list-item reveal" href="%s"><span class="list-item__no">%02d</span>'
            '<div><b>%s</b><p>%s</p></div></a>'
            % (link(p, "symptoms/index.html"), i + 1, t, d)
            for i, (t, d, p) in enumerate(sym_items)),
        note=callout("info", "증상은 사람마다 다릅니다",
                     "여기 정리된 증상이 전혀 없어도 정상적인 임신일 수 있고, 반대로 여러 증상이 있어도 임신이 아닐 수 있습니다. "
                     "증상만으로 임신을 판단하지 말고 반드시 임신 테스트기나 병원 검사로 확인하세요."),
    )

    add("symptoms/index.html",
        layout("symptoms/index.html",
               "임신 주차별 증상 총정리 — 극초기부터 막달까지 | Expectant",
               "임신 극초기·초기·중기·막달 증상을 주차별로 정리했습니다. 입덧 시작 시기, 태동 시기, "
               "가진통 구분법까지 시기마다 몸에 일어나는 변화를 안내합니다.",
               sym_body, "임신주차별증상,임신 극초기 증상,임신 초기 증상,임신 중기 증상,임신 막달 증상,태동시기,입덧시기"),
        entry("symptoms/index.html", "임신 주차별 증상", "극초기부터 막달까지 시기별 변화", "주차별 증상", "주차별 증상 타임라인"))

    # =================================================================== TOOLS
    cycles = "".join('<option value="%d"%s>%d일</option>' % (c, ' selected' if c == 28 else '', c)
                     for c in range(21, 41))

    def tool_page(path, h1, title, desc, kw, intro, form_html, guide_html):
        body = """
<section class="hub-hero">
  <div class="hero__bg" aria-hidden="true"><span class="blob blob--1"></span></div>
  <div class="wrap">
    {crumb}
    <span class="eyebrow">{calc} 계산기</span>
    <h1>{h1}</h1>
    <p>{intro}</p>
  </div>
</section>
<section class="section">
  <div class="wrap" style="max-width:900px">
    <div class="tool-card">{form}</div>
    <div class="prose" style="margin-top:52px">{guide}</div>
    {disc}
  </div>
</section>
""".format(crumb=breadcrumb(path, [("계산기", "tools/index.html"), (h1, None)]),
           calc=I["calc"], h1=h1, intro=intro, form=form_html, guide=guide_html,
           disc=G["DISCLAIMER"])
        add(path, layout(path, title, desc, body, kw, article=False),
            entry(path, h1, desc[:52], "계산기", kw))

    # -- due date
    tool_page(
        "tools/due-date.html", "출산 예정일 계산기",
        "출산 예정일 계산기 — 마지막 생리일로 D-day 계산 | Expectant",
        "마지막 생리 시작일과 평균 생리 주기를 입력하면 출산 예정일, 오늘 기준 임신 주수, 추정 배란일을 한 번에 계산해 드립니다.",
        "출산예정일 계산기,분만예정일,네겔레 법칙,임신 D-day",
        "마지막 생리 시작일만 알면 됩니다. 생리 주기가 28일과 다르다면 함께 입력해 주세요. 더 정확하게 계산됩니다.",
        """
<form data-calc="due" novalidate>
  <div class="field">
    <label for="t-lmp">마지막 생리 시작일</label>
    <input type="date" id="t-lmp" name="lmp" required>
  </div>
  <div class="field">
    <label for="t-cycle">평균 생리 주기 (기본 28일)</label>
    <select id="t-cycle" name="cycle">%s</select>
  </div>
  <button class="btn btn--primary" type="submit" style="width:100%%;margin-top:22px">예정일 계산하기</button>
  <div class="result" data-out hidden></div>
</form>
""" % cycles,
        """
<h2>어떤 방식으로 계산하나요?</h2>
<p>산부인과에서 표준으로 사용하는 <b>네겔레 법칙(Naegele's rule)</b>을 따릅니다.
마지막 생리 시작일(LMP)에 <b>280일(40주)</b>을 더한 날이 출산 예정일이에요.
생리 주기가 28일이 아닌 경우 배란일이 앞뒤로 밀리므로, 주기 길이에서 28을 뺀 만큼 예정일을 보정합니다.</p>
""" + table(["구분", "기준", "설명"], [
            ["임신 주수 시작점", "마지막 생리 시작일", "실제 수정보다 약 2주 이릅니다"],
            ["추정 배란·수정일", "LMP + 14일 (주기 보정)", "이 시점이 실제 임신 시작"],
            ["출산 예정일", "LMP + 280일", "40주 0일에 해당"],
            ["정상 만삭 범위", "37주 0일 ~ 41주 6일", "예정일에 정확히 낳는 경우는 약 5%"],
        ]) + """
<h2>예정일은 바뀔 수 있어요</h2>
<p>초음파로 아기의 크기(임신 초기에는 머리엉덩길이, CRL)를 측정하면 실제 임신 주수를 더 정확히 알 수 있습니다.
특히 <b>임신 8~13주 사이의 초음파</b>는 오차가 가장 작아, 이 시기 측정값과 LMP 기준 계산이 크게 다르면
병원에서 예정일을 조정합니다. 계산기 결과는 참고용으로 봐주세요.</p>
""" + callout("info", "예정일에 딱 맞춰 태어나는 아기는 드뭅니다",
              "출산의 대부분은 예정일 전후 2주 안에 이루어집니다. 예정일은 '이날 태어난다'가 아니라 "
              "'이 무렵이 만삭'이라는 기준점으로 이해하시면 좋아요.")
        + """<h2>자주 묻는 질문</h2>""" + faq([
            ("생리 주기가 불규칙한데 계산이 맞나요?",
             "주기가 불규칙하면 배란일 추정이 어려워 오차가 커집니다. 이 경우 초음파 측정으로 예정일을 정하는 것이 훨씬 정확합니다. 계산 결과는 대략적인 참고로만 활용해 주세요."),
            ("시험관·인공수정으로 임신했어요.",
             "보조생식술은 배아 이식일과 배아의 배양 일수를 기준으로 계산하므로 LMP 방식과 다릅니다. 시술받은 병원에서 안내한 예정일을 따라주세요."),
            ("쌍둥이도 예정일이 같나요?",
             "계산 방식은 같지만, 다태 임신은 평균적으로 더 이른 시기에 출산합니다. 쌍태아는 보통 임신 36~37주 무렵을 만삭으로 봅니다."),
        ]))

    # -- week
    tool_page(
        "tools/pregnancy-week.html", "임신 주수 계산기",
        "임신 주수 계산기 — 오늘 몇 주 몇 일인지 바로 확인 | Expectant",
        "마지막 생리일, 배란일, 출산 예정일 중 아는 날짜 하나만 입력하면 오늘 기준 임신 주수와 개월 수, 분기를 계산해 드립니다.",
        "임신주수 계산기,임신 몇주,임신 개월수,임신 분기",
        "마지막 생리일·배란일·출산 예정일 중 아는 것 하나만 있으면 됩니다.",
        """
<form data-calc="week" novalidate>
  <div class="field">
    <label for="w-mode">입력할 기준 날짜</label>
    <select id="w-mode" name="mode">
      <option value="lmp">마지막 생리 시작일</option>
      <option value="conception">배란일 / 수정일</option>
      <option value="edd">출산 예정일</option>
    </select>
  </div>
  <div class="field">
    <label for="w-date">날짜</label>
    <input type="date" id="w-date" name="date" required>
  </div>
  <button class="btn btn--primary" type="submit" style="width:100%;margin-top:22px">주수 계산하기</button>
  <div class="result" data-out hidden></div>
</form>
""",
        """
<h2>임신 주수를 세는 방법</h2>
<p>임신 주수는 <b>마지막 생리 시작일(LMP)</b>을 0주 0일로 잡고 셉니다.
실제 수정은 그보다 약 2주 뒤에 일어나기 때문에, 임신을 확인했을 때 이미 4~5주인 경우가 흔해요.
'임신 6주'라고 하면 수정 후로는 약 4주가 지난 상태입니다.</p>
""" + table(["분기", "주수", "특징"], [
            ["1분기 (초기)", "0주 ~ 13주 6일", "장기 형성기, 입덧과 피로가 가장 심함"],
            ["2분기 (중기)", "14주 0일 ~ 27주 6일", "안정기, 태동 시작, 정밀 초음파"],
            ["3분기 (후기·막달)", "28주 0일 ~ 출산", "급성장기, 가진통과 출산 준비"],
        ]) + """
<h3>주수와 개월 수는 왜 다를까요?</h3>
<p>임신에서 말하는 '개월'은 4주를 한 달로 셉니다. 그래서 임신 40주는 10개월이 되죠.
달력상의 달(28~31일)과는 계산이 조금 달라서, 임신 8개월이라고 하면 달력으로는 약 7개월이 지난 시점입니다.
병원에서는 오해를 줄이기 위해 대부분 <b>주수로만</b> 이야기합니다.</p>
""" + callout("tip", "병원에서는 주수로 말해주세요",
              "'임신 몇 개월이에요?'보다 '임신 몇 주 며칠이에요'가 훨씬 정확한 소통입니다. "
              "검사 시기와 태아 발달 기준이 모두 주 단위로 정해져 있기 때문이에요."))

    # -- test timing
    tool_page(
        "tools/test-timing.html", "임테기 검사시기 계산기",
        "임신 테스트기 검사시기 계산기 — 언제 하면 정확할까 | Expectant",
        "마지막 생리 시작일과 주기를 입력하면 얼리 임테기 가능일, 가장 정확한 검사일, 음성일 때 재검사할 날짜를 계산해 드립니다.",
        "임테기 사용시기 계산기,얼리임테기 시기,임신테스트 시기",
        "너무 일찍 검사하면 임신이어도 한 줄이 나옵니다. 언제 검사해야 가장 믿을 수 있는지 계산해 드릴게요.",
        """
<form data-calc="test" novalidate>
  <div class="field">
    <label for="c-lmp">마지막 생리 시작일</label>
    <input type="date" id="c-lmp" name="lmp" required>
  </div>
  <div class="field">
    <label for="c-cycle">평균 생리 주기</label>
    <select id="c-cycle" name="cycle">%s</select>
  </div>
  <button class="btn btn--primary" type="submit" style="width:100%%;margin-top:22px">검사 시기 계산하기</button>
  <div class="result" data-out hidden></div>
</form>
""" % cycles,
        """
<h2>왜 '생리 예정일 다음날'인가요?</h2>
<p>임신 테스트기는 소변 속 <b>hCG(융모성 성선자극호르몬)</b>를 감지합니다.
hCG는 수정란이 자궁내막에 착상한 뒤부터 만들어지기 시작하는데,
착상은 보통 <b>배란 후 6~12일</b> 사이에 일어나요.</p>
<p>착상 직후의 hCG는 아주 미량이라 일반 임테기의 감지 기준(보통 20~25 mIU/mL)에 못 미칩니다.
hCG는 초기에 약 <b>48~72시간마다 두 배</b>로 늘어나기 때문에, 며칠만 더 기다리면 감지 가능한 농도에 도달하죠.
생리 예정일이 지난 시점이면 대부분의 정상 임신에서 충분한 농도가 확보됩니다.</p>
""" + table(["시점", "검사 가능 여부", "참고"], [
            ["배란 후 8~9일", "대부분 음성", "착상 전이거나 hCG가 너무 낮음"],
            ["배란 후 10~12일", "얼리 제품만 일부 가능", "위음성이 흔합니다"],
            ["생리 예정일 당일", "일반 제품 가능", "약 90% 수준의 감지율"],
            ["생리 예정일 +1일 이후", "가장 권장", "정확도 약 99%"],
            ["음성인데 생리가 안 옴", "3일 후 재검사", "그래도 음성이면 병원 방문"],
        ]) + callout("tip", "아침 첫 소변으로 검사하세요",
                     "밤새 농축된 아침 첫 소변에 hCG 농도가 가장 높습니다. 특히 이른 시기에 검사한다면 "
                     "아침 첫 소변으로 하는 것이 위음성을 줄이는 가장 쉬운 방법이에요. "
                     "검사 전 물을 많이 마시면 소변이 희석되어 결과가 흐려질 수 있습니다."))

    # -- tools hub
    tools_body = """
<section class="hub-hero">
  <div class="hero__bg" aria-hidden="true"><span class="blob blob--1"></span><span class="blob blob--2"></span></div>
  <div class="wrap">
    {crumb}
    <span class="eyebrow">{calc} 계산기</span>
    <h1>날짜만 넣으면 계산이 끝나요</h1>
    <p>입력한 정보는 브라우저 안에서만 계산되고 어디에도 저장되거나 전송되지 않습니다.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="tool-grid">
      <div class="tool-card">
        <h3>{cal} 출산 예정일 계산기</h3>
        <p>마지막 생리 시작일로 예정일과 현재 주수를 함께 계산합니다.</p>
        <form data-calc="due" novalidate>
          <div class="field"><label>마지막 생리 시작일</label><input type="date" name="lmp" required></div>
          <div class="field"><label>평균 생리 주기</label><select name="cycle">{cycles}</select></div>
          <button class="btn btn--primary" type="submit" style="width:100%;margin-top:20px">계산하기</button>
          <div class="result" data-out hidden></div>
        </form>
        <a class="btn btn--ghost btn--sm" style="margin-top:16px" href="{p1}">자세한 설명 보기</a>
      </div>

      <div class="tool-card">
        <h3>{clock} 임신 주수 계산기</h3>
        <p>생리일·배란일·예정일 중 아는 날짜로 오늘의 주수를 확인하세요.</p>
        <form data-calc="week" novalidate>
          <div class="field"><label>기준 날짜 종류</label>
            <select name="mode">
              <option value="lmp">마지막 생리 시작일</option>
              <option value="conception">배란일 / 수정일</option>
              <option value="edd">출산 예정일</option>
            </select></div>
          <div class="field"><label>날짜</label><input type="date" name="date" required></div>
          <button class="btn btn--primary" type="submit" style="width:100%;margin-top:20px">계산하기</button>
          <div class="result" data-out hidden></div>
        </form>
        <a class="btn btn--ghost btn--sm" style="margin-top:16px" href="{p2}">자세한 설명 보기</a>
      </div>

      <div class="tool-card">
        <h3>{test} 임테기 검사시기 계산기</h3>
        <p>언제 검사해야 위음성 없이 정확한 결과를 얻을 수 있는지 알려드려요.</p>
        <form data-calc="test" novalidate>
          <div class="field"><label>마지막 생리 시작일</label><input type="date" name="lmp" required></div>
          <div class="field"><label>평균 생리 주기</label><select name="cycle">{cycles}</select></div>
          <button class="btn btn--primary" type="submit" style="width:100%;margin-top:20px">계산하기</button>
          <div class="result" data-out hidden></div>
        </form>
        <a class="btn btn--ghost btn--sm" style="margin-top:16px" href="{p3}">자세한 설명 보기</a>
      </div>
    </div>
    {disc}
  </div>
</section>
""".format(crumb=breadcrumb("tools/index.html", [("계산기", None)]),
           calc=I["calc"], cal=I["calendar"], clock=I["clock"], test=I["test"], cycles=cycles,
           p1=link("tools/due-date.html", "tools/index.html"),
           p2=link("tools/pregnancy-week.html", "tools/index.html"),
           p3=link("tools/test-timing.html", "tools/index.html"),
           disc=G["DISCLAIMER"])

    add("tools/index.html",
        layout("tools/index.html",
               "임신 계산기 3종 — 출산예정일 · 임신주수 · 임테기 시기 | Expectant",
               "출산 예정일 계산기, 임신 주수 계산기, 임신 테스트기 검사시기 계산기를 한 곳에서. "
               "날짜만 입력하면 바로 결과를 확인할 수 있습니다.",
               tools_body, "임신 계산기,출산예정일 계산기,임신주수 계산기,임테기 시기 계산기"),
        entry("tools/index.html", "임신 계산기", "예정일·주수·검사시기 계산", "계산기", "계산기 도구"))

    # =================================================================== GUIDE (준비 중)
    guide_topics = [
        ("guide/preparation.html", "임신 준비", I["leaf"],
         "임신을 계획하는 시기에 알아두면 좋은 것들",
         ["배란일과 가임기 계산하기", "임신 전 엽산 복용 시기와 용량", "임신 전 검사 체크리스트",
          "생활 습관 정비 (카페인·음주·체중)", "남편이 함께 준비할 것"]),
        ("guide/health.html", "임신 중 건강", I["heart"],
         "임신 기간 동안 몸을 돌보는 방법",
         ["임신 중 먹어도 되는 음식과 피할 음식", "임신 중 복용 가능한 약", "적정 체중 증가 범위",
          "임신성 당뇨와 빈혈 관리", "임신 중 운동과 여행"]),
        ("guide/birth.html", "출산 준비", I["bag"],
         "출산이 가까워지면 준비해야 할 것들",
         ["출산 가방 체크리스트", "진통 신호 구분하기 (가진통 vs 진진통)", "자연분만과 제왕절개",
          "무통 분만 이해하기", "병원 가야 하는 시점"]),
        ("guide/postpartum.html", "산후 회복", I["moon"],
         "출산 후의 몸과 마음을 돌보는 시간",
         ["산후조리 기간과 주의사항", "오로와 자궁 회복 과정", "모유수유 시작하기",
          "산후 우울감 알아차리기", "산후 검진 일정"]),
    ]

    for path, name, icon, sub, topics in guide_topics:
        body = """
<section class="hub-hero">
  <div class="hero__bg" aria-hidden="true"><span class="blob blob--2"></span></div>
  <div class="wrap">
    {crumb}
    <span class="eyebrow">{icon} 가이드</span>
    <h1>{name}</h1>
    <p>{sub}</p>
  </div>
</section>
<section class="section">
  <div class="wrap" style="max-width:820px">
    {note}
    <div class="section-head" style="margin-top:44px"><h2>준비 중인 콘텐츠</h2></div>
    <div class="steps">{topics}</div>
    <div class="cta-band" style="margin-top:48px">
      <h2>먼저 확인할 수 있는 내용</h2>
      <p>임신 확인 방법과 주차별 증상은 이미 자세히 정리되어 있어요.</p>
      <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:24px">
        <a class="btn btn--primary" href="{pt}">임신 확인 방법</a>
        <a class="btn btn--ghost" href="{sy}">주차별 증상</a>
      </div>
    </div>
  </div>
</section>
""".format(crumb=breadcrumb(path, [("가이드", "guide/index.html"), (name, None)]),
           icon=icon, name=name, sub=sub,
           note=callout("info", "이 카테고리는 준비 중입니다",
                        "아래 주제들이 순차적으로 공개될 예정이에요. 먼저 필요한 주제가 있다면 우선순위를 조정할 수 있습니다."),
           topics="".join('<div class="step"><div><b>%s</b><p>공개 예정</p></div></div>' % t for t in topics),
           pt=link("pregnancy-test/index.html", path), sy=link("symptoms/index.html", path))
        add(path, layout(path, "%s | Expectant" % name, sub, body, name),
            entry(path, name, sub, "가이드", name))

    guide_body = """
<section class="hub-hero">
  <div class="hero__bg" aria-hidden="true"><span class="blob blob--1"></span></div>
  <div class="wrap">
    {crumb}
    <span class="eyebrow">{book} 가이드</span>
    <h1>임신 준비부터 산후까지</h1>
    <p>임신 확인과 주차별 증상 다음으로 다룰 주제들입니다. 순차적으로 공개될 예정이에요.</p>
  </div>
</section>
<section class="section">
  <div class="wrap"><div class="cards">{cards}</div></div>
</section>
""".format(crumb=breadcrumb("guide/index.html", [("가이드", None)]), book=I["book"],
           cards="".join(
               '<a class="card reveal" href="%s"><span class="card__icon %s">%s</span>'
               '<h3>%s</h3><p>%s</p><div class="card__links">%s</div>'
               '<span class="card__more">보러가기 %s</span></a>'
               % (link(p, "guide/index.html"), cls, ic, n, s,
                  "".join('<span class="chip">%s</span>' % t for t in tp[:2]), I["arrow"])
               for (p, n, ic, s, tp), cls in zip(guide_topics, ["i-sage", "i-rose", "i-cream", "i-lav"])))

    add("guide/index.html",
        layout("guide/index.html", "임신·출산 가이드 | Expectant",
               "임신 준비, 임신 중 건강, 출산 준비, 산후 회복. 임신의 전 과정을 다루는 가이드입니다.",
               guide_body, "임신 준비,임신 중 건강,출산 준비,산후조리"),
        entry("guide/index.html", "임신·출산 가이드", "준비·건강·출산·산후", "가이드", "가이드"))

    # =================================================================== 404
    body404 = """
<section class="section" style="padding-block:120px;text-align:center">
  <div class="wrap" style="max-width:560px">
    <span class="eyebrow">404</span>
    <h1 style="font-size:clamp(1.8rem,4vw,2.6rem);margin-top:18px">찾으시는 페이지가 없어요</h1>
    <p style="margin-top:16px;color:var(--text-muted)">주소가 바뀌었거나 삭제된 페이지일 수 있습니다.
       아래에서 원하는 곳으로 이동해 보세요.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:32px">
      <a class="btn btn--primary" href="/">홈으로</a>
      <a class="btn btn--ghost" href="/pregnancy-test/">임신 확인 방법</a>
      <a class="btn btn--ghost" href="/symptoms/">주차별 증상</a>
    </div>
  </div>
</section>
"""
    add("404.html", layout("404.html", "페이지를 찾을 수 없습니다 | Expectant",
                           "요청하신 페이지를 찾을 수 없습니다.", body404))

    import content_test, content_symptoms
    content_test.build(G)
    content_symptoms.build(G)
