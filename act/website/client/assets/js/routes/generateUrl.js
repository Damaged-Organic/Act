import urls from "./routerUrls";

function generateUrl(routeName, params = {}){

    let currentRoute = urls[routeName],
        isParams = Object.keys(params).length > 0 ? true : false,
        paramsNeeded = /\:/gi.test(currentRoute);

    if(!currentRoute){
        console.error(`Router: route '${ routeName }' doesn't exist`);
        return;
    }

    if(paramsNeeded && !isParams){
        console.error(`Route: route '${ currentRoute }' requires params`);
        return;
    }

    if(isParams){
        
        for(let key in params){
            let regExp = new RegExp("(\\:"+ key +")", "gi");

            if(!regExp.test(currentRoute)){
                console.error(`Router: key '${ key }' doesn't exist in route '${ urls[routeName] }'`);
                return;
            }

            currentRoute = currentRoute.replace(regExp, params[key]);
        }

    }

    return currentRoute;
}

export default generateUrl;