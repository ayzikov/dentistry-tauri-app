import { fetch } from '@tauri-apps/plugin-http';

import { API_BASE_URL, API_ENDPOINTS } from '/src/url.config.dev';

interface PatientImage {
    id: number;
    date: string;
    time: string;
    image: string;
    patient: number;
}

interface PatientDetails {
    patient: {
        id: number;
        first_name: string;
        last_name: string;
        middle_name: string;
    };
}

// Получение ID пациента из URL
function getPatientId(): number | null {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    return id ? parseInt(id, 10) : null;
}

// Загрузка данных пациента
async function fetchPatientDetails(id: number): Promise<PatientDetails> {
    const response = await fetch(API_ENDPOINTS.PATIENTS.DETAIL_UPDATE_DELETE(id));
    if (!response.ok) throw new Error('Ошибка загрузки данных пациента');
    return response.json();
}

// Загрузка фотографий пациента
async function fetchPatientImages(id: number): Promise<PatientImage[]> {
    const response = await fetch(API_ENDPOINTS.MODULES.IMAGE_LIST_CREATE(id));
    if (!response.ok) throw new Error('Ошибка загрузки фотографий');
    return response.json();
}

// Группировка фотографий по дате
function groupImagesByDate(images: PatientImage[]): Record<string, PatientImage[]> {
    const groups: Record<string, PatientImage[]> = {};

    images.forEach(image => {
        if (!groups[image.date]) {
            groups[image.date] = [];
        }
        groups[image.date].push(image);
    });

    return groups;
}

// Отображение фотографий
function renderImages(groups: Record<string, PatientImage[]>) {
    const container = document.getElementById('photos-container');
    if (!container) return;

    container.innerHTML = '';

    Object.entries(groups).forEach(([date, images]) => {
        const groupDiv = document.createElement('div');
        groupDiv.className = 'date-group';

        const header = document.createElement('h2');
        header.className = 'date-header';
        header.textContent = date;

        const thumbnailsDiv = document.createElement('div');
        thumbnailsDiv.className = 'thumbnails';

        images.forEach(image => {
            const img = document.createElement('img');
            img.className = 'thumbnail';
            img.src = `${API_BASE_URL}${image.image}`;
            img.alt = `Фото от ${date}`;

            img.addEventListener('click', () => {
                const modal = document.getElementById('modal') as HTMLDivElement;
                const fullImage = document.getElementById('full-image') as HTMLImageElement;

                if (modal && fullImage) {
                    fullImage.src = `${API_BASE_URL}${image.image}`;
                    modal.style.display = 'flex';
                }
            });

            thumbnailsDiv.appendChild(img);
        });

        groupDiv.appendChild(header);
        groupDiv.appendChild(thumbnailsDiv);
        container.appendChild(groupDiv);
    });
}

// Настройка модального окна
function setupModal() {
    const modal = document.getElementById('modal');
    if (modal) {
        modal.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }
}

// Настройка кнопки "Назад"
function setupBackButton() {
    const backButton = document.getElementById('back-button');
    if (backButton) {
        backButton.addEventListener('click', () => {
            const patientId = getPatientId();
            if (patientId) {
                window.location.href = `/src/patient/patient.html?id=${patientId}`;
            } else {
                window.location.href = '../index.html';
            }
        });
    }
}

// Основная функция
async function main() {
    const patientId = getPatientId();
    if (!patientId) {
        alert('ID пациента не найден');
        return;
    }

    try {
        // Загрузка данных параллельно
        const [patientDetails, images] = await Promise.all([
            fetchPatientDetails(patientId),
            fetchPatientImages(patientId)
        ]);

        // Обновление заголовка
        const nameElement = document.getElementById('patient-name');
        if (nameElement) {
            const { last_name, first_name, middle_name } = patientDetails.patient;
            nameElement.textContent = `Фотографии пациента: ${last_name} ${first_name} ${middle_name}`;
        }

        // Группировка и отображение фото
        const groupedImages = groupImagesByDate(images);
        renderImages(groupedImages);

    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при загрузке данных');
    }

    setupModal();
    setupBackButton();
}

// Запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', main);