# Changelog

## 0.1.0 (2026-09-11)


### ⚠ BREAKING CHANGES

* migrate to zensical theme
* migrate to Zensical theme ([#62](https://github.com/intility/bifrost-zensical/issues/62))
* deprecate package ([#60](https://github.com/intility/bifrost-zensical/issues/60))
* **theme:** MathJax/arithmatex support is removed (mathjax.js, pymdownx.arithmatex, the unpkg MathJax script, and the Math showcase page).

### Features

* add localized-plugin as dependancy ([a0565d2](https://github.com/intility/bifrost-zensical/commit/a0565d2351a7b4471cd5f897e15c216d39ff1ae4))
* add markdown-callouts for GitHub alert syntax support ([#18](https://github.com/intility/bifrost-zensical/issues/18)) ([d63f72f](https://github.com/intility/bifrost-zensical/commit/d63f72fcafb084ea42a4f898f46315d4ee5294e1))
* add PyPI publishing and pin dependencies ([#13](https://github.com/intility/bifrost-zensical/issues/13)) ([32d671f](https://github.com/intility/bifrost-zensical/commit/32d671f3982b1ee9d647ed11009b40985f057319))
* auto-inject extensions, features, and theme defaults from plugin ([9178bec](https://github.com/intility/bifrost-zensical/commit/9178bec9be8e773c95f2997161c85ed63911f1d5))
* auto-inject extensions, features, and theme defaults from plugin ([815c9f8](https://github.com/intility/bifrost-zensical/commit/815c9f86025b477e6945672d72c12983bbc33616))
* bundle mkdocs-awesome-nav as runtime dependency ([#31](https://github.com/intility/bifrost-zensical/issues/31)) ([5f4f565](https://github.com/intility/bifrost-zensical/commit/5f4f565ea27ec4d1beedf8a23d35baba7badfc9a))
* deprecate package ([#60](https://github.com/intility/bifrost-zensical/issues/60)) ([a74115d](https://github.com/intility/bifrost-zensical/commit/a74115d32176034f9b86b184297655a7dcb12058))
* display version badge in header when extra.version is set ([#20](https://github.com/intility/bifrost-zensical/issues/20)) ([5787a4e](https://github.com/intility/bifrost-zensical/commit/5787a4e2107c0f16ea081590b7e397a56ead6f31))
* **docs:** Add MkDocs template with GitHub Pages deployment ([4957bc2](https://github.com/intility/bifrost-zensical/commit/4957bc23d0b0699914f454fe90b2788be091bd67))
* **docs:** Enable live reload for local documentation server ([b53d9ed](https://github.com/intility/bifrost-zensical/commit/b53d9edb9fd10138fa5750ff16d07d2e88e45dc7))
* Enhance Bifrost theme integration and syntax highlighting ([d2ee2d9](https://github.com/intility/bifrost-zensical/commit/d2ee2d9331ba2ab65f10fbebb87f3d6afce3edb0))
* migrate to zensical theme ([d4b8579](https://github.com/intility/bifrost-zensical/commit/d4b85793e94071153729425db41ab17a12eec1c3))
* migrate to Zensical theme ([#62](https://github.com/intility/bifrost-zensical/issues/62)) ([d4b8579](https://github.com/intility/bifrost-zensical/commit/d4b85793e94071153729425db41ab17a12eec1c3))
* **plugin:** inject default light/dark palette toggle ([#55](https://github.com/intility/bifrost-zensical/issues/55)) ([03fbf2b](https://github.com/intility/bifrost-zensical/commit/03fbf2b15731f6f755906a3fc12fc9c4d3b08d03))
* restructure as pip-installable MkDocs plugin ([ef822f4](https://github.com/intility/bifrost-zensical/commit/ef822f4758c4a5b6b146311d709a7ecce3157c47))
* restructure as pip-installable plugin with included defaults ([#4](https://github.com/intility/bifrost-zensical/issues/4)) ([a145b4c](https://github.com/intility/bifrost-zensical/commit/a145b4c1552359822146d19b79af5075a882b1e7))
* **theme:** rework theme onto cascade layers with vendored framework and fonts ([#51](https://github.com/intility/bifrost-zensical/issues/51)) ([dee710c](https://github.com/intility/bifrost-zensical/commit/dee710cc36d7764bbe89f9712cedabeea0f11384))


### Fixes

* add missing content.tabs.link feature ([416e47f](https://github.com/intility/bifrost-zensical/commit/416e47faff3ea277010bcd0e59eedf4a0d61d754))
* **ci:** fix check and deploy docs workflows ([25e6fb1](https://github.com/intility/bifrost-zensical/commit/25e6fb1a3f98983b0f278553e7f2aba7983cf4de))
* clean up version badge styling ([05ebc17](https://github.com/intility/bifrost-zensical/commit/05ebc177465f14872d805850de039b442e263779))
* **deps:** pin mkdocs&lt;2 and raise material floor to 9.7.5 ([#49](https://github.com/intility/bifrost-zensical/issues/49)) ([7863d6a](https://github.com/intility/bifrost-zensical/commit/7863d6a8c18148192ce2af3cd95fa1d6f9671cc6))
* **docs:** update URLs after repo rename to bifrost-mkdocs ([6a5cea1](https://github.com/intility/bifrost-zensical/commit/6a5cea10190147d26f3be2cd06ad3ebb4e19628f))
* **docs:** Update virtual environment activation command in README and enhance link styles in Bifrost theme ([6c310f8](https://github.com/intility/bifrost-zensical/commit/6c310f85739e7e7ff547562049013a042418bc77))
* formatting error ([fb8dcf9](https://github.com/intility/bifrost-zensical/commit/fb8dcf9f87c7bd350118c0b621bc7616049f2a89))
* **theme:** detect Material's slate scheme as dark mode ([#37](https://github.com/intility/bifrost-zensical/issues/37)) ([82624b3](https://github.com/intility/bifrost-zensical/commit/82624b3b3b4043cfdfb37abce953252c5bd652a3))


### Code refactoring

* **css:** drop extra.css, layer Bifrost framework, strip important ([#39](https://github.com/intility/bifrost-zensical/issues/39)) ([6b868f7](https://github.com/intility/bifrost-zensical/commit/6b868f757666331c5014e3cb97277e0d7f3e5aa8))


### Documentation

* add readme to python project file ([85484d1](https://github.com/intility/bifrost-zensical/commit/85484d13c700bd0f023cf41aac48cb4af10be38e))
* clean up README ([bbfebe3](https://github.com/intility/bifrost-zensical/commit/bbfebe3a2ed117dd57b60b183cb69d7624361c2e))
* Correct line number for changing the primary color in mkdocs.yaml ([a28484c](https://github.com/intility/bifrost-zensical/commit/a28484cf628b4ac4072810454ad6b951ff0b81d3))
* **README:** Add link to documentation preview and fix URL placeholder ([65a4570](https://github.com/intility/bifrost-zensical/commit/65a457027ca21e6373746c051218a34fbeec8f88))
* update README ([c1b842c](https://github.com/intility/bifrost-zensical/commit/c1b842cc28438411d79bc0428bab0f0f67160983))
* update README and mkdocs.yml ([bbd776b](https://github.com/intility/bifrost-zensical/commit/bbd776bfa0916db3f2afcf3cff66d322480afe96))
* update readme and quick start guide ([#54](https://github.com/intility/bifrost-zensical/issues/54)) ([9fe660c](https://github.com/intility/bifrost-zensical/commit/9fe660cbec17a22d0276b7a757e90ecd8142ca2f))


### CI

* add permissions to check workflow ([28abe84](https://github.com/intility/bifrost-zensical/commit/28abe84ee700d2fabf3280d1825762d651efdd95))
* codeql action-read ([7d3b91c](https://github.com/intility/bifrost-zensical/commit/7d3b91c49cdbe55fc8b919644f44ac781ccf316e))
* codeql read permission ([5c879f7](https://github.com/intility/bifrost-zensical/commit/5c879f7d680d04d78d3b4c1fb66e944a61b7c46e))

## Changelog

History for the deprecated `intility-bifrost-mkdocs` package lives in its [releases](https://github.com/intility/bifrost-mkdocs/releases).
