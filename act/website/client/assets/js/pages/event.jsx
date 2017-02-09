import React, { Component } from "react";
import autoBind from "autobind-decorator";

import PageMeta from "Meta/";

import * as scrapingsActions from "Actions/scrapingsActions";

import * as eventActions from "Actions/eventActions";
import EventStore from "Stores/eventStore";

import Header from "Pages/header/";
import EventComponent from "Components/event/";
import Footer from "Pages/footer/";

import Loader from "Components/loader";

import isMobile from "Utils/isMobile";

@autoBind
class Event extends Component{

    constructor(props){
        super(props);

        this.state = {
            isLoading: true,
            isMobile: isMobile(),
            metadata: EventStore.getMetaData(),
            sponsors: EventStore.getSponsors(),
            socials: EventStore.getSocials(),
            _event: EventStore.getEvent(),
            centers: EventStore.getCenters(),
            contacts: EventStore.getContacts(),
            disclaimer: EventStore.getDisclaimer()
        }
    }
    componentWillMount(){
        EventStore.on("change", this.handleStoreChange);
    }
    componentDidMount(){
        eventActions.loadData(this.props.params.id);
    }
    componentDidUpdate(prevProps, prevStates){
        if(this.state.isLoading) return;

        let path = this.props.location.pathname,
            head = document.querySelector("head").innerHTML;

        scrapingsActions.scrap(path, head);
    }
    componentWillReceiveProps(nextProps){
        this.setState({ isLoading: true });
        eventActions.loadData(nextProps.params.id);
    }
    componentWillUnmount(){
        EventStore.removeListener("change", this.handleStoreChange);
    }
    handleStoreChange(){
        if(EventStore.isLoading()) return;

        this.setState({
            isLoading: EventStore.isLoading(),
            metadata: EventStore.getMetaData(),
            sponsors: EventStore.getSponsors(),
            socials: EventStore.getSocials(),
            _event: EventStore.getEvent(),
            centers: EventStore.getCenters(),
            contacts: EventStore.getContacts(),
            disclaimer: EventStore.getDisclaimer()
        });
    }
    render(){
        let isLoading = this.state.isLoading,
            isMobile = this.state.isMobile,
            metadata = this.state.metadata,
            sponsors = this.state.sponsors,
            socials = this.state.socials,
            _event = this.state._event,
            centers = this.state.centers,
            contacts = this.state.contacts,
            disclaimer = this.state.disclaimer;

        return(
            <div id="page" class="__event">
                <PageMeta metadata={ metadata } />
                <Header sponsors={ sponsors } socials={ socials } location={ this.props.location } isMobile={ isMobile } />
                <main id="content">
                    <EventComponent
                        _event={ _event }
                        metadata={ metadata }
                        location={ this.props.location }
                        isLoading={ isLoading }
                        isMobile={ isMobile }
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

export default Event;
