// Импорт fetch из плагина Tauri
import { fetch } from '@tauri-apps/plugin-http';

// Импорт конфигурации API
import { API_ENDPOINTS } from '../url.config.dev';

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('patient-form');
    const statusMessage = document.getElementById('status-message');
    const backButton = document.getElementById('back-button');

    // Обработчик кнопки "Назад"
    backButton.addEventListener('click', function() {
        window.history.back();
    });

    // Обработчик отправки формы
    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Собираем данные формы
        const formData = {
            first_name: document.getElementById('first_name').value,
            last_name: document.getElementById('last_name').value,
            middle_name: document.getElementById('middle_name').value,
            birthdate: document.getElementById('birthdate').value,
            other_info: document.getElementById('other_info').value
        };

        try {
            // Отправляем данные на сервер
            const response = await fetch(API_ENDPOINTS.PATIENTS.LIST_CREATE, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                // Успешное добавление
                statusMessage.textContent = 'Пациент успешно добавлен!';
                statusMessage.className = 'status-message success';

                // Очищаем форму
                form.reset();

                // Через 2 секунды переходим обратно
                setTimeout(() => {
                    window.location.href = 'index.html';
                }, 2000);
            } else {
                // Ошибка сервера
                const errorData = await response.json();
                throw new Error(errorData.message || 'Ошибка сервера');
            }
        } catch (error) {
            // Ошибка сети или другая ошибка
            statusMessage.textContent = `Ошибка: ${error.message}`;
            statusMessage.className = 'status-message error';
            console.error('Ошибка при добавлении пациента:', error);
        }
    });
});