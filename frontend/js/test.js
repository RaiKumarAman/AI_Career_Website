let testData = JSON.parse(localStorage.getItem("test"));

function loadTest() {
    const container = document.getElementById("test");
    container.innerHTML = "";

    testData.questions.forEach((q, i) => {
        const questionDiv = document.createElement("div");
        questionDiv.className = "question";
        
        let optionsHTML = q.options.map(opt => `
            <label class="option">
                <input type="radio" name="q${i}" value="${opt}">
                <span>${opt}</span>
            </label>
        `).join("");

        questionDiv.innerHTML = `
            <strong>Q${i + 1}: ${q.question}</strong>
            ${optionsHTML}
        `;
        
        container.appendChild(questionDiv);
    });
}

async function submitTest() {
    const user_answers = {};
    let allAnswered = true;

    testData.questions.forEach((q, i) => {
        const selected = document.querySelector(`input[name="q${i}"]:checked`);
        if (selected) {
            user_answers[i] = selected.value;
        } else {
            allAnswered = false;
        }
    });

    if (!allAnswered) {
        alert("Please answer all questions before submitting!");
        return;
    }

    try {
        const res = await fetch(BASE_URL + "/test/submit", {
            method: "POST",
            headers: authHeaders(),
            body: JSON.stringify({
                test_id: testData.test_id,
                user_answers: user_answers
            })
        });

        if (!res.ok) {
            const error = await res.json();
            alert("Error: " + (error.detail || "Failed to submit test"));
            return;
        }

        const data = await res.json();
        localStorage.setItem("response", JSON.stringify(data));
        localStorage.setItem("testId", testData.test_id);

        window.location.href = "result.html";
    } catch (err) {
        console.error("ERROR:", err);
        alert("Failed to submit test");
    }
}

loadTest();