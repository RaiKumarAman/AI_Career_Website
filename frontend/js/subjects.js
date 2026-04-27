let selectedSubjects = [];

async function loadSubjects() {
    try {
        const res = await fetch(BASE_URL + "/subjects/suggest", {
            headers: authHeaders()
        });

        if (!res.ok) {
            throw new Error("Failed to load subjects");
        }

        const data = await res.json();
        const container = document.getElementById("subjects");
        container.innerHTML = "";

        data.subjects.forEach(sub => {
            const label = document.createElement("label");
            label.className = "checkbox-item";
            label.innerHTML = `
                <input type="checkbox" value="${sub}" onchange="selectSubject(this)">
                <span>${sub}</span>
            `;
            container.appendChild(label);
        });
    } catch (err) {
        console.error("ERROR:", err);
        document.getElementById("subjects").innerHTML = "<p class='text-danger'>Failed to load subjects</p>";
    }
}

function selectSubject(el) {
    if (el.checked) {
        selectedSubjects.push(el.value);
    } else {
        selectedSubjects = selectedSubjects.filter(s => s !== el.value);
    }
}

async function generateTest() {
    if (selectedSubjects.length === 0) {
        alert("Please select at least one subject!");
        return;
    }

    try {
        const language = getLanguageParam();
        const res = await fetch(BASE_URL + "/test/generate?language=" + language, {
            method: "POST",
            headers: authHeaders(),
            body: JSON.stringify({subjects: selectedSubjects})
        });

        if (!res.ok) {
            const error = await res.json();
            alert("Error: " + (error.detail || "Failed to generate test"));
            return;
        }

        const data = await res.json();
        localStorage.setItem("test", JSON.stringify(data));
        window.location.href = "test.html";
    } catch (err) {
        console.error("ERROR:", err);
        alert("Failed to generate test");
    }
}

function logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("test");
    window.location.href = "index.html";
}

function displayUserName() {
    const userNameEl = document.getElementById("user-name");
    if (userNameEl) {
        userNameEl.textContent = "User";
    }
}

loadSubjects();
displayUserName();