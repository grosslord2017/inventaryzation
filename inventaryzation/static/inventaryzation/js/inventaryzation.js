// function for close modal window

// waiting for download page
document.addEventListener("DOMContentLoaded", () => {
    
    var modal = document.getElementById('ModalDownload');
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

    //------------------------------------------
})

