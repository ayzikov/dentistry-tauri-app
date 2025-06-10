// Импорт fetch из плагина Tauri
import { fetch } from '@tauri-apps/plugin-http';

// Импорт конфигурации API
import { API_ENDPOINTS } from '/src/url.config.dev';

// Получение ID пациента из URL
function getPatientId(): number | null {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    return id ? parseInt(id, 10) : null;
}

let selectedFiles: File[] = [];

// Инициализация
function init() {
    const dropArea = document.getElementById('drop-area');
    const fileInput = document.getElementById('file-input') as HTMLInputElement;
    const browseButton = document.getElementById('browse-button');
    const addButton = document.getElementById('add-button');
    const backButton = document.getElementById('back-button');

    if (!dropArea || !fileInput || !browseButton || !addButton || !backButton) {
        console.error('Не удалось найти необходимые элементы');
        return;
    }

    // Обработчик кнопки "Назад"
    backButton.addEventListener('click', () => {
        window.history.back(); // Вернуться на предыдущую страницу
    });

    // Обработчик клика по кнопке "Выбрать файлы"
    browseButton.addEventListener('click', () => {
        fileInput.click();
    });

    // Обработчик выбора файлов через input
    fileInput.addEventListener('change', (e) => {
        const files = (e.target as HTMLInputElement).files;
        if (files) {
            handleFiles(files);
        }
    });

    // Настройка обработчиков для drag and drop
    setupDragAndDrop();

    // Обработчик кнопки "Добавить"
    addButton.addEventListener('click', async () => {
        const patientId = getPatientId();
        if (!patientId) {
            alert('ID пациента не найден');
            return;
        }

        if (selectedFiles.length === 0) {
            alert('Выберите хотя бы один файл');
            return;
        }

        // Отправляем каждый файл по отдельности
        for (const file of selectedFiles) {
            await uploadImage(patientId, file);
        }

        // Очищаем выбранные файлы после отправки
        selectedFiles = [];
        const previewContainer = document.getElementById('preview-container');
        if (previewContainer) {
            previewContainer.innerHTML = '';
        }
        alert('Фотографии успешно загружены');
    });
}

// Настройка обработчиков для drag and drop
function setupDragAndDrop() {
    const dropArea = document.getElementById('drop-area');
    if (!dropArea) return;

    // Предотвращаем стандартное поведение браузера
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });

    // Подсвечиваем область при перетаскивании
    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    // Обработка сброса файлов
    dropArea.addEventListener('drop', handleDrop, false);
}

function preventDefaults(e: Event) {
    e.preventDefault();
    e.stopPropagation();
}

function highlight() {
    const dropArea = document.getElementById('drop-area');
    if (dropArea) {
        dropArea.classList.add('dragover');
    }
}

function unhighlight() {
    const dropArea = document.getElementById('drop-area');
    if (dropArea) {
        dropArea.classList.remove('dragover');
    }
}

function handleDrop(e: DragEvent) {
    const dt = e.dataTransfer;
    if (dt && dt.files) {
        handleFiles(dt.files);
    }
}

// Обработка выбранных файлов
function handleFiles(files: FileList) {
    // Преобразуем FileList в массив
    const filesArray = Array.from(files);

    // Фильтруем только изображения
    const imageFiles = filesArray.filter(file => file.type.startsWith('image/'));

    // Добавляем в выбранные файлы
    selectedFiles = [...selectedFiles, ...imageFiles];

    // Показываем превью
    imageFiles.forEach(previewImage);
}

// Предпросмотр изображения
function previewImage(file: File) {
    const previewContainer = document.getElementById('preview-container');
    if (!previewContainer) return;

    const reader = new FileReader();
    reader.onload = (e) => {
        const previewItem = document.createElement('div');
        previewItem.className = 'preview-item';

        const img = document.createElement('img');
        img.src = e.target?.result as string;
        img.alt = file.name;

        const removeBtn = document.createElement('button');
        removeBtn.className = 'remove-btn';
        removeBtn.textContent = 'x';
        removeBtn.onclick = () => {
            // Удаляем файл из selectedFiles
            const index = selectedFiles.indexOf(file);
            if (index !== -1) {
                selectedFiles.splice(index, 1);
            }
            previewItem.remove();
        };

        previewItem.appendChild(img);
        previewItem.appendChild(removeBtn);
        previewContainer.appendChild(previewItem);
    };
    reader.readAsDataURL(file);
}

// Загрузка изображения на сервер
async function uploadImage(patientId: number, file: File) {
    const formData = new FormData();
    formData.append('image', file);

    try {
        const response = await fetch(API_ENDPOINTS.MODULES.IMAGE_LIST_CREATE(patientId), {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Ошибка загрузки: ${response.status} ${response.statusText}`);
        }

        console.log(`Файл ${file.name} успешно загружен`);
    } catch (error) {
        console.error(`Ошибка при загрузке файла ${file.name}:`, error);
        alert(`Ошибка при загрузке файла ${file.name}`);
    }
}

// Запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', init);