# Expectant — 임신·출산 정보 가이드

https://expectant.pages.dev

임신 테스트기(임테기) 사용법부터 주차별 증상, 출산 예정일 계산기까지
임신을 확인하고 준비하는 과정을 안내하는 정적 웹사이트입니다.

## 구조

```
index.html                     메인
pregnancy-test/                임신 확인 (임테기·피검사·초음파)
symptoms/                      주차별 증상 (극초기·초기·중기·막달)
tools/                         계산기 3종
guide/                         임신준비·건강·출산·산후 (준비 중)
assets/css/style.css           디자인 시스템 (Soft Pastel)
assets/js/site.js              네비·검색·목차·계산기
assets/js/search-index.js      검색 색인 (자동 생성)
```

## 빌드

HTML은 Python 생성기로 만들어집니다. 콘텐츠 수정 후:

```bash
python3 build.py
```

- `build.py` — 레이아웃, 네비게이션, 컴포넌트, 사이트맵
- `content_pages.py` — 홈·허브·계산기·가이드
- `content_test.py` — 임신 확인 카테고리 문서 8편
- `content_symptoms.py` — 주차별 증상 문서 4편

빌드 시 `sitemap.xml`, `robots.txt`, `assets/js/search-index.js`가 함께 갱신됩니다.

## 배포

Cloudflare Pages — 빌드 명령 없음, 출력 디렉터리 `/` (루트).
main 브랜치에 push하면 자동 배포됩니다.

## 면책

이 사이트의 내용은 일반적인 건강 정보이며 의사의 진단이나 치료를 대신하지 않습니다.
