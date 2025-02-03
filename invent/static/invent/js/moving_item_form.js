var locationURL = "{% url 'ajax_location_workers' %}";
var workerURL = "{% url 'ajax_worker_items' %}";
csrfToken = '{{ csrf_token }}';

const items_list = document.getElementById('table_items');

// ajax selection of work_place by location
function select_location(el) {
    if (el == 'src'){
        var locId = document.getElementById("locations_src").value;
        var work = document.getElementById('workers_src');

        // clear DOM <div id='table_items'>
        items_list.innerHTML = '';
    } else if (el == 'dst') {
        var locId = document.getElementById('locations_dst').value;
        var work = document.getElementById('workers_dst');
    }
    
    while (work.options.length) {
        work.options[0] = null;
    }
    
    if (locId != 0) {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("POST", locationURL);
        xmlhttp.setRequestHeader("content-type", "application/json");
        xmlhttp.setRequestHeader("X-CSRFToken", csrfToken);
        xmlhttp.send(JSON.stringify({locId: locId}));
    
        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                var response = JSON.parse(this.responseText);
                var workers = response['work_list'];
                
                for (i = 0; i < workers.length; i++) {
                    var work_place = workers[i][0] + ' ' + workers[i][1];
                    work.append(new Option(work_place, workers[i][2]));
                }
            }
        }
    } else if (locId != '' && el != 'dst') {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("POST", locationURL);
        xmlhttp.setRequestHeader("X-CSRFToken", csrfToken);
        xmlhttp.send(JSON.stringify({locId: locId}));

        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                var response = JSON.parse(this.responseText);
                var items = response['item_stock_list'];

                items_checkbox (items);
            }
        }
    }
}

// ajax selection of items by work_place
//document.getElementById('workers_src').onchange = function () {
function select_worker () {    
    var workId = document.getElementById('workers_src').value;
    
    // clear DOM <div id='table_items'>
    items_list.innerHTML = '';

    if (workId != '0') { 
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("POST", workerURL);
        xmlhttp.setRequestHeader("X-CSRFToken", csrfToken);
        xmlhttp.send(JSON.stringify({workId: workId}));

        xmlhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                var response = JSON.parse(this.responseText);
                var items = response['items_list'];
                
                // create element in DOM structure
                items_checkbox (items);
            }
        }
    }
}

function items_checkbox (items) {
    for (i = 0; i < items.length; i++) {
        let div = document.createElement('div');
        let input = document.createElement('input');
        let label = document.createElement('label');
        let br = document.createElement('br');
        div.className = 'check_element';
        input.id = items[i][0];
        input.type = 'checkbox';
        input.name = 'items';
        input.value = items[i][0];
        label.for = items[i][0];
        label.textContent = items[i][1] + ' ' + items[i][2] + ' ' + items[i][3];
        
        // add created element in DOM
        items_list.append(div); //create div element in DOM construction
        //items_list.append(input);
        //items_list.append(label);
        //items_list.append(br);
        div.appendChild(input); // add element in to our div conctruction
        div.appendChild(label);
    }
}