document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('password_again');
    const passwordRules = document.querySelector('.password-rules');
    const submitButton = document.querySelector('.form-button');


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

        rules.forEach((rule, index) => {
            const isValid = regexes[index].regex.test(password);
            rule.style.color = isValid ? 'green' : 'red';
            rule.textContent = isValid ? `✔ ${regexes[index].message}` : `✘ ${regexes[index].message}`;
        });
    }


    if (passwordInput) {
        passwordInput.addEventListener('focus', () => {
            passwordRules.style.display = 'block';
        });

        passwordInput.addEventListener('blur', () => {
            passwordRules.style.display = 'none';
        });


        passwordInput.addEventListener('input', checkPasswordStrength);
    }


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

$(document).ready(function() {
    $(".edit-comment-btn").click(function() {
        let commentText = $(this).data("comment-text");
        let editCommentUrl = $(this).data('edit-comment-url');

        $("#edit-comment-text").val(commentText);

        $('#editCommentForm').attr('action', editCommentUrl);
    });


    $(".delete-comment-btn").click(function () {
        let commentText = $(this).data("comment-text");  
        let deleteUrl = $(this).data("delete-comment-url"); 

        $("#delete-comment-text").text(commentText); 
        $("#deleteCommentForm").attr("action", deleteUrl);  

    });

});

 