async function loadResult() {
    const testId = localStorage.getItem("testId");
    const response = JSON.parse(localStorage.getItem("response"));

    if (!testId || !response) {
        document.getElementById("result").innerHTML = "<div class='card'><p class='text-danger'>Error: No test results found.</p></div>";
        return;
    }

    try {
        const res = await fetch(BASE_URL + `/test/results/${testId}`, {
            headers: authHeaders()
        });

        if (!res.ok) {
            throw new Error("Failed to fetch results");
        }

        const data = await res.json();

        const passStatus = data.passed ? 
            '<span class="result-status passed">✓ PASSED</span>' : 
            '<span class="result-status failed">✗ FAILED</span>';

        let examsHTML = data.exams && data.exams.length > 0 
            ? `<p><strong>Recommended Exams:</strong> ${data.exams.join(", ")}</p>`
            : "";

        let secondaryCareerHTML = data.secondary_careers && data.secondary_careers.length > 0
            ? `<p><strong>Alternative Career Paths:</strong> ${data.secondary_careers.join(", ")}</p>`
            : "";

        const resultHTML = `
            <div class="result-card mb-24">
                <div class="result-header">
                    <div>
                        <h2>Test Results</h2>
                    </div>
                    <div>${passStatus}</div>
                </div>

                <div class="grid-2">
                    <div class="result-metric">
                        <strong>${response.score}/${response.total}</strong>
                        <span>Questions Correct</span>
                    </div>
                    <div class="result-metric">
                        <strong>${response.accuracy}</strong>
                        <span>Accuracy</span>
                    </div>
                </div>

                <p><strong>Performance Analysis:</strong></p>
                <p class="text-muted">${response.feedback}</p>
            </div>

            <div class="result-card mb-24">
                <h3>Career Recommendation</h3>
                <p><strong>Suggested Career Path:</strong></p>
                <p class="text-muted">${data.career || "Based on your assessment results"}</p>
                ${secondaryCareerHTML}
                ${examsHTML}
                <p style="margin-top: 16px;"><strong>Why This Career?</strong></p>
                <p class="text-muted">${data.feedback || "This career aligns with your test performance and profile."}</p>
            </div>

            <div class="flex-between gap-20" style="flex-wrap: wrap;">
                <button class="btn btn-secondary" onclick="window.location.href='subjects.html'">
                    Take Another Test
                </button>
                <button class="btn btn-secondary" onclick="window.location.href='profile.html'">
                    Back to Profile
                </button>
                <button class="btn btn-success" onclick="downloadResults()">
                    Download Results
                </button>
            </div>
        `;

        document.getElementById("result").innerHTML = resultHTML;
    } catch (err) {
        console.error("ERROR:", err);
        document.getElementById("result").innerHTML = "<div class='card'><p class='text-danger'>Error loading results. Please try again.</p></div>";
    }
}

function downloadResults() {
    const testId = localStorage.getItem("testId");
    alert("Download feature coming soon! Test ID: " + testId);
}

loadResult();