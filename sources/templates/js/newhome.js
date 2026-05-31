// Content reveal on scroll
const elements = Array.from(document.querySelectorAll('.animated'));
const staggerScroll = 60;

let colMap = new Map();

function getColumnIndexes() {
  colMap.clear();

  const rows = [];

  elements.forEach(el => {
    const rect = el.getBoundingClientRect();
    const absTop = rect.top + window.scrollY;
    const left = rect.left;

    let row = rows.find(r => Math.abs(r.absTop - absTop) < 10);
    if (!row) {
      row = { absTop, items: [] };
      rows.push(row);
    }
    row.items.push({ el, left });
  });

  rows.forEach(row => {
    row.items.sort((a, b) => a.left - b.left);
    const cols = [];
    row.items.forEach(({ el, left }) => {
      let colIndex = cols.findIndex(c => Math.abs(c - left) < 10);
      if (colIndex === -1) {
        cols.push(left);
        colIndex = cols.length - 1;
      }
      colMap.set(el, colIndex);
    });
  });
}

function update() {
  const vh = window.innerHeight;

  elements.forEach(el => {
    const rect = el.getBoundingClientRect();
    const colIndex = colMap.get(el) || 0;

    const startOffset = colIndex * staggerScroll;

    const start = vh - startOffset + 30;
    const end = start - 300;

    let progress = (start - rect.top) / (start - end);
    progress = Math.max(0, Math.min(1, progress));

    const eased = Math.sin((progress * Math.PI) / 2);

    el.style.transform = `translate3d(0, ${(1 - eased) * 40}px, 0)`;
    el.style.opacity = eased;
  });

  requestAnimationFrame(update);
}

getColumnIndexes();
window.addEventListener('resize', getColumnIndexes);

update();


// Top toolbar
// Becomes "prominent" once the hero has scrolled out of view.
// We use a sentinel + IntersectionObserver instead of comparing
// window.scrollY against the hero height: the hero is position:fixed at
// height:100vh, and on iOS Safari 100vh tracks the *large* viewport and
// resizes as the address bar shows/hides, so the scrollY threshold was
// never reliably crossed there and the header never changed on scroll.
  const toolbar = document.querySelector('.top-toolbar');
  const hero = document.querySelector('.hero');

  const heroSentinel = document.createElement('div');
  heroSentinel.setAttribute('aria-hidden', 'true');
  heroSentinel.style.cssText = 'position:absolute;top:0;left:0;width:1px;pointer-events:none;';

  function sizeSentinel() {
    heroSentinel.style.height = hero.offsetHeight + 'px';
  }

  sizeSentinel();
  document.body.prepend(heroSentinel);

  new IntersectionObserver(([entry]) => {
    toolbar.classList.toggle('prominent', !entry.isIntersecting);
  }, { threshold: 0 }).observe(heroSentinel);

  window.addEventListener('resize', sizeSentinel);


// Video playback

// Hero video: fixed behind main, pause when .about reaches top of viewport
const heroVideo = document.querySelector('.hero video');
const aboutSection = document.querySelector('.about');

function updateHeroVideo() {
  if (aboutSection.getBoundingClientRect().top <= 0) {
    heroVideo.pause();
  } else if (heroVideo.paused) {
    heroVideo.play();
  }
}

window.addEventListener('scroll', updateHeroVideo, { passive: true });
updateHeroVideo();

// Feature videos: play when entering viewport, pause when fully gone
const featureVideos = document.querySelectorAll('main video');

const videoObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.play();
    } else {
      entry.target.pause();
    }
  });
}, { threshold: 0 });

featureVideos.forEach(video => videoObserver.observe(video));


// Audio
const button = document.getElementById('musicToggle');
const audio = document.getElementById('music');

let isPlaying = false;

button.addEventListener('click', async () => {
  if (!isPlaying) {
    try {
      await audio.play();
      isPlaying = true;
      button.setAttribute('aria-pressed', 'true');
    } catch (e) {
      console.log('Playback failed:', e);
    }
  } else {
    audio.pause();
    isPlaying = false;
    button.setAttribute('aria-pressed', 'false');
  }
});