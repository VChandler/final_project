window.onload = (event) => {
    const ele = document.getElementById("gauge-percent");
    setTimeout(function() {
        ele.classList.add("animate");
    }, 500);
    
    const dd = document.getElementById("genre");
    dd.addEventListener("change", function() {
        var checkboxes = document.querySelectorAll('input[type=checkbox]');
        for (var checkbox of checkboxes) {
            checkbox.checked = false;
        }
        console.log(dd.value)
        let toCheck = document.getElementsByName(dd.value)[0];
        toCheck.checked = true;
    });
};


