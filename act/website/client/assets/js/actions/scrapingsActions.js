import URLS from "../api";
import http from "Utils/http";

const URL = URLS.scrapings;

export function scrap(path, head){

    head = encodeURIComponent(head);

    http.post({
        url: URL,
        method: "POST",
        headers: { "Content-type": "application/x-www-form-urlencoded" },
        data: { path, head }
    })
    .then((response) => {
        console.log(response);
    })
    .catch((error) => {
        console.log(error);
    });

}
