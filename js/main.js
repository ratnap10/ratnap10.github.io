const toggle = document.getElementById('toggle');
const navRight = document.querySelector('.nav-right');

toggle.addEventListener('change', () => {
    navRight.classList.toggle('show-menu', toggle.checked);
});