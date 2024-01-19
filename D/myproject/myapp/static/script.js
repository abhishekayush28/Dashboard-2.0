// myapp/static/script.js
function fetchData() {
    // Get the selected value from the dropdown
    var selectedCategory = document.getElementById("categoryDropdown").value;
    console.log('Selected category:', selectedCategory);

    // Make an asynchronous request to Django view
    fetch(`/myapp/get_data/?category=${selectedCategory}`)
        .then(response => response.json())
        .then(data => {
            console.log('Data received:', data);
            // Display the result in the 'result' div
            document.getElementById("result").innerHTML = `<p>${JSON.stringify(data)}</p>`;
        })
        .catch(error => console.error('Error:', error));
}
