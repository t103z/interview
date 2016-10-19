/**
 * Created by 薛凯�? on 2016/10/19.
 */
import React from 'react';
import { Route, IndexRoute } from 'react-router';
import {Navbar, Nav, NavItem} from 'react-bootstrap';
import '../styles/headline.css';
import '../styles/registerinfo.css';

var RegisterPage;
RegisterPage = React.createClass({
    render : function() {
        return (
            <div>
                <HeadLine />
                <RegisterInfo />
            </div>
        )
    }
});

var HeadLine;
HeadLine = React.createClass({
    render : function() {
        return (
            <header  className="headline">
                <Navbar fixedTop>
                    <Navbar.Header>
                        <Navbar.Brand>
                            TestTalent
                        </Navbar.Brand>
                    </Navbar.Header>

                    <Nav pullRight>
                        <NavItem eventKey={1}>登陆</NavItem>
                        <NavItem eventKey={2}>注册</NavItem>
                    </Nav>
                </Navbar>
            </header>
        );
    }
});

var RegisterInfo;
RegisterInfo = React.createClass({
    getInitialState : function() {
        return {
            userEmail : "��������������",
            pass  : "��������������",
            confirmPass : "��ȷ����������",
            orgName : "��������",
            userName : "��ϵ������",
            caf : "�������Ҳ���֤��"
        };
    },

    emailChange : function(e) {
        var val = e.target.value;
        this.setState({userEmail: val});
    },

    passChange : function(e) {
        this.setState({pass: e.target.value});
    },

    confirmPassChange : function(e) {
        this.setState({confirmPass: e.target.value});
    },

    orgNameChange : function(e) {
        this.setState({orgName: e.target.value});
    },

    userNameChange : function(e) {
        this.setState({userName: e.target.value});
    },

    cafChange : function(e) {
        this.setState({caf: e.target.value});
    },

    checkInfo : function() {
        if((this.state.email == null) || (this.state.pass == null) || (this.state.confirmPass == null)
            || (this.state.orgName == null) || (this.state.userName == null) || (this.state.caf == null)) {
            alert("����������Ϣfuck0");
            return false;
        }
        if(this.state.pass != this.state.confirmPass) {
           alert("���벻һ��fuck1");
            return false;
        }
    },

    handleClick : function() {
        if(this.checkInfo()) {

        }
    },

    render : function () {
        return (
            <div className = "registerInfo">
                <div><label style = {{color: '#BEBEBE'}}>�����������˺�</label></div>
                <div><label>工作邮箱�?</label></div>
                <div><input id="email" name="email" type="email"
                            value = {this.state.userEmail} onChange={this.emailChange}
                            style= {{width: '500px', borderRadius: '10px', height: '40px'}}/></div>
                <div><label>登录密码�?</label></div>
                <div><input id="pass" name="password" type="text"
                            value = {this.state.pass} onChange={this.passChange}
                            style= {{width: '500px', borderRadius: '10px', height: '40px' }}/></div>
                <div><label>确认密码�?</label></div>
                <div><input id="confirmPass" name="confirmPassword" type="text"
                            value = {this.state.confirmPass} onChange={this.confirmPassChange}
                            style= {{width: '500px', borderRadius: '10px', height: '40px' }}/></div>
                <div><label>机构名称�?</label></div>
                <div><input id="orgName" name="orgName" type="text"
                            value = {this.state.orgName} onChange={this.orgNameChange}
                            style= {{width: '500px', borderRadius: '10px', height: '40px' }}/></div>
                <div><label>联系人姓名：</label></div>
                <div><input id="userName" name="userName" type="text"
                            value = {this.state.userName} onChange={this.userNameChange}
                            style= {{width: '500px', borderRadius: '10px', height: '40px' }}/></div>
                <div><label>验证码：</label></div>
                <div><input id="caf" name="caf" type="text"
                            value = {this.state.caf} onChange={this.cafChange}
                            style= {{width: '500px', borderRadius: '10px', height: '40px' }}/></div>
                <div><button type="submit" onClick = {this.handleClick}
                             style={{backgroundColor: '#00CC50', color : '#FFFFFF', borderRadius: '15px', width: '500px', height: '40px' }}>注册</button></div>
            </div>
        )
    }
});

export default RegisterPage;
