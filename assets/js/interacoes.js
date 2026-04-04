const btnMobile = document.querySelector('.menu-mobile');
const navLinks = document.querySelector('.nav-links');
const icone = document.querySelector ('.menu-mobile i');

btnMobile.addEventListener('click', () => {
    navLinks.classList.toggle('active');

    if (navLinks.classList.contains('active')){
        icone.classList.remove('bi-list');
        icone.classList.add('bi-x-lg');
    } else {
        icone.classList.remove('bi-x-lg');
        icone.classList.add('bi-list');
    }
});