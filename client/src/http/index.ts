import axios from "axios";

export const API_URL = 'http://localhost:5000';

const $api = axios.create({
    withCredentials: true,
    // credentials: 'include',
    baseURL: API_URL
})

$api.interceptors.request.use((config) => {
    // config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
    // config.headers["Access-Control-Allow-Origin"] = "*";
    return config;
})

export default $api;
