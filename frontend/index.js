// password show / hide - eye button on password inputs
document.addEventListener('DOMContentLoaded', function() {
    const togglePassword = document.getElementById('togglePassword');
    const passwordInput = document.getElementById('password_access_key');
    if (togglePassword && passwordInput) {
        togglePassword.addEventListener('click', function() {
            // Toggle the type attribute
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            // Toggle the icon
            this.classList.toggle('bi-eye');
            this.classList.toggle('bi-eye-slash');
        });
    }
});

function button_save_edit_creds() {
    // Get the modal element
    const modalElement = document.getElementById('myModal');
    // Set the title and message
    document.getElementById('modalLabel').textContent = "Info";
    document.getElementById('modalBody').innerHTML = "It is working fine!";
    // Create a Bootstrap modal instance and show it
    const modal = new bootstrap.Modal(modalElement);
    modal.show();
}