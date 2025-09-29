// Función para mostrar y ocultar la contraseña y cambiar color del icono LOGIN
$(document).ready(function () {
    $('#topass1').on('mouseenter', function () {
        $(this).css('color', 'blue');
    }).on('mouseleave', function () {
        // Si el campo está en modo texto, mantener rojo; si no, negro
        var passwordField = $('#password');
        if (passwordField.attr('type') === 'text') {
            $(this).css('color', 'red');
        } else {
            $(this).css('color', 'black');
        }
    });

    $('#topass1').click(function () {
        var passwordField = $('#password');
        var passwordFieldType = passwordField.attr('type');

        if (passwordFieldType === 'password') {
            passwordField.attr('type', 'text');
            $(this).removeClass('bi-eye-slash-fill').addClass('bi-eye-fill');
            $(this).css('color', 'red');
        } else {
            passwordField.attr('type', 'password');
            $(this).removeClass('bi-eye-fill').addClass('bi-eye-slash-fill');
            $(this).css('color', 'black');
        }
    });
});

// Función para mostrar y ocultar la contraseña y cambiar color del icono REGISTRO
$(document).ready(function () {
    $('#topass2').on('mouseenter', function () {
        $(this).css('color', 'blue');
    }).on('mouseleave', function () {
        // Si el campo está en modo texto, mantener rojo; si no, negro
        var passwordField = $('#password');
        if (passwordField.attr('type') === 'text') {
            $(this).css('color', 'red');
        } else {
            $(this).css('color', 'black');
        }
    });

    $('#topass2').click(function () {
        var passwordField = $('#password');
        var passwordFieldType = passwordField.attr('type');

        if (passwordFieldType === 'password') {
            passwordField.attr('type', 'text');
            $(this).removeClass('bi-eye-slash-fill').addClass('bi-eye-fill');
            $(this).css('color', 'red');
        } else {
            passwordField.attr('type', 'password');
            $(this).removeClass('bi-eye-fill').addClass('bi-eye-slash-fill');
            $(this).css('color', 'black');
        }
    });
});


/* function topass() {
    const passwordInput = document.getElementById('password');
    const icon = document.getElementById('topass');
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        icon.classList.remove('bi-eye-slash-fill');
        icon.classList.add('bi-eye-fill');
    } else {
        passwordInput.type = "password";
        icon.classList.remove('bi-eye-fill');
        icon.classList.add('bi-eye-slash-fill');
    }
} */