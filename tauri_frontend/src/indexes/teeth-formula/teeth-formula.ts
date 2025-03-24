import { fetch } from '@tauri-apps/plugin-http';
import { API_ENDPOINTS } from '/src/url.config.dev';


// Получение ID пациента из URL
function getPatientId(): number | null {
  const urlParams = new URLSearchParams(window.location.search);
  const id = urlParams.get('id');
  return id ? parseInt(id, 10) : null;
}

// Загрузка данных зубной формулы
async function fetchTeethFormulaData(patientId: number) {
  try {
    const response = await fetch(API_ENDPOINTS.MODULES.TEETH_FORMULA_LIST_CREATE(patientId), {
      method: 'GET',
    });

    if (!response.ok) {
      throw new Error('Ошибка при получении данных');
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Ошибка при загрузке данных зубной формулы:', error);
    return null;
  }
}

// Обновление значений зубов на странице
function updateTeethValues(teethData: Record<string, string>) {
  Object.entries(teethData).forEach(([toothId, value]) => {
    const toothValueElement = document.getElementById(`tooth${toothId.slice(2)}-value`) as HTMLElement;
    if (toothValueElement) {
      toothValueElement.textContent = value.trim() === '' ? '' : value;
    }
  });
}

// Состояние выбранных значений для зубов (теперь поддерживает строки)
const teethValues: Record<string, string | null> = {};

// Обработчик клика по зубу
function setupToothClickHandlers() {
  const teeth = document.querySelectorAll('.tooth');
  const selectionWindow = document.getElementById('selection-window') as HTMLElement;

  teeth.forEach(tooth => {
    tooth.addEventListener('click', (event) => {
      const toothId = tooth.getAttribute('data-tooth')!;

      // Получаем координаты зуба
      const toothRect = tooth.getBoundingClientRect();

      // Позиционируем окно выбора в 10px справа от зуба
      selectionWindow.style.display = 'block';

      // Удаляем старые обработчики, чтобы избежать дублирования
      const options = document.querySelectorAll('.selection-option');
      options.forEach(option => {
        option.replaceWith(option.cloneNode(true));
      });

      // Добавляем новые обработчики
      const newOptions = document.querySelectorAll('.selection-option');
      newOptions.forEach(option => {
        option.addEventListener('click', () => {
          const value = option.getAttribute('data-value');
          const toothValueElement = document.getElementById(`tooth${toothId}-value`) as HTMLElement;

          if (value === 'remove') {
            teethValues[`t_${toothId}`] = null; // Устанавливаем значение null
            toothValueElement.textContent = '';
          } else {
            teethValues[`t_${toothId}`] = value; // Сохраняем значение как строку
            toothValueElement.textContent = value;
          }

          // Скрываем окно выбора после выбора значения
          selectionWindow.style.display = 'none';
        });
      });
    });
  });
}

// Обработчик кнопки "Назад"
function setupBackButton() {
  const backButton = document.getElementById('back-button') as HTMLElement;
  backButton.addEventListener('click', () => {
    const patientId = getPatientId();
    if (patientId) {
      window.location.href = `/src/patient/patient.html?id=${patientId}`;
    }
  });
}

// Обработчик кнопки "Добавить"
function setupAddButton() {
  const addButton = document.getElementById('add-button') as HTMLElement;
  addButton.addEventListener('click', async () => {
    const patientId = getPatientId();
    if (!patientId) return;

    // Собираем данные со всех зубов на экране
    const teethData: Record<string, string> = {};

    // Проходим по всем зубам и собираем их значения
    const teethElements = document.querySelectorAll('[id^="tooth"][id$="-value"]');
    teethElements.forEach((element) => {
      const toothId = element.id.replace('tooth', '').replace('-value', ''); // Извлекаем ID зуба
      const value = element.textContent?.trim() || ''; // Получаем значение зуба

      // Если значение не пустое, добавляем его в данные
      if (value) {
        teethData[`t_${toothId}`] = value;
      }
    });

    // Формируем данные для отправки
    const data = {
      teeth: teethData,
    };

    try {
      const response = await fetch(API_ENDPOINTS.MODULES.TEETH_FORMULA_LIST_CREATE(patientId), {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error('Ошибка при отправке данных');
      }

      // Перенаправляем на страницу с детальной информацией о пациенте
      window.location.href = `/src/patient/patient.html?id=${patientId}`;
    } catch (error) {
      console.error('Ошибка:', error);
      alert('Произошла ошибка при отправке данных');
    }
  });
}

// Основная функция
async function main() {
  const patientId = getPatientId();
  if (!patientId) {
    console.error('ID пациента не найден');
    return;
  }

  // Загрузка данных зубной формулы
  const teethFormulaData = await fetchTeethFormulaData(patientId);
  if (teethFormulaData && teethFormulaData.length > 0) {
    const firstEntry = teethFormulaData[0];
    updateTeethValues(firstEntry.teeth);
  }

  // Настройка обработчиков
  setupToothClickHandlers();
  setupBackButton();
  setupAddButton();
}

// Запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', main);