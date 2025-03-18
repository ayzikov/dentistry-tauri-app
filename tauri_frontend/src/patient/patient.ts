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
  const registrationDate = document.getElementById('registration-date');
  const otherInfo = document.getElementById('other-info');

  if (patientName && birthdate && otherInfo) {
    patientName.textContent = `${patient.last_name} ${patient.first_name} ${patient.middle_name}`;
    birthdate.textContent = patient.birthdate;
    otherInfo.textContent = patient.other_info;
  }

  // Отображение значений под кнопками
  const ohisValue = document.getElementById('ohis-value');
  const piValue = document.getElementById('pi-value');
  const pmaValue = document.getElementById('pma-value');
  const cpitnValue = document.getElementById('cpitn-value');
  const cpuValue = document.getElementById('cpu-value');

  if (ohisValue) ohisValue.textContent = ohis_value !== null ? ohis_value.toString() : '';
  if (piValue) piValue.textContent = pi_value !== null ? pi_value.toString() : '';
  if (pmaValue) pmaValue.textContent = pma_value !== null ? pma_value.toString() : '';
  if (cpitnValue) cpitnValue.textContent = cpitn_value !== null ? cpitn_value.toString() : '';
  if (cpuValue) cpuValue.textContent = cpu_value !== null ? cpu_value.toString() : '';
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
  const otherInfo = document.getElementById('other-info');
  const ohisValue = document.getElementById('ohis-value');
  const piValue = document.getElementById('pi-value');
  const pmaValue = document.getElementById('pma-value');
  const cpitnValue = document.getElementById('cpitn-value');
  const cpuValue = document.getElementById('cpu-value');

  if (patientName) patientName.textContent = 'Загрузка данных...';
  if (birthdate) birthdate.textContent = 'Загрузка...';
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
}

// Запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', main);