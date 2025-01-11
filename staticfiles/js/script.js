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


                    const articlesContainer = document.querySelector('#articles-container');
                    articlesContainer.innerHTML += newArticles;


                    if (newButton) {
                        loadMoreButton.setAttribute('data-next-page', newButton.getAttribute('data-next-page'));
                    } else {
                        loadMoreButton.remove();
                    }
                });
        });
    }
});


document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password');
    const confirmPasswordInput = document.getElementById('password_again');
    const passwordRules = document.querySelector('.password-rules');
    const submitButton = document.querySelector('.form-button');


    if (passwordInput) {
        passwordInput.addEventListener('focus', () => {
            passwordRules.style.display = 'block';
        });

        passwordInput.addEventListener('blur', () => {
            passwordRules.style.display = 'none';
        });
    }


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