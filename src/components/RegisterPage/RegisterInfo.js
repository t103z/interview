import React, {PropTypes} from 'react';
import {FormGroup, FormControl, ControlLabel, Button, Form, Col, HelpBlock} from 'react-bootstrap';
import {connect} from 'react-redux';
import {register} from '../../actions/registerActions';
import md5 from 'js-md5';

class RegisterInfo extends React.Component {
  constructor(props) {
    super(props);
    this.emailChange = this.emailChange.bind(this);
    this.passChange = this.passChange.bind(this);
    this.confirmPassChange = this.confirmPassChange.bind(this);
    this.orgNameChange = this.orgNameChange.bind(this);
    this.userNameChange = this.userNameChange.bind(this);
    this.contactChange = this.contactChange.bind(this);

    this.getConPassValState = this.getConPassValState.bind(this);
    this.getUserValState = this.getUserValState.bind(this);
    this.getOrgValState = this.getOrgValState.bind(this);
    this.getContactValState = this.getContactValState.bind(this);
    this.getEmailValState = this.getEmailValState.bind(this);
    this.getPassValState = this.getPassValState.bind(this);

    this.getPassHelpBlock = this.getPassHelpBlock.bind(this);
    this.getConPassHelpBlock = this.getConPassHelpBlock.bind(this);
    this.getContactHelpBlock = this.getContactHelpBlock.bind(this);
      this.getOrgHelpBlock = this.getOrgHelpBlock.bind(this);
      this.getUserHelpBlock = this.getUserHelpBlock.bind(this);
      this.getEmailHelpBlock = this.getEmailHelpBlock.bind(this);

    this.handleClick = this.handleClick.bind(this);
    this.render = this.render.bind(this);

    this.state = {
      userName: "",
      userEmail: "",
      pass: "",
      confirmPass: "",
      orgName: "",
      contact: "",
      caf: "",
    };
  }

  getUserHelpBlock() {
    if(this.getUserValState() == 'warning') {
      return (<HelpBlock>用户名必须小于20位</HelpBlock>);
    }
    else if(this.getUserValState() == 'error') {
      return (<HelpBlock>用户名中含有非法字符</HelpBlock>);
    }
    return undefined;
  }

    getEmailHelpBlock() {
        if(this.getEmailValState() == 'warning') {
            return (<HelpBlock>请输入正确的邮箱</HelpBlock>);
        }
        else if(this.getEmailValState() == 'error') {
            return (<HelpBlock>请输入正确的邮箱</HelpBlock>);
        }
        return undefined;
    }

  getContactHelpBlock() {
    if(this.getContactValState() == 'warning') {
      return (<HelpBlock>联系人姓名必须小于20位</HelpBlock>);
    }
    else if(this.getContactValState() == 'error') {
      return (<HelpBlock>联系人姓名错误</HelpBlock>);
    }
    return undefined;
  }

  getOrgHelpBlock() {
    if(this.getOrgValState() == 'warning') {
      return (<HelpBlock>机构名称必须小于100位</HelpBlock>);
    }
    else if(this.getOrgValState() == 'error') {
      return (<HelpBlock>机构名称错误</HelpBlock>);
    }
    return undefined;
  }

  getPassHelpBlock() {
    if(this.getPassValState() == 'warning') {
      return (<HelpBlock>密码必须大于6位小于20位</HelpBlock>);
    }
    else if(this.getPassValState() == 'error') {
      return (<HelpBlock>密码中含有非法字符</HelpBlock>);
    }
    return undefined;
  }

  getConPassHelpBlock() {
    if(this.getConPassValState() == 'error') {
      return (<HelpBlock>两次密码不一致</HelpBlock>);
    }
    return undefined;
  }

  contactChange(e) {
    this.setState({contact: e.target.value});
  }

  emailChange(e) {
    this.setState({userEmail: e.target.value});
  }

  passChange(e) {
    this.setState({pass: e.target.value});
  }

  confirmPassChange(e) {
    this.setState({confirmPass: e.target.value});
  }

  orgNameChange(e) {
    this.setState({orgName: e.target.value});
  }

  userNameChange(e) {
    this.setState({userName: e.target.value});
  }

  getEmailValState(){
    const length = this.state.userEmail.length;
    if (length > 0)
    {
      const pattern = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
      if(pattern.test(this.state.userEmail)) {
        return 'success';
      }
      return 'error';
    }
  }

  getContactValState(){
    const length = this.state.contact.length;
    if(length > 20) return 'warning';
    if (length > 0) return 'success';
  }

  getPassValState(){
    const length = this.state.pass.length;
    if(length > 20) {
      return 'warning';
    }
    if (length >= 6) {
      let pattern = /^[a-zA-Z\d]+$/;
      if(pattern.test(this.state.pass)) {
        return 'success';
      }
      return 'error';
    }
    else if(length > 0) {
      let pattern = /^[a-zA-Z\d]+$/;
      if(pattern.test(this.state.pass)) {
        return 'warning';
      }
      return 'error';
    }
  }

  getConPassValState() {
    const length = this.state.confirmPass.length;
    if((length > 0) && (this.state.pass == this.state.confirmPass)) {
      return "success";
    }
    else if (length > 0) return 'error';
  }

  getOrgValState(){
    const length = this.state.orgName.length;
    if(length > 100) return 'warning';
    if (length > 0) return 'success';
  }

  getUserValState(){
    const length = this.state.userName.length;
    if(length > 20) return 'warning';
    if (length > 0) {
      let pattern = /^[a-zA-Z\d]+$/;
      if(pattern.test(this.state.userName)) {
        return 'success';
      }
      return 'error';
    }
  }

  handleClick() {
    if((this.getEmailValState() == "success") && (this.getPassValState() == "success")
      && (this.getConPassValState() == "success") && (this.getOrgValState() == "success")
      && (this.getUserValState() == "success") && (this.getContactValState() == "success")) {

      this.props.register({
        "username": this.state.userName,
        "type": "hr",
        "email": this.state.userEmail,
        "password": md5(this.state.pass),
        "organization": this.state.orgName,
        "contact": this.state.contact,
      });
    }
    else {
      alert("请先完善您的信息！");
    }
  }

  render() {
    return (
      <Form horizontal>
        <FormGroup controlId="userName" validationState={this.getUserValState()}>
          <Col componentClass={ControlLabel} sm={3}>用户名</Col>
          <Col sm={8}>
            <FormControl type="text" value = {this.state.userName} onChange = {this.userNameChange} placeholder="请输入您的用户名"/>
            <FormControl.Feedback />
              {this.getUserHelpBlock()}
          </Col>
        </FormGroup>

        <FormGroup controlId="userEmail" validationState={this.getEmailValState()}>
          <Col componentClass={ControlLabel} sm={3}>工作邮箱</Col>
          <Col sm={8}>
            <FormControl type="email" value = {this.state.userEmail} onChange = {this.emailChange} placeholder="请输入您的工作邮箱"/>
            <FormControl.Feedback />
              {this.getEmailHelpBlock()}
          </Col>
        </FormGroup>

        <FormGroup controlId="pass" validationState={this.getPassValState()}>
          <Col componentClass={ControlLabel} sm={3}>登录密码</Col>
          <Col sm={8}>
            <FormControl type="password"  value = {this.state.pass} onChange = {this.passChange} placeholder="请输入您的密码"/>
            <FormControl.Feedback />
            {this.getPassHelpBlock()}
          </Col>
        </FormGroup>

        <FormGroup controlId="confirmPass" validationState={this.getConPassValState()}>
          <Col componentClass={ControlLabel} sm={3}>确认登录密码</Col>
          <Col sm={8}>
            <FormControl type="password" value = {this.state.confirmPass} onChange = {this.confirmPassChange} placeholder="请确认您的密码"/>
            <FormControl.Feedback />
            {this.getConPassHelpBlock()}
          </Col>
        </FormGroup>

        <FormGroup controlId="orgName" validationState={this.getOrgValState()}>
          <Col componentClass={ControlLabel} sm={3}>机构名称</Col>
          <Col sm={8}>
            <FormControl type="text" value = {this.state.orgName} onChange = {this.orgNameChange} placeholder="请输入您的机构名称"/>
            <FormControl.Feedback />
              {this.getOrgHelpBlock()}
          </Col>
        </FormGroup>

        <FormGroup controlId="contact" validationState={this.getContactValState()}>
          <Col componentClass={ControlLabel} sm={3}>联系人姓名</Col>
          <Col sm={8}>
            <FormControl type="text" value = {this.state.contact} onChange = {this.contactChange} placeholder="请输入联系人姓名"/>
            <FormControl.Feedback />
              {this.getContactHelpBlock()}
          </Col>
        </FormGroup>

        <FormGroup>
          <Col smOffset={5} sm={10}>
            <Button bsStyle="primary" type="button" onClick = {this.handleClick}>注册</Button>
          </Col>
        </FormGroup>
      </Form>
    );
  }
}

RegisterInfo.propTypes = {
  register: PropTypes.func.isRequired,
};

function mapStateToProps() {
  return {};
}

export default connect(mapStateToProps, {register})(RegisterInfo);
