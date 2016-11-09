import React from 'react';
import {Row, Col, Tab, Nav, NavItem, NavDropdown, MenuItem, Modal} from 'react-bootstrap';
import ProblemTable from './ProblemTable';
import ChoiceModal from './ChoiceModal';

class ControlTab extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      key: 1,
      choiceShow: false
    };
    this.onTabSelect = this.onTabSelect.bind(this);
    this.onAddChoiceClick = this.onAddChoiceClick.bind(this);
    this.choiceClose = () => {this.setState({choiceShow: false})};
  }

  onTabSelect(key) {
    if (key > 2)
      key = 1;
    this.setState({key});
  }

  onAddChoiceClick(e) {
    this.setState({choiceShow: true})
  }

  render() {
    return (
      <div>
        <Tab.Container id="tab-container" activeKey={this.state.key} onSelect={this.onTabSelect}>
          <Row>
            <Col sm={12}>
              <Nav bsStyle="tabs">
                <NavItem eventKey={1}>
                  面试题目
                </NavItem>
                <NavItem eventKey={2}>
                  候选人名单
                </NavItem>
                {
                  this.state.key === 1 &&
                  <NavDropdown className="pull-right" title="添加面试题">
                    <MenuItem eventKey={3} onClick={() => {this.setState({choiceShow: true})}}>选择题</MenuItem>
                    <MenuItem eventKey={4} onClick={this.onAddChoiceClick}>填空题</MenuItem>
                    <MenuItem>编程题</MenuItem>
                    <MenuItem>简答题</MenuItem>
                  </NavDropdown>
                }
              </Nav>
            </Col>
            <Col sm={12}>
              <Tab.Content animation>
                <Tab.Pane eventKey={1}>
                  <ProblemTable/>
                </Tab.Pane>
                <Tab.Pane eventKey={2}>
                  Tab 2 content
                </Tab.Pane>
              </Tab.Content>
            </Col>
          </Row>
        </Tab.Container>
        <ChoiceModal show={this.state.choiceShow} onHide={this.choiceClose}/>
      </div>
    );
  }
}


export default ControlTab;
