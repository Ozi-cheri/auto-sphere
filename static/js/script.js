document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('password_again');
    const passwordRules = document.querySelector('.password-rules');
    const submitButton = document.querySelector('.form-button');

    // Function to check password strength
    function checkPasswordStrength() {
        const password = passwordInput.value;
        const rules = passwordRules.querySelectorAll('li');
        const regexes = [
            { regex: /.{8,}/, message: 'Password must be at least 8 characters.' },
            { regex: /[A-Z]/, message: 'Password must contain at least one uppercase letter.' },
            { regex: /\d/, message: 'Password must contain at least one number.' },
            { regex: /[^A-Za-z0-9]/, message: 'Password must contain at least one special character.' },
        ];

        rules.forEach((rule, index) => {
            const isValid = regexes[index].regex.test(password);
            rule.style.color = isValid ? 'green' : 'red';
            rule.textContent = isValid ? `✔ ${regexes[index].message}` : `✘ ${regexes[index].message}`;
        });
    }

    // Show password rules when focusing on the password field
    if (passwordInput) {
        passwordInput.addEventListener('focus', () => {
            passwordRules.style.display = 'block';
        });

        passwordInput.addEventListener('blur', () => {
            passwordRules.style.display = 'none';
        });

        // Check password strength on input
        passwordInput.addEventListener('input', checkPasswordStrength);
    }

    // Check if passwords match
    if (confirmPasswordInput) {
        confirmPasswordInput.addEventListener('input', () => {
            if (passwordInput.value === confirmPasswordInput.value && passwordRules.querySelectorAll('li').every((li) => li.style.color === 'green')) {
                submitButton.disabled = false;
            } else {
                submitButton.disabled = true;
            }
        });
    }
});
