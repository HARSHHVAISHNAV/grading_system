document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById('sidebar');
    const menuBtn = document.getElementById('menu-btn');
    const closeBtn = document.getElementById('close-btn');
    const mainContent = document.getElementById('main-content');

    // Function to open the sidebar
    const openSidebar = () => {
        sidebar.classList.add('active');
        mainContent.classList.add('active');
    };

    // Function to close the sidebar
    const closeSidebar = () => {
        sidebar.classList.remove('active');
        mainContent.classList.remove('active');
    };

    // Toggle sidebar on menu button click
    menuBtn.addEventListener('click', openSidebar);

    // Open sidebar when hovering over the menu button
    menuBtn.addEventListener('mouseenter', openSidebar);

    // Close sidebar on close button click
    closeBtn.addEventListener('click', closeSidebar);

    // Close sidebar when mouse leaves the sidebar
    sidebar.addEventListener('mouseleave', closeSidebar);
});
