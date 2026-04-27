const BASE_URL = "http://127.0.0.1:8000";

function getToken() {
    return localStorage.getItem("token");
}

function authHeaders() {
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + getToken()
    };
}

// Get current language for API requests
function getLanguageParam() {
    return languageManager?.getLanguage() || localStorage.getItem('language') || 'English';
}