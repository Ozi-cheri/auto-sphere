// Existing Load More functionality
document.addEventListener('DOMContentLoaded', () => {
    const loadMoreButton = document.getElementById('load-more');

    if (loadMoreButton) {
        loadMoreButton.addEventListener('click', () => {
            const nextPage = loadMoreButton.getAttribute('data-next-page');
            fetch(`?page=${nextPage}`)
                .then(response => response.text())
                .then(data => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(data, 'text/html');
                    const newArticles = doc.querySelector('#articles-container').innerHTML;
                    const newButton = doc.querySelector('#load-more');

                    // Append new articles
                    const articlesContainer = document.querySelector('#articles-container');
                    articlesContainer.innerHTML += newArticles;

                    // Update the "Load More" button
                    if (newButton) {
                        loadMoreButton.setAttribute('data-next-page', newButton.getAttribute('data-next-page'));
                    } else {
                        loadMoreButton.remove();
                    }
                });
        });
    }
});

// Add the Sign Up page functionality here
document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('password_again');
    const passwordRules = document.querySelector('.password-rules');
    const submitButton = document.querySelector('.form-button');

    // Show password rules when user focuses on password input
    if (passwordInput) {
        passwordInput.addEventListener('focus', () => {
            passwordRules.style.display = 'block';
        });

        passwordInput.addEventListener('blur', () => {
            passwordRules.style.display = 'none';
        });
    }

    // Enable submit button if passwords match
    if (confirmPasswordInput) {
        confirmPasswordInput.addEventListener('input', () => {
            if (passwordInput.value === confirmPasswordInput.value) {
                submitButton.disabled = false;
            } else {
                submitButton.disabled = true;
            }
        });
    }
});
