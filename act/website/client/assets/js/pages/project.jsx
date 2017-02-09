import React, { Component } from "react";
import autoBind from "autobind-decorator";

import PageMeta from "Meta/";

import * as scrapingsActions from "Actions/scrapingsActions";

import * as projectActions from "Actions/projectActions";
import ProjectStore from "Stores/projectStore";

import Header from "Pages/header/";
import Footer from "Pages/footer/";

import ProjectComponent from "Components/project/";

import Loader from "Components/loader";

import isMobile from "Utils/isMobile";

@autoBind
class Project extends Component{

    constructor(props){
        super(props);

        this.state = {
            isLoading: true,
            isMobile: isMobile(),
            metadata: ProjectStore.getMetaData(),
            sponsors: ProjectStore.getSponsors(),
            socials: ProjectStore.getSocials(),
            project: ProjectStore.getProject(),
            centers: ProjectStore.getCenters(),
            contacts: ProjectStore.getContacts(),
            disclaimer: ProjectStore.getDisclaimer()
        }
    }
    componentWillMount(){
        ProjectStore.on("change", this.handleStoreChange);
    }
    componentDidMount(){
        projectActions.loadData(this.props.params.id);
    }
    componentDidUpdate(prevProps, prevStates){
        if(this.state.isLoading) return;

        let path = this.props.location.pathname,
            head = document.querySelector("head").innerHTML;

        scrapingsActions.scrap(path, head);
    }
    componentWillReceiveProps(nextProps){
        projectActions.loadData(nextProps.params.id);
    }
    componentWillUnmount(){
        ProjectStore.removeListener("change", this.handleStoreChange);
    }
    handleStoreChange(){
        this.setState({
            isLoading: ProjectStore.isLoading(),
            metadata: ProjectStore.getMetaData(),
            sponsors: ProjectStore.getSponsors(),
            socials: ProjectStore.getSocials(),
            project: ProjectStore.getProject(),
            centers: ProjectStore.getCenters(),
            contacts: ProjectStore.getContacts(),
            disclaimer: ProjectStore.getDisclaimer()
        });
    }
    render(){
        let isLoading = this.state.isLoading,
            isMobile = this.state.isMobile,
            metadata = this.state.metadata,
            sponsors = this.state.sponsors,
            socials = this.state.socials,
            project = this.state.project,
            centers = this.state.centers,
            contacts = this.state.contacts,
            disclaimer = this.state.disclaimer;

        return(
            <div id="page" class="__project">
                <PageMeta metadata={ metadata } />
                <Header sponsors={ sponsors } socials={ socials } location={ this.props.location } isMobile={ isMobile } />
                <main id="content">
                    <ProjectComponent
                        project={ project }
                        metadata={ metadata }
                        location={ this.props.location }
                        isMobile={ isMobile }
                        isLoading={ isLoading }
                    />
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

export default Project;
