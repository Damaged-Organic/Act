import dispatcher from "../dispatcher";

import URLS from "../api";
import httpBundle from "Utils/httpBundle";
import * as aboutConstants from "Constants/aboutConstants";

export function loadData(){

    let urls = [
        URLS.metadata + "/about",
        URLS.sponsors,
        URLS.socials,
        URLS.activities,
        URLS.aboutContent,
        URLS.goalContent,
        URLS.centers + "?related=city",
        URLS.contacts + "?head_office",
        URLS.participants + "?head_office",
        URLS.partners,
        URLS.disclaimer
    ];

    dispatcher.dispatch({
        type: aboutConstants.LOAD_ABOUT_START,
        payload: { loading: true }
    });

    httpBundle(urls)
        .then((responses) => {
            responses = responses.map((response) => JSON.parse(response.data));

            let [metadata, sponsors, socials, activities, aboutContent, goalContent, centers, contacts, participants, partners, disclaimer] = responses;

            dispatcher.dispatch({
                type: aboutConstants.LOAD_ABOUT_END,
                payload: {
                    loading: false,
                    metadata,
                    sponsors,
                    socials,
                    activities,
                    aboutContent,
                    goalContent,
                    centers,
                    contacts,
                    participants,
                    partners,
                    disclaimer
                }
            });
        })
        .catch((error) => {
            error = JSON.parse(error.data);

            dispatcher.dispatch({
                type: aboutConstants.LOAD_ABOUT_ERROR,
                payload: {
                    loading: false,
                    error
                }
            });
        });

}