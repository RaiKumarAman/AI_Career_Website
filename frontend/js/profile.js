async function saveProfile() {
    const stream = document.getElementById("stream").value;
    const class_level = document.getElementById("class").value;
    const language = document.getElementById("language").value;

    await fetch(BASE_URL + "/user/profile", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify({stream, class_level, language})
    });

    window.location.href = "psychometric.html";
}