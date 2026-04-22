let testData = JSON.parse(localStorage.getItem("test"));

function loadTest() {
    const container = document.getElementById("test");

    testData.questions.forEach((q, i) => {
        container.innerHTML += `
            <p>${q.question}</p>
            ${q.options.map(opt => `
                <input type="radio" name="q${i}" value="${opt}">${opt}
            `).join("")}
        `;
    });
}

async function submitTest() {
    const answers = testData.questions.map((q, i) => {
        const selected = document.querySelector(`input[name="q${i}"]:checked`);
        return {
            question: q.question,
            selected_option: selected ? selected.value : ""
        };
    });

    await fetch(BASE_URL + "/test/submit", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify({
            test_id: testData.test_id,
            answers
        })
    });

    window.location.href = "result.html";
}

loadTest();