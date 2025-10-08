// Core JavaScript for Frames website
// Language: nl
// Auto-generated - do not edit directly

document.addEventListener('DOMContentLoaded', function () {
    // Inject JSON-LD schemas
    const schemaFiles = [
        '/lib/schema/nl/frames.json',
        '/lib/schema/nl/faq.json'
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

// YouTube facade - load iframe only when play button is clicked
document.addEventListener('click', function(e) {
    if (e.target.closest('.youtube-play-button')) {
        const player = document.getElementById('youtube-player');
        const videoId = player.dataset.videoId;

        // Create and inject iframe
        const iframe = document.createElement('iframe');
        iframe.src = `https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&mute=1&rel=0`;
        iframe.title = 'YouTube video player';
        iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
        iframe.allowFullscreen = true;
        iframe.referrerPolicy = 'no-referrer-when-downgrade';
        iframe.sandbox = 'allow-scripts allow-same-origin';
        iframe.style.position = 'absolute';
        iframe.style.top = '0';
        iframe.style.left = '0';
        iframe.style.width = '100%';
        iframe.style.height = '100%';

        // Remove facade and insert iframe
        player.innerHTML = '';
        player.appendChild(iframe);
    }
});

// Video overlay - remove iframe when closing to stop video
document.getElementById('video-toggle').addEventListener('change', function(e) {
    if (!e.target.checked) {
        const player = document.getElementById('youtube-player');
        const videoId = player.dataset.videoId;

        // Delay facade restoration until overlay animation completes (250ms transition + 50ms buffer)
        setTimeout(function() {
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

// Social sharing functionality
function shareOn(platform) {
    const url = encodeURIComponent(window.location.href);
    const title = encodeURIComponent(document.title);
    const text = encodeURIComponent('Frames is een analoge fotografie-app. Leg elke opname vast, volg instellingen, organiseer filmrolletjes en bewaar EXIF-metagegevens op iPhone & Mac.');

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