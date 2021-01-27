import React, { Component } from 'react'
import CustomizedTables from './CustomizedTables';
import Login from './Login';
import Upload from './Upload'

export class Database extends Component {
    
    constructor(props) {
        super(props)
       
        
        this.state = {
             payload : [],
             details : {},
             flag : true,
             method:'GET'
        }
    }
    

    hitDatabase = () => {
        console.log('this.props.payload- - - -', this.props.payload)
        var apiBaseUrl = this.props.payload.url
        var method = this.props.payload.method
        console.log('apiBaseUrl----', apiBaseUrl,method)
        fetch(apiBaseUrl, {
            cache: "no-cache",
            credentials: "same-origin",
            headers: {
                "content-type": "application/json",
                "Access-Control-Allow-Origin": "*"

            },
            body: JSON.stringify({
            "payload": this.props.payload
             }),
            method: method,
            mode: "cors",
            redirect: "follow",
            referrer: "no-referrer"
        }).then(response =>
            response.json().then(data => ({data: data,status: response.status }))
            .then(res => {console.log("for Connections is: ",res.data);
                    this.setState({ details: res.data, flag:false })
                    this.props.getDatafromDB(res.data,res.flag)

                })
        );     
        
    }
    

    render() {
        console.log('this.state.flag', this.state.flag)
        console.log('details--', this.state.details)
        if(this.state.flag)
        {
            this.hitDatabase()
        }
        if(this.state.details.errorMessage == "User does not exist")
        {
            return(   
               <Login />              
            )
        }else
        {
            return (
                <div>   
                    <Upload />
                </div>
            )
        }
       
    }
}

export default Database
