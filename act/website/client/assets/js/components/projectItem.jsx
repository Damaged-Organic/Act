import React, { Component } from "react";
import { Link } from "react-router";

import generateUrl from "Router/generateUrl";
import { toNamedMonth } from "Utils/dateConverter";

class ProjectItem extends Component{

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
        let project = this.props.project,
            photoObj = project.image || {},
            url = generateUrl("project", {id: project.id, slug: project.slug});

        return(
            <article class="project-item-holder">
                <a href={ url }>
                    <figure class={ this.state.isImageLoaded ? "loaded" : "" }>
                        <img
                            src={ photoObj.wide }
                            alt={ project.title }
                            onLoad={ () => this.handleImageLoaded() }
                            onError={ () => this.handleImageError() }
                        />
                    </figure>
                    <time class="time-holder" dateTime={ project.modified_at }>{ toNamedMonth(project.modified_at) }</time>
                    <span class="category-holder">{ project.project_area.title }</span>
                    <h3>{ project.title }</h3>
                </a>
            </article>
        );
    }

}

export default ProjectItem;