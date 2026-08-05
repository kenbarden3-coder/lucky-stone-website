const $ = (s, root = document) => root.querySelector(s);
const $$ = (s, root = document) => [...root.querySelectorAll(s)];

// Keep the durable Render build independently previewable while promoting internal
// navigation to clean Squarespace routes when the build is embedded there.
if (window.self !== window.top) {
  const parentOrigin = new URL(document.referrer || location.href).origin;
  const routeMap = {
    'garden-district.html': '/garden-district',
    'pitchers-point-beach-house.html': '/pitchers-point-beach-house',
    'capital-heights-hideaway.html': '/capital-heights-hideaway',
    'index.html': '/lucky-stone-redesign-private-staging'
  };
  $$('a[href]').forEach(link => {
    const url = new URL(link.getAttribute('href'), location.href);
    const file = url.pathname.split('/').pop();
    if (!routeMap[file]) return;
    link.href = `${parentOrigin}${routeMap[file]}${url.hash}`;
    link.target = '_top';
  });
}

$('[data-year]').textContent = new Date().getFullYear();

const menuButton = $('[data-menu-button]');
const mobileMenu = $('[data-mobile-menu]');
menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!open));
  mobileMenu.hidden = open;
  document.body.classList.toggle('menu-open', !open);
});
$$('.mobile-menu a').forEach(a => a.addEventListener('click', () => {
  menuButton?.setAttribute('aria-expanded', 'false');
  mobileMenu.hidden = true;
  document.body.classList.remove('menu-open');
}));

const header = $('[data-header]');
window.addEventListener('scroll', () => header?.classList.toggle('scrolled', scrollY > 40), {passive:true});

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('visible'); });
}, {threshold: .12});
$$('.reveal').forEach(el => observer.observe(el));

const moods = $$('.mood');
const cards = $$('.property-card');
moods.forEach(button => button.addEventListener('click', () => {
  moods.forEach(b => b.classList.remove('active'));
  button.classList.add('active');
  const filter = button.dataset.filter;
  cards.forEach(card => {
    const show = filter === 'all' || card.dataset.tags.includes(filter);
    card.classList.toggle('filtered-out', !show);
  });
}));

const today = new Date().toISOString().slice(0, 10);
$$('input[type="date"]').forEach(input => { input.min = today; });

function inquiryUrl(form, listingId = '') {
  const data = new FormData(form);
  const start = data.get('checkin');
  const end = data.get('checkout');
  const guestValue = String(data.get('guests') || '1');
  const numberOfGuests = guestValue.match(/\d+/)?.[0] || '1';
  if (start && end) {
    if (end <= start) throw new Error('Check-out must be after check-in.');
  }
  const place = data.get('place');
  const listingNames = {
    '113394': 'The Garden District House',
    '113397': 'Pitchers Point Beach House',
    '290981': 'The Capital Heights Hideaway'
  };
  const requestedHome = listingNames[listingId]
    || (place === 'baton-rouge' ? 'A Baton Rouge home'
      : place === 'long-beach' ? 'Pitchers Point Beach House'
      : 'Any Lucky Stone home');
  const subject = `Availability request: ${requestedHome}`;
  const body = [
    'Hi Lucky Stone,',
    '',
    `I would like to check availability for ${requestedHome}.`,
    `Check-in: ${start || 'Flexible'}`,
    `Check-out: ${end || 'Flexible'}`,
    `Guests: ${numberOfGuests}`,
    '',
    'Please send me availability and a direct quote.',
    '',
    'Name:',
    'Phone:'
  ].join('\n');
  return `mailto:luckystonelife@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}

$$('[data-stay-form], [data-property-booking-form]').forEach(form => {
  form.addEventListener('submit', e => {
    e.preventDefault();
    const error = $('[data-booking-error]', form);
    try {
      if (error) error.textContent = '';
      const listingId = form.dataset.listingId || '';
      window.location.href = inquiryUrl(form, listingId);
    } catch (err) {
      if (error) error.textContent = err.message;
    }
  });
});

const galleries = {
  garden: {kicker:'Baton Rouge · Garden District', title:'The Garden District House', count:10},
  beach: {kicker:'Long Beach · Mississippi Gulf Coast', title:'Pitchers Point Beach House', count:10},
  capital: {kicker:'Baton Rouge · Capital Heights', title:'The Capital Heights Hideaway', count:10}
};
const galleryModal = $('[data-gallery-modal]');
function openGallery(key) {
  const data = galleries[key];
  $('[data-modal-kicker]').textContent = data.kicker;
  $('[data-modal-title]').textContent = data.title;
  const grid = $('[data-modal-grid]');
  grid.innerHTML = '';
  for (let i=1; i<=data.count; i++) {
    const img = document.createElement('img');
    img.src = `assets/${key}/${key}-${String(i).padStart(2,'0')}.jpg`;
    img.alt = `${data.title} photo ${i}`;
    img.loading = 'lazy';
    grid.appendChild(img);
  }
  galleryModal.showModal();
  document.body.classList.add('modal-open');
}
$$('[data-gallery]').forEach(b => b.addEventListener('click', () => openGallery(b.dataset.gallery)));
$$('[data-details]').forEach(b => b.addEventListener('click', () => openGallery(b.dataset.details)));
$('[data-modal-close]')?.addEventListener('click', () => { galleryModal.close(); document.body.classList.remove('modal-open'); });
galleryModal?.addEventListener('click', e => { if (e.target === galleryModal) { galleryModal.close(); document.body.classList.remove('modal-open'); } });

const storyModal = $('[data-story-modal]');
$('[data-play-story]')?.addEventListener('click', () => storyModal.showModal());
$('[data-story-close]')?.addEventListener('click', () => storyModal.close());
storyModal?.addEventListener('click', e => { if (e.target === storyModal) storyModal.close(); });

const track = $('[data-review-track]');
$('[data-review-next]')?.addEventListener('click', () => track.scrollBy({left: track.clientWidth * .72, behavior:'smooth'}));
$('[data-review-prev]')?.addEventListener('click', () => track.scrollBy({left: -track.clientWidth * .72, behavior:'smooth'}));
