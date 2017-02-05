import React, { Component } from "react";
import { Link } from "react-router";

import generateUrl from "Router/generateUrl";
import { timeHasPassedFromNow } from "Utils/dateConverter";

class EventItem extends Component{

    constructor(props){
        super(props);
        
        this.state = {
            isImageLoaded: false
        }
    }
    handleImageLoaded(){
        this.setState({ isImageLoaded: true });
    }
    handleImageError(){
        this.setState({ isImageLoaded: false });
    }
    render(){
        let _event = this.props._event,
            photoObj = _event.image || {},
            location = this.props.location,
            url = generateUrl("event", {id: _event.id, slug: _event.slug});
        
        return(
            <article class="event-item-holder">
                <Link to={ url }>
                    <figure class={ this.state.isImageLoaded ? "loaded" : "" }>
                        <img
                            src={ photoObj.square }
                            alt={ _event.title }
                            onLoad={ () => this.handleImageLoaded() }
                            onError={ () => this.handleImageError() }
                        />
                    </figure>
                    <time class="time-holder" dateTime={_event.created_at}>{ timeHasPassedFromNow(_event.created_at) }</time>
                    <span class="category-holder">{ _event.event_category.title }</span>
                    <h2>{ _event.title }</h2>
                </Link>
            </article>
        );
    }

}

export default EventItem;