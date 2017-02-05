import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import generateUrl from "Router/generateUrl";

import EventItem from "Components/eventItem";

@translate(["headlines", "buttons"])
class Events extends Component{

    constructor(){
        super();
    }
    renderEvent(){
        let isMobile = this.props.isMobile,
            events = this.props.events.results || [];

        events = !isMobile ? events.slice(0, 3) : events.slice(0, 4);

        return events.map((_event) => <EventItem key={ _event.id } _event={ _event } location={ this.props.location } />);
    }
    render(){
        return(
            <section class="container home-events-holder">
                <div class="inner">
                    <span class="upper-divider"></span>
                    <h2>{ this.props.t("headlines:home.events") }</h2>
                    <div class="events">
                        { this.renderEvent() }
                    </div>
                    <div class="btn-more">
                        <Link to={ generateUrl("events") }>{ this.props.t("buttons:allEvents") }</Link>
                    </div>
                </div>
            </section>
        );
    }

}

export default Events;