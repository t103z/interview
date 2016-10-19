?import React from 'react';
import { Route, IndexRoute } from 'react-router';
import {Navbar, Nav, NavItem} from 'react-bootstrap';
import '../styles/changeuserinfo.css';

var ChangeUserInfo;
ChangeUserInfo = React.createClass({
    render : function() {
        return (
            <div>
                <CIHeadline />
                <ChangedInfo />
            </div>
        )
    }
});

var CIHeadline;
CIHeadline = React.createClass({
    render : function() {
        return (
            <header  style = {{ background: '#3498db'}}>
                <Navbar fixedTop>
                    <Navbar.Header>
                        ����
                    </Navbar.Header>
                </Navbar>
            </header>
        );
    }
});

var ChangedInfo;
ChangedInfo = React.createClass({
    getInitialState : function() {
        return {
            userEmail : "��������������",
            pass  : "��������������",
            confirmPass : "��ȷ����������",
            orgName : "���������Ļ�������",
            userName : "��������ϵ������",
        };
    },

    emailChange : function(e) {
        this.setState({userEmail: e.target.value});
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

    checkInfo : function() {
        if((this.state.email == null) || (this.state.pass == null) || (this.state.confirmPass == null)
            || (this.state.orgName == null) || (this.state.userName == null)) {
            alert("������������Ϣfuck0");
            return false;
        }
        if(this.state.pass != this.state.confirmPass) {
            alert("���벻һ��Fuck1");
            return false;
        }
    },

    handleClick : function() {
        if(this.checkInfo()) {

        }
    },

    render : function () {
        return (
            <div className = "changeUserInfo">
                <div><label style = {{color: '#BEBEBE'}}>�޸��û���Ϣ</label></div>
                <div><label>��������:</label></div>
                <div><input id="email" name="email" type="email"
                            value = {this.state.userEmail} onChange={this.emailChange}
                            style = {{width: '500px', borderRadius: '10px', height: '40px'}}/></div>
                <div><label>�޸�����:</label></div>
                <div><input id="pass" name="password" type="text"
                            value = {this.state.pass} onChange={this.passChange}
                            style = {{width: '500px', borderRadius: '10px', height: '40px' }}/></div>
                <div><label>ȷ������:</label></div>
                <div><input id="confirmPass" name="confirmPassword" type="text"
                            value = {this.state.confirmPass} onChange={this.confirmPassChange}
                            style = {{width: '500px', borderRadius: '10px', height: '40px' }}/></div>
                <div><label>��������:</label></div>
                <div><input id="orgName" name="orgName" type="text"
                            value = {this.state.orgName} onChange={this.orgNameChange}
                            style = {{width: '500px', borderRadius: '10px', height: '40px' }}/></div>
                <div><label>��ϵ������:</label></div>
                <div><input id="userName" name="userName" type="text"
                            value = {this.state.userName} onChange={this.userNameChange}
                            style = {{width: '500px', borderRadius: '10px', height: '40px' }}/></div>
                <div><button type="submit"
                             style ={{backgroundColor: '#00CC50', borderRadius: '15px', width: '500px', height: '40px' }}>�ύ�޸�</button></div>
            </div>
        )
    }
});

export default ChangeUserInfo;
