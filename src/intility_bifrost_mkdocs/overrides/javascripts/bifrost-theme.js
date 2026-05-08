/*
 * Bifrost theme sync.
 *
 * Mirrors Material for MkDocs' palette state onto the Bifrost CSS framework:
 *   data-md-color-scheme  -> .bf-lightmode / .bf-darkmode  on <html>
 *   data-md-color-primary -> .bf-theme-{teal,purple,pink,yellow}
 *
 * Also inserts an optional version badge into the header when a
 * <meta name="bifrost-version" content="..."> tag is present.
 *
 * Exposes pure functions on `module.exports` for unit testing under
 * Node's built-in test runner.
 */
(function (global) {
  var BIFROST_THEMES = ['teal', 'purple', 'pink', 'yellow'];
  var DARK_SCHEMES = ['dark', 'slate'];
  var DEFAULT_THEME = 'teal';

  function syncBifrostTheme(html, body) {
    if (!html || !body) return;

    var scheme = body.getAttribute('data-md-color-scheme');
    var primary = body.getAttribute('data-md-color-primary');

    if (DARK_SCHEMES.indexOf(scheme) !== -1) {
      html.classList.add('bf-darkmode');
      html.classList.remove('bf-lightmode');
    } else {
      html.classList.add('bf-lightmode');
      html.classList.remove('bf-darkmode');
    }

    BIFROST_THEMES.forEach(function (theme) {
      html.classList.remove('bf-theme-' + theme);
    });
    var resolved = BIFROST_THEMES.indexOf(primary) !== -1 ? primary : DEFAULT_THEME;
    html.classList.add('bf-theme-' + resolved);
  }

  function readVersion(doc) {
    if (!doc || !doc.querySelector) return null;
    var meta = doc.querySelector('meta[name="bifrost-version"]');
    if (!meta) return null;
    var content = meta.getAttribute('content');
    return content && content.length > 0 ? content : null;
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
    syncBifrostTheme(html, body);

    var version = readVersion(document);
    if (version) {
      insertVersionBadge(document, document.querySelector('.md-header__topic'), version);
    }

    var observer = new MutationObserver(function () {
      syncBifrostTheme(html, body);
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
      DARK_SCHEMES: DARK_SCHEMES,
      DEFAULT_THEME: DEFAULT_THEME,
    };
  }
})(typeof window !== 'undefined' ? window : globalThis);
