import React, { Component } from "react";
import { translate } from "react-i18next";

@translate(["headlines"])
class Participants extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        if(nextProps.participants.length > 0){
            return true;
        }
        return false;
    }
    getFullName(name, surname){
        return name + " " + surname;
    }
    renderParticipants(){
        let participants = this.props.participants || [];

        return participants.map((participant) => {
            let photo = participant.photo,
                fullName = this.getFullName(participant.name, participant.surname);

            return(
                <div key={ participant.id } class="participant">
                    <div class="inner">
                        <figure>
                            <img src={ photo.square } alt={ fullName } />
                        </figure>
                        <div class="info-holder">
                            <h3>{ fullName }</h3>
                            <p>{ participant.position }</p>
                        </div>
                    </div>
                </div>
            );
        });
    }
    render(){
        return(
            <section class="container participants-holder">
                <span class="upper-divider"></span>
                <h2>{ this.props.t("headlines:about.team") }</h2>
                <div class="inner">
                    { this.renderParticipants() }
                </div>
            </section>
        );
    }

}

export default Participants;