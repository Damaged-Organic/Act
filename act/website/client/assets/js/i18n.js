import i18n from "i18next";
import XHR from 'i18next-xhr-backend';

import { staticPath } from "Settings";

i18n
    .use(XHR)
    .init({
        lng: "uk",
        lngs: ["uk"],
        fallbackLng: "uk",
        debug: false,
        ns: ["common"],
        defaultNS: "common",
        load: "currentOnly",
        backend: {
            loadPath: staticPath("/locales/{{lng}}/{{ns}}.json")
        },
        preload: ["uk"]
    });

export default i18n;
