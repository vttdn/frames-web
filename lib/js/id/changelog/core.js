// Changelog JavaScript for Frames website
// Language: id
// Auto-generated - do not edit directly

document.addEventListener('DOMContentLoaded', function () {
    // Determine the base schema path based on current URL
    const path = window.location.pathname;
    const lang = 'id';

    // Build schema path dynamically
    let schemaBasePath = '/lib/schema/' + lang + '/changelog';

    // Detect if we're on an entry page or index page
    const isIndexPage = path.match(/\/changelog\/?$/) || path.match(/\/changelog\/page-\d+\/?$/);
    const isEntryPage = !isIndexPage && path.match(/\/changelog\/[^/]+\/?$/);

    let schemaFiles = [];

    if (isEntryPage) {
        // Extract the entry slug from the URL
        const slug = path.match(/\/changelog\/([^/]+)\/?$/)[1];
        schemaBasePath += '/' + slug;
        schemaFiles = [
            schemaBasePath + '/blogposting.json',
            schemaBasePath + '/breadcrumb.json',
            schemaBasePath + '/organization.json'
        ];
    } else if (isIndexPage) {
        // Check if we're on a paginated page
        const pageMatch = path.match(/\/changelog\/page-(\d+)\/?$/);
        if (pageMatch) {
            schemaBasePath += '/page-' + pageMatch[1];
        }

        schemaFiles = [
            schemaBasePath + '/breadcrumb.json',
            schemaBasePath + '/organization.json'
        ];

        // Blog schema only on first page
        if (!pageMatch) {
            schemaFiles.unshift(schemaBasePath + '/blog.json');
        }
    }

    // Inject all schema files
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

    // Get description from meta tag (works for both index and entry pages)
    const metaDescription = document.querySelector('meta[name="description"]');
    const text = encodeURIComponent(metaDescription ? metaDescription.getAttribute('content') : "Log perubahan untuk Frames, fitur terbaru dan peningkatan untuk aplikasi fotografi film Frames.");

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