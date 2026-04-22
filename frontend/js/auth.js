async function login() {
    const username = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    try {
        const res = await fetch("https://fluffy-space-system-x6qqj7rgw4w36qj5-8000.app.github.dev/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: formData
        });

        const data = await res.json();
        console.log("LOGIN RESPONSE:", data);

        if (!res.ok) {
            alert(data.detail || "Login failed");
            return;
        }

        localStorage.setItem("token", data.access_token);

        window.location.href = "profile.html";

    } catch (err) {
        console.error("ERROR:", err);
        alert("Backend not reachable");
    }
}