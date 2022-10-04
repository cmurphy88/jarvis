import { axios } from "../../libs/axios";

export async function getUsersHomes(id) {
    const response = await axios.get(`/homes/users/${id}`);
    return response.data;
};

export async function addNewHome(name, user_id, is_admin) {
    const response = axios.post('/homes/create', {
        name: name,
        user_id: user_id,
        is_admin: is_admin
    });

    console.log(response.Promise);
    return response;
    // axios.post(`/homes/${}`)
};


