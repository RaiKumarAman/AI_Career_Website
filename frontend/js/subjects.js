let selectedSubjects = [];

async function loadSubjects() {
    const res = await fetch(BASE_URL + "/subjects/suggest", {
        headers: authHeaders()
    });

    const data = await res.json();

    const container = document.getElementById("subjects");

    data.subjects.forEach(sub => {
        container.innerHTML += `
            <input type="checkbox" value="${sub}" onchange="selectSubject(this)">
            ${sub}<br>
        `;
    });
}

function selectSubject(el) {
    if (el.checked) selectedSubjects.push(el.value);
}

async function generateTest() {
    const res = await fetch(BASE_URL + "/test/generate", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify({subjects: selectedSubjects})
    });

    const data = await res.json();

    localStorage.setItem("test", JSON.stringify(data));

    window.location.href = "test.html";
}

loadSubjects();