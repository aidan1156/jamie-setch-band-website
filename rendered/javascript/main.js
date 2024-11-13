

function navigateTo(page) {
    console.log(page)
}

function toggleSideNav() {
    document.body.classList.toggle('side-nav-open')
}

window.site = {}
window.site.navigateTo = navigateTo
window.site.toggleSideNav = toggleSideNav