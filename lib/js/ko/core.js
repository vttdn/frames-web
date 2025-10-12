// Core JavaScript for Frames website
// Language: ko
// Auto-generated - do not edit directly

document.addEventListener('DOMContentLoaded', function () {
    // Inject JSON-LD schemas
    const schemaFiles = [
        '/lib/schema/ko/frames.json',
        '/lib/schema/ko/faq.json',
        '/lib/schema/ko/organization.json',
        '/lib/schema/ko/webpage-homepage.json'
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
// --- Video toggle (stop video) ---
const videoToggle = document.getElementById('video-toggle');
if (videoToggle) {
    videoToggle.addEventListener('change', function(e) {
        if (!e.target.checked) {
            const player = document.getElementById('youtube-player');
            if (!player) return;

            // Delay facade restoration until overlay animation completes
            setTimeout(() => {
                player.innerHTML = `
                    <div class="youtube-facade">
                        <img src="/lib/img/shared/video-thumbnail.webp"
                             srcset="/lib/img/shared/video-thumbnail.webp 1x, /lib/img/shared/video-thumbnail@2x.webp 2x"
                             alt="YouTube video thumbnail"
                             width="1280"
                             height="720"
                             loading="lazy">
                        <button class="youtube-play-button" aria-label="Play video">
                            <svg width="68" height="48" viewBox="0 0 68 48" fill="none">
                                <path d="M66.52 7.74c-.78-2.93-2.49-5.41-5.42-6.19C55.79.13 34 0 34 0S12.21.13 6.9 1.55c-2.93.78-4.63 3.26-5.42 6.19C.06 13.05 0 24 0 24s.06 10.95 1.48 16.26c.78 2.93 2.49 5.41 5.42 6.19C12.21 47.87 34 48 34 48s21.79-.13 27.1-1.55c2.93-.78 4.64-3.26 5.42-6.19C67.94 34.95 68 24 68 24s-.06-10.95-1.48-16.26z" fill="red"/>
                                <path d="M45 24L27 14v20l18-10z" fill="#fff"/>
                            </svg>
                        </button>
                    </div>
                `;
            }, 300);
        }
    });
}

// --- YouTube overlay — lazy-load iframe only when the play button is clicked ---
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

        player.innerHTML = '';
        player.appendChild(iframe);

        overlay.classList.add('show');
        document.body.classList.add('body-no-scroll');

        playBtn.setAttribute('aria-expanded', 'true');
        overlay.setAttribute('aria-hidden', 'false');
    });

    // --- Close video ---
    closeBtn.addEventListener('click', closeYoutubeOverlay);
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) closeYoutubeOverlay();
    });

    function closeYoutubeOverlay() {
        overlay.classList.remove('show');
        document.body.classList.remove('body-no-scroll');
        setTimeout(() => { player.innerHTML = ''; }, 300);
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
    const text = encodeURIComponent("Frames는 필름 사진 앱입니다. 모든 촬영을 기록하고, 카메라 설정을 추적하며, 롤을 정리하고, iPhone과 Mac에서 EXIF 메타데이터를 저장하세요.");

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