import dispatcher from "../dispatcher";

import URLS from "../api";
import httpBundle from "Utils/httpBundle";

import * as projectsConstants from "Constants/projectsConstants";

export function loadData(searchString){

    let urls = [
        URLS.metadata + "/projects",
        URLS.sponsors,
        URLS.socials,
        URLS.projects + searchString,
        URLS.projectCategories,
        URLS.centers + "?related=city",
        URLS.contacts + "?head_office",
        URLS.disclaimer
    ];

    dispatcher.dispatch({
        type: projectsConstants.LOAD_PROJECTS_START,
        payload: { loading: true }
    });

    httpBundle(urls)
        .then((responses) => {
            responses = responses.map((response) => JSON.parse(response.data));
            
            let [metadata, sponsors, socials, projects, categories, centers, contacts, disclaimer] = responses;

            dispatcher.dispatch({
                type: projectsConstants.LOAD_PROJECTS_END,
                payload: {
                    loading: false,
                    metadata,
                    sponsors,
                    socials,
                    projects,
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
                type: projectsConstants.LOAD_PROJECTS_END,
                payload: {
                    loading: false,
                    error: error
                }
            });

        });
}

