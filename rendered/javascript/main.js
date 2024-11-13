

function navigateTo(page) {
    console.log(page)
}

function toggleSideNav() {
    document.body.classList.toggle('side-nav-open')
}

window.site = {}
window.site.navigateTo = navigateTo
window.site.toggleSideNav = toggleSideNav


const els = document.querySelectorAll('.nav-links')
for (el of els) {
    el.addEventListener('click', (e) => {
        
    })
}