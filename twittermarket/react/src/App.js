import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

import { Login } from './Login/login';
import { Home } from './Home/home'
import { Signup } from './Signup/signup'
import './App.css';

function App() {
  return (
    <Router>
    <div className="App">
        <Switch>
        <Route exact path="/home">
          <Home />
        </Route>
        <Route exact path="/signup">
          <Signup />
        </Route>
        <Route exact path="/">
          <Login />
        </Route>
      </Switch>
    </div>
  </Router>
  );
}

export default App;
