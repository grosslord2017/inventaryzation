function all_changed(row, flag) {
    for (let i=1; i<row.length; i++) {
        row[i].getElementsByClassName('category')[0].disabled = flag;
        if (flag === true){
            row[i].getElementsByClassName('through')[0].classList.add('line-through');
        } else {
            row[i].getElementsByClassName('through')[0].classList.remove('line-through');
        };
    };
}

document.addEventListener("DOMContentLoaded", () => {
    const checkbox = document.getElementById('all_items');
    checkbox.addEventListener('change', () => {

        let row = document.getElementsByClassName('row');
        if (checkbox.checked == true) {
            all_changed(row, true);
        } else {
            all_changed(row, false);
        };

    });
})
