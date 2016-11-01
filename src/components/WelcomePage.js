import React, {PropTypes} from 'react';
import {Jumbotron, Button} from 'react-bootstrap';
import {LinkContainer} from 'react-router-bootstrap';
import '../styles/welcome-page.css';

const WelcomePage = () => {
  return (
    <div className="welcome">
      <Jumbotron>
        <h1>欢迎</h1>
        <p>欢迎访问面试管理平台</p>
        <p>
          <LinkContainer to="/hr">
            <Button bsStyle="primary">登录</Button>
          </LinkContainer>
        </p>
      </Jumbotron>
    </div>
  );
};

export default WelcomePage;
