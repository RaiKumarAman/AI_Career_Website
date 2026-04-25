async function signup() {
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    if (!name || !email || !password) {
        alert("Please fill all fields");
        return;
    }

    try {
        const res = await fetch(BASE_URL + "/api/auth/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                email: email,
                password: password
            })
        });

        const data = await res.json();
        console.log("SIGNUP RESPONSE:", data);

        if (!res.ok) {
            alert(data.detail || "Signup failed");
            return;
        }

        // 🔥 store token (since backend returns it)
        localStorage.setItem("token", data.access_token);

        // 🔥 redirect to profile setup
        window.location.href = "profile.html";

    } catch (err) {
        console.error("ERROR:", err);
        alert("Backend not reachable. Please check your connection.");
    }
}