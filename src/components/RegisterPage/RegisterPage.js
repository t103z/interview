﻿import React from 'react';
import RegisterInfo from './RegisterInfo';
import * as RegisterActions from '../../actions/registerActions';
import { Panel } from  'react-bootstrap';

class RegisterPage extends React.Component {
    render() {
        return (
          <Panel style={{width: '700px', margin: '0 auto'}}>
            <h3>注册主考方账号</h3>
            <RegisterInfo
              clickAction={RegisterActions.register}/>
          </Panel>
        );
    }
}

export default RegisterPage;
