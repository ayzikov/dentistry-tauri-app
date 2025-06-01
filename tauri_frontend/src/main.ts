// Импорт fetch из плагина Tauri
import { fetch } from '@tauri-apps/plugin-http';

// Импорт конфигурации API
import { API_ENDPOINTS } from './url.config.dev';

// Интерфейс для данных пациента
interface Patient {
  id: number;
  first_name: string;
  last_name: string;
  middle_name: string;
  birthdate: string;
  other_info: string;
  registration_date: string;
}

// Загрузка списка пациентов
async function fetchPatients(): Promise<Patient[]> {
  try {
    console.log('Отправка запроса на:', API_ENDPOINTS.PATIENTS.LIST_CREATE);
    const response = await fetch(API_ENDPOINTS.PATIENTS.LIST_CREATE);
    console.log('Ответ сервера:', response);

    if (!response.ok) {
      console.error('Ошибка:', response.status, response.statusText);
      throw new Error('Ошибка при загрузке списка пациентов');
    }

    const data = await response.json();
    console.log('Данные получены:', data);
    return data;
  } catch (error) {
    console.error('Ошибка в fetchPatients:', error);
    throw error;
  }
}

// Фильтрация списка пациентов
function filterPatients(patients: Patient[], searchText: string): Patient[] {
  const lowerCaseSearchText = searchText.toLowerCase();
  return patients.filter(patient => {
    const fullName = `${patient.last_name} ${patient.first_name} ${patient.middle_name}`.toLowerCase();
    return fullName.includes(lowerCaseSearchText);
  });
}

// Отображение списка пациентов
function renderPatients(patients: Patient[]) {
  const patientList = document.getElementById('patient-list');
  if (!patientList) return;

  patientList.innerHTML = ''; // Очищаем список

  patients.forEach(patient => {
    const patientItem = document.createElement('div');
    patientItem.className = 'patient-item';
    patientItem.textContent = `${patient.last_name} ${patient.first_name} ${patient.middle_name}`;

    // Обработчик клика по пациенту
    patientItem.addEventListener('click', () => {
      window.location.href = `/src/patient/patient.html?id=${patient.id}`;
    });

    patientList.appendChild(patientItem);
  });
}

// Основная функция
async function main() {
  let patients: Patient[] = [];

  try {
    patients = await fetchPatients();
    renderPatients(patients); // Первоначальное отображение списка
  } catch (error) {
    console.error('Ошибка:', error);
  }

  // Поиск пациента
  const searchInput = document.getElementById('search-input') as HTMLInputElement;
  if (searchInput) {
    searchInput.addEventListener('input', () => {
      const searchText = searchInput.value.trim();
      const filteredPatients = filterPatients(patients, searchText);
      renderPatients(filteredPatients);
    });
  }
}

// Запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', main);

document.addEventListener('DOMContentLoaded', () => {
    const addPatientButton = document.getElementById('add-patient-button');

    if (addPatientButton) {
        addPatientButton.addEventListener('click', () => {
            // Здесь будет логика добавления пациента
            console.log('Кнопка "Добавить пациента" нажата');
            // Например, открытие модального окна или переход на другую страницу
            window.location.href = '/src/create_patient/create_patient.html'; // Замените на ваш URL
        });
    }
});