function loadUserProfileTemplate(el) {

    let tempUname = $(el).closest('div').prev('li').attr('data-uname');

    uName = tempUname.split("'")[1];

    $.ajax({
        data: {
            userName : uName,
        },
        type : 'POST',
        url : '/GetUser',
        success: function(data) {
            document.getElementById('name').innerHTML = data.name
            document.getElementById('licenseplate').innerHTML = data.licenseplate
            document.getElementById('role').innerHTML = data.role
        }
    });
}