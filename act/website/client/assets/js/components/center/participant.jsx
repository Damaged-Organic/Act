import React, { Component } from "react";

class Participant extends Component{

    constructor(props){
        super(props);
        
    }
    renderPhoto(photo, alt){
        if(!photo) return;

        return(
            <figure>
                <img src={ photo } alt={ alt } />
            </figure>
        );
    }
    render(){
        let participant = this.props.participant,
            photoObj = participant.photo || {};

        return(
            <article class="participant">
                <div class="inner">
                    { this.renderPhoto(photoObj.square, participant.surname) }
                    <span class="position-holder">{ participant.position }</span>
                    <h3>{ participant.name } {participant.surname}</h3>
                </div>
            </article>
        );
    }

}

export default Participant;