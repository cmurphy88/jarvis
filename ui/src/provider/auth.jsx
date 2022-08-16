import { post } from "../shared/api";
import { axios } from "../libs/axios";

const localStorageKey = "__jarvis_token__";

async function getToken() {
    return window.localStorage.getItem(localStorageKey);
}

function handleUserResponse({ user }) {
    window.localStorage.setItem(localStorageKey, user.token);
    return user;
}

async function getCurrentUser() {
    const response = await axios.get("/users/me");

    return response.data;
}

async function login(formData) {
    const form_data = new FormData()

    form_data.append("username", formData.username)
    form_data.append("password", formData.password)

    const response = await axios.post("/login", form_data
    ).then((response) => {
        return response;
    });
    return response.data;
}


// async function logout() {
//     const response = await redaxios.delete("/api/sessions");

//     return response.data.data;
// }


function register({ username, password }) {
    return post("register", { username, password }).then(handleUserResponse);
}

async function logout() {
    window.localStorage.removeItem(localStorageKey);
}
export { getToken, login, register, logout, getCurrentUser };
