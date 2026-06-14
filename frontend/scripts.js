console.log("script.js loaded successfully");
async function loginUser() {
    // Get values from input boxes
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Message area
    const messageElement = document.getElementById("message");

    // Basic frontend validation
    if (username === "" || password === "") {
        messageElement.innerText = "Please enter username and password";
        messageElement.style.color = "red";
        return;
    }

    try {
        // Send request to FastAPI backend
        const response = await fetch("http://127.0.0.1:8000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        // Convert backend response into JavaScript object
        const data = await response.json();

        // Show response message
        if (data.success) {
            messageElement.innerText = data.message;
            messageElement.style.color = "green";
        } else {
            messageElement.innerText = data.message;
            messageElement.style.color = "red";
        }

    } catch (error) {
        messageElement.innerText = "Backend server is not running";
        messageElement.style.color = "red";
    }
}