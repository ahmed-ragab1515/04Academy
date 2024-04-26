// Define global variable for base URL
const baseURL = "http://localhost:8000/";
// ================ Open and Close Mobile Menu ================
document.querySelector(".mobile-menu__close").addEventListener("click", () => {
  document.querySelector(".mobile-menu").classList.toggle("toggle");
  document.querySelector(".overlay").classList.toggle("show");
});

document.querySelectorAll(".header__menu-toggle").forEach((item) => {
  item.addEventListener("click", () => {
    document.querySelector(".mobile-menu").classList.toggle("toggle");
    document.querySelector(".overlay").classList.toggle("show");
  });
});

// ================ Open and Close Mobile Submenu ================
document.querySelector(".mobile__expand-icon").addEventListener("click", () => {
  document.querySelector(".mobile__submenu").classList.toggle("open");
});

// ================ Get The Current Year ================
const currentYear = new Date().getFullYear();
document.getElementById("current-year").innerHTML = currentYear;

// ================ Activate Progress bar ================
const steps = document.querySelectorAll(".steps-names > span");
const progressBar = document.querySelector(".progress-bar");
const nextBtn = document.getElementById("next-btn");

const oneSpan = steps[0];
let spanStyle = window.getComputedStyle(oneSpan);
const widthStep = parseInt(spanStyle.width);

progressBar.style.width = `${widthStep / 2}px`;

// ================= Hide Input Label =================
const inputFields = document.querySelectorAll(".step__input");

inputFields.forEach((item) => {
  item.addEventListener("input", () => {
    if (item.value.trim() !== "") {
      item.parentElement.classList.remove("error");
      item.parentElement.querySelector(".step__label--one").style.visibility =
        "hidden";
    } else {
      item.parentElement.querySelector(".step__label--one").style.visibility =
        "visible";
    }
  });
});

// ================= Open & Close Step Menu =================
const selectContainers = document.querySelectorAll(
  ".step__input-container--select"
);
const options = document.querySelectorAll(".step__menu-option");

for (let i = 0; i < selectContainers.length; i++) {
  const selectContainer = selectContainers[i];
  selectContainer.addEventListener("click", () => {
    selectContainer.querySelector(".step__menu").classList.toggle("show");
    selectContainer.querySelector(".step__icon").classList.toggle("rotate");
  });
}

for (let i = 0; i < options.length; i++) {
  const option = options[i];
  const optionsList = option.parentElement;

  option.addEventListener("click", (e) => {
    e.stopPropagation();
    if (optionsList.classList.contains("show")) {
      option.parentElement.classList.remove("show");
      optionsList.parentElement
        .querySelector(".step__icon")
        .classList.remove("rotate");

      optionsList.parentElement.querySelector(".step__hidden-input").value =
        option.dataset.value;
      optionsList.parentElement.querySelector(".step__label--one").innerHTML =
        option.dataset.value;
      optionsList.parentElement.querySelector(".step__label--one").style.color =
        "var(--primary-color)";
      optionsList.parentElement.classList.remove("error");
    }
  });
}

const paymentFields = document.querySelectorAll(".payment__input-field");

paymentFields.forEach((item) => {
  item.addEventListener("input", () => {
    if (!isEmpty(item.value)) {
      item.parentElement.classList.remove("error");
    }
  });
});
// ================= Validate Form =================
const submit_btn = document.getElementById("submit-btn");
submit_btn.addEventListener("click", (e) => {
  e.preventDefault();
  const rulesCheckBox = document.querySelector("#rules");

  let isValid = true;

  paymentFields.forEach((item) => {
    if (isEmpty(item.value)) {
      item.parentElement.classList.add("error");
      isValid = false;
    }
  });

  if (!rulesCheckBox.checked) {
    rulesCheckBox.classList.add("error");
    isValid = false;
  }

  if (isValid) {
    updateProgressBar();
    goToNextStep(7);
    const form = document.querySelector("#contact_form");
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    updateFormData(3, data);
    updateFormData(4, data);
    updateFormData(5, data);
    console.log(data);
  }
});


const radioOptions = document.querySelectorAll(".step__label--radio");
radioOptions.forEach((item) => {
  item.addEventListener("click", () => {
    item.parentElement.parentElement.querySelector(".error-msg").style.display =
      "none";
    item.parentElement.querySelector(".hidden-input").value =
      item.dataset.value;
  });
});

const checkboxOptions = document.querySelectorAll(".step__label--checkbox");

checkboxOptions.forEach((item) => {
  item.addEventListener("click", () => {
    item.parentElement.parentElement.querySelector(".error-msg").style.display =
      "none";
  });
});

// ================= Utility Functions =================
function getStepFields(num) {
  const step = document.getElementById(`step${num}`);
  let fields;
  if (num === 3 || num === 4 || num === 5) {
    fields = step.querySelectorAll(".step__checkbox");
  } else {
    fields = step.querySelectorAll(
      ".step__input, .step__hidden-input, .step__radio, .step__checkbox, .payment__input-field"
    );
  }

  return fields;
}

function updateProgressBar() {
  progressBar.style.width = `${
    parseInt(progressBar.style.width) + widthStep + 3
  }px`;
}

function showErrorMsg(name) {
  const errorMsg = document.getElementById(`${name}__error-msg`);
  errorMsg.textContent = errorMsg.dataset.msg;
  errorMsg.style.display = "block";
}

function updateFormData(stepNumber, data) {
  const fields = getStepFields(stepNumber);
  let collectedData = [];
  let currentName;
  fields.forEach((item) => {
    currentName = item.name
    if (item.checked === true) {
      collectedData.push(item.value);
    }
  });
  if (collectedData.length === 0) {
    showErrorMsg(currentName);
    isValid = false;
  } else {
    data[currentName] = collectedData;
  }
}


function isEmpty(value) {
  return value.trim() === "";
}

function addErrorClass(id) {
  const containerWithError = document.querySelector(
    `.step__input-container input#${id}`
  ).parentElement;
  containerWithError.classList.add("error");
}

function validateEmail(email) {
  const re =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

function goToNextStep(currentStep) {
  const currentStepElement = document.getElementById(`step${currentStep}`);
  const nextStepElement = document.getElementById(`step${currentStep + 1}`);

  currentStepElement.style.display = "none";
  nextStepElement.style.display = "flex";
}

// ================= Validate Step =================
function validateStep(stepNumber) {
  const step = document.getElementById(`step${stepNumber}`);
  const fields = getStepFields(stepNumber);

  let isValid = true;

  for (let item of fields) {
    switch (item.name) {
      case "first_name":
      case "last_name":
      case "age":
      case "gender":
      case "nationality":
      case "whatsapp":
      case "email":
      case "difficulties":
        if (isEmpty(item.value)) {
          addErrorClass(item.name);
          isValid = false;
        }
        break;

      case "email":
        if (!validateEmail(item.value)) {
          addErrorClass(item.name);
          isValid = false;
        }
        break;

      case "level":
      case "class":
      case "curriculum":
      case "students":
      case "time_period":
      case "time":
      case "session":
      case "hours":
      case "subscription":
        const hiddenInput = step.querySelector(`#${item.name}__hidden-input`);
        if (hiddenInput && isEmpty(hiddenInput.value)) { // Add a check for hiddenInput
        // if (isEmpty(hiddenInput.value)) {
          showErrorMsg(item.name);
          isValid = false;
        }
        break;

      case "goals":
      case "days":
      case "subjects":
        const checkedFields = Array.from(fields).filter(item => item.checked);
        if (checkedFields.length === 0) {
          showErrorMsg(item.name);
          isValid = false;
        }
    }


  }

  if (isValid && stepNumber === 1) {
    fetchEducationalLevels();
    fetchClassLevels();
    fetchCurriculumList();
  }

  if (isValid && stepNumber === 2) {
    fetchSubjects();
  }

  if (isValid && stepNumber === 3) {
    fetchStudentCountData();
    fetchStudyGoalData();
  }

  if (isValid && stepNumber === 4) {
    fetchDaysData();
    fetchTimePeriodData();
    fetchTimeData();
  }

  if (isValid && stepNumber === 5) {
    fetchSessionFrequencyData();
    fetchSessionDurationData();
    fetchSubscriptionPlanData();
  }

  if (isValid) {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });

    updateProgressBar();

    goToNextStep(stepNumber);
  }
}



function fetchEducationalLevels() {
  fetch(baseURL+'GetEducationalLevelList/')
      .then(response => response.json())
      .then(data => {
          const levelOptions = document.querySelector('#level__options');
          data.data.forEach(level => {
              const label = document.createElement('label');
              label.setAttribute('for', `level${level.id}`);
              label.classList.add('step__label-box', 'step__label', 'step__label--radio');
              label.setAttribute('data-value', level.name);
              label.innerHTML = `
                  <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
                  ${level.name}
                  <input type="radio" id="level${level.id}" name="level" value="${level.id}" class="step__radio" />
              `;
              label.addEventListener('change', () => {
                  const selectedId = parseInt(label.querySelector('input').id.replace('level', ''));
                  console.log(selectedId);
              });
              levelOptions.appendChild(label);
          });
          document.getElementById('level__error-msg').setAttribute('data-msg', 'برجاء اختيار المرحلة الدراسية');
      })
      .catch(error => console.error('Error fetching educational levels:', error));
}

function fetchClassLevels() {
  fetch(baseURL+'GetClassLevelList/')
      .then(response => response.json())
      .then(data => {
          const classOptions = document.querySelector('#class__options');
          data.data.forEach(level => {
              const label = document.createElement('label');
              label.setAttribute('for', `class${level.id}`);
              label.classList.add('step__label-box', 'step__label', 'step__label--radio');
              label.setAttribute('data-value', level.name);
              label.innerHTML = `
                  <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
                  ${level.name}
                  <input type="radio" id="class${level.id}" name="class" value="${level.id}" class="step__radio" />
              `;
              classOptions.appendChild(label);
          });
          document.getElementById('class__error-msg').setAttribute('data-msg', 'برجاء اختيار الصف الدراسي');
      })
      .catch(error => console.error('Error fetching class levels:', error));
}

function fetchCurriculumList() {
  fetch(baseURL+'GetCurriculumList/')
      .then(response => response.json())
      .then(data => {
          const curriculumOptions = document.querySelector('#curriculum__options');
          data.data.forEach(curriculum => {
              const label = document.createElement('label');
              label.setAttribute('for', `curriculum${curriculum.id}`);
              label.classList.add('step__label-box', 'step__label', 'step__label--radio');
              label.setAttribute('data-value', curriculum.name);
              label.innerHTML = `
                  <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
                  ${curriculum.name}
                  <input type="radio" id="curriculum${curriculum.id}" name="curriculum" value="${curriculum.id}" class="step__radio" />
              `;
              curriculumOptions.appendChild(label);
          });
          document.getElementById('curriculum__error-msg').setAttribute('data-msg', 'برجاء تحديد المنهج الدراسي');
      })
      .catch(error => console.error('Error fetching curriculum list:', error));
}

function fetchSubjects() {
  fetch(baseURL+'GetSubjectList/')
    .then(response => response.json())
    .then(data => {
      const subjectsContainer = document.querySelector('#step3 .step__options');
      data.data.forEach(subject => {
        const label = document.createElement('label');
        label.setAttribute('for', `subject${subject.id}`);
        label.classList.add('step__label-box', 'step__label', 'step__label--checkbox');
        label.setAttribute('data-value', subject.name);
        const imageUrl = `http://localhost:8000${subject.image}`; // Prepend base URL
        label.innerHTML = `
          <img src="${imageUrl}" alt="${subject.name}" class="subject-img" />
          ${subject.name}
          <input type="checkbox" id="subject${subject.id}" name="subjects" value="${subject.id}" class="step__checkbox" />
        `;
        subjectsContainer.appendChild(label);
      });
    })
    .catch(error => console.error('Error fetching subjects:', error));
}

function fetchStudentCountData() {
  fetch(baseURL+'GetStudentCountList/')
    .then(response => response.json())
    .then(data => {
      const studentsOptions = document.getElementById('students__options');
      data.data.forEach(studentCount => {
        const label = document.createElement('label');
        label.setAttribute('for', `number${studentCount.id}`);
        label.classList.add('step__label-box', 'step__label', 'step__label--radio');
        label.setAttribute('data-value', studentCount.count);
        label.innerHTML = `
          <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
          ${studentCount.count}
          <input type="radio" id="number${studentCount.id}" name="students" value="${studentCount.id}" class="step__radio" />
        `;
        studentsOptions.appendChild(label);
      });
    })
    .catch(error => console.error('Error fetching student count data:', error));
}

function fetchStudyGoalData() {
  fetch(baseURL+'GetStudyGoalList/')
    .then(response => response.json())
    .then(data => {
      const goalsOptions = document.getElementById('goals__options');
      data.data.forEach(goal => {
        const label = document.createElement('label');
        label.setAttribute('for', `goal${goal.id}`);
        label.classList.add('step__label-box', 'step__label', 'step__label--checkbox');
        label.setAttribute('data-value', goal.goal);
        label.innerHTML = `
          <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
          ${goal.goal}
          <input type="checkbox" id="goal${goal.id}" name="goals" value="${goal.id}" class="step__checkbox" />
        `;
        goalsOptions.appendChild(label);
      });
    })
    .catch(error => console.error('Error fetching study goal data:', error));
}

function fetchDaysData() {
  fetch(baseURL+'GetDaysList/')
    .then(response => response.json())
    .then(data => {
      const daysOptions = document.getElementById('days__options');
      data.data.forEach(day => {
        const label = document.createElement('label');
        label.setAttribute('for', `day${day.id}`);
        label.classList.add('step__label-box', 'step__label', 'step__label--checkbox');
        label.setAttribute('data-value', day.name);
        label.innerHTML = `
          <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
          ${day.name}
          <input type="checkbox" id="day${day.id}" name="days" value="${day.id}-${day.name}" class="step__checkbox" />
        `;
        daysOptions.appendChild(label);
      });
    })
    .catch(error => console.error('Error fetching days data:', error));
}

function fetchTimePeriodData() {
  const timePeriodData = [
    { id:'الفترة الصباحية', value: 'الفترة الصباحية' },
    { id: 'الفترة المسائية', value: 'الفترة المسائية' }
  ];

  const timePeriodOptions = document.getElementById('time_period__options');
  if (timePeriodOptions) {
    timePeriodData.forEach((period, index) => {
      const label = document.createElement('label');
      label.setAttribute('for', `period${index + 1}`);
      label.classList.add('step__label-box', 'step__label', 'step__label--radio');
      label.setAttribute('data-value', period.value);
      label.innerHTML = `
        <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
        ${period.value}
        <input type="radio" id="period${index + 1}" name="time_period" value="${period.value}" class="step__radio" />
      `;
      timePeriodOptions.appendChild(label);
    });
  } else {
    console.error('Element with ID "time_period__options" not found.');
  }
}

function fetchTimeData() {
  fetch(baseURL+'GetSuitableTimingList/')
    .then(response => response.json())
    .then(data => {
      const timeOptions = document.getElementById('time__options');
      data.data.forEach(time => {
        const label = document.createElement('label');
        label.setAttribute('for', `time${time.id}`);
        label.classList.add('step__label-box', 'step__label', 'step__label--radio');
        label.setAttribute('data-value', time.time);
        label.innerHTML = `
          <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
          ${time.time}
          <input type="radio" id="time${time.id}" name="time" value="${time.id}" class="step__radio" />
        `;
        timeOptions.appendChild(label);
      });
    })
    .catch(error => console.error('Error fetching time data:', error));
}

function fetchSessionFrequencyData() {
  fetch(baseURL+'GetSessionFrequencyList/')
    .then(response => response.json())
    .then(data => {
      const sessionOptions = document.getElementById('session__options');
      data.data.forEach(item => {
        const label = document.createElement('label');
        label.setAttribute('for', `session${item.id}`);
        label.classList.add('step__label-box', 'step__label', 'step__label--radio');
        label.setAttribute('data-value', item.name);
        label.innerHTML = `
          <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
          ${item.name}
          <input type="radio" id="session${item.id}" name="session" value="${item.id}-${item.name}" class="step__radio" />
        `;
        sessionOptions.appendChild(label);
      });
    })
    .catch(error => console.error('Error fetching session frequency data:', error));
}

function fetchSessionDurationData() {
  fetch(baseURL+'GetSessionDurationList/')
    .then(response => response.json())
    .then(data => {
      const hoursOptions = document.getElementById('hours__options');
      data.data.forEach((item, index) => {
        const label = document.createElement('label');
        label.setAttribute('for', `hour${index + 1}`);
        label.classList.add('step__label-box', 'step__label', 'step__label--radio');
        label.setAttribute('data-value', item.name);
        label.innerHTML = `
          <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
          ${item.name}
          <input type="radio" id="hour${index + 1}" name="hours" value="${item.id}" class="step__radio" />
        `;
        hoursOptions.appendChild(label);
      });
    })
    .catch(error => console.error('Error fetching session duration data:', error));
}

function fetchSubscriptionPlanData() {
  fetch(baseURL+'GetSubscriptionPlanList/')
    .then(response => response.json())
    .then(data => {
      const subscriptionOptions = document.getElementById('subscription__options');
      data.data.forEach((item, index) => {
        const label = document.createElement('label');
        label.setAttribute('for', `plan${index + 1}`);
        label.classList.add('step__label-box', 'step__label', 'step__label--radio', 'subscription_label');
        label.setAttribute('data-value', item.name);
        label.innerHTML = `
          <img src="./assets/images/correct-icon.svg" alt="correct icon" class="correct-icon" />
          <span class="subscription_discount">خصم ${item.discount}%</span>
          <span>${item.name}</span>
          <span class="subscription_duration">${item.duration}</span>
          <span class="subscription_price">${item.price} درهم</span>
          <input type="radio" id="plan${index + 1}" name="subscription" value="${item.id}" class="step__radio" />
        `;
        subscriptionOptions.appendChild(label);
      });
    })
    .catch(error => console.error('Error fetching subscription plan data:', error));
}

function postData() {
  // Gather form data
  var formData = {
      first_name: document.getElementById("first_name").value,
      last_name: document.getElementById("last_name").value,
      age: parseInt(document.getElementById("age").value),
      gender: document.getElementById("gender").value,
      nationality: document.getElementById("nationality").value,
      whatsapp_number: document.getElementById("whatsapp").value,
      email: document.getElementById("email").value,
      difficulties: document.getElementById("difficulties").value === "نعم" ? true : false,
      notes: document.getElementById("notes").value,
      educational_level: getSelectedId("level__options"),
      class_level: getSelectedId("class__options"),
      curriculum: getSelectedId("curriculum__options"),
      subjects: Array.from(document.querySelectorAll("#subjects__options input[type=checkbox]:checked")).map(function(subject) {
          return parseInt(subject.value);
      }),
      student_count: getSelectedId("students__options"),
      goals: Array.from(document.querySelectorAll("#goals__options input[type=checkbox]:checked")).map(function(goal) {
          return parseInt(goal.value);
      }),
      suitable_day: Array.from(document.querySelectorAll("#days__options input[type=checkbox]:checked")).map(function(suitable_day) {
        return parseInt(suitable_day.value);
      }),
      time_period: getSelectedRadioValue("time_period__options"),
      suitable_timing: getSelectedId("time__options"),
      session_frequency: getSelectedId("session__options"),
      session_duration: getSelectedId("hours__options"),
      subscription_plan: getSelectedId("subscription__options"),
      card_number: document.querySelector("input[name='card_number']").value,
      security_code: document.querySelector("input[name='security_code']").value,
      expiration_date: document.querySelector("input[name='expiration_date']").value,
      card_name: document.querySelector("input[name='card_name']").value
  };

  // Make POST request
  fetch(baseURL+'StudentApplicationOp/add/', {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      return response.json();
  })
  .then(data => {
      console.log("data is >>> ",data); // Handle success response from server
  })
  .catch(error => {
      console.error('There was a problem with your fetch operation:', error);
  });
}

function getSelectedId(containerId) {
  const options = document.querySelectorAll(`#${containerId} input[type="radio"]`);
  let selectedId = null;
  options.forEach(input => {
      if (input.checked) {
          console.log(`Selected ID for ${containerId}:`, input.value);
          selectedId = parseInt(input.value);
      }
  });
  return selectedId;
}

function getSelectedRadioValue(containerId) {
  const radios = document.querySelectorAll(`#${containerId} input[type="radio"]:checked`);
  return radios.length > 0 ? radios[0].value : null;
}
