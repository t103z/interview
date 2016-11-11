import React from 'react';
import { Route, IndexRoute } from 'react-router';

import App from './components/App';
import HomePage from './components/HomePage';
import FuelSavingsPage from './containers/FuelSavingsPage'; // eslint-disable-line import/no-named-as-default
import AboutPage from './components/AboutPage.js';
import NotFoundPage from './components/NotFoundPage.js';
import HRRoomTable from './components/HRRoomTable';
import InterviewerPage from './components/InterviewerPage/InterviewerPage';
import CandidateManagerTable from './components/candidateManager/CandidateManagerTable'
import LoginPage from './components/LoginPage';

export default (
  <Route path="/" component={App}>
    <IndexRoute component={CandidateManagerTable}/>
    <Route path="fuel-savings" component={FuelSavingsPage}/>
    <Route path="about" component={AboutPage}/>
    <Route path="interviewer" component={InterviewerPage} />
    <Route path="login" component={LoginPage}/>
    <Route path="*" component={NotFoundPage}/>
  </Route>
);
