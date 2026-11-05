(function () {
  var root = document.documentElement;
  var toggle = document.querySelector(".theme-toggle");
  var navBtn = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");

  function systemDark() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  function theme() {
    var explicit = root.getAttribute("data-theme");
    if (explicit === "light" || explicit === "dark") return explicit;
    return systemDark() ? "dark" : "light";
  }

  function paintToggle() {
    if (!toggle) return;
    var dark = theme() === "dark";
    toggle.setAttribute("aria-pressed", dark ? "true" : "false");
    toggle.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
  }

  paintToggle();

  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = theme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("midchat-theme", next); } catch (err) { /* private mode */ }
      paintToggle();
    });
  }

  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    var onScheme = function () {
      if (!root.getAttribute("data-theme")) paintToggle();
    };
    if (mq.addEventListener) mq.addEventListener("change", onScheme);
  }

  function closeNav() {
    if (!nav || !navBtn) return;
    nav.classList.remove("is-open");
    navBtn.setAttribute("aria-expanded", "false");
  }

  if (navBtn && nav) {
    navBtn.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      navBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (event) {
      if (event.target.closest("a")) closeNav();
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeNav();
    });
  }

  document.addEventListener("click", function (event) {
    var btn = event.target.closest(".player-btn");
    if (!btn) return;
    var src = btn.getAttribute("data-video");
    if (!src) return;
    var video = document.createElement("video");
    video.controls = true;
    video.playsInline = true;
    video.preload = "none";
    video.setAttribute("aria-label", btn.getAttribute("data-title") || "Demo video");
    var source = document.createElement("source");
    source.src = src;
    source.type = "video/mp4";
    video.appendChild(source);
    var fallback = document.createElement("a");
    fallback.href = src;
    fallback.textContent = "Open the demo video";
    video.appendChild(fallback);
    btn.replaceWith(video);
    var play = video.play();
    if (play && typeof play.catch === "function") play.catch(function () {});
  });

  var links = window.MIDCHAT_LINKS || {};
  var slots = document.querySelectorAll("[data-chatgpt]");
  for (var i = 0; i < slots.length; i++) {
    var el = slots[i];
    var id = el.getAttribute("data-chatgpt");
    var url = links[id];
    if (!url) continue;
    var anchor = document.createElement("a");
    anchor.className = "btn btn-primary";
    anchor.href = url;
    anchor.target = "_blank";
    anchor.rel = "noopener noreferrer";
    anchor.textContent = "Open in ChatGPT";
    el.replaceWith(anchor);
  }
})();
