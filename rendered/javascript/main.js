

function navigateTo(page) {
    const current = document.querySelector('.page:not(.hidden)')
    if (current) {
        current.classList.add('hidden')
    }
    const next = document.querySelector('#' + page)
    next.classList.remove('hidden')
    document.querySelector('nav').dataset.size = next.dataset.nav
    closeSideNav()
    history.pushState('hi', "", page);

    let els = document.querySelectorAll('.nav-link.selected')
    for (const el of els) {
        el.classList.remove('selected')
    }

    els = document.querySelectorAll('.nav-link[data-navid="' + page + '"]')
    for (const el of els) {
        el.classList.add('selected')
    }
}

function toggleSideNav() {
    document.body.classList.toggle('side-nav-open')
}

function closeSideNav() {
    document.body.classList.remove('side-nav-open')
}

window.site = {}
window.site.navigateTo = navigateTo
window.site.toggleSideNav = toggleSideNav


const els = document.querySelectorAll('.nav-link')
for (const el of els) {
    el.addEventListener('click', (e) => {
        e.preventDefault()
        navigateTo(e.target.dataset.navid)
    })
}

window.addEventListener('popstate', (e) => {
    let path = window.location.pathname
    path = path.slice(1, path.length).split('.')[0]
    navigateTo(path)
})