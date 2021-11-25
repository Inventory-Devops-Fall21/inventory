$(function () {

    // ****************************************
    //  U T I L I T Y   F U N C T I O N S
    // ****************************************

    // Updates the form with data from the response
    function update_form_data(res) {
        $("#inv_id").val(res.id);
        $("#inv_name").val(res.name);
        $("#inv_quantity").val(res.quantity);
        $("#inv_restock_level").val(res.restock_level);
        $("#inv_condition").val(res.condition);
    }

    /// Clears all form fields
    function clear_form_data() {
        $("#inv_name").val("");
        $("#inv_quantity").val("");
        $("#inv_restock_level").val("");
        $("#inv_condition").val("");
    }

    // Updates the flash message area
    function flash_message(message) {
        $("#flash_message").empty();
        $("#flash_message").append(message);
    }

    // ****************************************
    // Create a Pet
    // ****************************************

    $("#create-btn").click(function () {
        var name = $("#inv_name").val();
        var quantity = parseInt($("#inv_quantity").val(), 10); // Base 10
        var restock_level = parseInt($("#inv_restock_level").val(), 10);
        var condition = $("#inv_condition").val().toLowerCase();

        var data = {
            "name": name,
            "quantity": quantity,
            "restock_level": restock_level,
            "condition": condition
        };

        var ajax = $.ajax({
            type: "POST",
            url: "/inventory",
            contentType: "application/json",
            data: JSON.stringify(data),
        });

        ajax.done(function (res) {
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function (res) {
            flash_message(res.responseJSON.message)
        });
    });


    // ****************************************
    // Update a Pet
    // ****************************************

    $("#update-btn").click(function () {

        var inv_id = $("#inv_id").val();
        var name = $("#inv_name").val();
        var category = $("#inv_category").val();
        var available = $("#inv_available").val() == "true";

        var data = {
            "name": name,
            "category": category,
            "available": available
        };

        var ajax = $.ajax({
            type: "PUT",
            url: "/inventory/" + inv_id,
            contentType: "application/json",
            data: JSON.stringify(data)
        })

        ajax.done(function (res) {
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function (res) {
            flash_message(res.responseJSON.message)
        });

    });

    // ****************************************
    // Retrieve a Pet
    // ****************************************

    $("#retrieve-btn").click(function () {
        var inv_id = $("#inv_id").val();

        var ajax = $.ajax({
            type: "GET",
            url: "/inventory/" + inv_id,
            contentType: "application/json",
            data: ''
        })

        ajax.done(function (res) {
            //alert(res.toSource())
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function (res) {
            clear_form_data()
            flash_message(res.responseJSON.message)
        });
    });

    // ****************************************
    // Delete a Pet
    // ****************************************

    $("#delete-btn").click(function () {

        var inv_id = $("#inv_id").val();

        var ajax = $.ajax({
            type: "DELETE",
            url: "/inventory/" + inv_id,
            contentType: "application/json",
            data: '',
        })

        ajax.done(function (res) {
            clear_form_data()
            flash_message("Pet has been Deleted!")
        });

        ajax.fail(function (res) {
            flash_message("Server error!")
        });
    });

    // ****************************************
    // Clear the form
    // ****************************************

    $("#clear-btn").click(function () {
        $("#inv_id").val("");
        clear_form_data()
    });

    // ****************************************
    // Search for a Pet
    // ****************************************

    $("#search-btn").click(function () {

        var name = $("#inv_name").val();
        var category = $("#inv_category").val();
        var available = $("#inv_available").val() == "true";

        var queryString = ""

        if (name) {
            queryString += 'name=' + name
        }
        if (category) {
            if (queryString.length > 0) {
                queryString += '&category=' + category
            } else {
                queryString += 'category=' + category
            }
        }
        if (available) {
            if (queryString.length > 0) {
                queryString += '&available=' + available
            } else {
                queryString += 'available=' + available
            }
        }

        var ajax = $.ajax({
            type: "GET",
            url: "/inventory?" + queryString,
            contentType: "application/json",
            data: ''
        })

        ajax.done(function (res) {
            //alert(res.toSource())
            $("#search_results").empty();
            $("#search_results").append('<table class="table-striped" cellpadding="10">');
            var header = '<tr>'
            header += '<th style="width:10%">ID</th>'
            header += '<th style="width:40%">Name</th>'
            header += '<th style="width:40%">Category</th>'
            header += '<th style="width:10%">Available</th></tr>'
            $("#search_results").append(header);
            var firstPet = "";
            for (var i = 0; i < res.length; i++) {
                var inv = res[i];
                var row = "<tr><td>" + inv._id + "</td><td>" + inv.name + "</td><td>" + inv.category + "</td><td>" + inv.available + "</td></tr>";
                $("#search_results").append(row);
                if (i == 0) {
                    firstPet = inv;
                }
            }

            $("#search_results").append('</table>');

            // copy the first result to the form
            if (firstPet != "") {
                update_form_data(firstPet)
            }

            flash_message("Success")
        });

        ajax.fail(function (res) {
            flash_message(res.responseJSON.message)
        });

    });

})
