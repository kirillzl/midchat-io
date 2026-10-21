/* Gible cookieless beacon (first-party). Each site serves it from its own domain:
   <script src="/_g/s.js" data-p="garlic" defer></script>          (events go to /_g/e next to the script)
   <script src="/_g/s.js" data-p="midchat" data-e="https://gible.co/_g/e" defer></script>   (static hosts: self-hosted copy)
   Legacy https://gible.co/b.js still posts to /api/hub/b. Call gible.track("signup"|"aha"|"checkout"|"share"|"invite", {v:"a"|"b"}).
   No cookies, no storage. */
(function () {
  var s = document.currentScript, p = s && s.getAttribute('data-p'); if (!p || navigator.webdriver) return;
  var u = s.src ? new URL(s.src, location.href) : null;
  var api = s.getAttribute('data-e') || (!u ? '/_g/e' : /\/b\.js$/.test(u.pathname) ? u.origin + '/api/hub/b' : u.origin + u.pathname.replace(/[^\/]*$/, 'e'));
  // sendBeacon only same-origin: EasyPrivacy blocks every third-party ping (*$ping,third-party); cross-origin uses fetch.
  var same = new URL(api, location.href).origin === location.origin;
  function track(e, o) { try { var d = JSON.stringify({ p: p, e: e, v: o && o.v, h: location.hostname });
    if (!(same && navigator.sendBeacon && navigator.sendBeacon(api, new Blob([d], { type: 'text/plain' })))) fetch(api, { method: 'POST', body: d, keepalive: true }); } catch (x) {} }
  window.gible = { track: track };
  track('pv', window.gibleVariant ? { v: window.gibleVariant } : null);
})();
