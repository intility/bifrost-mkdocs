/*
 * Unit tests for src/intility_bifrost_mkdocs/overrides/javascripts/bifrost-theme.js
 *
 * Run with:
 *   node --test tests/javascripts/
 *
 * No external dependencies. Uses Node's built-in `node:test` runner and a
 * tiny hand-rolled DOM stub so the JS module can be loaded as CommonJS.
 */
const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');

const MODULE_PATH = path.resolve(
  __dirname,
  '..',
  '..',
  'src',
  'intility_bifrost_mkdocs',
  'overrides',
  'javascripts',
  'bifrost-theme.js',
);

const {
  syncBifrostTheme,
  readVersion,
  insertVersionBadge,
  isMacPlatform,
  searchHotkeyLabel,
  isSearchHotkey,
  insertSearchHint,
  BIFROST_THEMES,
} = require(MODULE_PATH);

function makeClassList() {
  const set = new Set();
  return {
    add(c) { set.add(c); },
    remove(c) { set.delete(c); },
    contains(c) { return set.has(c); },
    toArray() { return [...set]; },
  };
}

function makeHtml(initialClasses = []) {
  const classList = makeClassList();
  initialClasses.forEach((c) => classList.add(c));
  return { classList };
}

function makeBody(scheme, primary) {
  return {
    getAttribute(name) {
      if (name === 'data-md-color-scheme') return scheme;
      if (name === 'data-md-color-primary') return primary;
      return null;
    },
  };
}

// ---------------------------------------------------------------------------
// syncBifrostTheme — light/dark mode mapping
// ---------------------------------------------------------------------------

test('slate scheme maps to bf-darkmode (Material standard)', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('slate', 'teal'));
  assert.ok(html.classList.contains('bf-darkmode'));
  assert.ok(!html.classList.contains('bf-lightmode'));
});

test('dark scheme maps to bf-darkmode (plugin documented)', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('dark', 'teal'));
  assert.ok(html.classList.contains('bf-darkmode'));
  assert.ok(!html.classList.contains('bf-lightmode'));
});

test('default scheme maps to bf-lightmode (Material standard)', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('default', 'teal'));
  assert.ok(html.classList.contains('bf-lightmode'));
  assert.ok(!html.classList.contains('bf-darkmode'));
});

test('light scheme maps to bf-lightmode (plugin documented)', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('light', 'teal'));
  assert.ok(html.classList.contains('bf-lightmode'));
  assert.ok(!html.classList.contains('bf-darkmode'));
});

test('missing scheme falls back to bf-lightmode', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody(null, 'teal'));
  assert.ok(html.classList.contains('bf-lightmode'));
  assert.ok(!html.classList.contains('bf-darkmode'));
});

test('unknown scheme value falls back to bf-lightmode', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('chartreuse', 'teal'));
  assert.ok(html.classList.contains('bf-lightmode'));
  assert.ok(!html.classList.contains('bf-darkmode'));
});

test('switching from dark back to light removes bf-darkmode', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('slate', 'teal'));
  assert.ok(html.classList.contains('bf-darkmode'));

  syncBifrostTheme(html, makeBody('default', 'teal'));
  assert.ok(html.classList.contains('bf-lightmode'));
  assert.ok(!html.classList.contains('bf-darkmode'));
});

// ---------------------------------------------------------------------------
// syncBifrostTheme — primary/theme mapping
// ---------------------------------------------------------------------------

BIFROST_THEMES.forEach((primary) => {
  test(`primary=${primary} applies bf-theme-${primary}`, () => {
    const html = makeHtml();
    syncBifrostTheme(html, makeBody('default', primary));
    assert.ok(html.classList.contains('bf-theme-' + primary));
  });
});

test('missing primary defaults to bf-theme-teal', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('default', null));
  assert.ok(html.classList.contains('bf-theme-teal'));
});

test('unknown primary defaults to bf-theme-teal', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('default', 'mauve'));
  assert.ok(html.classList.contains('bf-theme-teal'));
});

test('switching theme removes the previous bf-theme-* class', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('default', 'purple'));
  assert.ok(html.classList.contains('bf-theme-purple'));

  syncBifrostTheme(html, makeBody('default', 'pink'));
  assert.ok(html.classList.contains('bf-theme-pink'));
  assert.ok(!html.classList.contains('bf-theme-purple'));
});

test('only one bf-theme-* class is set at a time', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('default', 'yellow'));
  const themeClasses = html.classList.toArray().filter((c) => c.startsWith('bf-theme-'));
  assert.equal(themeClasses.length, 1);
  assert.equal(themeClasses[0], 'bf-theme-yellow');
});

// ---------------------------------------------------------------------------
// syncBifrostTheme — guards
// ---------------------------------------------------------------------------

test('returns silently when html or body is missing', () => {
  // Should not throw.
  syncBifrostTheme(null, null);
  syncBifrostTheme(makeHtml(), null);
  syncBifrostTheme(null, makeBody('slate', 'teal'));
});

// ---------------------------------------------------------------------------
// readVersion / insertVersionBadge
// ---------------------------------------------------------------------------

function makeDoc({ version = null, hasBadge = false } = {}) {
  const calls = [];
  return {
    querySelector(selector) {
      calls.push(selector);
      if (selector === 'meta[name="bifrost-version"]') {
        if (version === null) return null;
        return {
          getAttribute(name) {
            return name === 'content' ? version : null;
          },
        };
      }
      return null;
    },
    createElement(_tag) {
      return {
        className: '',
        textContent: '',
      };
    },
    _calls: calls,
  };
}

function makeHeaderTopic({ alreadyBadged = false } = {}) {
  const appended = [];
  return {
    querySelector(selector) {
      if (selector === '.bf-header-version' && alreadyBadged) {
        return { existing: true };
      }
      return null;
    },
    appendChild(child) {
      appended.push(child);
      return child;
    },
    appended,
  };
}

test('readVersion returns content when meta tag is present', () => {
  const doc = makeDoc({ version: '1.2.3' });
  assert.equal(readVersion(doc), '1.2.3');
});

test('readVersion returns null when meta tag is absent', () => {
  const doc = makeDoc({ version: null });
  assert.equal(readVersion(doc), null);
});

test('readVersion returns null for empty content', () => {
  const doc = {
    querySelector: () => ({ getAttribute: () => '' }),
  };
  assert.equal(readVersion(doc), null);
});

test('insertVersionBadge appends a badge with the version text', () => {
  const doc = makeDoc();
  const topic = makeHeaderTopic();
  const badge = insertVersionBadge(doc, topic, '0.7.0');
  assert.ok(badge);
  assert.equal(badge.textContent, 'v0.7.0');
  assert.match(badge.className, /bf-header-version/);
  assert.equal(topic.appended.length, 1);
});

test('insertVersionBadge skips when a badge is already present', () => {
  const doc = makeDoc();
  const topic = makeHeaderTopic({ alreadyBadged: true });
  const badge = insertVersionBadge(doc, topic, '0.7.0');
  assert.equal(badge, null);
  assert.equal(topic.appended.length, 0);
});

test('insertVersionBadge is a no-op without version, doc, or topic', () => {
  const doc = makeDoc();
  const topic = makeHeaderTopic();
  assert.equal(insertVersionBadge(null, topic, '1.0.0'), null);
  assert.equal(insertVersionBadge(doc, null, '1.0.0'), null);
  assert.equal(insertVersionBadge(doc, topic, null), null);
  assert.equal(topic.appended.length, 0);
});

// ---------------------------------------------------------------------------
// Search hotkey: platform detection + label
// ---------------------------------------------------------------------------

test('isMacPlatform detects mac via platform string', () => {
  assert.equal(isMacPlatform({ platform: 'MacIntel' }), true);
  assert.equal(isMacPlatform({ platform: 'iPhone' }), true);
});

test('isMacPlatform detects mac via userAgent fallback', () => {
  assert.equal(isMacPlatform({ platform: '', userAgent: 'Mozilla/5.0 (Macintosh)' }), true);
});

test('isMacPlatform is false for windows/linux and missing navigator', () => {
  assert.equal(isMacPlatform({ platform: 'Win32' }), false);
  assert.equal(isMacPlatform({ platform: 'Linux x86_64' }), false);
  assert.equal(isMacPlatform(null), false);
});

test('searchHotkeyLabel reflects platform', () => {
  assert.equal(searchHotkeyLabel(true), '⌘ K');
  assert.equal(searchHotkeyLabel(false), 'Ctrl K');
});

// ---------------------------------------------------------------------------
// isSearchHotkey: modifier gating per platform
// ---------------------------------------------------------------------------

test('isSearchHotkey matches Cmd+K only on mac', () => {
  assert.equal(isSearchHotkey({ key: 'k', metaKey: true }, true), true);
  assert.equal(isSearchHotkey({ key: 'K', metaKey: true }, true), true);
  // Ctrl+K should not trigger on mac (it is a native input binding there).
  assert.equal(isSearchHotkey({ key: 'k', ctrlKey: true }, true), false);
});

test('isSearchHotkey matches Ctrl+K only off mac', () => {
  assert.equal(isSearchHotkey({ key: 'k', ctrlKey: true }, false), true);
  assert.equal(isSearchHotkey({ key: 'k', metaKey: true }, false), false);
});

test('isSearchHotkey ignores other keys and bare k, and missing event', () => {
  assert.equal(isSearchHotkey({ key: 'j', metaKey: true }, true), false);
  assert.equal(isSearchHotkey({ key: 'k' }, true), false);
  assert.equal(isSearchHotkey(null, true), false);
});

// ---------------------------------------------------------------------------
// insertSearchHint
// ---------------------------------------------------------------------------

function makeForm({ alreadyHinted = false } = {}) {
  const appended = [];
  return {
    querySelector(selector) {
      if (selector === '.bf-search-hint' && alreadyHinted) return { existing: true };
      return null;
    },
    appendChild(child) {
      appended.push(child);
      return child;
    },
    appended,
  };
}

function makeHintDoc() {
  return {
    createElement(_tag) {
      return {
        className: '',
        textContent: '',
        _attrs: {},
        setAttribute(name, value) { this._attrs[name] = value; },
      };
    },
  };
}

test('insertSearchHint appends a kbd with the platform label', () => {
  const doc = makeHintDoc();
  const form = makeForm();
  const hint = insertSearchHint(doc, form, true);
  assert.ok(hint);
  assert.equal(hint.className, 'bf-search-hint');
  assert.equal(hint.textContent, '⌘ K');
  assert.equal(hint._attrs['aria-hidden'], 'true');
  assert.equal(form.appended.length, 1);
});

test('insertSearchHint uses Ctrl K off mac', () => {
  const hint = insertSearchHint(makeHintDoc(), makeForm(), false);
  assert.equal(hint.textContent, 'Ctrl K');
});

test('insertSearchHint skips when a hint already exists', () => {
  const form = makeForm({ alreadyHinted: true });
  assert.equal(insertSearchHint(makeHintDoc(), form, true), null);
  assert.equal(form.appended.length, 0);
});

test('insertSearchHint is a no-op without doc or form', () => {
  assert.equal(insertSearchHint(null, makeForm(), true), null);
  assert.equal(insertSearchHint(makeHintDoc(), null, true), null);
});
