// File: project/digital_storefront/static/digital_storefront/js/main.js
// Description: Add your global JavaScript code here.
// This file is for including global JavaScript code that applies to the entire project.

// Function to perform initialization tasks when the DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    // Your global JavaScript code here
    // Example: Add event listeners, initialize components, etc.

    // Initialize tooltips using a third-party library like Tippy.js
    tippy('[data-tooltip]', {
        arrow: true,
        placement: 'top',
    });

    // Call custom functions
    customFunction();

    // ...
});
