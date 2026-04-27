async function saveProfile() {
    const stream = document.getElementById("stream").value;
    const class_level = document.getElementById("class").value;
    const language = getLanguageParam();

    if (!stream || !class_level) {
        alert("Please select both stream and class level");
        return;
    }

    try {
        const res = await fetch(BASE_URL + "/user/profile", {
            method: "POST",
            headers: authHeaders(),
            body: JSON.stringify({stream, class_level, language})
        });

        if (!res.ok) {
            const error = await res.json();
            alert("Error: " + (error.detail || "Failed to save profile"));
            return;
        }

        window.location.href = "psychometric.html";
    } catch (err) {
        console.error("ERROR:", err);
        alert("Failed to save profile");
    }
}

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

function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}

function displayUserName() {
    const userNameEl = document.getElementById("user-name");
    if (userNameEl) {
        userNameEl.textContent = "User";
    }
}

displayUserName();