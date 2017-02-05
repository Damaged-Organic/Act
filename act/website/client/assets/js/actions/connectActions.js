import dispatcher from "../dispatcher";

import URLS from "../api";

import http from "Utils/http";
import httpBundle from "Utils/httpBundle";
import * as connectConstants from "Constants/connectConstants";

export function loadData(){

    let urls = [
        URLS.metadata + "/worksheet",
        URLS.sponsors,
        URLS.socials,
        URLS.centers + "?related=city",
        URLS.contacts + "?head_office",
        URLS.disclaimer
    ];

    dispatcher.dispatch({
        type: connectConstants.LOAD_CONNECT_START,
        payload: { loading: true }
    });

    httpBundle(urls)
        .then((responses) => {
            responses = responses.map((response) => JSON.parse(response.data));

            let [metadata, sponsors, socials, centers, contacts, disclaimer] = responses;

            dispatcher.dispatch({
                type: connectConstants.LOAD_CONNECT_END,
                payload: {
                    loading: false,
                    metadata,
                    sponsors,
                    socials,
                    centers,
                    contacts,
                    disclaimer
                }
            });
        })
        .catch((error) => {
            error = JSON.parse(error.data);

            dispatcher.dispatch({
                type: connectConstants.LOAD_CONNECT_ERROR,
                payload: {
                    loading: false,
                    error
                }
            });
        });
}

export function sendForm(data){

    dispatcher.dispatch({
        type: connectConstants.SEND_CONNECT_START,
        payload: { loading: true }
    });

    http.post({
        url: URLS.worksheets,
        method: "POST",
        headers: { "Content-type": "application/x-www-form-urlencoded" },
        data: data
    })
    .then((response) => {
        response = JSON.parse(response.data);

        dispatcher.dispatch({
            type: connectConstants.SEND_CONNECT_END,
            payload: {
                loading: false,
                hasMessage: true,
                hasErrors: false
            }
        });
    })
    .catch((error) => {
        error = JSON.parse(error.data);

        dispatcher.dispatch({
            type: connectConstants.SEND_CONNECT_ERROR,
            payload: {
                loading: false,
                hasMessage: false,
                hasErrors: true,
                error
            }
        });
    });

}