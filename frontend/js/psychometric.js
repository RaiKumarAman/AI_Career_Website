let questions = [];

async function loadQuestions() {
    const res = await fetch(BASE_URL + "/psychometric/generate", {
        headers: authHeaders()
    });

    const data = await res.json();
    questions = data.questions;

    const container = document.getElementById("questions");

    questions.forEach(q => {
        container.innerHTML += `
            <p>${q.question}</p>
            <input type="number" min="1" max="5" id="q${q.id}">
        `;
    });
}

async function submitTest() {
    const answers = questions.map(q => ({
        question_id: q.id,
        rating: parseInt(document.getElementById("q" + q.id).value)
    }));

    await fetch(BASE_URL + "/psychometric/submit", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify({questions, answers})
    });

    window.location.href = "subjects.html";
}

loadQuestions();