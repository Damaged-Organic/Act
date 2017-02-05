import React, { Component } from "react";
import { translate } from "react-i18next";

import Filters from "./filters";
import Categories from "./categories";

import EventItem from "Components/eventItem";
import Pagination from "Components/pagination/";
import Empty from "Components/empty";

@translate(["common"])
class EventComponent extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        let eventsCount = nextProps.events.count || 0,
            categoriesCount = nextProps.categories.length;
        
        return (eventsCount > 0 || categoriesCount > 0) ? true : false;
    }
    renderEvent(eventItems){
        return eventItems.map((_event, index) => {
            return <EventItem key={ _event.id } _event={ _event } location={ this.props.location } />;
        });
    }
    renderEmpty(){
        return <Empty message={ this.props.t("empty") } />
    }
    render(){
        let isMobile = this.props.isMobile,
            events = this.props.events,
            eventItems = events.results || [],
            centers = this.props.centers,
            categories = this.props.categories,
            location = this.props.location;

        return(
            <div class="inner">
                <Filters centers={ centers } location={ location } />
                <Categories categories={ categories } location={ location } />
                <section class="events">
                    <div class="inner">
                        { events.count > 0 ? this.renderEvent(eventItems) : this.renderEmpty() }
                    </div>
                </section>
                <Pagination quantity={ events.count } splitBy={ 9 } url="events" location={ location } />
            </div>
        );
    }
}

export default EventComponent;