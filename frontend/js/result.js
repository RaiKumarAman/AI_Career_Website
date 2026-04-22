async function loadResult() {
    const testData = JSON.parse(localStorage.getItem("test"));

    const res = await fetch(BASE_URL + "/recommend", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify({test_id: testData.test_id})
    });

    const data = await res.json();

    document.getElementById("result").innerHTML = `
        <h3>${data.career}</h3>
        <p>${data.feedback}</p>
        <p>Exams: ${data.exams.join(", ")}</p>
    `;
}

loadResult();