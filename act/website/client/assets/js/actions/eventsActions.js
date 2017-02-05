import dispatcher from "../dispatcher";

import URLS from "../api";

import httpBundle from "Utils/httpBundle";
import * as eventsConstants from "Constants/eventsConstants";

export function loadData(searchString){

    let urls = [
        URLS.metadata + "/events",
        URLS.sponsors,
        URLS.socials,
        URLS.events + searchString,
        URLS.eventsCategories,
        URLS.centers + "?related=city",
        URLS.contacts + "?head_office",
        URLS.disclaimer
    ];

    dispatcher.dispatch({
        type: eventsConstants.LOAD_EVENTS_START,
        payload: { loading: true }
    });

    httpBundle(urls)
        .then((responses) => {
            responses = responses.map((response) => JSON.parse(response.data));
            
            let [metadata, sponsors, socials, events, categories, centers, contacts, disclaimer] = responses;

            dispatcher.dispatch({
                type: eventsConstants.LOAD_EVENTS_END,
                payload: {
                    loading: false,
                    metadata,
                    sponsors,
                    socials,
                    events,
                    categories,
                    centers,
                    contacts,
                    disclaimer
                }
            });

        })
        .catch((error) => {
            error = JSON.parse(error.data);

            dispatcher.dispatch({
                type: eventsConstants.LOAD_EVENTS_ERROR,
                payload: {
                    loading: false,
                    error: error
                }
            });
        });

}