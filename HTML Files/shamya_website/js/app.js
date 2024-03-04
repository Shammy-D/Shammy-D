document.addEventListener('DOMContentLoaded', function() {
    fetchData();
});

async function fetchData() {
    try {
        const response = await fetch('/api/external');
        const data = await response.json();

        const dataContainer = document.getElementById('data');
        dataContainer.innerHTML = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}
