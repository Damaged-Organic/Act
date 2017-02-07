import React, { Component } from "react";
import Helmet from "react-helmet";

class PageMeta extends Component{

    constructor(props){
        super(props);

    }
    render(){
        let metadata = this.props.metadata,
            openGraph = metadata.open_graph || {},
            twitterCard = metadata.twitter_card || {};

        return(
            <Helmet
                title={ metadata.title }
                meta={[
                    { name: "robots", content: metadata.robots },
                    { name: "description", content: metadata.description },
                    { property: "og:title", content: openGraph.title },
                    { property: "og:type", content: openGraph.type },
                    { property: "og:url", content: document.URL },
                    { property: "og:image", content: openGraph.image },
                    { property: "og:description", content: openGraph.description },
                    { name: "twitter:card", content: twitterCard.card },
                    { name: "twitter:title", content: twitterCard.title },
                    { name: "twitter:image", content: twitterCard.image },
                    { name: "twitter:description", content: twitterCard.description },
                ]}
            />
        );
    }

}

export default PageMeta;
