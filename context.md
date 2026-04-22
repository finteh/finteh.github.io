# FinTech Association — Project Context
 
This document is the single source of truth for the FinTech Association website
rebuild (finteh.org). Any contributor — human or AI — should read this first
before writing code or content.
 
---
 
## 1. What the organization is
 
FinTech Association is a non-governmental professional community founded on
**5 November 2017 in St. Petersburg**, formally established by Protocol No. 1
signed publicly at the Erarta Museum event. Officially incorporated as a
non-governmental organization without forming a legal entity. Current office
address: Tadeusza Kościuszki 10, 05-500 Warsaw, Poland.
 
The association grew out of a Telegram chat started by its founder while
working at Rocketbank (the most innovative Russian bank at the time). What
began as a personal network of fintech builders evolved into a self-governing
community of experts from major banks (Sberbank, Gazprombank, Rocketbank),
fintech startups, crypto projects, and financial infrastructure operators.
 
### Core model
 
- **Members** are individuals only. Membership is free — you join by entering
  the public Telegram chat. No fees, no application forms.
- **Organizations** join as **partners**, not members. Partnership is a
  separate track with its own terms.
- The **Telegram chat is the registry**. The **chat history is the protocol**.
  **Votes in the chat are decisions**. Everything is public by default.
- The association is governed by a **Board** elected from the community, and
  decisions are made through open voting in the chat.
 
This radical transparency is the association's unique feature. It should be
presented on the website as a manifesto, not hidden.
 
---
 
## 2. Target audiences
 
The website must serve three distinct audiences:
 
1. **Prospective members** (individuals) — developers, analysts, founders,
   experts in fintech and crypto. They need to know: what this community is,
   who's in it, and how to join.
2. **Prospective partners** (organizations) — companies seeking collaboration,
   expertise, audits, or access to the network. Different pitch, different
   CTA, different page.
3. **External audiences** — journalists, regulators, potential collaborators
   evaluating the association's seriousness. They need credentials, track
   record, named people.
 
---
 
## 3. What the association does
 
Four active directions, plus historical context:
 
### Audit and expert assessment
Association experts perform audits of smart contracts, blockchain projects,
and fintech products. The process is operated by the president: he receives
requests, scopes the TOR, negotiates budget with the client, selects experts
from the pool (sometimes external experts are engaged), holds payment in
escrow, and publishes the final report under the association's name.
Audits are a paid service — pricing is always per-request, no public rates.
 
### Research
The flagship research direction is **UBI (Universal Basic Income)**. The
association has engaged with the **World Bank, the Central Bank of the
Russian Federation, and universities in Russia and Estonia** on this topic.
Currently dormant but planned to reactivate.
 
### Validator Relay Program
Originally, several board experts ran validator nodes in public blockchain
networks, mainly **Cosmos and Graphene ecosystems**. Live nodes are currently
inactive, but the association has designed a new program: "Validator Relay" —
when a large validator winds down, the association takes over delegations
and continues validating, keeping the network decentralized and generating
modest revenue ($500+/month per node). The association has physical
infrastructure available (hardware, UPS) from a previous "home data center"
project.
 
### Incubator
Built originally for projects proposed by association experts (not open to
outside submissions — entry is by invitation through the Board). Designed
for projects with **open source code and free licenses**. Support includes
mentorship, office space, connections, technical consulting. Investment
comes from the project's own investor, with association members able to
co-invest. **On pause since 2020** (Covid, then war). Not currently active
but could be reactivated.
 
---
 
## 4. Current website problems (finteh.org as of 2026)
 
- Structure is shaped by the template, not by the organization's real model.
- Membership — the core of any association — is not a proper section.
- Services, incubator, and nodes are scattered as top-level items with no
  clear relationship.
- "Pages" in the menu is a catch-all dumping ground.
- President's personal page — a key asset the founder actually uses in
  outreach — doesn't exist as a proper landing.
- UBI project, with its prestigious partners, is completely absent.
- "How we work" (the chat-as-registry model) is not explained anywhere.
- English text has errors; no serious multilingual setup.
 
---
 
## 5. Site structure (approved)
 
Top-level menu (7 items, no "Home" — logo links to homepage):
**About · Community · Join · Services · Programs · Reports · Events · Contact**
 
### About
- Mission & Values
- Our Story (Rocketbank → Erarta → today)
- How We Work (the manifesto about chat = registry)
- Charter & Governance
- Board of Directors
- Expert Pool (public bios)
- President (personal landing page — major asset)
 
### Community
- Join the Telegram chat
- Community values / Code of conduct
- Notable discussions / outcomes
 
### Join
- For Individuals → Membership (via Telegram)
- For Organizations → Partnership (form, terms)
 
### Services
- Audit (process, case studies, request form — no public pricing)
- Expert Consulting
 
### Programs
- UBI / Social Fintech Research (flagship, with history and status)
- Incubator (by invitation only — takes projects from members and experts;
  not open to public submissions)
- Validator Relay Program (new — also a standalone landing for outreach)
 
### Reports & Publications
- Audit Reports (with filters by industry/technology)
- Research (UBI and related)
- Methodology (minimal for now; expand as formalized)
- Blog / News
 
### Events
- Upcoming
- Past (with materials: slides, video, photos)
 
### Contact
- President (direct)
- General
- Office (Warsaw)
 
---
 
## 6. Design approach: hub + landing pages
 
The site uses a **hub + landing pages** pattern:
 
- The **hub layer** is the full site structure (About, Charter, Reports,
  etc.) — the confirming layer where visitors verify the organization is
  serious.
- The **landing layer** is a set of focused, conversion-oriented pages:
  Home, Membership, Partnership, Audit, Validator Relay, UBI. Each has its
  own scripted flow from hero to CTA.
 
Every landing must allow the visitor to jump into the hub at any point
(full navigation visible, contextual links in-text, complete footer).
 
### Standard landing anatomy
1. Hero (one sentence: what and why for me)
2. Proof / why trust (numbers, dates, partners, track record)
3. What / How (the offer explained, step-by-step)
4. Value / Benefits (concrete, not generic)
5. Deeper proof (cases, reports, stories)
6. Who runs this (president + board link)
7. CTA (one primary action)
8. Footer (full nav + contacts)
 
---
 
## 7. Tone of voice
 
**Professional-strict but human. Rockstars, not bureaucrats.** The community
consists of people who build fintech daily — not corporate officials.
 
Inspiration: the philosophy of the book "Write, Shorten" (Ilyahov).
 
Rules:
- Short sentences, no water.
- Concrete facts instead of abstractions.
- Verbs instead of nominalizations.
- No corporate cliches: "we strive", "our mission is to", "innovative
  solutions", "cutting-edge".
- No generic benefit icons (Networking / Research / Safe) — they mean
  nothing and everyone has them.
- Every sentence must promise or deliver something specific.
- Honesty over marketing: if the incubator is on pause — say so. If there
  are no upcoming events — show the archive.
- "Как пойдёт", "вроде как", "возможно" — forbidden. If you can't commit to
  a benefit, cut the sentence.
 
---
 
## 8. Languages
 
- **English** — **primary language of the site, and the language the homepage
  is built in**. Used by the president for international outreach, links to
  expert bios, etc.
- **Russian** — full parallel version, added via Astro i18n in stage 7 of the
  workflow (§12). 95% of the chat conversations happen in Russian; the
  community lives there. When added, Russian content must match the English
  canon in tone and structure — not the other way around.
- **Polish** — NOT needed. Office is in Warsaw but no Polish-speaking
  members participate actively.
 
i18n will be added after the English content stabilizes. Use Astro's native
i18n (Astro 4+), with routes `/en/` and `/ru/`, English as default.
 
---
 
## 9. Technical stack
 
- **Framework:** Astro (SSG, island architecture, zero-JS by default)
- **Styling:** Tailwind CSS
- **Content:** Markdown / MDX in content collections
- **Template base:** AstroWind (https://github.com/arthelokyo/astrowind)
  — chosen for its rich widget library (Hero, Features, Stats, Content,
  Steps, CallToAction) that maps directly onto our landing anatomy.
- **Hosting:** Cloudflare Pages (deploy from GitHub main branch)
- **Repository:** GitHub
- **Forms:** Cloudflare Workers (when needed, e.g. Partnership form, audit
  request)
- **CMS:** none initially. If needed later — Decap CMS (git-based,
  file-based, stays in repo).
- **TypeScript:** yes, Astro default.
 
### Visual direction
- Serious, restrained palette: deep navy / graphite / one accent color.
- NOT: playful gradients, pastel illustrations, stock "handshake" imagery.
- Real photos where possible (president, board, events).
- Typography: strong sans-serif headings (Inter Tight / Geist), clean
  readable body (Inter / system-ui).
 
---
 
## 10. Homepage specification (approved, final — English canon)
 
The homepage has 10 screens. Content below is approved **verbatim** — do not
rewrite, paraphrase, "improve", or translate without explicit instruction.
When the site is built (stage 3), this is the canonical English text.
 
### Screen 1 — Hero
- H1: The association for people building fintech
- Sub: A community of developers, analysts, and founders building fintech
  and crypto. Since 2017. No membership fees, no bureaucracy.
- Primary CTA: Join Telegram
- Secondary CTA: How we work
 
### Screen 2 — Stats
- Tagline: Since 2017
- Two counters only (the other candidates — audit reports, events — were
  dropped because honest numbers are low; we'll add them when they grow):
  - **1,477** chat members
  - **7+** countries
 
### Screen 3 — How we work
- H2: How the association works
- Body:
  > The charter signed in 2017 is clear on this: to become a member, join
  > the Telegram chat.
  >
  > The chat is the registry. The chat history is the protocol. Votes in
  > the chat are decisions. Everything is public by default.
  >
  > Not an experiment. Eight years and counting.
- Link: Read full charter →
 
### Screen 4 — Who's in the chat
- H2: Who's in the chat
- Body:
  > Banking app developers from major banks. Founders of fintech startups.
  > Blockchain experts. Analysts, lawyers, investors, owners of
  > infrastructure projects.
  >
  > Through the chat, people have hired developers, found investors, and
  > closed deals.
- Links: Meet the board → · Expert pool →
 
### Screen 5 — What we do
- H2: What we do
- Four cards:
  1. **Code audit and expert assessment.** Association experts audit smart
     contracts, blockchain projects, and fintech products. Reports are
     published openly, under the association's name. → Request audit
  2. **Research.** Our flagship is the UBI project. We've worked with the
     World Bank, the Central Bank of Russia, and universities in Russia and
     Estonia. → Read more
  3. **Blockchain Validators.** We run validator nodes on Cosmos and
     Graphene networks. Through our Relay Program, we take on delegations
     from winding-down validators. → Validator Relay
  4. **Incubator.** For open-source projects with permissive licenses.
     By invitation only — we take on projects from members and experts.
     → Read more
 
### Screen 6 — Latest reports
- H2: Latest reports
- 3–4 cards (placeholder for now, real reports to come)
- Link: All reports →
 
### Screen 7 — President
- Tagline: Led by
- Name: Aleksandr Kwaskoff
- Role: President
- Body: Founded the association in 2017 from a Telegram chat started while
  working at Rocketbank. Expert in fintech and crypto. Runs audit requests
  end to end: scoping, expert selection, sign-off.
- Links: Full bio → · Direct contact →
 
### Screen 8 — Partnership
- H2: Organizations join as partners, not members
- Body: Membership is for individuals only. Companies join as partners:
  joint projects, access to expertise, presence in the community.
- Link: Partnership details →
 
### Screen 9 — Events
- H2: Upcoming event
- Either: upcoming event card, or fallback to "Events archive →"
 
### Screen 10 — Final CTA
- H2: To join, post in the chat
- Body: Introduce yourself and ask your first question. You'll get answers
  from people who build fintech and crypto every day.
- Primary CTA: Join Telegram
- Secondary: For organizations: Partnership → · For press: Contact →
 
### Intentionally omitted from the homepage
- Generic benefit icon blocks ("Networking / Advantages / Research / Safe")
- Newsletter signup form (Telegram and blog are the channels)
- Partner logos (none curated yet; add when real assets exist)
- "Our mission" text blocks with corporate filler
- Counters for reports and events (re-add when numbers become meaningful)
 
---
 
## 10a. Russian locale (for i18n stage 7, reference)
 
These are the Russian-language drafts we iterated on before translating to
the English canon above. Kept as reference for the i18n stage — but note
that when Russian is added via i18n, it must match the English structure
and tone, not diverge. Treat these as drafts, not yet approved for the RU
locale; re-verify against the English canon when building /ru/.
 
### Screen 1 — Hero
- H1: Финтех-ассоциация для тех, кто его строит
- Sub: Сообщество разработчиков, аналитиков и основателей финтех- и
  крипто-проектов. С 2017 года. Без членских взносов и бюрократии.
 
### Screen 2 — Stats
- Tagline: С 2017 года
- 1477 участников в чате · 7+ стран
 
### Screen 3 — How we work
- H2: Как устроена ассоциация
- Body:
  > Устав, подписанный в 2017 году, утверждает чётко: чтобы стать членом,
  > достаточно вступить в Telegram-чат.
  >
  > Чат — это и есть реестр. Переписка — это протокол. Голосования в
  > чате — это решения. Всё публично по умолчанию.
  >
  > Это не эксперимент, это работает восемь лет.
 
### Screen 4 — Who's in the chat
- H2: Кто в чате
- Body:
  > Разработчики банковских приложений из крупных банков. Основатели
  > финтех-стартапов. Эксперты по блокчейну. Аналитики, юристы, инвесторы,
  > владельцы инфраструктурных проектов.
  >
  > Через чат прошли найм разработчиков, поиск инвесторов и сделки по
  > заказной разработке.
 
### Screen 5 — What we do
- H2: Направления
- Four cards:
  1. **Аудит кода и экспертиза.** Эксперты ассоциации проводят аудит
     смарт-контрактов, блокчейн-проектов и финтех-продуктов. Отчёт — от
     имени ассоциации, публикуется открыто.
  2. **Исследования.** Флагман — проект UBI. Работали с Мировым банком,
     ЦБ РФ, университетами России и Эстонии.
  3. **Blockchain-валидаторы.** Держим ноды в сетях на Cosmos и Graphene.
     Через программу Relay принимаем делегации от уходящих валидаторов.
  4. **Инкубатор.** Для проектов с открытым кодом и свободными лицензиями.
     Только по приглашению — берём проекты от членов и экспертов.
 
### Screen 7 — President
- Tagline: Ассоциацией руководит
- Name: Aleksandr Kwaskoff (Александр Квасков — Russian spelling TBD with
  president; Kwaskoff is the established international transliteration)
- Role: президент
- Body: Собрал ассоциацию в 2017 году из Telegram-чата, который начал
  вести, работая в Рокетбанке. Эксперт по финтеху и крипте. Ведёт запросы
  на аудит: собирает ТЗ, подбирает экспертов, принимает работу.
 
### Screen 8 — Partnership
- H2: Организации — партнёры, а не члены
- Body: Членство — только для физлиц. Компании вступают как партнёры:
  совместные проекты, доступ к экспертизе, присутствие в сообществе.
 
### Screen 10 — Final CTA
- H2: Чтобы вступить — напишите в чат
- Body: Представьтесь и задайте первый вопрос. В чате вам ответят эксперты,
  которые строят финтех и крипту каждый день.
 
---
 
## 10b. Brand name convention
 
- **Logo (visual mark):** `FinTechAssociation` — one word, no space. Used
  in: header logo, favicon, social avatars. When rendered as a two-line
  stacked logo, visually separate as `FinTech` / `Association`.
- **Written name in all text:** `FinTech Association` — two words with a
  space. Used in: page copy, meta titles, SEO, alt texts, footer copyright,
  document names, email signatures, `<title>` template.
- **Domain, email:** `finteh.org`, `inbox@finteh.org`.
 
---
 
## 11. Open items / to be decided later
 
Resolved (as of current revision):
- ✅ President name — Aleksandr Kwaskoff
- ✅ Homepage numbers — 1,477 members and 7+ countries (other counters dropped)
- ✅ Incubator framing — "By invitation only", not "on pause"
- ✅ Validator name — "Blockchain Validators", not "Validation"
 
Still open:
- **President's photo** — professional, not a selfie.
- **Charter URL** — where does "Read full charter →" link to? Currently
  charter is a pinned message in the Telegram chat; needs a stable public
  URL (GitHub gist, Notion page, or page on finteh.org itself).
- **Last 3–4 audit reports** — covers + titles + dates for Screen 6.
- **Upcoming event vs. archive fallback** — decide per deploy.
- **Monetization of Validator Relay** — terms, commission %, supported
  networks list (for the standalone Validator Relay landing).
- **Partners list** — if and when to surface publicly.
- **Expert pool bios** — photos, role, expertise areas, contact.
- **Board member names and bios** — for the "Meet the board →" link target.
- **Russian locale of president's name** — Александр Квасков, Квасков vs
  Квасков with patronymic; to confirm with the president himself.
 
---
 
## 12. Working process with Claude Code
 
Do not attempt to build the whole site in one prompt. Work in stages:
 
1. **Project init** — fork AstroWind, strip demos, base deploy.
2. **Brand styling** — palette, fonts, style guide page.
3. **Homepage** — build the 10 screens per section 10 above.
4. **President page** — founder's personal landing.
5. **Validator Relay page** — external-outreach landing.
6. **Other pages** — as content is ready.
7. **i18n** — added last, when content is stable.
 
Before each stage: `git checkout -b feature/stage-name`.
After each stage: review locally, deploy to preview, approve, merge.
