// Privacy page JavaScript for Frames website
// Language: ja
// Auto-generated - do not edit directly

document.addEventListener('DOMContentLoaded', function () {
    // Inject JSON-LD schemas
    const schemaFiles = [
        '/lib/schema/ja/organization.json',
        '/lib/schema/ja/webpage-privacy.json'
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

// Share Overlay
const shareOverlay = document.getElementById('overlay-social-share');
const body = document.body;
const shareButton = document.getElementById('button-social-share');

document.addEventListener('click', (e) => {
  // Open overlay
  if (e.target.closest('#button-social-share')) {
    shareOverlay.classList.add('show');
    body.classList.add('body-no-scroll');

    // ARIA updates
    shareButton.setAttribute('aria-expanded', 'true');
    shareOverlay.setAttribute('aria-hidden', 'false');
  }

  // Close overlay (either clicking close button or backdrop)
  if (
    e.target.closest('#button-social-share-close') ||
    e.target === shareOverlay
  ) {
    shareOverlay.classList.remove('show');
    body.classList.remove('body-no-scroll');

    // ARIA updates
    shareButton.setAttribute('aria-expanded', 'false');
    shareOverlay.setAttribute('aria-hidden', 'true');
  }
});

// Social sharing functionality
function shareOn(platform) {
    const url = encodeURIComponent(window.location.href);
    const title = encodeURIComponent(document.title);
    const metaDescription = document.querySelector('meta[name="description"]');
    const text = encodeURIComponent(metaDescription ? metaDescription.getAttribute('content') : "");

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