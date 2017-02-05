import http from "./http";

function httpBundle(urls){
    let request = urls.map((url) => {

        return http.get({
            method: "GET",
            headers: {
                "Accept": "*/*",
                "Content-type": "application/json"
            },
            url
        });

    });

    return Promise.all(request);
}

export default httpBundle;