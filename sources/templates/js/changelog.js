// Changelog JavaScript for Frames website
// Language: {{ lang }}
// Auto-generated - do not edit directly

document.addEventListener('DOMContentLoaded', function () {
    // Determine the base schema path based on current URL
    const path = window.location.pathname;
    const lang = '{{ lang }}';

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
            '/lib/schema/' + lang + '/organization.json',
            schemaBasePath + '/blogposting.json',
            schemaBasePath + '/breadcrumb.json'
        ];
    } else if (isIndexPage) {
        // Check if we're on a paginated page
        const pageMatch = path.match(/\/changelog\/page-(\d+)\/?$/);
        if (pageMatch) {
            schemaBasePath += '/page-' + pageMatch[1];
        }

        schemaFiles = [
            '/lib/schema/' + lang + '/organization.json',
            schemaBasePath + '/breadcrumb.json'
        ];

        // Blog schema only on first page
        if (!pageMatch) {
            schemaFiles.splice(1, 0, schemaBasePath + '/blog.json');
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