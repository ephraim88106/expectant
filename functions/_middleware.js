// Cloudflare Pages Functions 미들웨어
// 기본 도메인(*.pages.dev)으로 들어온 요청을 정식 도메인으로 301 리다이렉트한다.
// 같은 내용이 두 도메인에 동시에 노출되어 중복 콘텐츠로 잡히는 것과,
// 애드센스·서치콘솔이 엉뚱한 도메인을 심사하는 것을 막기 위함.
const CANONICAL_HOST = "expectant.ephseed.com";

export async function onRequest({ request, next }) {
  const url = new URL(request.url);
  if (url.hostname.endsWith(".pages.dev")) {
    url.hostname = CANONICAL_HOST;
    url.protocol = "https:";
    return Response.redirect(url.toString(), 301);
  }
  return next();
}
