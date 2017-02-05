import React, { Component } from "react";
import { translate } from "react-i18next";

import EventItem from "Components/eventItem";

@translate(["headlines"])
class RelatedEvents extends Component{

    constructor(props){
        super(props);
        
    }
    renderEvents(){
        return this.props.events.map((_event) => <EventItem key={ _event.id } _event={ _event } location={ this.props.location } />);
    }
    render(){
        if(this.props.events.length <= 0) return null;

        return(
            <div class="events-holder">
                <span class="upper-divider"></span>
                <h2>{ this.props.t("headlines:projects.relatedEvents") }</h2>
                <div class="inner">
                    { this.renderEvents() }
                </div>
            </div>
        );
    }

}

export default RelatedEvents;