import React, { Component } from "react";
import autoBind from "autobind-decorator";

import PageMeta from "Meta/";

import * as scrapingsActions from "Actions/scrapingsActions";

import * as centersActions from "Actions/centersActions";
import CentersStore from "Stores/centersStore";

import Header from "Pages/header/";
import CentersComponent from "Components/centers/";

import Loader from "Components/loader";

import isMobile from "Utils/isMobile";

@autoBind
class Centers extends Component{

    constructor(props){
        super(props);

        this.state = {
            isLoading: true,
            isMobile: isMobile(),
            metadata: CentersStore.getMetaData(),
            sponsors: CentersStore.getSponsors(),
            socials: CentersStore.getSocials(),
            centers: CentersStore.getCenters()
        }
    }
    componentWillMount(){
        CentersStore.on("change", this.handleCenterStoreChange);
    }
    componentDidMount(){
        centersActions.loadData();
    }
    componentDidUpdate(prevProps, prevStates){
        if(this.state.isLoading) return;

        let path = this.props.location.pathname,
            head = document.querySelector("head").innerHTML;

        scrapingsActions.scrap(path, head);
    }
    componentWillUnmount(){
        CentersStore.removeListener("change", this.handleCenterStoreChange);
    }
    handleCenterStoreChange(){
        if(CentersStore.isLoading()) return;

        this.setState({
            isLoading: CentersStore.isLoading(),
            metadata: CentersStore.getMetaData(),
            sponsors: CentersStore.getSponsors(),
            socials: CentersStore.getSocials(),
            centers: CentersStore.getCenters()
        });
    }
    render(){
        let isLoading = this.state.isLoading,
            isMobile = this.state.isMobile,
            metadata = this.state.metadata,
            sponsors = this.state.sponsors,
            socials = this.state.socials,
            centers = this.state.centers;

        return(
            <div id="page" class="__centers">
                <PageMeta metadata={ metadata } />
                <Header sponsors={ sponsors } socials={ socials } location={ this.props.location } isMobile={ isMobile } />
                <main id="content">
                    <CentersComponent centers={ centers } isMobile={ isMobile } />
                </main>
                <Loader isLoading={ isLoading } />
            </div>
        );
    }
}

export default Centers;
