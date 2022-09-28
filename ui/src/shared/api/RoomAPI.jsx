import { axios } from "../../libs/axios";

export async function getHomeRooms(id) {
    const response = await axios.get(`homes/${id}/rooms`);
    return response.data;
}

export async function getRoom(id) {
    const response = await axios.get(`rooms/${id}`);
    return response.data;
}

export async function createNewRoom(name, home_id) {
    axios.post('rooms', {
        name: name,
        home_id: home_id
    }) 
}