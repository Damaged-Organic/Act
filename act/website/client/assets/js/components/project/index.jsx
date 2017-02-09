import React, { Component } from "react";
import { Link } from "react-router";

import generateUrl from "Router/generateUrl";
import { separateBySlashes } from "Utils/dateConverter";

import Socials from "Components/socials";
import Documents from "Components/documents";
import RelatedEvents from "./relatedEvents";

class ProjectComponent extends Component{

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
    renderNavigation(project){
        let prev = project.prev_object || {},
            next = project.next_object || {},
            prevUrl = generateUrl("project", {id: prev.id, slug: prev.slug}),
            nextUrl = generateUrl("project", {id: next.id, slug: next.slug});

        return(
            <div class="navigation-holder">
                <Link to={ nextUrl } class={ next.id ? "icon icon-arrow-left": "icon icon-arrow-left disabled" }></Link>
                <Link to={ prevUrl } class={ prev.id ? "icon icon-arrow-right": "icon icon-arrow-right disabled" }></Link>
            </div>
        );
    }
    renderCenters(centers){
        centers = centers || [];

        return centers.map((center) => {
            let url = generateUrl("center", {id: center.id});

            return <Link key={ center.id } to={ url }>{ center.city.name }</Link>;
        });
    }
    render(){
        let isLoading = this.props.isLoading,
            isMobile = this.props.isMobile,
            project = this.props.project,
            metadata = this.props.metadata,
            photo = project.image || {},
            projectDocuments = project.project_attached_documents || [],
            relatedEvents = project.events || [],
            location = this.props.location;

        return(
            <article class="container project-holder extra-padding-top">
                <div class="inner">
                    <span class="upper-divider"></span>
                    <h1>{ project.title }</h1>
                    <div class="centers-holder">
                        { this.renderCenters(project.centres) }
                    </div>
                    <div class={ this.state.isImageLoaded ? "photo-holder loaded" : "photo-holder" }>
                        <span class="category-holder">{ project.project_area ? project.project_area.title : null }</span>    
                        <figure>
                            <img
                                src={ photo.original }
                                alt={ project.title }
                                onLoad={ () => this.handleImageLoaded() }
                                onError={ () => this.handleImageError() }
                            />
                        </figure>
                    </div>
                    { this.renderNavigation(project) }
                    <div class="date-share-holder">
                        <time dateTime={ project.modified_at }>{ separateBySlashes(project.modified_at) }</time>
                        { !isLoading ? <Socials metadata={ metadata } /> : null }
                    </div>
                    <div class="content-holder" dangerouslySetInnerHTML={{ __html: project.content }}></div>
                    <aside class="additional-content-holder">
                        <Documents documents={ projectDocuments } />
                        <RelatedEvents events={ relatedEvents } lcoation={ location } />
                    </aside>
                </div>
            </article>
        );
    }

}

export default ProjectComponent;