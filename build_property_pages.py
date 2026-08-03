from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent

PROPERTIES = [
    {
        "file": "garden-district.html",
        "key": "garden",
        "listing": "113394",
        "title": "The Garden District House",
        "seo": "Garden District Vacation Rental Near LSU | Lucky Stone",
        "description": "A family-friendly 3-bedroom Baton Rouge vacation rental near LSU, City Park, Government Street, and the St. Patrick's Day parade route.",
        "location": "Baton Rouge · Garden District",
        "badge": "Guest favorite · 5.0 ★",
        "lede": "A century-old charmer made for porch mornings, LSU weekends, and nights under the backyard trees.",
        "story": "Welcome to our Garden District home, a relaxed Baton Rouge base close to LSU, City Park, Government Street, and the neighborhood's best-known parade route. The house pairs historic character with practical family comforts, plenty of room to gather, and a fenced yard for slower evenings at home.",
        "stats": [("9", "guests"), ("3", "bedrooms"), ("2", "bathrooms")],
        "highlights": ["Two guest bikes", "Coffee bar", "Fenced backyard", "Full kitchen", "Washer and dryer", "Fast Wi-Fi", "Family-ready spaces", "Easy LSU access"],
        "nearby": ["Historic City Park and golf course", "Government Street restaurants", "LSU campus and stadiums", "Downtown Baton Rouge"],
        "quote": "Clean, comfortable, and thoughtfully decorated. The host was incredibly welcoming and responsive — I truly felt at home.",
        "reviewer": "Steven · verified guest",
    },
    {
        "file": "pitchers-point-beach-house.html",
        "key": "beach",
        "listing": "113397",
        "title": "Pitchers Point Beach House",
        "seo": "Long Beach Mississippi Vacation Rental Near the Gulf | Lucky Stone",
        "description": "A bright 3-bedroom Long Beach, Mississippi vacation rental for up to 10 guests, with beach gear and an easy walk to the Gulf.",
        "location": "Long Beach · Mississippi Gulf Coast",
        "badge": "Steps to the Gulf · 4.95 ★",
        "lede": "Bright, breezy, and built for barefoot family days—seven open lots from the Gulf.",
        "story": "Pitchers Point is our easygoing Gulf Coast home for family beach weeks, long weekends, and room to reconnect. The open living spaces keep everyone together while practical beach gear, generous parking, and an outdoor shower make the sand-to-supper transition simple.",
        "stats": [("10", "guests"), ("3", "bedrooms"), ("2", "bathrooms")],
        "highlights": ["Beach chairs and wagon", "Cooler and beach toys", "Outdoor shower", "Full kitchen", "Washer and dryer", "Fast Wi-Fi", "Roomy parking", "Family gathering spaces"],
        "nearby": ["Long Beach shoreline", "Pass Christian dining", "Gulfport attractions", "Mississippi Gulf Coast sunsets"],
        "quote": "The house was beautiful and felt like home. A short walk to the beach and close to everything we needed.",
        "reviewer": "Mallory · verified guest",
    },
    {
        "file": "capital-heights-hideaway.html",
        "key": "capital",
        "listing": "290981",
        "title": "The Capital Heights Hideaway",
        "seo": "Capital Heights Baton Rouge Vacation Rental | Lucky Stone",
        "description": "A renovated 2-bedroom Capital Heights vacation rental in Baton Rouge with two king beds, modern kitchen, and easy city access.",
        "location": "Baton Rouge · Capital Heights",
        "badge": "Freshly renovated · 4.85 ★",
        "lede": "Polished comfort in the middle of the city, with neighborhood restaurants and everyday essentials close by.",
        "story": "The Capital Heights Hideaway delivers an efficient, comfortable Baton Rouge stay without giving up style. Two king bedrooms, a modern kitchen, a spa-like shower, and a large living-room TV make it an easy choice for couples, small families, visiting professionals, and city weekends.",
        "stats": [("6", "guests"), ("2", "bedrooms"), ("1", "bathroom")],
        "highlights": ["Two king beds", "Spa-like shower", "70-inch living-room TV", "Four TVs total", "Modern kitchen", "Washer and dryer", "Fast Wi-Fi", "Central Baton Rouge location"],
        "nearby": ["Capital Heights neighborhood", "Mid City restaurants", "LSU and downtown", "Everyday shopping and essentials"],
        "quote": "A clean, beautifully renovated home in a convenient location, with quick answers whenever we needed anything.",
        "reviewer": "Lucky Stone guest",
    },
]


def stat_markup(items):
    return "".join(f'<li><strong>{escape(value)}</strong>{escape(label)}</li>' for value, label in items)


def list_markup(items):
    return "".join(f"<li>{escape(item)}</li>" for item in items)


def photo_markup(p):
    return "".join(
        f'<figure><img src="assets/{p["key"]}/{p["key"]}-{i:02d}.jpg" alt="{escape(p["title"])} photo {i}" loading="lazy"></figure>'
        for i in range(1, 11)
    )


def page(p):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="{escape(p['description'])}">
  <meta name="theme-color" content="#0b2b40">
  <title>{escape(p['seo'])}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="property-page">
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="announcement"><span>Book direct for local support & our best available rate</span><span aria-hidden="true">✦</span><span>Secure checkout powered by Hostaway</span></div>
  <header class="site-header property-header" data-header>
    <a class="brand" href="index.html" aria-label="Lucky Stone Vacation Rentals home"><span class="brand-mark" aria-hidden="true">L</span><span><strong>Lucky Stone</strong><small>Vacation Rentals</small></span></a>
    <nav class="desktop-nav" aria-label="Main navigation"><a href="index.html#stays">Our stays</a><a href="#details">Details</a><a href="#gallery">Photos</a><a href="index.html#our-story">Our story</a></nav>
    <a class="button button-small button-sun" href="#book">Check dates <span>↓</span></a>
    <button class="menu-button" type="button" aria-label="Open menu" aria-expanded="false" data-menu-button><span></span><span></span></button>
  </header>
  <div class="mobile-menu" data-mobile-menu hidden><a href="index.html#stays">Our stays</a><a href="#details">Details</a><a href="#gallery">Photos</a><a href="index.html#our-story">Our story</a><a class="button button-sun" href="#book">Check dates</a></div>

  <main id="main">
    <section class="property-hero" id="top">
      <img src="assets/{p['key']}/{p['key']}-01.jpg" alt="{escape(p['title'])}">
      <div class="property-hero-shade"></div>
      <div class="property-hero-copy reveal"><p class="eyebrow">{escape(p['location'])}</p><h1>{escape(p['title'])}</h1><p>{escape(p['lede'])}</p><div class="property-hero-actions"><a class="button button-coral" href="#book">See live availability</a><a class="text-button" href="#gallery">View photos ↓</a></div></div>
      <div class="image-badge property-hero-badge">{escape(p['badge'])}</div>
    </section>

    <section class="property-intro section-pad" id="details">
      <div><p class="eyebrow dark">Your Lucky Stone stay</p><h2>A real home base—not a faceless rental.</h2><p>{escape(p['story'])}</p></div>
      <ul class="property-big-stats">{stat_markup(p['stats'])}</ul>
    </section>

    <section class="property-booking" id="book">
      <div class="property-booking-copy"><p class="eyebrow">Ready when you are</p><h2>Check this home's live dates.</h2><p>Your availability, quote, secure payment, confirmation, and automated stay messages continue in Lucky Stone's Hostaway booking system.</p></div>
      <form class="property-booking-form" data-property-booking-form data-listing-id="{p['listing']}">
        <label><span>Check in</span><input type="date" name="checkin" required></label>
        <label><span>Check out</span><input type="date" name="checkout" required></label>
        <label><span>Guests</span><select name="guests">{''.join(f'<option>{i} guest{"s" if i != 1 else ""}</option>' for i in range(1, int(p['stats'][0][0]) + 1))}</select></label>
        <button class="button button-sun" type="submit">View live price & availability ↗</button>
        <p class="booking-error" data-booking-error aria-live="polite"></p>
        <small>No charge is made on this page.</small>
      </form>
    </section>

    <section class="property-features section-pad">
      <div><p class="eyebrow dark">At the house</p><h2>The details that make the stay easier.</h2><ul class="feature-checks">{list_markup(p['highlights'])}</ul></div>
      <div class="nearby-card"><p class="eyebrow">Close to what matters</p><h3>Explore the neighborhood.</h3><ul>{list_markup(p['nearby'])}</ul><p>Exact address and arrival instructions are shared securely with confirmed guests.</p></div>
    </section>

    <section class="property-gallery section-pad" id="gallery"><div class="section-heading"><div><p class="eyebrow dark">A look inside</p><h2>Photo highlights.</h2></div><p>Professional property photography. The full gallery and current listing details are also available in the secure booking portal.</p></div><div class="property-photo-grid">{photo_markup(p)}</div></section>

    <section class="property-review"><blockquote><div class="stars">★★★★★</div><p>“{escape(p['quote'])}”</p><footer>{escape(p['reviewer'])}</footer></blockquote></section>

    <section class="final-cta"><p class="eyebrow">Live availability · Secure checkout · Direct local support</p><h2>Put this Lucky Stone stay<br>on your calendar.</h2><a class="button button-coral" href="#book">Check dates and pricing ↑</a><small>Booking and payment are securely powered by Hostaway.</small></section>
  </main>

  <footer class="footer"><a class="brand footer-brand" href="index.html"><span class="brand-mark">L</span><span><strong>Lucky Stone</strong><small>Vacation Rentals</small></span></a><div><strong>Explore</strong><a href="index.html#stays">Our stays</a><a href="index.html#our-story">Our story</a><a href="index.html#guide">Local guide</a></div><div><strong>Stay in touch</strong><a href="https://instagram.com/luckystonelife/" target="_blank" rel="noopener">Instagram ↗</a><a href="mailto:luckystonelife@gmail.com">luckystonelife@gmail.com</a></div><div><strong>Book safely</strong><a href="https://luckystonevacationrentals.holidayfuture.com/listings/{p['listing']}" target="_blank" rel="noopener">Secure property listing ↗</a><span>Availability powered by Hostaway</span></div><p class="copyright">© <span data-year></span> Lucky Stone Vacation Rentals. Made with a little luck in Louisiana.</p></footer>
  <script src="app.js"></script>
</body>
</html>
'''


for property_data in PROPERTIES:
    output = ROOT / property_data["file"]
    output.write_text(page(property_data), encoding="utf-8")
    print(output)
