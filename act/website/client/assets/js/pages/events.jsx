import React, { Component } from "react";
import autoBind from "autobind-decorator";
import { translate } from "react-i18next";

import PageMeta from "Meta/";

import * as scrapingsActions from "Actions/scrapingsActions";

import * as eventsActions from "Actions/eventsActions";
import EventsStore from "Stores/eventsStore";

import Header from "Pages/header/";
import Footer from "Pages/footer";
import EventComponent from "Components/events/";

import Loader from "Components/loader";

import isMobile from "Utils/isMobile";

@autoBind
class Events extends Component{

    constructor(props){
        super(props);

        this.state = {
            isLoading: true,
            isMobile: isMobile(),
            metadata: EventsStore.getMetaData(),
            sponsors: EventsStore.getSponsors(),
            socials: EventsStore.getSocials(),
            events: EventsStore.getEvents(),
            categories: EventsStore.getCategories(),
            centers: EventsStore.getCenters(),
            contacts: EventsStore.getContacts(),
            disclaimer: EventsStore.getDisclaimer()
        }
    }
    componentWillMount(){
        EventsStore.on("change", this.handleStoreChange);
    }
    componentWillUpdate(nextProps, nextState){
        if(nextProps.location.search !== this.props.location.search){
            this.setState({ isLoading: true });
            eventsActions.loadData(nextProps.location.search);
        }
    }
    shouldComponentUpdate(nextProps, nextState){
        if(nextState.sponsors.length){
            return true;
        }
        return false;
    }
    componentDidMount(){
        eventsActions.loadData(this.props.location.search);
    }
    componentDidUpdate(prevProps, prevStates){
        if(this.state.isLoading) return;

        let path = this.props.location.pathname,
            head = document.querySelector("head").innerHTML;

        scrapingsActions.scrap(path, head);
    }
    componentWillUnmount(){
        EventsStore.removeListener("change", this.handleStoreChange);
    }
    handleStoreChange(){

        this.setState({
            isLoading: EventsStore.isLoading(),
            metadata: EventsStore.getMetaData(),
            sponsors: EventsStore.getSponsors(),
            socials: EventsStore.getSocials(),
            events: EventsStore.getEvents(),
            categories: EventsStore.getCategories(),
            centers: EventsStore.getCenters(),
            contacts: EventsStore.getContacts(),
            disclaimer: EventsStore.getDisclaimer()
        });
    }
    render(){
        let isLoading = this.state.isLoading,
            isMobile = this.state.isMobile,
            metadata = this.state.metadata,
            sponsors = this.state.sponsors,
            socials = this.state.socials,
            events = this.state.events,
            categories = this.state.categories,
            centers = this.state.centers,
            contacts = this.state.contacts,
            disclaimer = this.state.disclaimer;

        return(
            <div id="page" class="__events">
                <PageMeta metadata={ metadata } />
                <Header sponsors={ sponsors } socials={ socials } location={ this.props.location } isMobile={ isMobile } />
                <main id="content">
                    <div class="container events-holder extra-padding-top">
                        <div class="inner">
                            <span class="upper-divider"></span>
                            <h1>{ this.props.t("headlines:events.ourEvents") }</h1>
                            <EventComponent
                                events={ events }
                                centers={ centers }
                                categories={ categories }
                                location={ this.props.location }
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

export default translate(["headlines"], {wait: true})(Events);
