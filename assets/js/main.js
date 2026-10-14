// Active-section highlight for the fixed nav
(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav-links a'));
  var map = {};
  links.forEach(function (a) {
    var id = a.getAttribute('href').slice(1);
    var sec = document.getElementById(id);
    if (sec) map[id] = a;
  });
  var sections = Object.keys(map).map(function (id) { return document.getElementById(id); });

  if ('IntersectionObserver' in window && sections.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (l) { l.classList.remove('active'); });
          var active = map[e.target.id];
          if (active) active.classList.add('active');
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
    sections.forEach(function (s) { io.observe(s); });
  }

  // Tiny easter egg: press ` to leave a note (a nod to the reference site)
  var toast = null;
  document.addEventListener('keydown', function (ev) {
    if (ev.key === '`' || ev.code === 'Backquote') {
      if (toast) return;
      toast = document.createElement('div');
      toast.textContent = '✳ still curious, still building.';
      toast.style.cssText = 'position:fixed;left:50%;bottom:28px;transform:translateX(-50%);' +
        'background:#1c1b19;color:#fcfbf9;padding:9px 16px;border-radius:999px;font-size:13px;' +
        'font-family:system-ui,sans-serif;z-index:99;box-shadow:0 6px 20px rgba(0,0,0,.18);';
      document.body.appendChild(toast);
      setTimeout(function () { if (toast) { toast.remove(); toast = null; } }, 2600);
    }
  });
})();
