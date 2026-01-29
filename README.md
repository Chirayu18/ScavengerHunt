# A Journey Through Us 💕

A romantic scavenger hunt web app for Chavi (Weewee).

## Quick Start

### Option 1: Python HTTPS Server (Recommended for GPS testing)

```bash
cd scavenger-hunt
python server.py
```

Then open **https://localhost:8443** in your browser.

> ⚠️ You'll see a security warning because of the self-signed certificate. Click "Advanced" → "Proceed to localhost" to continue.

### Option 2: Simple HTTP Server (GPS may not work)

```bash
cd scavenger-hunt
python -m http.server 8000
```

Then open **http://localhost:8000**

> Note: The Geolocation API requires HTTPS on most browsers, so GPS tracking may not work with HTTP.

### Option 3: VS Code Live Server

If you have the Live Server extension, just right-click `index.html` and select "Open with Live Server".

## Testing on Phone

1. Make sure your phone and computer are on the same WiFi network
2. Find your computer's local IP address:
   - Windows: `ipconfig`
   - Mac/Linux: `ifconfig` or `ip addr`
3. Open `https://YOUR_IP:8443` on your phone
4. Accept the certificate warning

## The Journey

| # | Location | Memory |
|---|----------|--------|
| 1 | Park in Jette | Night skies & drunk snowman ⛄ |
| 2 | Mykonos Pitta Gyros | Greek street food 🥙 |
| 3 | Café Léopold Royal | First date ☕ |
| 4 | Triumphal Arch | Cinquantenaire 🏛️ |
| 5 | Docks Bruxsel | Second date dinner 🍽️ |
| 6 | Sunset Spot | Promise ring 💍 |

## 🔐 Skip Codes (Secret!)

If GPS isn't working or you need to skip to a specific location, **tap the "Location #" text 3 times** to reveal a secret code input.

| Location | Skip Code |
|----------|-----------|
| 1 - Park in Jette | `SNOWMAN23` |
| 2 - Mykonos Pitta Gyros | `GYROS4EVR` |
| 3 - Café Léopold Royal | `FIRSTDATE` |
| 4 - Triumphal Arch | `GOLDEN50` |
| 5 - Docks Bruxsel | `DOCKS2ND` |
| 6 - Sunset Spot | `SUNSET4US` |

**How to use:**
1. On the hunt screen, tap "Location #" three times quickly
2. A code input field will appear
3. Enter the code for the current location (or any location to jump to it)
4. Press the checkmark button or hit Enter

> 💡 **Tip:** You can write these codes on the physical envelopes as a backup in case GPS has issues!

## Files

```
scavenger-hunt/
├── index.html      # Main HTML structure
├── styles.css      # Pinkish romantic theme
├── app.js          # GPS tracking & app logic
├── server.py       # HTTPS server for testing
├── cert.pem        # SSL certificate
├── key.pem         # SSL private key
└── README.md       # This file
```

## GPS Radius Settings

Each location has a different GPS radius (in meters):
- Park in Jette: 100m (big park)
- Mykonos: 80m
- Café Léopold: 80m
- Triumphal Arch: 90m
- Docks Bruxsel: 100m
- Sunset Spot: 80m

## Customization

To adjust locations or clues, edit the `locations` array in `app.js`.

To change skip codes, edit the `skipCodes` object at the top of `app.js`.

---

Made with ♥ for Chavi
