import dispatcher from "../dispatcher";

import URLS from "../api";
import http from "Utils/http";

import * as subscribeConstants from "Constants/subscribeConstants";

export function subscribe(data = {}){

    dispatcher.dispatch({
        type: subscribeConstants.LOAD_SUBSCRIBE_START,
        payload: { loading: true }
    });

    http.post({
        url: URLS.subscribers,
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        data: data
    })
    .then((response) => {
        response = JSON.parse(response.data);

        dispatcher.dispatch({
            type: subscribeConstants.LOAD_SUBSCRIBE_END,
            payload: {
                loading: false,
                email: response.email,
                error: ""
            }
        });
    })
    .catch((error) => {
        error = JSON.parse(error.data);

        dispatcher.dispatch({
            type: subscribeConstants.LOAD_SUBSCRIBE_ERROR,
            payload: {
                loading: false,
                email: "",
                error: error.detail
            }
        });
    });

}

export function checkSubscriber(id, hash){

    let url = URLS.subscribers + "/subscribe/"+ id +"/"+ hash;

    dispatcher.dispatch({
        type: subscribeConstants.CHECK_SUBSCRIBE_START,
        payload: { loading: true }
    });

    http.get({
        url: url,
        method: "GET",
        headers: {
            "Accept": "*/*",
            "Content-type": "application/json"
        },
    })
    .then((response) => {
        response = JSON.parse(response.data);

        dispatcher.dispatch({
            type: subscribeConstants.CHECK_SUBSCRIBE_END,
            payload: {
                loading: false,
                isChecked: true,
                email: response.email
            }
        });

    })
    .catch((error) => {
        error = JSON.parse(error.data);

        dispatcher.dispatch({
            type: subscribeConstants.CHECK_SUBSCRIBE_ERROR,
            payload: {
                loading: false,
                isChecked: false,
                error: error.detail
            }
        });
    });

}

export function confirmSubscribe(id, hash, email){

    let url = URLS.subscribers + "/subscribe/"+ id +"/"+ hash;

    dispatcher.dispatch({
        type: subscribeConstants.CONFIRM_SUBSCRIBE_START,
        payload: { loading: true }
    });

    http.request({
        url: url,
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        data: { email }
    })
    .then((response) => {
        response = JSON.parse(response.data);

        dispatcher.dispatch({
            type: subscribeConstants.CONFIRM_SUBSCRIBE_END,
            payload: {
                loading: false,
                isConfirmed: true,
                email: response.email
            }
        });
    })
    .catch((error) => {
        error = JSON.parse(error.data);

        dispatcher.dispatch({
            type: subscribeConstants.CONFIRM_SUBSCRIBE_ERROR,
            payload: {
                loading: false,
                isConfirmed: false,
                error: error.detail
            }
        });
    });

}

export function checkUnsubscriber(id, hash){

    let url = URLS.subscribers + "/unsubscribe/"+ id +"/"+ hash;

    dispatcher.dispatch({
        type: subscribeConstants.CHECK_UNSUBSCRIBE_START,
        payload: { loading: true }
    });

    http.get({
        url: url,
        method: "GET"
    })
    .then((response) => {
        response = JSON.parse(response.data);

        dispatcher.dispatch({
            type: subscribeConstants.CHECK_UNSUBSCRIBE_END,
            payload: {
                loading: false,
                isChecked: true,
                email: response.email
            }
        });

    })
    .catch((error) => {
        error = JSON.parse(error.data);

        dispatcher.dispatch({
            type: subscribeConstants.CHECK_UNSUBSCRIBE_ERROR,
            payload: {
                loading: false,
                isChecked: false,
                error: error.detail
            }
        });
    });

}

export function confirmUnsubscribe(id, hash, email){

    let url = URLS.subscribers + "/unsubscribe/"+ id +"/"+ hash;

    dispatcher.dispatch({
        type: subscribeConstants.CONFIRM_UNSUBSCRIBE_START,
        payload: { loading: true }
    });

    http.request({
        url: url,
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        data: { email }
    })
    .then((response) => {
        response = JSON.parse(response.data);

        dispatcher.dispatch({
            type: subscribeConstants.CONFIRM_UNSUBSCRIBE_END,
            payload: {
                loading: false,
                isConfirmed: true,
                email: response.email
            }
        });
    })
    .catch((error) => {
        error = JSON.parse(error.data);

        dispatcher.dispatch({
            type: subscribeConstants.CONFIRM_UNSUBSCRIBE_ERROR,
            payload: {
                loading: false,
                isConfirmed: false,
                error: error.detail
            }
        });
    });

}