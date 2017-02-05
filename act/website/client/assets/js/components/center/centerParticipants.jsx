import React, { Component } from "react";
import { translate } from "react-i18next";

import Participant from "./participant";

@translate(["center"], {wait: true})
class CenterParticipants extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        return nextProps.participants.length > 0 ? true : false;
    }
    renderParticipant(participants){
        return participants.map((participant) => <Participant key={ participant.id } participant={ participant } />);
    }
    render(){
        let participants = this.props.participants;

        if(participants.length <= 0) return null;

        return(
            <div class="container participants-holder">
                <div class="inner">
                    <span class="upper-divider"></span>
                    <h2>{ this.props.t("center:headlines.participants") }</h2>
                    <section class="participants">
                        { this.renderParticipant(participants) }
                    </section>
                </div>
            </div>
        );
    }

}

export default CenterParticipants;