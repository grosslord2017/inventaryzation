window.addEventListener('load', () => {
    // фильтр по операциям
    const select = document.querySelector(".filter_operation_type_button");
    select.addEventListener('change', ()=> {
        let val = select.value;
        let bloksOperation = document.querySelectorAll(".content_operation");
        bloksOperation.forEach(operation => {
            if (select.value === '---' || operation.textContent === select.value) {
                operation.parentNode.classList.remove("hide-block");
            } else {
                operation.parentNode.classList.add("hide-block");
            };
        });
    });


    //поиск по id (они же номера актов)
    const input = document.querySelector(".search_input");
    input.addEventListener('input', ()=> {
        let blockId = document.querySelectorAll(".content_id")
        blockId.forEach(id => {
            if (input.value === '' || id.textContent === input.value) {
                id.parentNode.classList.remove("hide-block");
            } else {
                id.parentNode.classList.add("hide-block");
            };
        });
    });
    

    // поиск по дате
    const date_filter = document.querySelector("#date");
    const curentDate = new Date().toISOString().slice(0, 10); // 2025-01-01
    date_filter.max = curentDate;
    date_filter.addEventListener('change', ()=> {
        let blockDate = document.querySelectorAll(".content_date");
        blockDate.forEach(date => {
            if (date.textContent === date_filter.value || date_filter.value === '') {
                date.parentNode.classList.remove("hide-block");
            } else {
                date.parentNode.classList.add("hide-block");
            };
        });
    });

});