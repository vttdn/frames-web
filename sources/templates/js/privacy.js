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


// Dropdowns (e.g. footer language picker)
// Each .dropdown is a checkbox-driven menu. Close an open one when an
// interaction lands outside of it, and on Escape. We listen for both
// pointerdown and touchstart: on iOS Safari, pointer and click events are not
// dispatched to document-level listeners for taps on non-interactive elements
// (plain background), but touch events are, so touchstart is what actually
// closes the menu on a mobile tap.
const dropdowns = Array.from(document.querySelectorAll('.dropdown'));

if (dropdowns.length) {
  function closeDropdownsOutside(e) {
    dropdowns.forEach(dropdown => {
      const toggle = dropdown.querySelector('.dropdown-toggle');
      if (toggle && toggle.checked && !dropdown.contains(e.target)) {
        toggle.checked = false;
      }
    });
  }

  document.addEventListener('pointerdown', closeDropdownsOutside);
  document.addEventListener('touchstart', closeDropdownsOutside, { passive: true });

  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    dropdowns.forEach(dropdown => {
      const toggle = dropdown.querySelector('.dropdown-toggle');
      if (toggle && toggle.checked) {
        toggle.checked = false;
      }
    });
  });
}