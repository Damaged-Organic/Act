import React, { Component } from "react";
import Helmet from "react-helmet";

import { staticPath } from "Settings";

class Meta extends Component{

    constructor(props){
        super(props);

    }
    render(){
        return(
            <Helmet
                htmlAttributes={{ lang: "uk", prefix: "og: http://ogp.me/ns#" }}
                titleTemplate="%s | Act"
                defaultTitle="Act | Мережа центрів громадського контролю"
                meta={[
                    { name: "HandheldFriendly", content: "true" },
                    { name: "MobileOptimized", content: "320" },
                    { name: "viewport", content: "width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui" },
                    { name: "format-detection", content: "telephone=no" },
                    { name: "format-detection", content: "address=no" },
                    { name: "mobile-web-app-capable", content: "yes" },
                    { name: "apple-mobile-web-app-capable", content: "yes" },
                    { name: "apple-mobile-web-app-status-bar-style", content: "black" },
                    { name: "apple-mobile-web-app-title", content: "Act" },
                    { "http-equiv": "cleartype", content: "no" },
                    { "http-equiv": "X-UA-Compatible", content: "IE=edge, chrome=1" },
                    { name: "msapplication-TileColor", content: "#333333" },
                    { name: "msapplication-TileImage", content: staticPath("/images/favicons/144x144.png") }
                ]}
                link={[
                    { rel: "apple-touch-icon", href: staticPath("/images/favicons/57x57.png") },
                    { rel: "apple-touch-icon", href: staticPath("/images/favicons/60x60.png") },
                    { rel: "apple-touch-icon", href: staticPath("/images/favicons/72x72.png") },
                    { rel: "apple-touch-icon", href: staticPath("/images/favicons/76x76.png") },
                    { rel: "apple-touch-icon", href: staticPath("/images/favicons/114x114.png") },
                    { rel: "apple-touch-icon", href: staticPath("/images/favicons/120x120.png") },
                    { rel: "apple-touch-icon", href: staticPath("/images/favicons/144x144.png") },
                    { rel: "apple-touch-icon", href: staticPath("/images/favicons/152x152.png") },
                    { rel: "apple-touch-icon", href: staticPath("/images/favicons/180x180.png") },
                    { rel: "icon", type: "image/png", href: staticPath("/images/favicons/16x16.png") },
                    { rel: "icon", type: "image/png", href: staticPath("/images/favicons/32x32.png") },
                    { rel: "icon", type: "image/png", href: staticPath("/images/favicons/96x96.png") },
                    { rel: "icon", type: "image/png", href: staticPath("/images/favicons/160x160.png") },
                    { rel: "icon", type: "image/png", href: staticPath("/images/favicons/192x192.png") },
                ]}
            />
        );
    }

}

export default Meta;
