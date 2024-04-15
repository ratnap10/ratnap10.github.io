const toggle = document.getElementById('toggle');
const navRight = document.querySelector('.nav-right');

toggle.addEventListener('change', () => {
    navRight.classList.toggle('show-menu', toggle.checked);
});

var acc = new XMLHttpRequest();

acc.onreadystatechange = function() {
    if (acc.readyState == XMLHttpRequest.DONE) {
        if (acc.status == 200) {
            console.log(acc.responseText);
        } else {
            console.error('Terjadi kesalahan:', acc.status);
        }
    }
};

acc.open('GET', 'Repu.json', true);
acc.send();