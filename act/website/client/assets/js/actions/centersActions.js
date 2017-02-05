import dispatcher from "../dispatcher";

import URLS from "../api";
import httpBundle from "../utils/httpBundle";
import * as centersConstants from "../constants/centersConstants";

export function loadData(){

    let urls = [
        URLS.metadata + "/centres",
        URLS.sponsors,
        URLS.socials,
        URLS.centers + "?related=city"
    ];

    dispatcher.dispatch({
        type: centersConstants.LOAD_CENTERS_START,
        payload: { loading: true }
    });

    httpBundle(urls)
        .then((responses) => {
            responses = responses.map((response) => JSON.parse(response.data));
            
            let [metadata, sponsors, socials, centers] = responses;

            dispatcher.dispatch({
                type: centersConstants.LOAD_CENTERS_END,
                payload: {
                    loading: false,
                    metadata,
                    sponsors,
                    socials,
                    centers
                }
            });
        })
        .catch((error) => {
            error = JSON.parse(error.data);

            dispatcher.dispatch({
                type: centersConstants.LOAD_CENTERS_ERROR,
                payload: {
                    loading: false,
                    error
                }
            });

        });

}