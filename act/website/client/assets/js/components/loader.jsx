import React, { Component } from "react";

class Loader extends Component{

    constructor(props){
        super(props);

    }
    render(){
        let isLoading = this.props.isLoading;

        return(
            <div id="loader-holder" class={ !isLoading ? "__loaded" : "" }>
                <div class="svg-holder">
                    <svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
                        <g>
                            <path class="tall" d="M172.7,0.9c22.2,0,44.3,0,66.5,0c0.5,0.3,1.1,0.6,1.6,0.8c13.9,3.4,21.2,12.2,20.8,26.4c-1,35.2-2.3,70.4-3.5,105.6
                                c-1.4,39.9-2.6,79.8-4.1,119.7c-0.6,16.1-11.6,26.6-27.7,26.6c-13.3,0-26.5,0-39.8,0c-17.1,0-28.1-10.7-28.6-27.8
                                c-0.7-21.7-1.4-43.3-2.1-65c-1.5-42.1-2.9-84.1-4.5-126.2c-0.2-5.1-0.7-10.2-1.1-15.2c0-8.4,0-16.9,0-25.3
                                c1.2-2.3,2.2-4.7,3.5-6.9C157.9,6.4,164.9,3.1,172.7,0.9z"/>

                            <path class="dot" d="M206.5,308.2c6.2,0,12.5,0,18.7,0c19.9,0.1,32.9,11,35.1,30.8c1.1,10.2,1.1,20.6,0,30.8c-1.9,18.4-12.6,29-31,30.2
                                c-15.4,1-30.9,0.9-46.2,0c-17.4-1.1-28.2-11-30.3-28.2c-1.4-11.6-1.4-23.8,0.2-35.4c2.4-17.8,15.1-27.8,33-28.2
                                C192.8,308.1,199.6,308.2,206.5,308.2z"/>
                        </g>
                    </svg>
                </div>
            </div>
        );
    }

}

export default Loader;