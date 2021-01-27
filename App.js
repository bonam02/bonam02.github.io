import React from 'react';
import {BrowserRouter, Switch, Route } from 'react-router-dom';
import Loginscreen from './Loginscreen';
import CenteredGrid from './CenteredGrid';
import Register from './Register';
import Upload from './Upload'



const App = () => (
  <div className="app-routes">
    <BrowserRouter>
        <Switch>
          <Route path="/login" component={Loginscreen} />
          <Route path="/register" component={Register} />
          <Route path="/Upload" component={Upload} />
          <Route path="/center" component={CenteredGrid} />
        </Switch>
    </BrowserRouter>
    

  </div>

);

export default App;