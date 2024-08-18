document.addEventListener('DOMContentLoaded', function() {
    /**
     * Initializes edit functionality for Edit buttons.
     * 
     * For each button of `editButtons`:
     * - When clicked, gets the ID of the targeted reservation
     * - Copies that existing reservation's text into the form fields
     *   (including checking the appropriate table number checkboxes)
     * - Changes Submit button text to "Update"
     * - Sets the form's action to `edit_reservation/<the reservation ID>`
    */

    let editButtons = document.getElementsByClassName("edit");
    let reservationForm = document.getElementById("reservationForm");
    // Locates form fields
    let formDate = document.getElementById("id_date");
    let formTime = document.getElementById("id_start_time");
    let formLength = document.getElementById("id_duration");
    let formMobile = document.getElementById("id_mobile");
    let submitButton = document.getElementById("submitButton");

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let reservId = e.target.getAttribute("data-reservation_id");

            // Gets details of existing reservation
            let reservationDate = document.getElementById(`date${reservId}`).innerText;
            let reservationTime = document.getElementById(`time${reservId}`).innerText;
            let reservationLength = document.getElementById(`length${reservId}`).innerText;
            let reservationTables = document.getElementsByClassName(`table-for-${reservId}`).length;
            let reservationMobile = document.getElementById(`mobile${reservId}`).innerText;

            // Sets form field values identically
            formDate.value = reservationDate;
            formTime.value = reservationTime;
            formLength.value = reservationLength;
            for (let i = 0; i < reservationTables; i++) {
                let checkboxValue = document.getElementsByClassName(`table-for-${reservId}`)[i].innerText;
                let checkbox = document.querySelector(`input[type="checkbox"][value="${checkboxValue}"]`);
                checkbox.click();
            };
            formMobile.value = reservationMobile;

            submitButton.innerText = "Update";
            reservationForm.setAttribute("action", `edit_reservation/${reservId}`);
        });
    };

});
