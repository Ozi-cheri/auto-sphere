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
