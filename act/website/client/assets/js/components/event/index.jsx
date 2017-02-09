import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import { timeHasPassedFromNow } from "Utils/dateConverter";

import generateUrl from "Router/generateUrl";

import Socials from "Components/socials";
import Documents from "Components/documents";

import ProjectItem from "Components/projectItem";

@translate(["headlines"])
class EventComponent extends Component{

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
        this.setState({ isImageLoaded: true });
    }
    shouldComponentUpdate(nextProps, nextState){
        if(Object.keys(nextProps._event).length > 0){
            return true;
        }
        return false;
    }
    renderCenters(centres){
        centres = centres || [];
        
        return centres.map((center) => {
            let url = generateUrl("center", {id: center.id});

            return <Link to={ url } key={ center.id }>{ center.city.name }</Link>;
        });
    }
    renderNavigation(_event){
        let prev = _event.prev_object || {},
            next = _event.next_object || {},
            prevUrl = generateUrl("event", {id: prev.id, slug: prev.slug}),
            nextUrl = generateUrl("event", {id: next.id, slug: next.slug});

        return(
            <div class="navigation-holder">
                <Link to={ nextUrl } class={ next.id ? "icon icon-arrow-left" : "icon icon-arrow-left disabled" }></Link>
                <Link to={ prevUrl } class={ prev.id ? "icon icon-arrow-right" : "icon icon-arrow-right disabled" }></Link>  
            </div>
        );
    }
    renderRelatedProject(project){
        if(project){
            return(
                <div class="projects-holder">
                    <span class="upper-divider"></span>
                    <h2>{ this.props.t("headlines:events.relatedProject") }</h2>
                    <ProjectItem project={ project } />
                </div>
            );
        }
    }
    render(){
        let isLoading = this.props.isLoading,
            isMobile = this.props.isMobile,
            _event = this.props._event,
            metadata = this.props.metadata,
            photoObj = _event.image || {},
            eventCategory = _event.event_category,
            eventDocuments = _event.event_attached_documents || [],
            eventProject = _event.project,
            location = this.props.location;

        return(
            <article class="container event-holder extra-padding-top">
                <div class="inner">
                    <span class="upper-divider"></span>
                    <h1>{ _event.title }</h1>
                    <div class="centers-holder">
                        { this.renderCenters(_event.centres) }
                    </div>
                    { this.renderNavigation(_event) }
                    <div class={ this.state.isImageLoaded ? "photo-holder loaded" : "photo-holder" }>
                        <span class="category-holder">{ eventCategory ? eventCategory.title : "" }</span>    
                        <figure>
                            <img
                                src={ photoObj.original }
                                alt={ _event.title }
                                onLoad={ () => this.handleImageLoaded() }
                                onError={ () => this.handleImageError() }
                            />
                        </figure>
                    </div>
                    <div class="date-share-holder">
                        <time dateTime={ _event.created_at }>{ timeHasPassedFromNow(_event.created_at) }</time>
                        { !isLoading ? <Socials metadata={ metadata } /> : null }
                    </div>
                    <div class="content-holder" dangerouslySetInnerHTML={{ __html: _event.content }}></div>
                    <aside class="additional-content-holder">
                        {
                            eventDocuments.length
                                ? <Documents documents={ eventDocuments } />
                                : null
                        }
                        { this.renderRelatedProject(eventProject) }
                    </aside>
                </div>
            </article>
        );
    }

}

export default EventComponent;