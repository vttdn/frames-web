// Privacy page JavaScript for Frames website
// Language: {{ lang }}
// Auto-generated - do not edit directly

// Twitter sharing configuration
const TWITTER_HANDLE = "{{ locale_data.social.twitter if locale_data.social is defined and locale_data.social.twitter else global_config.urls.social.handle.twitter }}";
const VIA_TEXT = "{{ locale_data.share_dropdown.via }}";

document.addEventListener('DOMContentLoaded', function () {
    // Inject JSON-LD schemas
    const schemaFiles = [
        '/lib/schema/{{ lang }}/organization.json',
        '/lib/schema/{{ lang }}/breadcrumb-privacy.json',
        '/lib/schema/{{ lang }}/webpage-privacy.json'
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

//
// Top toolbar
//
    const toolbar = document.querySelector('.top-toolbar');

    function handleScroll() {
      if (window.scrollY > 0) {
        toolbar.classList.add('prominent');
      } else {
        toolbar.classList.remove('prominent');
      }
    }

    handleScroll();
    // Events
    window.addEventListener('scroll', handleScroll);