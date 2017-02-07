import React, { Component } from "react";
import autoBind from "autobind-decorator";

import PageMeta from "Meta/";

import * as scrapingsActions from "Actions/scrapingsActions";

import * as homeActions from "Actions/homeActions";
import HomeStore from "Stores/homeStore";

import Loader from "Components/loader";

import Header from "Pages/header/";
import Footer from "Pages/footer/";

import Intro from "Components/home/intro";
import Centers from "Components/home/centers/";
import Activities from "Components/home/activities/";
import Projects from "Components/home/projects";
import Events from "Components/home/events";

import isMobile from "Utils/isMobile";

@autoBind
class Home extends Component{

    constructor(props){
        super(props);

        this.state = {
            isLoading: true,
            isMobile: isMobile(),
            metadata: HomeStore.getMetaData(),
            sponsors: HomeStore.getSponsors(),
            socials: HomeStore.getSocials(),
            intro: HomeStore.getIntro(),
            centers: HomeStore.getCenters(),
            activities: HomeStore.getActivities(),
            projects: HomeStore.getProjects(),
            events: HomeStore.getEvents(),
            disclaimer: HomeStore.getDisclaimer(),
            contacts: HomeStore.getContacts()
        };
    }
    componentWillMount(){
        HomeStore.on("change", this.handleStoreChange);
    }
    componentDidMount(){
        homeActions.loadData();
    }
    componentDidUpdate(prevProps, prevStates){
        if(this.state.isLoading) return;

        let path = this.props.location.pathname,
            head = document.querySelector("head").innerHTML;

        scrapingsActions.scrap(path, head);
    }
    componentWillUnmount(){
        HomeStore.removeListener("change", this.handleStoreChange);
    }
    handleStoreChange(){
        if(HomeStore.isLoading()) return;

        this.setState({
            isLoading: HomeStore.isLoading(),
            metadata: HomeStore.getMetaData(),
            sponsors: HomeStore.getSponsors(),
            socials: HomeStore.getSocials(),
            intro: HomeStore.getIntro(),
            centers: HomeStore.getCenters(),
            activities: HomeStore.getActivities(),
            projects: HomeStore.getProjects(),
            events: HomeStore.getEvents(),
            disclaimer: HomeStore.getDisclaimer(),
            contacts: HomeStore.getContacts()
        });
    }
    render(){
        let isLoading = this.state.isLoading,
            isMobile = this.state.isMobile,
            metadata = this.state.metadata,
            sponsors = this.state.sponsors,
            socials = this.state.socials,
            intro = this.state.intro,
            centers = this.state.centers,
            activities = this.state.activities,
            projects = this.state.projects,
            events = this.state.events,
            disclaimer = this.state.disclaimer,
            contacts = this.state.contacts;

        return(
            <div id="page" class="__home">
                <PageMeta metadata={ metadata } />
                <Header sponsors={ sponsors } socials={ socials } location={ this.props.location } isMobile={ isMobile } />
                <main id="content">
                    <Intro intro={ intro } />
                    <Centers centers={ centers } isMobile={ isMobile } />
                    <Activities activities={ activities } />
                    { events.count > 0 ? <Events events={ events } isMobile={ isMobile } /> : ""}
                    { projects.count > 0 ? <Projects projects={ projects } /> : ""}
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

export default Home;
