// File: project/events/static/events/js/main.js
// Description: Add your global JavaScript code here.
// This file is for including global JavaScript code that applies to the entire project.

// Example: Function to perform initialization tasks when the DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    // Your global JavaScript code here
    // Example: Add event listeners, initialize components, etc.

    // Example: Initialize date pickers using a third-party library like Flatpickr
    flatpickr('.datepicker', {
        dateFormat: 'Y-m-d',
    });

    // Example: Call custom functions
    customFunction();

    // ...
});
