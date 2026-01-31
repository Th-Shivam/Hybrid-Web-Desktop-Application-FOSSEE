import axios from 'axios';

// Hardcoded for now as requested
const API_BASE_URL = 'http://127.0.0.1:8000/api';

// 1. Upload CSV
export const uploadCSV = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    
    // Returns promise
    return axios.post(`${API_BASE_URL}/upload-csv/`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
};

// 2. Get Latest Summary
export const getLatestAnalysis = async () => {
    return axios.get(`${API_BASE_URL}/latest-analysis/`);
};

// 3. Get Upload History
export const getRecentUploads = async () => {
    return axios.get(`${API_BASE_URL}/recent-analysis/`);
};
