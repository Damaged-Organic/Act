import dispatcher from "../dispatcher";

import URLS from "../api";

import httpBundle from "Utils/httpBundle";
import * as eventConstants from "Constants/eventConstants";

export function loadData(eventId){

    let urls = [
        URLS.metadata + "/events/" + eventId,
        URLS.sponsors,
        URLS.socials,
        URLS.events +"/"+ eventId,
        URLS.centers +"?related=city",
        URLS.contacts + "?head_office",
        URLS.disclaimer
    ];

    dispatcher.dispatch({
        type: eventConstants.LOAD_EVENT_START,
        payload: { loading: true }
    });

    httpBundle(urls)
        .then((responses) => {
            responses = responses.map((response) => JSON.parse(response.data));

            let [metadata, sponsors, socials, _event, centers, contacts, disclaimer] = responses;

            dispatcher.dispatch({
                type: eventConstants.LOAD_EVENT_END,
                payload: {
                    loading: false,
                    metadata,
                    sponsors,
                    socials,
                    _event,
                    centers,
                    contacts,
                    disclaimer
                }
            });

        })
        .catch((error) => {
            error = JSON.parse(error.data);

            dispatcher.dispatch({
                type: eventConstants.LOAD_EVENT_ERROR,
                payload: {
                    loading: true,
                    error
                }
            });
        });

}