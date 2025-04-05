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

// Загрузка истории расчетов
async function fetchHistoryData(patientId: number) {
  try {
    const response = await fetch(API_ENDPOINTS.MODULES.PMA_LIST_CREATE(patientId), {
      method: 'GET',
    });

    if (!response.ok) {
      throw new Error('Ошибка при получении данных');
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Ошибка при загрузке истории расчетов:', error);
    return null;
  }
}

// Отображение истории расчетов
function renderHistory(historyData: any[]) {
  const historyList = document.getElementById('history-list');
  if (!historyList) return;

  historyList.innerHTML = '';

  historyData.forEach((item, index) => {
    const historyItem = document.createElement('div');
    historyItem.className = `history-item ${index === 0 ? 'highlighted' : ''}`;

    const date = new Date(item.date);
    const formattedDate = `${String(date.getDate()).padStart(2, '0')}.${String(date.getMonth() + 1).padStart(2, '0')}.${date.getFullYear()}`;

    historyItem.textContent = `${formattedDate}: ${item.value}`;
    historyList.appendChild(historyItem);
  });
}

// Обработчик клика по зубу
function setupToothClickHandlers() {
  const teeth = document.querySelectorAll('.tooth');
  const selectionWindow = document.getElementById('selection-window') as HTMLElement;

  teeth.forEach(tooth => {
    tooth.addEventListener('click', (event) => {
      const toothId = tooth.getAttribute('data-tooth')!;
      const toothRect = tooth.getBoundingClientRect();

      // Рассчитываем позицию окна
      let posLeft = toothRect.right + 10;
      let posTop = toothRect.top;

      // Проверка на выход за правый край экрана
      if (posLeft + selectionWindow.offsetWidth > window.innerWidth) {
        posLeft = toothRect.left - selectionWindow.offsetWidth - 10;
      }

      // Проверка на выход за нижний край экрана
      if (posTop + selectionWindow.offsetHeight > window.innerHeight) {
        posTop = window.innerHeight - selectionWindow.offsetHeight - 10;
      }

      // Позиционируем окно
      selectionWindow.style.left = `${posLeft}px`;
      selectionWindow.style.top = `${posTop}px`;
      selectionWindow.style.display = 'flex';


      // Обновляем обработчики
      const options = document.querySelectorAll('.selection-option');
      options.forEach(option => {
        option.replaceWith(option.cloneNode(true));
      });

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
async function main() {
  const patientId = getPatientId();
  if (!patientId) {
    console.error('ID пациента не найден');
    return;
  }
  // Загрузка и отображение истории расчетов
  const historyData = await fetchHistoryData(patientId);
  if (historyData) {
    renderHistory(historyData);
  }

  setupToothClickHandlers();
  setupBackButton();
  setupAddButton();
}

document.addEventListener('DOMContentLoaded', main);