function nextScreen(screenId) {
    const currentScreen = document.querySelector('.container:not([style*="display: none"])');
    currentScreen.style.display = 'none';
    document.getElementById(screenId).style.display = 'block';
}

function prevScreen(screenId) {
    const currentScreen = document.querySelector('.container:not([style*="display: none"])');
    currentScreen.style.display = 'none';
    document.getElementById(screenId).style.display = 'block';
}

function feedback(response) {
    alert(`Feedback: ${response}`);
}

function nextScreenByGender() {
    const genderSelect = document.getElementById('gender-select');
    const selectedGender = genderSelect.value;
    if (selectedGender === 'male') {
        nextScreen('male_screen');
    } else if (selectedGender === 'female') {
        nextScreen('female_screen');
    } else {
        alert('Please select a gender');
    }
}

function reviewSymptoms() {
    const selectedSymptoms = document.querySelectorAll('input[name="symptom"]:checked');
    const symptomList = document.getElementById('selected-symptoms');
    symptomList.innerHTML = Array.from(selectedSymptoms).map(symptom => symptom.value).join(', ');
    nextScreen('symptom_review');
}

document.getElementById('woundImage').addEventListener('change', function() {
    var form = document.getElementById('uploadForm');
    var formData = new FormData(form);
    fetch('/predict/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').innerText = 'Error: ' + data.error;
        } else {
            document.getElementById('result').innerText = 'Prediction: ' + data.result;
        }
    })
    .catch(error => {
        document.getElementById('result').innerText = 'Error: ' + error;
    });
});
