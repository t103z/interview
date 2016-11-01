import React from 'react';
import {Navbar, Nav, NavItem} from 'react-bootstrap';
import {LinkContainer, IndexLinkContainer} from 'react-router-bootstrap';
import '../styles/navigation.css';


const Navigation = () => {
  return (
    <header className="navigation">
      <Navbar fixedTop>
        <Navbar.Header>
          <Navbar.Brand>
            <a href="/">面试管理平台</a>
          </Navbar.Brand>
        </Navbar.Header>
        <Nav>
          <IndexLinkContainer to="/hr">
            <NavItem eventKey={1}>房间管理</NavItem>
          </IndexLinkContainer>
          <LinkContainer to="/interviewer">
            <NavItem eventKey={3}>面试官管理台</NavItem>
          </LinkContainer>
          <LinkContainer to="/about">
            <NavItem eventKey={4}>About</NavItem>
          </LinkContainer>
        </Nav>

        <Nav pullRight>
          <NavItem eventKey={5}>登录</NavItem>
          <NavItem eventKey={6}>注册</NavItem>
        </Nav>
      </Navbar>
    </header>
  );
};

export default Navigation;
