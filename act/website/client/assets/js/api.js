const API_SCHEMA = "https://";
const API_DOMAIN = "act.org.ua/api/"; 

const PATHS = {
    cities: "cities",
    projects: "projects",
    metadata: "metadata",
    centers: "centres",
    centersSubpages: "centres_subpages",
    participants: "participants",
    sponsors: "sponsors",
    projectCategories: "projects_areas",
    socials: "socials",
    eventsCategories: "events_categories",
    worksheets: "worksheets",
    activities: "activities",
    events: "events",
    intro: "intro_content",
    subscribers: "subscribers",
    contacts: "contacts",
    aboutContent: "about_content",
    goalContent: "goal_content",
    disclaimer: "disclaimer_content",
    partners: "partners",
    scrapings: "scrapings"
}

const URLS = Object.keys(PATHS).reduce((path, key) => {

    path[key] = API_SCHEMA + API_DOMAIN + PATHS[key];
    return path;

}, {});

export default URLS;
