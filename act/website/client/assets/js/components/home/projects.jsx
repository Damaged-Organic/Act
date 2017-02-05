import React, { Component } from "react";
import { translate } from "react-i18next";

import generateUrl from "Router/generateUrl";

import ProjectItem from "Components/projectItem";

@translate(["headlines", "buttons"])
class Projects extends Component{

    constructor(){
        super();
    }
    renderProject(){
        let projects = this.props.projects.results || [];

        projects = projects.slice(0, 3);

        return projects.map((project) => <ProjectItem key={ project.id } project={ project } />);
    }
    render(){
        let url = this.props.projects.url;
        
        return(
            <section class="container home-projects-holder">
                <div class="inner">
                    <span class="upper-divider"></span>
                    <h2>{ this.props.t("headlines:home.projects") }</h2>
                    <div class="projects">
                        { this.renderProject() }
                    </div>
                    <div class="btn-more">
                        <a href={ generateUrl("projects") }>{ this.props.t("buttons:allProjects") }</a>
                    </div>
                </div>
            </section>
        );
    }

}

export default Projects;