import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';
import DropDownMenu from 'material-ui/DropDownMenu';
import MenuItem from 'material-ui/MenuItem';
import UploadPage from './UploadPage';
import CenteredGrid from './CenteredGrid';
import Database from './Database';
import Upload from './Upload';


class Login extends Component {
  constructor(props){
    super(props);
    var localloginComponent=[];
    localloginComponent.push(
      <MuiThemeProvider key={"theme"}>
        <div>
         <TextField
          style={{"margin-left": "40%"}}
           hintText="Please enter your username"
           floatingLabelText="User Name"
           onChange={(event,newValue) => this.setState({username:newValue})}
           />
         <br/>
           <TextField
            style={{"margin-left": "40%"}}
             type="password"
             hintText="Enter your Password"
             floatingLabelText="Password"
             onChange = {(event,newValue) => this.setState({password:newValue})}
             />
           <br/>
           <RaisedButton label="Submit" primary={true} style={{"margin-left": "40%"}} onClick={(event) => this.handleClick(event)}/>
       </div>
       </MuiThemeProvider>
    )
    this.state={
      username:'',
      password:'',
      menuValue:1,
      loginComponent:localloginComponent,
      loginRole:'student',
      instanceDetails:[],
      test : [],
      showModel : false,
      payload:{first_name:"",last_name:"",password:"",url:"",method:"",userid:""}
    }
  }
  
  handleClick(event){
    var self = this;
        
    this.setState({
      showModel: !this.state.showModel,
      payload : {"password":this.state.password,"url":window.homeURL + "login","method":"POST","userid":this.state.username}
    
    }) 

  }

  handleSubmitAction(){
    console.log("once or twice ")
    if(this.state.showModel)
    {    
      return <Database payload={this.state.payload} getDatafromDB={this.getDatafromDB} />
    }

  }

  getDatafromDB(data,flag){
    flag = true
    console.log("hai Iam back ",data,flag)
    if(flag)
    {
      return <Upload />
    }

  }


  handleMenuChange(value){
    console.log("menuvalue",value);
    var loginRole;
  
    this.setState({menuValue:value,
                   loginRole:loginRole})
  }
  render() {
    window.homeURL = "http://localhost:8000/api/students/"
    var sss = this.state.instanceDetails.data;
    console.log("Our if :::",this.state.showModel)
    if(this.state.showModel && this.state.username.length > 0 && this.state.password.length > 0)
    {
      console.log("inside if login ")
      return <Database payload={this.state.payload} getDatafromDB={this.getDatafromDB} />
    }
    
    return (

      
      <div>
      
      <div>
        <MuiThemeProvider>
        <AppBar title="Financepeer(HandsOn)"/>
        {this.state.loginComponent}
        </MuiThemeProvider>
      
        
      </div>
      
    </div>
    );
  }
}

const style = {
  margin: 15,
};

export default Login;