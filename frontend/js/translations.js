// Bilingual Translation System - English & Hindi
const translations = {
  English: {
    // Navbar & General
    title: "AI Career Advisor",
    logout: "Logout",
    back: "Back",
    continue: "Continue",
    submit: "Submit",
    loading: "Loading...",
    error: "Error",
    success: "Success",
    about: "About",
    
    // Auth Pages
    welcomeBack: "Welcome Back",
    signIn: "Sign In",
    emailAddress: "Email Address",
    enterEmail: "Enter your email",
    password: "Password",
    enterPassword: "Enter your password",
    dontHaveAccount: "Don't have an account?",
    signUpHere: "Sign up here",
    createAccount: "Create Account",
    name: "Name",
    enterName: "Enter your name",
    signUp: "Sign Up",
    alreadyHaveAccount: "Already have an account?",
    loginHere: "Login",
    
    // Profile Page
    completeProfile: "Complete Your Profile",
    helpUnderstand: "Help us understand your background to provide better recommendations",
    stream: "Stream",
    selectStream: "Select your stream",
    science: "Science",
    commerce: "Commerce",
    arts: "Arts",
    classLevel: "Class / Education Level",
    selectClass: "Select your class",
    tenth: "10th",
    eleventh: "11th",
    twelfth: "12th",
    passed: "Passed 12th",
    preferredLanguage: "Preferred Language",
    language: "Language",
    englishLang: "English",
    hindiLang: "हिंदी (Hindi)",
    selectLanguage: "Select Language",
    saveProfile: "Save Profile",
    
    // Psychometric Test
    psychometricTest: "Psychometric Assessment",
    psychometricDescription: "Answer the following questions honestly. There are no right or wrong answers.",
    submitAnswers: "Submit Assessment",
    question: "Question",
    of: "of",
    
    // Subjects Page
    selectSubjects: "Select Your Subjects",
    chooseSubjectsForTest: "Choose the subjects you want to be tested on",
    proceedToTest: "Proceed to Test",
    subjectSelected: "subjects selected",
    selectAtLeast: "Please select at least one subject",
    
    // Evaluation Test
    evaluationTest: "Evaluation Test",
    answerCarefully: "Answer all questions carefully. Select the best option for each question.",
    submitTest: "Submit Answers",
    testNotFound: "Test not found",
    
    // Results Page
    resultsAndRecommendations: "Your Results & Career Recommendations",
    careerRecommendation: "Career Recommendation",
    recommendedCareer: "Recommended Career",
    secondaryOptions: "Secondary Career Options",
    recommendations: "Recommendations",
    examsToConsider: "Exams to Consider",
    feedback: "Feedback",
    score: "Score",
    
    // Messages & Alerts
    loginFailed: "Login failed",
    pleaseEnterBothEmailAndPassword: "Please enter both email and password",
    backendNotReachable: "Backend not reachable. Please check your connection.",
    signupSuccess: "Account created successfully! Please login.",
    profileSaved: "Profile saved successfully!",
    testSubmitted: "Test submitted successfully!",
    assessmentSubmitted: "Assessment submitted successfully!",
    loadingResults: "Loading results...",
    noResults: "No results found",
    sessionExpired: "Session expired. Please login again.",
    allRightsReserved: "All rights reserved.",
    
    // Common
    yes: "Yes",
    no: "No",
    ok: "OK",
    cancel: "Cancel",
    next: "Next",
    previous: "Previous",
    save: "Save",
    update: "Update",
    delete: "Delete",
    search: "Search",
    filter: "Filter",
    reset: "Reset"
  },
  
  Hindi: {
    // Navbar & General
    title: "एआई करियर सलाहकार",
    logout: "लॉगआउट",
    back: "वापस",
    continue: "जारी रखें",
    submit: "जमा करें",
    loading: "लोड हो रहा है...",
    error: "त्रुटि",
    success: "सफल",
    about: "परिचय",
    
    // Auth Pages
    welcomeBack: "स्वागत है",
    signIn: "साइन इन करें",
    emailAddress: "ईमेल पता",
    enterEmail: "अपना ईमेल दर्ज करें",
    password: "पासवर्ड",
    enterPassword: "अपना पासवर्ड दर्ज करें",
    dontHaveAccount: "खाता नहीं है?",
    signUpHere: "यहां साइन अप करें",
    createAccount: "खाता बनाएं",
    name: "नाम",
    enterName: "अपना नाम दर्ज करें",
    signUp: "साइन अप करें",
    alreadyHaveAccount: "पहले से खाता है?",
    loginHere: "लॉगिन",
    
    // Profile Page
    completeProfile: "अपनी प्रोफाइल पूरी करें",
    helpUnderstand: "हमें आपकी पृष्ठभूमि को समझने में मदद करें ताकि हम बेहतर सिफारिशें प्रदान कर सकें",
    stream: "स्ट्रीम",
    selectStream: "अपनी स्ट्रीम चुनें",
    science: "विज्ञान",
    commerce: "वाणिज्य",
    arts: "कला",
    classLevel: "कक्षा / शिक्षा स्तर",
    selectClass: "अपनी कक्षा चुनें",
    tenth: "10वीं",
    eleventh: "11वीं",
    twelfth: "12वीं",
    passed: "12वीं पास की",
    preferredLanguage: "पसंदीदा भाषा",
    language: "भाषा",
    englishLang: "English",
    hindiLang: "हिंदी",
    selectLanguage: "भाषा चुनें",
    saveProfile: "प्रोफाइल सेव करें",
    
    // Psychometric Test
    psychometricTest: "मनोवैज्ञानिक मूल्यांकन",
    psychometricDescription: "निम्नलिखित प्रश्नों का ईमानदारी से उत्तर दें। कोई सही या गलत उत्तर नहीं हैं।",
    submitAnswers: "मूल्यांकन जमा करें",
    question: "प्रश्न",
    of: "का",
    
    // Subjects Page
    selectSubjects: "अपने विषय चुनें",
    chooseSubjectsForTest: "वह विषय चुनें जिन पर आप परीक्षा देना चाहते हैं",
    proceedToTest: "परीक्षा के लिए जारी रखें",
    subjectSelected: "विषय चुने गए",
    selectAtLeast: "कृपया कम से कम एक विषय चुनें",
    
    // Evaluation Test
    evaluationTest: "मूल्यांकन परीक्षा",
    answerCarefully: "सभी प्रश्नों का सावधानीपूर्वक उत्तर दें। प्रत्येक प्रश्न के लिए सर्वश्रेष्ठ विकल्प चुनें।",
    submitTest: "उत्तर जमा करें",
    testNotFound: "परीक्षा नहीं मिली",
    
    // Results Page
    resultsAndRecommendations: "आपके परिणाम और करियर सिफारिशें",
    careerRecommendation: "करियर सिफारिश",
    recommendedCareer: "अनुशंसित करियर",
    secondaryOptions: "माध्यमिक करियर विकल्प",
    recommendations: "सिफारिशें",
    examsToConsider: "विचार करने के लिए परीक्षाएं",
    feedback: "प्रतिक्रिया",
    score: "स्कोर",
    
    // Messages & Alerts
    loginFailed: "लॉगिन विफल",
    pleaseEnterBothEmailAndPassword: "कृपया ईमेल और पासवर्ड दोनों दर्ज करें",
    backendNotReachable: "बैकएंड तक पहुंचने योग्य नहीं। कृपया अपने कनेक्शन की जांच करें।",
    signupSuccess: "खाता सफलतापूर्वक बनाया गया! कृपया लॉगिन करें।",
    profileSaved: "प्रोफाइल सफलतापूर्वक सेव हो गई!",
    testSubmitted: "परीक्षा सफलतापूर्वक जमा कर दी गई!",
    assessmentSubmitted: "मूल्यांकन सफलतापूर्वक जमा कर दिया गया!",
    loadingResults: "परिणाम लोड हो रहे हैं...",
    noResults: "कोई परिणाम नहीं मिला",
    sessionExpired: "सत्र समाप्त हो गया। कृपया फिर से लॉगिन करें।",
    allRightsReserved: "सर्वाधिकार सुरक्षित।",
    
    // Common
    yes: "हां",
    no: "नहीं",
    ok: "ठीक है",
    cancel: "रद्द करें",
    next: "अगला",
    previous: "पिछला",
    save: "सेव करें",
    update: "अपडेट करें",
    delete: "हटाएं",
    search: "खोज",
    filter: "फ़िल्टर",
    reset: "रीसेट करें"
  }
};
