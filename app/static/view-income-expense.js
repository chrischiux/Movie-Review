$(document).ready(function () {
    // hide edit form on page load
    var form = document.getElementById("editForm");
    form.style.display = "none";
});

function showEditForm(id, name, amount) {
    var form = document.getElementById("editForm");
    form.style.display = "block";
    document.getElementById("recordID").value = id;
    document.getElementById("name").value = name;
    document.getElementById("amount").value = amount;
    try {
        var alert = document.getElementById("alert");
        alert.style.display = "none";
    }
    finally { }

}