document.addEventListener('DOMContentLoaded', function() {

    console.log("Can you hear me?");

    let editButtons = document.getElementsByClassName("edit");

    // The Form Fields
    let formDate = document.getElementById("id_date");
    let formTime = document.getElementById("id_start_time");
    let formLength = document.getElementById("id_duration");
    let formTables = document.getElementById("id_tables");
    let formContact = document.getElementById("id_contact");

    let reservationForm = document.getElementById("reservationForm");

    let submitButton = document.getElementById("submitButton");

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let reservId = e.target.getAttribute("data-reservation_id");

            let reservationDate = document.getElementById(`date${reservId}`).innerText;
            let reservationTime = document.getElementById(`time${reservId}`).innerText;
            let reservationLength = document.getElementById(`length${reservId}`).innerText;
            let reservationTables = document.getElementsByClassName(`table-for-${reservId}`).length;
            console.log(reservationTables);
            // let reservationTables = document.querySelectorAll(`.table-for-${reservId}`);
            // let reservationTable = document.getElementsByClassName(`table-for-${reservId}`)[0].getAttribute("data-table-id");
            // console.log(String(reservationTable));
            let reservationContact = document.getElementById(`contact${reservId}`).innerText;

            formDate.value = reservationDate;
            formTime.value = reservationTime;
            formLength.value = reservationLength;
            // for (let reservationTable of reservationTables) {
            //     let toCheck = reservationTable.getAttribute("data-table_id");
            //     console.log(toCheck);
            //     let checkedBox = document.getElementById(`${toCheck}`);
            //     checkedBox.click();
            // };
            // for (let i = 0; i < reservationTables.length; i++) {
            //     console.log(reservationTables[i].classList.value);
            // };
            // reservationTables.forEach(reservationTable => {
            //     let attributeValue = reservationTable.getAttribute("data-table_id");
            //     console.log(attributeValue);
            // });
            formContact.value = reservationContact;


            submitButton.innerText = "Update";
            // reservationForm.setAttribute("action", `edit_comment/${commentId}`);
        });
    };

});
