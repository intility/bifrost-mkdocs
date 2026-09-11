/*
 * Unit tests for src/intility_bifrost_zensical/theme/javascripts/bifrost-theme.js
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
  'intility_bifrost_zensical',
  'theme',
  'javascripts',
  'bifrost-theme.js',
);

const {
  syncBifrostTheme,
  readVersion,
  insertVersionBadge,
  BIFROST_THEMES,
} = require(MODULE_PATH);

function makeClassList() {
  const set = new Set();
  return {
    add(c) { set.add(c); },
    remove(c) { set.delete(c); },
    toggle(c, force) { force ? set.add(c) : set.delete(c); },
    contains(c) { return set.has(c); },
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

test('slate scheme maps to bf-darkmode', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('slate', 'teal'));
  assert.ok(html.classList.contains('bf-darkmode'));
  assert.ok(!html.classList.contains('bf-lightmode'));
});

test('default scheme maps to bf-lightmode', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('default', 'teal'));
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

test('extra.primary meta tag wins over the palette primary', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('default', 'teal'), makeDoc({ primary: 'purple' }));
  assert.ok(html.classList.contains('bf-theme-purple'));
  assert.ok(!html.classList.contains('bf-theme-teal'));
});

test('switching theme removes the previous bf-theme-* class', () => {
  const html = makeHtml();
  syncBifrostTheme(html, makeBody('default', 'purple'));
  assert.ok(html.classList.contains('bf-theme-purple'));

  syncBifrostTheme(html, makeBody('default', 'pink'));
  assert.ok(html.classList.contains('bf-theme-pink'));
  assert.ok(!html.classList.contains('bf-theme-purple'));
});

// ---------------------------------------------------------------------------
// readVersion / insertVersionBadge
// ---------------------------------------------------------------------------

function makeDoc({ version = null, primary = null } = {}) {
  const metas = { 'meta[name="bifrost-version"]': version, 'meta[name="bifrost-primary"]': primary };
  return {
    querySelector(selector) {
      const content = metas[selector];
      if (content === undefined || content === null) return null;
      return {
        getAttribute(name) {
          return name === 'content' ? content : null;
        },
      };
    },
    createElement(_tag) {
      return {
        className: '',
        textContent: '',
      };
    },
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

