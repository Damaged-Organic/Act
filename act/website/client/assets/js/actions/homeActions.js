import dispatcher from "../dispatcher";

import httpBundle from "../utils/httpBundle";
import * as homeConstants from "../constants/homeConstants";

import URLS from "../api";

export function loadData(){

    let urls = [
        URLS.metadata + "/index",
        URLS.sponsors,
        URLS.socials,
        URLS.intro,
        URLS.centers + "?related=city",
        URLS.activities,
        URLS.projects,
        URLS.events,
        URLS.disclaimer,
        URLS.contacts + "?head_office"
    ];

    dispatcher.dispatch({
        type: homeConstants.LOAD_HOME_START,
        payload: { loading: true }
    });

    httpBundle(urls)
        .then((responses) => {
            responses = responses.map((response) => {
                return JSON.parse(response.data);
            });

            let [metadata, sponsors, socials, intro, centers, activities, projects, events, disclaimer, contacts] = responses;

            dispatcher.dispatch({
                type: homeConstants.LOAD_HOME_END,
                payload: {
                    loading: false,
                    metadata,
                    sponsors,
                    socials,
                    intro,
                    centers,
                    activities,
                    projects,
                    events,
                    disclaimer,
                    contacts
                }
            });
        })
        .catch((error) => {
            error = JSON.parse(error.data);

            dispatcher.dispatch({
                type: homeConstants.LOAD_HOME_ERROR,
                payload: {
                    loading: false,
                    error
                }
            });

        });

}