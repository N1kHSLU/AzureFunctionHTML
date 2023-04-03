const form = document.querySelector("#form");
const apiResult = document.querySelector("#api_result");

form.addEventListener("submit", (event) => {
    event.preventDefault();
    const from = form.elements["from"].value;
    const to = form.elements["to"].value;

    const apiUrl = `http://transport.opendata.ch/v1/connections?from=${from}&to=${to}&limit=1`;
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const departureTime = new Date(data.departure_time);
            const formattedTime = departureTime.toLocaleString();
            document.querySelector("#departure_time").value = formattedTime;
            apiResult.textContent = `Abfahrt am: ${formattedTime}`;
        })
        .catch(error => console.log(error));
});