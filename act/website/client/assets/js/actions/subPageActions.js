import dispatcher from "../dispatcher";

import URLS from "../api";
import httpBundle from "Utils/httpBundle";
import * as subPageConstants from "Constants/subPageConstants";

export function loadData(subPageId){

    let urls = [
        URLS.metadata + "/centres_subpages/" + subPageId,
        URLS.sponsors,
        URLS.socials,
        URLS.centersSubpages + "/"+ subPageId,
        URLS.centers + "?related=city",
        URLS.contacts + "?head_office",
        URLS.disclaimer
    ];

    dispatcher.dispatch({
        type: subPageConstants.LOAD_SUBPAGE_START,
        payload: { loading: true }
    });

    httpBundle(urls)
        .then((responses) => {
            responses = responses.map((response) => JSON.parse(response.data));

            let [metadata, sponsors, socials, subPage, centers, contacts, disclaimer] = responses;

            dispatcher.dispatch({
                type: subPageConstants.LOAD_SUBPAGE_END,
                payload: {
                    loading: false,
                    metadata,
                    sponsors,
                    socials,
                    subPage,
                    centers,
                    contacts,
                    disclaimer
                }
            });
        })
        .catch((error) => {
            error = JSON.parse(error.data);

            dispatcher.dispatch({
                type: subPageConstants.LOAD_SUBPAGE_ERROR,
                payload: {
                    loading: false,
                    error
                }
            });
        });
}