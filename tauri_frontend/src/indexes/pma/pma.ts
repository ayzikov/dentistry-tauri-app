import { fetch } from '@tauri-apps/plugin-http';
import { API_ENDPOINTS } from '/src/url.config.dev';

// Состояние выбранных значений для зубов
const teethValues: Record<string, number | null> = {};

// Получение ID пациента из URL
function getPatientId(): number | null {
  const urlParams = new URLSearchParams(window.location.search);
  const id = urlParams.get('id');
  return id ? parseInt(id, 10) : null;
}

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
            teethValues[`t_${toothId}`] = null;
            toothValueElement.textContent = '';
          } else {
            const numericValue = parseInt(value!, 10);
            teethValues[`t_${toothId}`] = numericValue;
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

    const data = {
      teeth: Object.fromEntries(
        Object.entries(teethValues).filter(([_, value]) => value !== null)
      ),
    };

    try {
      const response = await fetch(API_ENDPOINTS.MODULES.PMA_LIST_CREATE(patientId), {
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
function main() {
  setupToothClickHandlers();
  setupBackButton();
  setupAddButton();
}

document.addEventListener('DOMContentLoaded', main);