const API_BASE_URL = 'http://127.0.0.1:8000';

export const API_ENDPOINTS = {
  PATIENTS: {
    LIST_CREATE: `${API_BASE_URL}/patient/`,
    DETAIL_UPDATE_DELETE: (id: number | string) => `${API_BASE_URL}/patient/${id}/`,
  },

  MODULES: {
    OHIS_LIST_CREATE: (id: number | string) => `${API_BASE_URL}/module/patient/${id}/ohis/`,
    PI_LIST_CREATE: (id: number | string) => `${API_BASE_URL}/module/patient/${id}/pi/`,
    PMA_LIST_CREATE: (id: number | string) => `${API_BASE_URL}/module/patient/${id}/pma/`,
    CPITN_LIST_CREATE: (id: number | string) => `${API_BASE_URL}/module/patient/${id}/cpitn/`,
    CPU_LIST_CREATE: (id: number | string) => `${API_BASE_URL}/module/patient/${id}/cpu/`,
    TEETH_FORMULA_LIST_CREATE: (id: number | string) => `${API_BASE_URL}/module/patient/${id}/teeth-formula/`,
  },
};