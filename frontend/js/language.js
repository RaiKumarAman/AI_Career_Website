// Language Manager - Handles language switching, persistence, and UI updates
class LanguageManager {
  constructor() {
    this.currentLanguage = localStorage.getItem('language') || 'English';
    this.initLanguage();
  }

  // Initialize language on page load
  initLanguage() {
    this.applyLanguage(this.currentLanguage);
  }

  // Get current language
  getLanguage() {
    return this.currentLanguage;
  }

  // Set and save language preference
  setLanguage(lang) {
    if (lang === 'English' || lang === 'Hindi') {
      this.currentLanguage = lang;
      localStorage.setItem('language', lang);
      this.applyLanguage(lang);
      // Notify all pages about language change
      window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
      return true;
    }
    return false;
  }

  // Apply translations to all elements with data-key attribute
  applyLanguage(lang) {
    // Update all elements with data-key attribute
    document.querySelectorAll('[data-key]').forEach(el => {
      const key = el.getAttribute('data-key');
      if (translations[lang] && translations[lang][key]) {
        const translatedText = translations[lang][key];

        // Handle different element types
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
          // For input and textarea, set placeholder and value for buttons
          if (el.type === 'button' || el.tagName === 'BUTTON') {
            el.innerText = translatedText;
          } else {
            el.placeholder = translatedText;
          }
        } else if (el.tagName === 'OPTION') {
          // For select options
          el.innerText = translatedText;
        } else if (el.tagName === 'LABEL') {
          // For labels
          el.innerText = translatedText;
        } else {
          // For all other elements (headings, paragraphs, buttons, etc.)
          el.innerText = translatedText;
        }
      } else {
        console.warn(`Translation missing for key: ${key} in language: ${lang}`);
      }
    });

    // Update document language attribute for proper text rendering
    document.documentElement.lang = lang === 'Hindi' ? 'hi' : 'en';

    // Add class for styling based on language (useful for RTL or specific styling)
    document.documentElement.setAttribute('data-language', lang);
  }

  // Get translated text for a key
  getText(key) {
    return translations[this.currentLanguage]?.[key] || key;
  }

  // Format message with translations
  formatMessage(templateKey, variables = {}) {
    let message = this.getText(templateKey);
    Object.keys(variables).forEach(key => {
      message = message.replace(`{${key}}`, variables[key]);
    });
    return message;
  }
}

// Initialize language manager globally
const languageManager = new LanguageManager();

// Auto-initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  languageManager.initLanguage();

  // Set up language selector if it exists
  const languageSelector = document.getElementById('languageSelector');
  if (languageSelector) {
    languageSelector.value = languageManager.getLanguage();
    languageSelector.addEventListener('change', (e) => {
      languageManager.setLanguage(e.target.value);
      // Reload page to ensure all JS renders with new language
      location.reload();
    });
  }
});

// Listen for language changes from other tabs/windows
window.addEventListener('storage', (e) => {
  if (e.key === 'language' && e.newValue !== languageManager.getLanguage()) {
    languageManager.currentLanguage = e.newValue;
    languageManager.applyLanguage(e.newValue);
  }
});

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = LanguageManager;
}
