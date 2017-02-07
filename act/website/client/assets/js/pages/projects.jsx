import React, { Component } from "react";
import autoBind from "autobind-decorator";
import { translate } from "react-i18next";

import PageMeta from "Meta/";

import * as scrapingsActions from "Actions/scrapingsActions";

import * as projectsActions from "Actions/projectsActions";
import ProjectsStore from "Stores/projectsStore";

import Header from "Pages/header/";
import Footer from "Pages/footer/";

import ProjectsComponent from "Components/projects/";

import Loader from "Components/loader";

import isMobile from "Utils/isMobile";

@autoBind
class Projects extends Component{

    constructor(props){
        super(props);

        this.state = {
            isLoading: true,
            isMobile: isMobile(),
            metadata: ProjectsStore.getMetaData(),
            sponsors: ProjectsStore.getSponsors(),
            socials: ProjectsStore.getSocials(),
            projects: ProjectsStore.getProjects(),
            categories: ProjectsStore.getCategories(),
            centers: ProjectsStore.getCenters(),
            contacts: ProjectsStore.getContacts(),
            disclaimer: ProjectsStore.getDisclaimer()
        }
    }
    componentWillMount(){
        ProjectsStore.on("change", this.handleProjectStoreChange);
    }
    componentWillUpdate(nextProps, nextState){
        if(nextProps.location.search !== this.props.location.search){
            this.setState({ isLoading: true });
            projectsActions.loadData(nextProps.location.search);
        }
    }
    shouldComponentUpdate(nextProps, nextState){
        return nextState.sponsors.length ? true : false;
    }
    componentDidMount(){
        projectsActions.loadData(this.props.location.search);
    }
    componentDidUpdate(prevProps, prevStates){
        if(this.state.isLoading) return;

        let path = this.props.location.pathname,
            head = document.querySelector("head").innerHTML;

        scrapingsActions.scrap(path, head);
    }
    componentWillUnmount(){
        ProjectsStore.removeListener("change", this.handleProjectStoreChange);
    }
    handleProjectStoreChange(){
        if(ProjectsStore.isLoading()) return;

        this.setState({
            isLoading: ProjectsStore.isLoading(),
            metadata: ProjectsStore.getMetaData(),
            sponsors: ProjectsStore.getSponsors(),
            socials: ProjectsStore.getSocials(),
            projects: ProjectsStore.getProjects(),
            categories: ProjectsStore.getCategories(),
            centers: ProjectsStore.getCenters(),
            contacts: ProjectsStore.getContacts(),
            disclaimer: ProjectsStore.getDisclaimer()
        });
    }
    render(){
        let isLoading = this.state.isLoading,
            isMobile = this.state.isMobile,
            metadata = this.state.metadata,
            sponsors = this.state.sponsors,
            socials = this.state.socials,
            projects = this.state.projects,
            categories = this.state.categories,
            centers = this.state.centers,
            contacts = this.state.contacts,
            disclaimer = this.state.disclaimer;

        return(
            <div id="page" class="__projects">
                <PageMeta metadata={ metadata } />
                <Header sponsors={ sponsors } socials={ socials } location={ this.props.location } isMobile={ isMobile } />
                <main id="content">
                    <div class="container projects-holder extra-padding-top">
                        <div class="inner">
                            <span class="upper-divider"></span>
                            <h1>{ this.props.t("headlines:projects.ourProjects") }</h1>
                            <ProjectsComponent
                                centers={ centers }
                                categories={ categories }
                                projects={ projects }
                                location={ this.props.location }
                                routeParams={ this.props.routeParams }
                                isMobile={ isMobile }
                            />
                        </div>
                    </div>
                </main>
                <Loader isLoading={ isLoading } />
                <Footer
                    centers={ centers }
                    socials={ socials }
                    contacts={ contacts }
                    disclaimer={ disclaimer }
                />
            </div>
        );
    }
}

export default translate(["headlines"], {wait:true})(Projects);
