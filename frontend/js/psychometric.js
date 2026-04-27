let questions = [];

async function loadQuestions() {
    try {
        const language = getLanguageParam();
        const res = await fetch(BASE_URL + "/psychometric/generate?language=" + language, {
            headers: authHeaders()
        });

        if (!res.ok) {
            throw new Error("Failed to load questions");
        }

        const data = await res.json();
        questions = data.questions;

        const container = document.getElementById("questions");
        container.innerHTML = "";

        questions.forEach((q, idx) => {
            const questionDiv = document.createElement("div");
            questionDiv.className = "question";
            
            questionDiv.innerHTML = `
                <strong>Q${idx + 1}: ${q.question}</strong>
                <div class="form-group">
                    <label for="q${q.id}">Rate your level of agreement (1-5)</label>
                    <input type="range" id="q${q.id}" min="1" max="5" value="3" class="form-range">
                    <div class="flex-between gap-12" style="margin-top: 8px; font-size: 0.9rem; color: #94a3b8;">
                        <span>Strongly Disagree</span>
                        <span id="val${q.id}">3</span>
                        <span>Strongly Agree</span>
                    </div>
                </div>
            `;
            
            container.appendChild(questionDiv);

            document.getElementById("q" + q.id).addEventListener("change", (e) => {
                document.getElementById("val" + q.id).textContent = e.target.value;
            });
        });
    } catch (err) {
        console.error("ERROR:", err);
        document.getElementById("questions").innerHTML = "<p class='text-danger'>Failed to load psychometric questions</p>";
    }
}

async function submitTest() {
    const answers = questions.map(q => ({
        question_id: q.id,
        rating: parseInt(document.getElementById("q" + q.id).value)
    }));

    try {
        const res = await fetch(BASE_URL + "/psychometric/submit", {
            method: "POST",
            headers: authHeaders(),
            body: JSON.stringify({questions, answers})
        });

        if (!res.ok) {
            const error = await res.json();
            alert("Error: " + (error.detail || "Failed to submit assessment"));
            return;
        }

        window.location.href = "subjects.html";
    } catch (err) {
        console.error("ERROR:", err);
        alert("Failed to submit assessment");
    }
}

function goBack() {
    window.location.href = "profile.html";
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

loadQuestions();
displayUserName();