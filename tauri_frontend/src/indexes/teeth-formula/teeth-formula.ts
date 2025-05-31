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
function updateTeethValues(teethData: Record<string, string | string[]>) {
    Object.entries(teethData).forEach(([toothKey, value]) => {
        const toothId = toothKey.slice(2); // Убираем префикс "t_"
        const toothElement = document.getElementById(`tooth${toothId}`);
        if (!toothElement) return;

        const valuesContainer = toothElement.querySelector('.tooth-values');
        if (!valuesContainer) return;

        // Очищаем контейнер перед добавлением новых значений
        valuesContainer.innerHTML = '';

        let values: string[] = [];

        // Обрабатываем разные форматы данных
        if (typeof value === 'string') {
            values = value.split(',')
                .map(v => v.trim())
                .filter(v => v !== '');
        } else if (Array.isArray(value)) {
            values = value.filter(v => v.trim() !== '');
        }

        // Добавляем значения в контейнер
        values.forEach(val => {
            const valueElement = document.createElement('div');
            valueElement.className = 'tooth-value-item';
            valueElement.textContent = val;
            valuesContainer.appendChild(valueElement);
        });
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
      const toothRect = tooth.getBoundingClientRect();

      // Рассчитываем позицию окна (без изменений)
      let posLeft = toothRect.right + 10;
      let posTop = toothRect.top;
      if (posLeft + selectionWindow.offsetWidth > window.innerWidth) {
        posLeft = toothRect.left - selectionWindow.offsetWidth - 10;
      }
      if (posTop + selectionWindow.offsetHeight > window.innerHeight) {
        posTop = window.innerHeight - selectionWindow.offsetHeight - 10;
      }

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
            const toothValuesContainer = tooth.querySelector('.tooth-values') as HTMLElement;

            if (value === 'remove') {
                // Полная очистка всех значений
                teethValues[`t_${toothId}`] = [];
                toothValuesContainer.innerHTML = '';
            } else {
                // Инициализация массива значений если нужно
                if (!teethValues[`t_${toothId}`]) {
                    teethValues[`t_${toothId}`] = [];
                }

                // Добавляем значение только если его еще нет
                if (!teethValues[`t_${toothId}`].includes(value)) {
                    teethValues[`t_${toothId}`].push(value);

                    // Создаем новый элемент для значения
                    const valueElement = document.createElement('div');
                    valueElement.className = 'tooth-value-item';
                    valueElement.textContent = value;

                    // Добавляем в контейнер значений
                    toothValuesContainer.appendChild(valueElement);
                }
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

        // Собираем данные со всех зубов
        const teethData: Record<string, string> = {};

        document.querySelectorAll('.tooth').forEach(toothElement => {
            const toothId = toothElement.getAttribute('data-tooth');
            if (!toothId) return;

            const valuesContainer = toothElement.querySelector('.tooth-values');
            if (!valuesContainer) return;

            // Собираем все значения для зуба
            const values = Array.from(valuesContainer.children)
                .map(item => item.textContent?.trim() || '')
                .filter(v => v !== '');

            if (values.length > 0) {
                teethData[`t_${toothId}`] = values.join(', ');
            }
        });

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

// Закрытие окна при клике вне области
document.addEventListener('click', (event) => {
  const target = event.target as HTMLElement;
  const selectionWindow = document.getElementById('selection-window') as HTMLElement;

  // Если клик не по зубу и не по окну выбора
  if (!target.closest('.tooth') && !target.closest('.selection-window')) {
    selectionWindow.style.display = 'none';
  }
});

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