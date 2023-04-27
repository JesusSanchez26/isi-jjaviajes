const form = document.querySelector('form');
const email = document.querySelector('input[name="email"]');
const password = document.querySelector('input[name="password"]');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Aquí se debe realizar la validación de las credenciales
    const validEmail = 'correo@example.com';
    const validPassword = 'contraseña';

    if (email.value === validEmail && password.value === validPassword) {
        window.location.href = 'otra-pagina.html';
    } else {
        alert('Email o contraseña incorrectos');
    }
});