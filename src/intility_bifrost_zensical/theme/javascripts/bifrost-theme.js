/* Bifrost theme sync */
(function (global) {
  var BIFROST_THEMES = ['teal', 'purple', 'pink', 'yellow', 'green'];
  var DEFAULT_THEME = 'teal';

  function readMeta(doc, name) {
    if (!doc || !doc.querySelector) return null;
    var meta = doc.querySelector('meta[name="' + name + '"]');
    if (!meta) return null;
    var content = meta.getAttribute('content');
    return content && content.length > 0 ? content : null;
  }

  // `extra.primary` (stamped as a meta tag by main.html) wins over the
  // palette's primary, so one config line changes the color without
  // redefining the whole palette.
  function syncBifrostTheme(html, body, doc) {
    if (!html || !body) return;

    var dark = body.getAttribute('data-md-color-scheme') === 'slate';
    html.classList.toggle('bf-darkmode', dark);
    html.classList.toggle('bf-lightmode', !dark);

    var primary = readMeta(doc, 'bifrost-primary') || body.getAttribute('data-md-color-primary');

    BIFROST_THEMES.forEach(function (theme) {
      html.classList.remove('bf-theme-' + theme);
    });
    var resolved = BIFROST_THEMES.indexOf(primary) !== -1 ? primary : DEFAULT_THEME;
    html.classList.add('bf-theme-' + resolved);
  }

  function readVersion(doc) {
    return readMeta(doc, 'bifrost-version');
  }

  function insertVersionBadge(doc, headerTopic, version) {
    if (!doc || !headerTopic || !version) return null;
    if (headerTopic.querySelector && headerTopic.querySelector('.bf-header-version')) {
      return null;
    }
    var badge = doc.createElement('span');
    badge.className = 'bf-badge bf-badge-pill bfc-theme-fade-bg bf-header-version';
    badge.textContent = 'v' + version;
    headerTopic.appendChild(badge);
    return badge;
  }

  function init() {
    var html = document.documentElement;
    var body = document.body;
    syncBifrostTheme(html, body, document);

    var version = readVersion(document);
    if (version) {
      insertVersionBadge(document, document.querySelector('.md-header__topic'), version);
    }

    var observer = new MutationObserver(function () {
      syncBifrostTheme(html, body, document);
    });
    observer.observe(body, {
      attributes: true,
      attributeFilter: ['data-md-color-scheme', 'data-md-color-primary'],
    });
  }

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
    } else {
      init();
    }
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
      syncBifrostTheme: syncBifrostTheme,
      readVersion: readVersion,
      insertVersionBadge: insertVersionBadge,
      BIFROST_THEMES: BIFROST_THEMES,
      DEFAULT_THEME: DEFAULT_THEME,
    };
  }
})(typeof window !== 'undefined' ? window : globalThis);
