window.addEventListener('load', () => {

    // фильтр по дате, создание предела поиску по дате
    const date_filter = document.querySelector("#date");
    const curentDate = new Date().toISOString().slice(0, 10); // 2025-01-14
    date_filter.max = curentDate;
    date_filter.addEventListener('change', ()=> {
        let all_blocks = document.querySelectorAll(".operation_date_zone");

        all_blocks.forEach(block => {
            let vision = block.getElementsByClassName(`${date_filter.value}`);
            if (vision.length || date_filter.value === '') {
                block.parentNode.parentNode.classList.remove("hide-block");
            } else {
                block.parentNode.parentNode.classList.add("hide-block");
            }
        })
    });
    

    // фильтр по операции
    const select = document.querySelector(".filter_operation_type_button");
    select.addEventListener('change', ()=> {
        let val = select.value;
        let bloksOperation = document.querySelectorAll(".operation_name_zone");
        bloksOperation.forEach(operation => {
            if (select.value === '---' || operation.textContent === select.value) {
                operation.parentNode.parentNode.classList.remove("hide-block");
            } else {
                operation.parentNode.parentNode.classList.add("hide-block");
            };
        });
    });


    //поиск по инвентарному номеру или действующим лицам
    const input = document.querySelector(".search_input");
    input.addEventListener('input', ()=> {
        let inv_zone = document.querySelectorAll(".inv_number_zone"); //по инвентарному номеру
        let from_whom = document.querySelectorAll(".from_who_zone"); //по отправителю
        let to_whom = document.querySelectorAll(".to_who_zone"); // по получателю


        const regex = /^\d+$/; // если в инпут приходит число - ищим по инвентарному номеру, иначе по фамилии
        let test = input.value;
        if ((test !== null) && (regex.test(test))) {
            inv_zone.forEach(inv => {
                let inv_val = inv.querySelector('p').textContent;
                if (inv_val.startsWith(input.value)) { //поиск по началу совпадения 
                    inv.parentNode.parentNode.parentNode.classList.remove("hide-block");
                } else {
                    inv.parentNode.parentNode.parentNode.classList.add("hide-block");
                }
            });
        } else {
            from_whom.forEach(whom => { // поиск по from_whom
                let whom_val = whom.querySelector('p').textContent;
                if (whom_val.startsWith(input.value)) {
                    whom.parentNode.parentNode.classList.remove("hide-block");
                } else {
                    whom.parentNode.parentNode.classList.add("hide-block");
                }
            })
            to_whom.forEach(whom => { // дополнительный поиск по to_whom
                let whom_val = whom.querySelector('p').textContent;
                console.log(whom_val);
                if (whom_val.startsWith(input.value)) {
                    whom.parentNode.parentNode.classList.remove("hide-block");
                }
            })
        }




        /*inv_zone.forEach(inv => {
            let inv_val = inv.querySelector('p').textContent;
            if (inv_val.startsWith(input.value)) { //поиск по началу совпадения 
                inv.parentNode.parentNode.parentNode.classList.remove("hide-block");
            } else {
                inv.parentNode.parentNode.parentNode.classList.add("hide-block");
            }
        });*/

        /*from_whom.forEach(whom => {
            let whom_val = whom.querySelector('p').textContent;
            if (whom_val.startsWith(input.value)) {
                whom.parentNode.parentNode.classList.remove("hide-block");
            } else {
                whom.parentNode.parentNode.classList.add("hide-block");
            }
        })*/

    });
    

});