// Blog JavaScript for Frames website
// Language: {{ lang }}
// Auto-generated - do not edit directly

document.addEventListener('DOMContentLoaded', function () {
    // Determine the base schema path based on current URL
    const path = window.location.pathname;
    const lang = '{{ lang }}';

    // Build schema path dynamically
    let schemaBasePath = '/lib/schema/' + lang + '/blog';

    // Detect page type from URL
    const isIndexPage = path.match(/\/blog\/?$/) || path.match(/\/blog\/page\/\d+\/?$/);
    const isEntryPage = !isIndexPage && path.match(/\/blog\/[^/]+\/?$/) && !path.includes('/topic/');
    const isCategoryPage = path.match(/\/blog\/topic\/[^/]+(?:\/page\/\d+)?\/?$/);

    let schemaFiles = [];

    if (isEntryPage) {
        // Extract the entry slug from the URL
        const slug = path.match(/\/blog\/([^/]+)\/?$/)[1];
        schemaBasePath += '/' + slug;
        schemaFiles = [
            '/lib/schema/' + lang + '/organization.json',
            schemaBasePath + '/blogposting.json',
            schemaBasePath + '/breadcrumb-blog.json'
        ];
    } else if (isCategoryPage) {
        // Extract category slug and page number if present
        const categoryMatch = path.match(/\/blog\/topic\/([^/]+)(?:\/page\/(\d+))?\/?$/);
        const categorySlug = categoryMatch[1];
        const pageNum = categoryMatch[2];

        schemaBasePath += '/topic/' + categorySlug;
        if (pageNum) {
            schemaBasePath += '/page/' + pageNum;
        }

        schemaFiles = [
            '/lib/schema/' + lang + '/organization.json',
            schemaBasePath + '/blog-list.json',
            schemaBasePath + '/breadcrumb-blog-category.json'
        ];
    } else if (isIndexPage) {
        // Check if we're on a paginated page
        const pageMatch = path.match(/\/blog\/page\/(\d+)\/?$/);
        if (pageMatch) {
            schemaBasePath += '/page/' + pageMatch[1];
        }

        schemaFiles = [
            '/lib/schema/' + lang + '/organization.json',
            schemaBasePath + '/breadcrumb-blog.json'
        ];

        // Blog list schema only on first page
        if (!pageMatch) {
            schemaFiles.splice(1, 0, schemaBasePath + '/blog-list.json');
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