import { axios } from "../../lib/axios";

export async function getUsersRoutines(id) {
    const response = await axios.get(`/routines/${id}`);
    return response.data;
}

export async function getAllUsersRoutines(id) {
    const response = await axios.get(`/routines/users/${id}`);
    return response.data;
}