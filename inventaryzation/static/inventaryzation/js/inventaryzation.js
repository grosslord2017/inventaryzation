function openMenu(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// function for close modal window

// waiting for download page
document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("defaultOpen").click();
    
    var modal = document.getElementById('myModal');
    var btn = document.getElementById("myBtn");
    var span = document.getElementsByClassName("close")[0];
    var download = document.getElementsByClassName("submit")[0];

    btn.onclick = function() {
        modal.style.display = "block";
    }

    span.onclick = function() {
        close();
    }
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            close();
        }
    }
    
    download.onclick = function() {
        setTimeout(close, 50);
    }

    function close () {
        modal.style.display = "none";
    }
})


