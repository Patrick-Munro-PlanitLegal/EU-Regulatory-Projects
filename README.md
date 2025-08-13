# EU Tech Regulations Tracker

Professional compliance dashboard for EU technology regulations and German implementation. Static single-page app ready for GitHub Pages.

## Quick start

- Open `index.html` in a browser.
- Optional offline capability via `sw.js` (auto-registered on load).

## Deploy on GitHub Pages

1. Push this repository to GitHub.
2. In the repository settings, enable Pages:
   - Source: `main` branch, root.
3. Ensure the site root contains `index.html` and `sw.js`.
4. Your app will be available at the Pages URL.

Notes:
- For user/org pages (username.github.io), the service worker scope `/sw.js` works as-is.
- For project pages (username.github.io/repo), either update the registration path in `index.html` to `navigator.serviceWorker.register('./sw.js')` or set a `base` tag.

## Data

- Data and dates are hardcoded inside `index.html` (`regulationsData`).
- Update `lastUpdated` and timeline items as needed.

## Export formats

- JSON: Complete database
- CSV: Compliance matrix (properly escapes quotes)
- TXT: Executive summary

## Accessibility and UX

- Keyboard shortcuts: Ctrl/Cmd+F focuses search, Esc closes modals
- ARIA roles and `rel="noopener noreferrer"` applied where appropriate

## License

- Code: MIT
- Content: © respective rights holders; EU legal texts are public domain. This tool is for educational purposes only and not legal advice.
