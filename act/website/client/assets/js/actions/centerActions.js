import dispatcher from "../dispatcher";

import URLS from "../api";
import httpBundle from "Utils/httpBundle";
import * as centerConstants from "Constants/centerConstants";

export function loadData(centerId){

    let urls = [
        URLS.metadata + "/centres/" + centerId,
        URLS.sponsors,
        URLS.socials,
        URLS.centers + "/" + centerId,
        URLS.centers + "?related=city",
        URLS.disclaimer,
        URLS.contacts + "?head_office"
    ];

    dispatcher.dispatch({
        type: centerConstants.LOAD_CENTER_START,
        payload: { loading: true }
    });

    httpBundle(urls)
        .then((responses) => {
            responses = responses.map((response) => JSON.parse(response.data));

            let [metadata, sponsors, socials, center, cities, disclaimer, contacts] = responses;

            dispatcher.dispatch({
                type: centerConstants.LOAD_CENTER_END,
                payload: {
                    loading: false,
                    metadata,
                    sponsors,
                    socials,
                    center,
                    cities,
                    disclaimer,
                    contacts
                }
            });
        })
        .catch((error) => {
            error = JSON.parse(error.data);

            dispatcher.dispatch({
                type: centerConstants.LOAD_CENTER_ERROR,
                payload: {
                    loading: false,
                    error
                }
            });
        });
}
