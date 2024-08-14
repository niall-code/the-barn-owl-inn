let tableButtons = document.getElementsByClassName("table");

for (let i = 0; i < tableButtons.length; i++) {
    tableButtons[i].addEventListener("click", function() {
        // this.style.backgroundColor = "red";
        if (this.style.backgroundColor !== "firebrick") {
            this.style.backgroundColor = "firebrick";
        } else {
            this.style.backgroundColor = "burlywood";
        };
    });
    // document.getElementById('id_tables_{i}').addEventListener('click', checkboxSelected);
};

// function tableSelected(event) {
//     if (this.style.backgroundColor === "burlywood") {
//         this.style.backgroundColor = "firebrick";
            // let identifier = Number(this.id.charAt(-1) - 1);
            // document.getElementById('id_tables_' + identifier).click();
//     };
// }

//     // function checkboxSelected(event) {
//     //     let identifier = this.id.charAt(-1);
//     //     tableButtons[identifier].click();
//     // }



// document.getElementsByTagName("h2")[0].addEventListener("click", function() {this.style.color = "red"});
// document.getElementsByTagName("button")[0].addEventListener("click", function() {this.style.backgroundColor = "blue"});
// document.getElementsByClassName("table")[1].addEventListener("click", function() {this.style.backgroundColor = "green"});