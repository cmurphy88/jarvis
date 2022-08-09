import axios from "axios";

export async function getCurrentUser() {
    const response = await axios.get("/api/user");

    return response.data.data;
}

export async function signUp(
    email,
    first_name,
    last_name,
    password,
) {
    const response = await axios.post("/api/user", { email, first_name, last_name, password });

    return response.data.data;
}