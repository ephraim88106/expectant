/* Expectant — site interactions */
(function () {
  'use strict';

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Header shadow on scroll ---------- */
  var header = $('.header');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-stuck', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Mobile drawer ---------- */
  var drawer = $('.drawer');
  if (drawer) {
    var openDrawer = function () {
      drawer.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    };
    var closeDrawer = function () {
      drawer.classList.remove('is-open');
      document.body.style.overflow = '';
    };
    $$('[data-drawer-open]').forEach(function (b) { b.addEventListener('click', openDrawer); });
    $$('[data-drawer-close]').forEach(function (b) { b.addEventListener('click', closeDrawer); });
    $('.drawer__scrim') && $('.drawer__scrim').addEventListener('click', closeDrawer);
    $$('.drawer__toggle').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!open));
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) closeDrawer();
    });
  }

  /* ---------- Search ---------- */
  var search = $('.search');
  if (search && window.SITE_INDEX) {
    var input   = $('.search__field input', search);
    var results = $('.search__results', search);
    var idx     = window.SITE_INDEX;
    var base    = document.documentElement.getAttribute('data-base') || '';

    var openSearch = function () {
      search.classList.add('is-open');
      document.body.style.overflow = 'hidden';
      setTimeout(function () { input.focus(); }, 60);
      if (!input.value) render('');
    };
    var closeSearch = function () {
      search.classList.remove('is-open');
      document.body.style.overflow = '';
    };

    var esc = function (s) { return s.replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    }); };

    var highlight = function (text, q) {
      if (!q) return esc(text);
      var i = text.toLowerCase().indexOf(q.toLowerCase());
      if (i < 0) return esc(text);
      return esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + q.length)) + '</mark>' + esc(text.slice(i + q.length));
    };

    var render = function (q) {
      var list;
      if (!q.trim()) {
        list = idx.slice(0, 7);
      } else {
        var k = q.trim().toLowerCase();
        list = idx.map(function (it) {
          var score = 0;
          if (it.t.toLowerCase().indexOf(k) > -1) score += 10;
          if ((it.d || '').toLowerCase().indexOf(k) > -1) score += 4;
          if ((it.k || '').toLowerCase().indexOf(k) > -1) score += 6;
          return { it: it, s: score };
        }).filter(function (r) { return r.s > 0; })
          .sort(function (a, b) { return b.s - a.s; })
          .slice(0, 8)
          .map(function (r) { return r.it; });
      }
      if (!list.length) {
        results.innerHTML = '<div class="search__empty">검색 결과가 없어요.<br>다른 키워드로 찾아보세요.</div>';
        return;
      }
      results.innerHTML = list.map(function (it, i) {
        return '<a href="' + base + it.u + '"' + (i === 0 ? ' class="is-active"' : '') + '>' +
               '<strong>' + highlight(it.t, q.trim()) + '</strong>' +
               '<span>' + esc(it.c + ' · ' + (it.d || '')) + '</span></a>';
      }).join('');
    };

    input.addEventListener('input', function () { render(input.value); });

    input.addEventListener('keydown', function (e) {
      var items = $$('a', results);
      if (!items.length) return;
      var cur = items.findIndex(function (a) { return a.classList.contains('is-active'); });
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        if (cur > -1) items[cur].classList.remove('is-active');
        var next = e.key === 'ArrowDown'
          ? (cur + 1) % items.length
          : (cur - 1 + items.length) % items.length;
        items[next].classList.add('is-active');
        items[next].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'Enter') {
        e.preventDefault();
        var target = items[cur > -1 ? cur : 0];
        if (target) window.location.href = target.getAttribute('href');
      }
    });

    $$('[data-search-open]').forEach(function (b) { b.addEventListener('click', openSearch); });
    $('.search__scrim') && $('.search__scrim').addEventListener('click', closeSearch);

    /* /?s=키워드 로 들어오면 검색창을 열어준다 (schema.org SearchAction 대응) */
    try {
      var q0 = new URLSearchParams(window.location.search).get('s');
      if (q0) { input.value = q0; openSearch(); render(q0); }
    } catch (e) { /* noop */ }

    document.addEventListener('keydown', function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); openSearch(); }
      if (e.key === 'Escape' && search.classList.contains('is-open')) closeSearch();
      if (e.key === '/' && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) {
        e.preventDefault(); openSearch();
      }
    });
  }

  /* ---------- FAQ accordion ---------- */
  $$('.faq__q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
    });
  });

  /* ---------- Timeline tabs ---------- */
  $$('.timeline').forEach(function (tl) {
    var tabs   = $$('.timeline__tab', tl);
    var panels = $$('.timeline__panel', tl);
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () {
        tabs.forEach(function (t) { t.classList.remove('is-active'); t.setAttribute('aria-selected', 'false'); });
        panels.forEach(function (p) { p.classList.remove('is-active'); });
        tab.classList.add('is-active');
        tab.setAttribute('aria-selected', 'true');
        if (panels[i]) panels[i].classList.add('is-active');
      });
    });
  });

  /* ---------- Card spotlight ---------- */
  $$('.card').forEach(function (card) {
    card.addEventListener('pointermove', function (e) {
      var r = card.getBoundingClientRect();
      card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      card.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  /* ---------- Auto TOC + scroll spy ---------- */
  var tocList = $('.toc__list');
  var prose   = $('.prose');
  if (tocList && prose) {
    var heads = $$('h2, h3', prose).filter(function (h) { return !h.hasAttribute('data-no-toc'); });
    heads.forEach(function (h, i) {
      if (!h.id) h.id = 'sec-' + (i + 1);
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent.trim();
      a.setAttribute('data-depth', h.tagName === 'H3' ? '3' : '2');
      tocList.appendChild(a);
    });
    var links = $$('a', tocList);
    if ('IntersectionObserver' in window && heads.length) {
      var spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          links.forEach(function (l) {
            l.classList.toggle('is-active', l.getAttribute('href') === '#' + en.target.id);
          });
        });
      }, { rootMargin: '-90px 0px -70% 0px', threshold: 0 });
      heads.forEach(function (h) { spy.observe(h); });
    }
  }

  /* ---------- Reading progress ---------- */
  var bar = $('.progress');
  if (bar) {
    var tick = function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
    };
    tick();
    window.addEventListener('scroll', tick, { passive: true });
    window.addEventListener('resize', tick);
  }

  /* ---------- Reveal on scroll ---------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: .06 });
    $$('.reveal').forEach(function (el, i) {
      el.style.transitionDelay = Math.min(i % 4, 3) * 70 + 'ms';
      io.observe(el);
    });
  } else {
    $$('.reveal').forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ======================================================================
     Calculators
     ====================================================================== */
  var DAY = 86400000;
  var fmt = function (d) {
    return d.getFullYear() + '년 ' + (d.getMonth() + 1) + '월 ' + d.getDate() + '일 (' +
           '일월화수목금토'[d.getDay()] + ')';
  };
  var fmtShort = function (d) {
    return (d.getMonth() + 1) + '월 ' + d.getDate() + '일';
  };
  var today0 = function () {
    var t = new Date(); t.setHours(0, 0, 0, 0); return t;
  };
  var parseDate = function (v) {
    if (!v) return null;
    var p = v.split('-').map(Number);
    if (p.length !== 3 || !p[0]) return null;
    var d = new Date(p[0], p[1] - 1, p[2]);
    d.setHours(0, 0, 0, 0);
    return isNaN(d.getTime()) ? null : d;
  };

  /* Naegele: EDD = LMP + 280 days, adjusted for cycle length */
  function computeFromLMP(lmp, cycle) {
    var adj = (typeof cycle === 'number' && cycle >= 20 && cycle <= 45) ? (cycle - 28) : 0;
    var edd = new Date(lmp.getTime() + (280 + adj) * DAY);
    var conception = new Date(lmp.getTime() + (14 + adj) * DAY);
    return { edd: edd, conception: conception, start: lmp };
  }

  function gestation(startLMP, ref) {
    var days = Math.floor((ref - startLMP) / DAY);
    if (days < 0) days = 0;
    return { w: Math.floor(days / 7), d: days % 7, total: days };
  }

  function trimesterOf(w) {
    if (w < 14) return { n: '임신 초기 (1분기)', href: 'symptoms/first-trimester.html' };
    if (w < 28) return { n: '임신 중기 (2분기)', href: 'symptoms/second-trimester.html' };
    return { n: '임신 후기 (3분기)', href: 'symptoms/third-trimester.html' };
  }

  /* --- Due-date calculator --- */
  $$('[data-calc="due"]').forEach(function (form) {
    var out = $('[data-out]', form);
    var run = function (e) {
      e && e.preventDefault();
      var lmp = parseDate($('[name="lmp"]', form).value);
      var cycEl = $('[name="cycle"]', form);
      var cyc = cycEl ? parseInt(cycEl.value, 10) : 28;
      if (!lmp) { out.hidden = true; return; }
      var r = computeFromLMP(lmp, cyc);
      var g = gestation(lmp, today0());
      var tri = trimesterOf(g.w);
      var left = Math.max(0, Math.ceil((r.edd - today0()) / DAY));
      var pct  = Math.min(100, Math.max(0, (g.total / 280) * 100));

      out.hidden = false;
      out.innerHTML =
        '<div class="result__label">출산 예정일</div>' +
        '<div class="result__big">' + fmt(r.edd) + '</div>' +
        '<div class="bar" aria-hidden="true"><span style="width:' + pct.toFixed(1) + '%"></span></div>' +
        '<div class="result__meta">' +
          '<div><b>' + g.w + '주 ' + g.d + '일</b><span>오늘 기준 임신 주수</span></div>' +
          '<div><b>' + tri.n + '</b><span>현재 시기</span></div>' +
          '<div><b>D-' + left + '</b><span>예정일까지</span></div>' +
          '<div><b>' + fmtShort(r.conception) + '</b><span>추정 배란·수정일</span></div>' +
        '</div>' +
        '<p style="font-size:.8rem;color:var(--text-muted);margin-top:14px">' +
        '마지막 생리 시작일 기준 네겔레 법칙(280일)으로 계산했어요. 실제 예정일은 초음파 측정으로 조정될 수 있습니다.</p>';
    };
    form.addEventListener('submit', run);
    $$('input, select', form).forEach(function (i) { i.addEventListener('change', run); });
  });

  /* --- Pregnancy week calculator --- */
  $$('[data-calc="week"]').forEach(function (form) {
    var out = $('[data-out]', form);
    var run = function (e) {
      e && e.preventDefault();
      var mode = $('[name="mode"]', form) ? $('[name="mode"]', form).value : 'lmp';
      var dv = parseDate($('[name="date"]', form).value);
      if (!dv) { out.hidden = true; return; }
      var lmp;
      if (mode === 'lmp')        lmp = dv;
      else if (mode === 'conception') lmp = new Date(dv.getTime() - 14 * DAY);
      else                        lmp = new Date(dv.getTime() - 280 * DAY); // EDD given
      var g = gestation(lmp, today0());
      if (g.total > 320) { out.hidden = false; out.innerHTML = '<p style="color:var(--rose-700)">날짜를 다시 확인해 주세요. 계산된 주수가 범위를 벗어났어요.</p>'; return; }
      var tri = trimesterOf(g.w);
      var edd = new Date(lmp.getTime() + 280 * DAY);
      var pct = Math.min(100, (g.total / 280) * 100);
      var month = Math.floor(g.w / 4) + 1;

      out.hidden = false;
      out.innerHTML =
        '<div class="result__label">오늘 기준 임신 주수</div>' +
        '<div class="result__big">임신 ' + g.w + '주 ' + g.d + '일</div>' +
        '<div class="bar" aria-hidden="true"><span style="width:' + pct.toFixed(1) + '%"></span></div>' +
        '<div class="result__meta">' +
          '<div><b>' + tri.n + '</b><span>현재 시기</span></div>' +
          '<div><b>임신 ' + month + '개월</b><span>개월 수</span></div>' +
          '<div><b>' + fmtShort(edd) + '</b><span>출산 예정일</span></div>' +
          '<div><b>D-' + Math.max(0, Math.ceil((edd - today0()) / DAY)) + '</b><span>예정일까지</span></div>' +
        '</div>';
    };
    form.addEventListener('submit', run);
    $$('input, select', form).forEach(function (i) { i.addEventListener('change', run); });
  });

  /* --- Pregnancy-test timing calculator --- */
  $$('[data-calc="test"]').forEach(function (form) {
    var out = $('[data-out]', form);
    var run = function (e) {
      e && e.preventDefault();
      var lmp = parseDate($('[name="lmp"]', form).value);
      var cyc = parseInt($('[name="cycle"]', form).value, 10) || 28;
      if (!lmp) { out.hidden = true; return; }

      var ovul   = new Date(lmp.getTime() + (cyc - 14) * DAY);   // 황체기 14일 가정
      var nextP  = new Date(lmp.getTime() + cyc * DAY);          // 다음 생리 예정일
      var early  = new Date(ovul.getTime() + 10 * DAY);          // 얼리 임테기 (10 DPO)
      var best   = new Date(nextP.getTime() + 1 * DAY);          // 생리 예정일 다음날
      var retest = new Date(best.getTime() + 3 * DAY);           // 음성일 때 재검사

      var t = today0();
      var dLeft = Math.ceil((best - t) / DAY);
      var status = dLeft > 0
        ? '정확한 검사까지 <b style="color:var(--rose-600)">D-' + dLeft + '</b>'
        : '지금 검사해도 좋은 시기예요';

      out.hidden = false;
      out.innerHTML =
        '<div class="result__label">가장 정확한 검사 시점</div>' +
        '<div class="result__big">' + fmt(best) + '</div>' +
        '<p style="font-size:.87rem;color:var(--ink-700);margin-top:6px">' + status + '</p>' +
        '<div class="result__meta">' +
          '<div><b>' + fmtShort(ovul) + '</b><span>추정 배란일</span></div>' +
          '<div><b>' + fmtShort(early) + '</b><span>얼리 임테기 가능일<br>(배란 10일 후)</span></div>' +
          '<div><b>' + fmtShort(nextP) + '</b><span>다음 생리 예정일</span></div>' +
          '<div><b>' + fmtShort(retest) + '</b><span>음성 시 재검사일</span></div>' +
        '</div>' +
        '<p style="font-size:.8rem;color:var(--text-muted);margin-top:14px">' +
        '생리 주기가 규칙적이라는 가정하에 계산했어요. 주기가 불규칙하면 검사 시점이 며칠 늦어질 수 있습니다.</p>';
    };
    form.addEventListener('submit', run);
    $$('input, select', form).forEach(function (i) { i.addEventListener('change', run); });
  });

  /* ---------- 쿠팡 추천 상품 랜덤 노출 ----------
     페이지 주제에 맞는 후보군(window.COUPANG_POOL) 안에서 접속할 때마다 하나를 고른다.
     레일과 본문에는 서로 다른 상품이 뜨도록 한다.
     JS가 없으면 서버가 렌더한 기본 상품이 그대로 보인다. */
  (function () {
    var pool = window.COUPANG_POOL;
    if (!Array.isArray(pool) || pool.length < 2) return;

    var picked = [];
    function pick() {
      var avail = pool.filter(function (p) { return picked.indexOf(p.key) < 0; });
      if (!avail.length) avail = pool;
      var p = avail[Math.floor(Math.random() * avail.length)];
      picked.push(p.key);
      return p;
    }

    $$('[data-coupang-slot]').forEach(function (slot) {
      var p = pick();
      var frame = slot.querySelector('iframe');
      if (frame && frame.getAttribute('src') !== p.iframe) frame.setAttribute('src', p.iframe);
      if (frame) frame.setAttribute('title', p.name);

      var nameEl = slot.querySelector('[data-coupang-name]');
      if (nameEl) nameEl.textContent = p.name;
      var whyEl = slot.querySelector('[data-coupang-why]');
      if (whyEl) whyEl.textContent = p.why;
      var linkEl = slot.querySelector('[data-coupang-link]');
      if (linkEl) linkEl.setAttribute('href', p.link);
    });
  })();

  /* ---------- Year in footer ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
