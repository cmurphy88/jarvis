import { axios } from "../../lib/axios";

export async function getHomeRooms(id) {
    const response = await axios.get(`homes/${id}/rooms`);
    return response.data;
}