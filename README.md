# Expectant — 임신·출산 정보 가이드

https://expectant.ephseed.com

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

## 매일 자동 발행 (스케줄 태스크)

매일 21:00 KST에 `_content-queue.json`의 pending 항목 중 order가 가장 작은 글 1편을 작성해 푸시한다.

1. `_content-queue.json` 읽기 → 다음 발행할 항목 확인
2. `guide_articles/<slug를 밑줄로>.py` 생성 (모듈 규약은 `content_guide.py` 상단 주석 참고)
3. 해당 항목 `status`를 `published`, `published_at`을 오늘 날짜로 변경
4. `python3 build.py` 실행
5. 커밋 + 푸시 (Cloudflare Pages 자동 배포)

pending이 모두 소진되면 기존 글과 겹치지 않는 새 주제를 큐에 추가한 뒤 계속 진행한다.
