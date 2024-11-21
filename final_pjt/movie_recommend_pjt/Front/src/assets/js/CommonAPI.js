// local vue api axios instance
import axios from 'axios';
import { useRouter } from 'vue-router';
// import { userStore } from "@/store/user";

// const router = useRouter();
// const store = userStore();

//HTTP GET CALL
function httpGetAxios(endpoints, param) {
    return axios({
        headers: {
            // 'Access-Control-Allow-Origin': '*',
        },
        params: param,
        url: endpoints,
        method: 'get'
    })
}

//HTTP POST CALL
function httpPostAxios(endpoints, param) {
    return axios.post(endpoints, param, {
        headers: {
            // 'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json; charset=utf-8',
        }
    })
}

// const signOut = () => {
//     authStore.$reset();
//     location.href = "/signin";
// }

export { httpPostAxios, httpGetAxios };