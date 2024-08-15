document.addEventListener('DOMContentLoaded', function() {

    let editButtons = document.getElementsByClassName("edit");
    let reservationForm = document.getElementById("reservationForm");
    let formDate = document.getElementById("id_date");
    let formTime = document.getElementById("id_start_time");
    let formLength = document.getElementById("id_duration");
    let formContact = document.getElementById("id_contact");
    let submitButton = document.getElementById("submitButton");

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let reservId = e.target.getAttribute("data-reservation_id");

            let reservationDate = document.getElementById(`date${reservId}`).innerText;
            let reservationTime = document.getElementById(`time${reservId}`).innerText;
            let reservationLength = document.getElementById(`length${reservId}`).innerText;
            let reservationTables = document.getElementsByClassName(`table-for-${reservId}`).length;
            let reservationContact = document.getElementById(`contact${reservId}`).innerText;

            formDate.value = reservationDate;
            formTime.value = reservationTime;
            formLength.value = reservationLength;
            for (let i = 0; i < reservationTables; i++) {
                let checkboxValue = document.getElementsByClassName(`table-for-${reservId}`)[i].innerText;
                let checkbox = document.querySelector(`input[type="checkbox"][value="${checkboxValue}"]`);
                checkbox.click();
            };
            formContact.value = reservationContact;

            submitButton.innerText = "Update";
            reservationForm.setAttribute("action", `edit_reservation/${reservId}`);
        });
    };

});
