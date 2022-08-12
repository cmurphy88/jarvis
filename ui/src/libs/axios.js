import Axios from "axios";
import { getApiUrl } from "../config";
import storage from "../utils/storage"

function authRequestInterceptor(config) {
    const token = storage.getAccessToken();
    if (!config?.headers) {
        throw new Error(
            `Expected 'config' and 'config.headers' not to be undefined`
        );
    }
    if (token) {
        config.headers.authorization = `Bearer ${token}`;
    }
    config.headers.Accept = "application/json";
    return config;

}

export const axios = Axios.create({
    baseURL: getApiUrl(),
});

axios.interceptors.request.use(authRequestInterceptor);