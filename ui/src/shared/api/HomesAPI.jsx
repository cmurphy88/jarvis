import { axios } from "../../libs/axios";

export async function getUsersHomes(id) {
    const response = await axios.get(`/homes/users/${id}`);
    return response.data;
}
