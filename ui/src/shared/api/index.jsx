import { axios } from "../../lib/axios";

function get({ url }) {
    axios
        .get(url)
        .then((response) => {
            return response;
        })
        .catch((error) => {
            return Promise.reject(error);
        });
}

function post(url, body, headers) {
    axios({
        method: 'post',
        url: url,
        data: body,
        config: { headers: { ...headers } }
    })
        .then(function (response) {
            return (response);
        })
        .catch(function (response) {
        });


}

function put({ url, body }) {
    axios
        .put(url, body)
        .then((response) => {
            return response;
        })
        .catch((error) => {
            return Promise.reject(error);
        });
}

function del({ url }) {
    axios
        .delete(url)
        .then((response) => {
            return response;
        })
        .catch((error) => {
            return Promise.reject(error);
        });
}

export { get, post, put, del };
