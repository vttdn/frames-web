// Core JavaScript for Frames website
// Language: ja
// Auto-generated - do not edit directly

document.addEventListener('DOMContentLoaded', function () {
    // Inject JSON-LD schemas
    const schemaFiles = [
        '/lib/schema/ja/frames.json',
        '/lib/schema/ja/faq.json'
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
document.getElementById('youtube-video-toggle').addEventListener('click', function() {
        const overlay = document.getElementById('youtube-overlay');
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

        // Show overlay
        overlay.classList.add('show');

        // Prevent background scrolling
        document.body.classList.add('body-no-scroll');
});

// Video overlay - remove iframe when closing to stop video
document.getElementById('youtube-overlay-close').addEventListener('click', function() {
        const overlay = document.getElementById('youtube-overlay');
        const player = document.getElementById('youtube-player');

        // Removes player
        setTimeout(function() {
            player.innerHTML = '';
        }, 300);

        // Show overlay
        overlay.classList.remove('show');

        // Release body scrolling
        document.body.classList.remove('body-no-scroll');
});

// Social sharing functionality
function shareOn(platform) {
    const url = encodeURIComponent(window.location.href);
    const title = encodeURIComponent(document.title);
    const text = encodeURIComponent('Framesはフィルム写真アプリです。すべてのショットを記録し、カメラ設定を管理、ロールを整理、iPhoneとMacでEXIFメタデータを保存できます。');

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