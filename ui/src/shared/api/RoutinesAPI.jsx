import { axios } from "../../libs/axios";

export async function getUsersRoutines(id) {
    const response = await axios.get(`/routines/${id}`);
    return response.data;
}

export async function getAllUsersRoutines(id) {
    const response = await axios.get(`/routines/users/${id}`);
    return response.data;
}

export async function getRoomRoutines(roomId) {
    const response = await axios.get(`/rooms/${roomId}/routines`);
    return response.data;
}