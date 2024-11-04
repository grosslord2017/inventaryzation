// ajax request for decommissioned item. For finish - reloadweb page.
function confirm_remove (item_id) {
    console.log(item_id);
    var locationURL = "{% url 'ajax_decommissioned' %}"
    csrfToken = '{{ csrf_token }}';
    if (confirm('Вы действительно хотите списать данный эелемент?')) {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("POST", locationURL);
        xmlhttp.setRequestHeader("content-type", "application/json");
        xmlhttp.setRequestHeader("X-CSRFToken", csrfToken);
        xmlhttp.send(JSON.stringify({item_id: item_id}));
    
        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                location.reload();
            }
        }
    }
}
