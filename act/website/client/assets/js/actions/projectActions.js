import dispatcher from "../dispatcher";

import URLS from "../api";

import httpBundle from "Utils/httpBundle";
import * as projectConstants from "Constants/projectConstants";

export function loadData(projectId){

    let urls = [
        URLS.metadata + "/projects/" + projectId,
        URLS.sponsors,
        URLS.socials,
        URLS.projects +"/"+ projectId,
        URLS.centers + "?related=city",
        URLS.contacts + "?head_office",
        URLS.disclaimer
    ];

    dispatcher.dispatch({
        type: projectConstants.LOAD_PROJECT_START,
        payload: { loading: true }
    });

    httpBundle(urls)
        .then((responses) => {
            responses = responses.map((response) => JSON.parse(response.data));

            let [metadata, sponsors, socials, project, centers, contacts, disclaimer] = responses;

            dispatcher.dispatch({
                type: projectConstants.LOAD_PROJECT_END,
                payload: {
                    loading: false,
                    metadata,
                    sponsors,
                    socials,
                    project,
                    centers,
                    contacts,
                    disclaimer
                }
            });
        })
        .catch((error) => {
            error = JSON.parse(error.data);

            dispatcher.dispatch({
                type: projectConstants.LOAD_PROJECT_ERROR,
                payload: {
                    loading: false,
                    error
                }
            });
        });

}