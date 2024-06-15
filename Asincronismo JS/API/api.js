const API = 'https://imdb-top-100-movies.p.rapidapi.com/top1';

const options = {
    method: 'GET',
    headers: {
        'x-rapidapi-key': '752d2d2431msh0304c1be5af4024p144590jsnc0c8ebe32de2',
        'x-rapidapi-host': 'imdb-top-100-movies.p.rapidapi.com'
    }
};

async function fetchData(url) {
    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
}

// Example usage of fetchData
(async () => {
    try {
        const result = await fetchData(API);
        console.table(result);

    } catch (error) {
        console.error('Error in anonymous function:', error);
    }
})();