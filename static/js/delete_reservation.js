document.addEventListener('DOMContentLoaded', function() {

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
