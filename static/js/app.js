document.getElementById("prediction-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    // Show loading spinner
    document.getElementById("loading").classList.remove("d-none");

    const area = document.getElementById("area").value;
    const bedrooms = document.getElementById("bedrooms").value;
    const bathrooms = document.getElementById("bathrooms").value;
    const floors = document.getElementById("floors").value;
    const age = document.getElementById("age").value;

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            area: area,
            bedrooms: bedrooms,
            bathrooms: bathrooms,
            floors: floors,
            age: age
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("loading").classList.add("d-none"); // Hide loading spinner
        const resultElement = document.getElementById("result");
        resultElement.innerText = `Estimated Price: $${data.price.toFixed(2)}`;
        resultElement.classList.add("show"); // Show result with animation
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("loading").classList.add("d-none"); // Hide loading spinner
        document.getElementById("result").innerText = "Error predicting price.";
    });
});
