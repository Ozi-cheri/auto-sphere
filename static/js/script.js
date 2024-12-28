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

                    document.querySelector('#articles-container').innerHTML += newArticles;
                    if (newButton) {
                        loadMoreButton.setAttribute('data-next-page', newButton.getAttribute('data-next-page'));
                    } else {
                        loadMoreButton.remove();
                    }
                });
        });
    }

    
    const toggleButton = document.getElementById('navbar-toggle');
    const navLinks = document.getElementById('nav-links');

    if (toggleButton) {
        toggleButton.addEventListener('click', () => {
            navLinks.classList.toggle('show');
        });
    }
});
