    async function login() {
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value;

        if (!email || !password) {
            alert("Please enter both email and password");
            return;
        }

        try {
            const res = await fetch(BASE_URL + "/api/auth/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email: email,
                    password: password
                })
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
            alert("Backend not reachable. Please check your connection.");
        }
    }

    function logout() {
        localStorage.removeItem("token");
        window.location.href = "index.html";
    }

    