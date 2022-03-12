import "./App.css";
import {
  AppBar,
  Toolbar,
  Typography,
  Container,
  Grid,
  Card,
  CardContent,
  CardActions,
  CardMedia,
  Button,
} from "@mui/material";
import { typographyVariant } from "@mui/system";
import { CCarousel } from "@coreui/react";
import { CCarouselCaption } from "@coreui/react";
import { CCarouselItem, CImage } from "@coreui/react";
import Asthma from "./Components/Asthma";
import Pneumonia from "./Components/Pneumonia";

import ReactDOM from 'react-dom';  
import { 
  BrowserRouter as Router,
  Switch,
  Routes,
  Link,
  Route
} from "react-router-dom";

import Home from "./Components/Home";
import Covid from "./Components/Covid";




function App() {
  return (
    <Router>
    <div className="App">
    
    <Routes>
      <Route path="/" element={<Home />}>
        {/* <Route path="expenses" element={< />} />
        <Route path="invoices" element={<Invoices />} /> */}
      </Route>

      <Route path="/asthma" element={<Asthma/>}>

      </Route>

      <Route path="/covid" element={<Covid/>}>
        
      </Route>
      
      <Route path="/pneumonia" element={<Pneumonia/>}>
        
      </Route>
    </Routes>
    
    
     
    </div>
    </Router>
  );
}

export default App;


        