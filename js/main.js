document.addEventListener('DOMContentLoaded', () => {
    // Add active state to navigation items
    const currentPath = location.pathname.split('/').pop() || 'index.html';
    const menuItems = document.querySelectorAll('.nav-links a');

    menuItems.forEach(item => {
        // Do not touch the Donate button's classes
        if (item.classList.contains('nav-donate')) return;

        const itemHref = item.getAttribute('href');
        if (itemHref === currentPath) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });
});
