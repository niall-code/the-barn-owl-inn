document.addEventListener('DOMContentLoaded', function() {
    /**
     * Initializes delete functionality for Delete buttons.
     * 
     * For each button of `deleteButtons`:
     * - When clicked, gets the ID of the targeted reservation
     * - Sets the modal's `deleteConfirm` button's href accordingly
     * - Displays the deletion confirmation modal
    */

    let deleteButtons = document.getElementsByClassName("delete");
    let deleteConfirm = document.getElementById("deleteConfirm");
    let deleteModal = document.getElementById("deleteModal");
    let span = document.getElementsByClassName("close")[0];

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let reservId = e.target.getAttribute("data-reservation_id");
            deleteConfirm.href = `delete_reservation/${reservId}`;
            deleteModal.style.display = "block";
        });
    };

    span.addEventListener("click", () => {
        deleteModal.style.display = "none";
    });

});
