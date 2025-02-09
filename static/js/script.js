// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Get DOM elements for password and confirmation inputs, rules, and submit button
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('password_again');
    const passwordRules = document.querySelector('.password-rules');
    const submitButton = document.querySelector('.form-button');

    // Function to check password strength
    function checkPasswordStrength() {
        const password = passwordInput.value;
        const rules = passwordRules.querySelectorAll('li');
        const regexes = [{
                regex: /.{8,}/,
                message: 'Password must be at least 8 characters.'
            },
            {
                regex: /[A-Z]/,
                message: 'Password must contain at least one uppercase letter.'
            },
            {
                regex: /\d/,
                message: 'Password must contain at least one number.'
            },
            {
                regex: /[^A-Za-z0-9]/,
                message: 'Password must contain at least one special character.'
            },
        ];

        // Check each rule and update the UI accordingly
        rules.forEach((rule, index) => {
            const isValid = regexes[index].regex.test(password);
            rule.style.color = isValid ? 'green' : 'red';
            rule.textContent = isValid ? `✔ ${regexes[index].message}` : `✘ ${regexes[index].message}`;
        });
    }

    // Show password rules on focus and hide on blur
    if (passwordInput) {
        passwordInput.addEventListener('focus', () => {
            passwordRules.style.display = 'block';
        });
        passwordInput.addEventListener('blur', () => {
            passwordRules.style.display = 'none';
        });
        passwordInput.addEventListener('input', checkPasswordStrength);
    }

    // Enable submit button if passwords match and all rules are met
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

// jQuery code for handling comment edit and delete actions
$(document).ready(function() {
    // Open edit comment form with existing text and URL
    $(".edit-comment-btn").click(function() {
        let commentText = $(this).data("comment-text");
        let editCommentUrl = $(this).data('edit-comment-url');

        $("#edit-comment-text").val(commentText);
        $('#editCommentForm').attr('action', editCommentUrl);
    });

    // Open delete comment confirmation with text and URL
    $(".delete-comment-btn").click(function () {
        let commentText = $(this).data("comment-text");
        let deleteUrl = $(this).data("delete-comment-url");

        $("#delete-comment-text").text(commentText);
        $("#deleteCommentForm").attr("action", deleteUrl);
    });
});
