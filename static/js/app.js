window.onload = (event) => {
    const ele = document.getElementById('gauge-percent');
    setTimeout(function() {
        ele.classList.add('animate');
    }, 500);
    
    const dd = document.getElementById('genre');
    dd.addEventListener('change', function() {
        var checkboxes = document.querySelectorAll('input[type=checkbox]');
        for (var checkbox of checkboxes) {
            checkbox.checked = false;
        }
        console.log(dd.value)
        let toCheck = document.getElementsByName(dd.value)[0];
        toCheck.checked = true;
    });

    let genre = dd.getAttribute('data-genre');
    console.log(genre);
    if (genre != null && genre !== '') {
        document.getElementById('genre').value = genre;
    } else {
        document.getElementById('genre').value = 'genre_Pop';
    }


    const navlinks = document.getElementsByClassName('nav-link');
    for (var i = 0; i < navlinks.length; i++) {
        navlinks[i].addEventListener('click', function() {
            let anchor = this.getAttribute('href');
            let scrollTo = document.getElementById(anchor.substring(1));
            scrollTo.scrollIntoView();
        }, false);
    }
};


