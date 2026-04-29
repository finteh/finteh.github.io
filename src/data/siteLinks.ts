// Central registry of external and internal links referenced from homepage
// and landing pages. All entries are placeholders ("#") until the real URL
// is confirmed — update them here, not per-component. Final-URL intent is
// noted above each entry so the rollout owner knows where each should point.

export const siteLinks = {
  // Primary CTA — FinTech Association public Telegram chat.
  // Final: https://t.me/<handle> (confirm invite link with the president).
  joinTelegram: '#',

  // In-page anchor to Screen 3 on the homepage — keep as a hash.
  howWeWork: '#how-we-work',

  // "Read full charter" — currently a pinned message inside the Telegram
  // chat. Final: a stable public URL (GitHub gist, Notion page, or a page
  // on finteh.org itself — see context.md §11, open item).
  charter: '#',

  // "Meet the board" — About → Board of Directors.
  // Final: /about/board
  board: '#',

  // "Expert pool" — About → Expert Pool (public bios).
  // Final: /about/expert-pool
  expertPool: '#',

  // Audit request — Services → Audit (no public pricing, request form).
  // Final: /services/audit
  auditRequest: '#',

  // UBI / Social Fintech Research — flagship Programs entry.
  // Final: /programs/ubi
  ubiResearch: '#',

  // Validator Relay Program (also standalone outreach landing).
  // Final: /programs/validator-relay
  validatorRelay: '#',

  // Incubator page (by invitation only — no public submissions).
  // Final: /programs/incubator
  incubator: '#',

  // All reports — Reports & Publications → Audit Reports.
  // Final: /reports
  allReports: '#',

  // President's personal landing page (major asset per context.md §5).
  // Final: /about/president
  presidentBio: '#',

  // Direct contact with the president.
  // Final: mailto:president@finteh.org (or /contact/president).
  presidentContact: '#',

  // Partnership page — Join → For Organizations.
  // Final: /join/partnership
  partnership: '#',

  // Events archive — Events → Past.
  // Final: /events
  eventsArchive: '#',

  // General / press contact — Contact → General.
  // Final: /contact  (or mailto:inbox@finteh.org).
  pressContact: '#',
} as const;

export type SiteLinkKey = keyof typeof siteLinks;
