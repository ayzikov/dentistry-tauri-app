// Импорт fetch из плагина Tauri
import { fetch } from '@tauri-apps/plugin-http';

// Импорт конфигурации API
import { API_ENDPOINTS } from '../url.config.dev';

// Интерфейс для данных пациента
interface PatientDetails {
  patient: {
    id: number;
    first_name: string;
    last_name: string;
    middle_name: string;
    birthdate: string;
    registration_date: string;
    other_info: string;
  };
  ohis_value: number | null;
  pi_value: number | null;
  pma_value: number | null;
  cpitn_value: number | null;
  cpu_value: number | null;
}

// Получение ID пациента из URL
function getPatientId(): number | null {
  const urlParams = new URLSearchParams(window.location.search);
  const id = urlParams.get('id');
  return id ? parseInt(id, 10) : null;
}

// Загрузка данных пациента
async function fetchPatientDetails(id: number): Promise<PatientDetails> {
  try {
    console.log('Отправка запроса на:', API_ENDPOINTS.PATIENTS.DETAIL_UPDATE_DELETE(id));
    const response = await fetch(API_ENDPOINTS.PATIENTS.DETAIL_UPDATE_DELETE(id));
    console.log('Ответ сервера:', response);

    if (!response.ok) {
      console.error('Ошибка:', response.status, response.statusText);
      throw new Error('Ошибка при загрузке данных пациента');
    }

    const data = await response.json();
    console.log('Данные получены:', data);
    return data;
  } catch (error) {
    console.error('Ошибка в fetchPatientDetails:', error);
    throw error;
  }
}

// Отображение данных пациента
function renderPatientDetails(details: PatientDetails) {
  const { patient, ohis_value, pi_value, pma_value, cpitn_value, cpu_value } = details;

  // Отображение основной информации о пациенте
  const patientName = document.getElementById('patient-name');
  const birthdate = document.getElementById('birthdate');
  const registration_date = document.getElementById('registration_date');
  const otherInfo = document.getElementById('other-info');

  if (patientName && birthdate && otherInfo && registration_date) {
    patientName.textContent = `${patient.last_name} ${patient.first_name} ${patient.middle_name}`;
    birthdate.textContent = patient.birthdate;
    registration_date.textContent = patient.registration_date;
    otherInfo.textContent = patient.other_info;
  }

  // Отображение значений внутри кнопок
  const renderIndexButton = (buttonId: string, value: number | null) => {
    const button = document.getElementById(buttonId);
    if (button) {
      button.innerHTML = value !== null
        ? `${button.textContent?.trim()} <span class="index-value">${value}</span>`
        : button.textContent || '';
    }
  };

  renderIndexButton('ohis-button', ohis_value);
  renderIndexButton('pi-button', pi_value);
  renderIndexButton('pma-button', pma_value);
  renderIndexButton('cpitn-button', cpitn_value);
  renderIndexButton('cpu-button', cpu_value);
}

// Обработчик кнопки "Назад"
function setupBackButton() {
  const backButton = document.getElementById('back-button');
  if (backButton) {
    backButton.addEventListener('click', () => {
      window.location.href = '../index.html'; // Возврат к главному окну
    });
  }
}

// Обработчик кнопки "OHIS"
function setupOhisButton() {
  const ohisButton = document.getElementById('ohis-button');
  if (ohisButton) {
    ohisButton.addEventListener('click', () => {
      const patientId = getPatientId();
      if (patientId) {
        window.location.href = `/src/indexes/ohis/ohis.html?id=${patientId}`;
      } else {
        console.error('ID пациента не найден');
      }
    });
  }
}

// Обработчик кнопки "PI"
function setupPiButton() {
  const piButton = document.getElementById('pi-button');
  if (piButton) {
    piButton.addEventListener('click', () => {
      const patientId = getPatientId();
      if (patientId) {
        window.location.href = `/src/indexes/pi/pi.html?id=${patientId}`;
      } else {
        console.error('ID пациента не найден');
      }
    });
  }
}

// Обработчик кнопки "CPITN"
function setupCpitnButton() {
  const cpitnButton = document.getElementById('cpitn-button');
  if (cpitnButton) {
    cpitnButton.addEventListener('click', () => {
      const patientId = getPatientId();
      if (patientId) {
        window.location.href = `/src/indexes/cpitn/cpitn.html?id=${patientId}`;
      } else {
        console.error('ID пациента не найден');
      }
    });
  }
}

// Обработчик кнопки "PMA"
function setupPmaButton() {
  const pmaButton = document.getElementById('pma-button');
  if (pmaButton) {
    pmaButton.addEventListener('click', () => {
      const patientId = getPatientId();
      if (patientId) {
        window.location.href = `/src/indexes/pma/pma.html?id=${patientId}`;
      } else {
        console.error('ID пациента не найден');
      }
    });
  }
}

// Обработчик кнопки "TEETH_FORMULA"
function setupTeethFormulaButton() {
  const teethformulaButton = document.getElementById('teeth-formula-button');
  if (teethformulaButton) {
    teethformulaButton.addEventListener('click', () => {
      const patientId = getPatientId();
      if (patientId) {
        window.location.href = `/src/indexes/teeth-formula/teeth-formula.html?id=${patientId}`;
      } else {
        console.error('ID пациента не найден');
      }
    });
  }
}

// Обработчик кнопки "Загрузить фото"
function setupDownPhotoButton() {
  const photoButton = document.getElementById('down-photo-button');
  if (photoButton) {
    photoButton.addEventListener('click', () => {
      const patientId = getPatientId();
      if (patientId) {
        window.location.href = `/src/indexes/download_images/download_images.html?id=${patientId}`;
      } else {
        console.error('ID пациента не найден');
      }
    });
  }
}

// Обработчик кнопки "Фото"
function setupPhotoButton() {
  const photoButton = document.getElementById('photo-button');
  if (photoButton) {
    photoButton.addEventListener('click', () => {
      const patientId = getPatientId();
      if (patientId) {
        window.location.href = `/src/indexes/view_images/view_images.html?id=${patientId}`;
      } else {
        console.error('ID пациента не найден');
      }
    });
  }
}


// Основная функция
async function main() {
  const patientId = getPatientId();
  if (!patientId) {
    console.error('ID пациента не найден');
    return;
  }

  // Очистка данных перед загрузкой
  const patientName = document.getElementById('patient-name');
  const birthdate = document.getElementById('birthdate');
  const registration_date = document.getElementById('registration_date');
  const otherInfo = document.getElementById('other-info');
  const ohisValue = document.getElementById('ohis-value');
  const piValue = document.getElementById('pi-value');
  const pmaValue = document.getElementById('pma-value');
  const cpitnValue = document.getElementById('cpitn-value');
  const cpuValue = document.getElementById('cpu-value');

  if (patientName) patientName.textContent = 'Загрузка данных...';
  if (birthdate) birthdate.textContent = 'Загрузка...';
  if (registration_date) registration_date.textContent = 'Загрузка...';
  if (otherInfo) otherInfo.textContent = 'Загрузка...';
  if (ohisValue) ohisValue.textContent = '';
  if (piValue) piValue.textContent = '';
  if (pmaValue) pmaValue.textContent = '';
  if (cpitnValue) cpitnValue.textContent = '';
  if (cpuValue) cpuValue.textContent = '';

  try {
    const patientDetails = await fetchPatientDetails(patientId);
    renderPatientDetails(patientDetails);
  } catch (error) {
    console.error('Ошибка:', error);
  }

  setupBackButton();
  setupOhisButton();
  setupPiButton();
  setupCpitnButton();
  setupPmaButton();
  setupTeethFormulaButton();
  setupDownPhotoButton();
  setupPhotoButton();
}

// Запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', main);