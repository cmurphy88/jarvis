import { axios } from "../../lib/axios";
import { useEffect, useState } from "react";

export async function getUsersHomes(id) {
    const response = await axios.get(`/homes/users/${id}`);
    return response.data;
}