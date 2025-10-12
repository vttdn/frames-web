// Core JavaScript for Frames website
// Language: sv
// Auto-generated - do not edit directly

document.addEventListener('DOMContentLoaded', function () {
    // Inject JSON-LD schemas
    const schemaFiles = [
        '/lib/schema/sv/frames.json',
        '/lib/schema/sv/faq.json',
        '/lib/schema/sv/organization.json',
        '/lib/schema/sv/webpage-homepage.json'
    ];

    schemaFiles.forEach((url) => {
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Failed to fetch ${url}: ${response.status}`);
                }
                return response.json();
            })
            .then(jsonData => {
                const script = document.createElement('script');
                script.type = 'application/ld+json';
                script.textContent = JSON.stringify(jsonData);
                document.head.appendChild(script);
            })
            .catch(error => {
                console.error('Error injecting JSON-LD:', error);
            });
    });
});

// Toggle for pricing plans
function initPlanToggle() {
  const toggle = document.querySelector('.plans-toggle');
  if (!toggle) return;
  
  const monthlyLabel = toggle.querySelector('[for="monthly"]');
  const yearlyLabel = toggle.querySelector('[for="yearly"]');
  const pricingPlans = document.getElementById('pricing-plans');
  
  // Wait for the dynamic content to be populated
  function calculateWidths() {
    // Reset any previous styles
    toggle.style.removeProperty('--monthly-width');
    toggle.style.removeProperty('--yearly-width');
    
    // Check if labels have actual content
    const monthlyText = monthlyLabel.textContent.trim();
    const yearlyText = yearlyLabel.textContent.trim();
    
    console.log('Monthly text:', monthlyText, 'Width:', monthlyLabel.scrollWidth);
    console.log('Yearly text:', yearlyText, 'Width:', yearlyLabel.scrollWidth);
    
    // Only calculate if labels have content (not empty or placeholders)
    if (monthlyText && yearlyText && monthlyText !== 'label_period' && yearlyText !== 'label_period_yearly') {
      const monthlyWidth = monthlyLabel.scrollWidth + 'px';
      const yearlyWidth = yearlyLabel.scrollWidth + 'px';
      
      toggle.style.setProperty('--monthly-width', monthlyWidth);
      toggle.style.setProperty('--yearly-width', yearlyWidth);
      
      console.log('Widths set:', monthlyWidth, yearlyWidth);
    } else {
      // Retry if content isn't ready yet
      console.log('Labels not populated yet, retrying...');
      setTimeout(calculateWidths, 50);
    }
  }
  
  // Handle pricing plans class toggle
  if (pricingPlans) {
    toggle.addEventListener('change', function(e) {
      if (e.target.type === 'radio') {
        pricingPlans.classList.toggle('yearly', e.target.id === 'yearly');
      }
    });
    
    // Set initial state
    const yearlyRadio = document.getElementById('yearly');
    pricingPlans.classList.toggle('yearly', yearlyRadio && yearlyRadio.checked);
  }
  
  // Start the calculation process with a longer delay
  setTimeout(calculateWidths, 100);
}

// Wait longer for template rendering
document.addEventListener('DOMContentLoaded', function() {
  setTimeout(initPlanToggle, 300);
});

// Fallback
window.addEventListener('load', function() {
  setTimeout(initPlanToggle, 200);
});

//
// Share Overlay — open/close modal with ARIA + scroll lock
//

document.addEventListener('DOMContentLoaded', () => {
  const overlay = document.getElementById('overlay-social-share');
  const openBtn = document.getElementById('button-social-share');
  const closeBtn = document.getElementById('button-social-share-close');
  const body = document.body;

  if (!overlay || !openBtn || !closeBtn) return;

  openBtn.addEventListener('click', () => {
    overlay.classList.add('show');
    body.classList.add('body-no-scroll');

    // ARIA
    openBtn.setAttribute('aria-expanded', 'true');
    overlay.setAttribute('aria-hidden', 'false');
  });

  const closeOverlay = () => {
    overlay.classList.remove('show');
    body.classList.remove('body-no-scroll');

    // ARIA
    openBtn.setAttribute('aria-expanded', 'false');
    overlay.setAttribute('aria-hidden', 'true');
  };

  closeBtn.addEventListener('click', closeOverlay);

  // Close when clicking backdrop
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) closeOverlay();
  });
});


//
// YouTube overlay — lazy-load iframe only when the play button is clicked
//
document.addEventListener('DOMContentLoaded', () => {
  const overlay   = document.getElementById('youtube-overlay');
  const player    = document.getElementById('youtube-player');
  const closeBtn  = document.getElementById('button-youtube-close');
  const playBtn   = document.getElementById('youtube-video-toggle');

  if (!overlay || !player || !playBtn || !closeBtn) return;

  // --- Open video ---
  playBtn.addEventListener('click', () => {
    const videoId = player.dataset.videoId;
    if (!videoId) return;

    // Create iframe
    const iframe = document.createElement('iframe');
    iframe.src = `https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&mute=1&rel=0&modestbranding=1`;
    iframe.title = 'YouTube video player';
    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen';
    iframe.referrerPolicy = 'no-referrer-when-downgrade';
    iframe.style.cssText = `
      position:absolute;
      inset:0;
      width:100%;
      height:100%;
      border:0;
    `;

    // Replace placeholder with iframe
    player.innerHTML = '';
    player.appendChild(iframe);

    // Show overlay
    overlay.classList.add('show');
    document.body.classList.add('body-no-scroll');

    // ARIA
    playBtn.setAttribute('aria-expanded', 'true');
    overlay.setAttribute('aria-hidden', 'false');
  });

  // --- Close video (button) ---
  closeBtn.addEventListener('click', closeYoutubeOverlay);

  // --- Close video (click outside modal) ---
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) closeYoutubeOverlay();
  });

  // --- Shared close logic ---
  function closeYoutubeOverlay() {
    overlay.classList.remove('show');
    document.body.classList.remove('body-no-scroll');

    // Remove iframe after fade-out transition
    setTimeout(() => { player.innerHTML = ''; }, 300);

    // ARIA
    playBtn.setAttribute('aria-expanded', 'false');
    overlay.setAttribute('aria-hidden', 'true');
  }
});


//
// Social sharing functionality
//
function shareOn(platform) {
    const url = encodeURIComponent(window.location.href);
    const title = encodeURIComponent(document.title);
    const text = encodeURIComponent("Frames är en filmfotografiapp för analogfotografer. Logga varje bild, spåra kamerainställningar, organisera rullar och spara EXIF-metadata på iPhone & Mac.");

    let shareUrl = '';

    switch(platform) {
        case 'facebook':
            shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
            break;
        case 'twitter':
            shareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${text}`;
            break;
        case 'linkedin':
            shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${url}`;
            break;
        case 'whatsapp':
            shareUrl = `https://wa.me/?text=${text}%20${url}`;
            break;
        case 'reddit':
            shareUrl = `https://reddit.com/submit?url=${url}&title=${title}`;
            break;
        case 'email':
            shareUrl = `mailto:?subject=${title}&body=${text}%20${url}`;
            break;
    }

    if (shareUrl) {
        window.open(shareUrl, '_blank', 'width=600,height=400');
    }
}