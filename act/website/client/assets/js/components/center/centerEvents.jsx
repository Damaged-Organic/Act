import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import { toNamedMonth } from "Utils/dateConverter";

import EventItem from "Components/eventItem";

import generateUrl from "Router/generateUrl";

@translate(["center"], {wait: true})
class CenterEvents extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        return nextProps.events.length > 0 ? true : false;
    }
    renderTopEvent(topEvent){

        let photo = topEvent.image || {},
            url = generateUrl("event", {id: topEvent.id, slug: topEvent.slug});

        return(
            <article class="top-event-holder">
                <Link to={ url }>
                    <figure>
                        <img src={ photo.wide } alt={ topEvent.title } />
                    </figure>
                    <time class="date-holder" dateTime={ topEvent.created_at }>{ toNamedMonth(topEvent.created_at) }</time>
                    <span class="category-holder">{ topEvent.event_category.title }</span>
                    <h3>{ topEvent.title }</h3>
                </Link>
            </article>
        );
    }
    renderEvents(events){
        return events.map((_event) => <EventItem key={ _event.id } _event={ _event } location={ this.props.location } />);
    }
    render(){
        let events = this.props.events,
            topEvent = this.props.topEvent,
            centerId = this.props.centerId,
            url = generateUrl("events"),
            query = { centres: centerId };

        if(events.length <= 0) return null;

        events = Object.keys(topEvent).length ? this.props.events.slice(0, 4) : this.props.events.slice(0, 3);

        events = events.filter((_event) => topEvent.id !== _event.id );

        return(
            <div class="container events-holder">
                <div class="inner">
                    <span class="upper-divider"></span>
                    <h2>{ this.props.t("center:headlines.events") }</h2>
                    <section class="events">
                        { (Object.keys(topEvent).length > 0) ? this.renderTopEvent(topEvent) : null }
                        <div class="inner">
                            { this.renderEvents(events) }    
                        </div>
                    </section>
                    <div class="btn">
                        <Link to={{ pathname: url, query: query }}>{ this.props.t("center:buttons.allEvents") }</Link>
                    </div>
                </div>
            </div>
        );
    }

}

export default CenterEvents;