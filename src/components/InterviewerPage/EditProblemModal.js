import React, {PropTypes} from 'react';
import {connect} from 'react-redux';
import {Modal, Button, FormGroup, ControlLabel, FormControl, InputGroup, HelpBlock} from 'react-bootstrap';
import {editProblem} from '../../actions/problemActions';

const OptionControl = ({checked, content, onContentChange, onCheckedChange, onDelete}) => {
  return (
    <InputGroup>
      <InputGroup.Addon>
        <input type="checkbox" checked={checked} onChange={onCheckedChange}/>
      </InputGroup.Addon>
      <FormControl type="text" value={content || ''} onChange={onContentChange}/>
      <InputGroup.Button>
        <Button onClick={onDelete}>删除</Button>
      </InputGroup.Button>
    </InputGroup>
  );
};

OptionControl.propTypes = {
  checked: PropTypes.bool,
  content: PropTypes.string,
  onContentChange: PropTypes.func,
  onCheckedChange: PropTypes.func,
  onDelete: PropTypes.func
};

const initialState = {
  editOptionContent: undefined,
  editOptionChecked: false,
  title: '',
  description: '',
  options: [],
  sampleInput: '',
  sampleOutput: '',
  updated: false,
  type: 'choice'
};

export class EditProblemModal extends React.Component {
  constructor(props) {
    super(props);
    this.state = initialState;
    this.onAddOption = this.onAddOption.bind(this);
    this.onOptionContentChange = this.onOptionContentChange.bind(this);
    this.onOptionCheckedChange = this.onOptionCheckedChange.bind(this);
    this.onOptionDelete = this.onOptionDelete.bind(this);
    this.getHelpBlock = this.getHelpBlock.bind(this);
    this.onSaveClick = this.onSaveClick.bind(this);
  }

  componentDidUpdate() {
    if (this.props.show === true && this.state.updated === false) {
      const problem = this.props.problems.find(problem => problem.id === this.props.selectedProblem);
      this.setState({
        editOptionContent: '',
        editOptionChecked: false,
        title: problem.content.title,
        description: problem.content.description,
        type: problem.type,
        updated: true
      });
      if (problem.type === 'choice') {
        let id = 0;
        const optionMap = (option) => {
          id = id + 1;
          return {
            id: id - 1,
            content: option.content,
            checked: option.correct
          };
        };
        this.setState({
          options: problem.content.option.map(optionMap)
        });
      }
      else if (problem.type === 'code') {
        this.setState({
          sampleInput: problem.content.sampleInput,
          sampleOutput: problem.content.sampleOutput
        });
      }
    }
  }

  onAddOption() {
    this.setState({
      options: [...this.state.options,
        {
          id: this.state.options.length,
          checked: this.state.editOptionChecked,
          content: this.state.editOptionContent
        }]
    });
    this.setState({
      editOptionChecked: false,
      editOptionContent: '',
    });
  }

  onOptionContentChange(id) {
    return (e) => {
      this.setState({
        options: [
          ...this.state.options.slice(0, id),
          {
            id: id,
            content: e.target.value,
            checked: this.state.options[id].checked
          },
          ...this.state.options.slice(id + 1)
        ]
      });
    };
  }

  onOptionCheckedChange(id) {
    return () => {
      this.setState({
        options: [
          ...this.state.options.slice(0, id),
          {
            id: id,
            content: this.state.options[id].content,
            checked: !this.state.options[id].checked
          },
          ...this.state.options.slice(id + 1)
        ]
      });
    };
  }

  onOptionDelete(id) {
    return () => {
      this.setState({
        options: [
          ...this.state.options.slice(0, id),
          ...this.state.options.slice(id + 1).map(option => {
            return {
              id: option.id - 1,
              checked: option.checked,
              content: option.content
            };
          })
        ]
      });
    };
  }

  getValidationState() {
    if (this.state.editOptionContent && this.state.editOptionContent.length > 0 &&
      this.state.options.find(option => option.content === this.state.editOptionContent) != undefined)
      return 'error';
  }

  getHelpBlock() {
    if (this.getValidationState() === 'error')
      return (
        <HelpBlock>此选项与已有选项重复</HelpBlock>
      );
    else
      return undefined;
  }

  disableSave() {
    if (this.props.type === 'choice') {
      return this.state.title === undefined || this.state.title.length === 0 ||
        this.state.description === undefined || this.state.description.length === 0 ||
        this.state.options.length === 0;
    }
    else if (this.props.type === 'code') {
      return this.state.title === undefined || this.state.title.length === 0 ||
        this.state.description === undefined || this.state.description.length === 0 ||
        this.state.sampleInput === undefined || this.state.sampleInput.length === 0 ||
        this.state.sampleOutput === undefined || this.state.sampleOutput.length === 0;
    }
    else {
      return this.state.title === undefined || this.state.title.length === 0 ||
        this.state.description === undefined || this.state.description.length === 0;
    }
  }

  onSaveClick() {
    const problemOptions = this.state.options.map(option => {
      return {
        content: option.content,
        correct: option.checked
      };
    });
    let problemContent;
    if (this.state.type === 'choice') {
      problemContent = {
        title: this.state.title,
        description: this.state.description,
        option: problemOptions
      };
    }
    else if (this.state.type === 'code') {
      problemContent = {
        title: this.state.title,
        description: this.state.description,
        sampleInput: this.state.sampleInput,
        sampleOutput: this.state.sampleOutput
      };
    }
    else {
      problemContent = {
        title: this.state.title,
        description: this.state.description,
      };
    }
    const problemInfo = {
      id: this.props.selectedProblem,
      roomId: this.props.roomId,
      type: this.state.type,
      content: problemContent
    };
    this.props.editProblem(problemInfo);
    this.setState(initialState);
    this.props.onHide();
  }

  render() {
    return (
      <Modal onHide={this.props.onHide} show={this.props.show}>
        <Modal.Header closeButton>
          <Modal.Title >题目信息</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <FormGroup controlId="title">
            <ControlLabel>标题</ControlLabel>
            <FormControl type="text" placeholder="题目标题" value={this.state.title || ''}
                         onChange={(e) => {
                           this.setState({title: e.target.value});
                         }}/>
          </FormGroup>
          <FormGroup controlId="description">
            <ControlLabel>题目描述</ControlLabel>
            { this.state.type === 'blank' && <p>使用【】标出填空位置</p>}
            <FormControl componentClass="textarea" placeholder="在此添加题目描述" style={{height: 200}}
                         value={this.state.description || ''} onChange={(e) => {
              this.setState({description: e.target.value});
            }}/>
          </FormGroup>
          { this.state.type === 'choice' &&
          <div>
            <FormGroup controlId="add_option" validationState={this.getValidationState()}>
              <ControlLabel>选项</ControlLabel>
              <InputGroup>
                <InputGroup.Addon>
                  <input type="checkbox" checked={this.state.editOptionChecked}
                         onChange={() => {
                           this.setState({editOptionChecked: !this.state.editOptionChecked});
                         }}/>
                </InputGroup.Addon>
                <FormControl type="text" placeholder="选项内容"
                             value={this.state.editOptionContent || ''}
                             onChange={(e) => {
                               this.setState({editOptionContent: e.target.value});
                             }}/>
                <InputGroup.Button>
                  <Button onClick={this.onAddOption}
                          disabled={this.state.editOptionContent === undefined || this.state.editOptionContent.length === 0
                          || this.getValidationState() === 'error'}>添加</Button>
                </InputGroup.Button>
              </InputGroup>
              {this.getHelpBlock()}
            </FormGroup>
            {
              this.state.options.length > 0 &&
              <FormGroup>
                <ControlLabel>已添加选项</ControlLabel>

              </FormGroup>
            }
            { this.state.options.length > 0 &&
            this.state.options.map((option) =>
              <OptionControl key={option.id} checked={option.checked} content={option.content}
                             onContentChange={this.onOptionContentChange(option.id)}
                             onCheckedChange={this.onOptionCheckedChange(option.id)}
                             onDelete={this.onOptionDelete(option.id)}/>
            )}
          </div>
          }
          {
            this.state.type === 'code' &&
            <div>
              <FormGroup controlId="sample_input">
                <ControlLabel>样例输入</ControlLabel>
                <FormControl componentClass="textarea" placeholder="在此添加样例输入" style={{height: 160}}
                             value={this.state.sampleInput || ''} onChange={(e) => {
                  this.setState({sampleInput: e.target.value});
                }}/>
              </FormGroup>
              <FormGroup controlId="sample_onput">
                <ControlLabel>样例输出</ControlLabel>
                <FormControl componentClass="textarea" placeholder="在此添加样例输出" style={{height: 160}}
                             value={this.state.sampleOutput || ''} onChange={(e) => {
                  this.setState({sampleOutput: e.target.value});
                }}/>
              </FormGroup>
            </div>
          }

        </Modal.Body>
        <Modal.Footer>
          <Button bsStyle="primary"
                  disabled={this.disableSave()}
                  onClick={this.onSaveClick}>保存</Button>
          <Button onClick={() => {this.props.onHide();this.setState(initialState);}}>关闭</Button>
        </Modal.Footer>
      </Modal>

    );
  }
}

// TODO: check selectedProblem type (string or number)
EditProblemModal.propTypes = {
  onHide: PropTypes.func.isRequired,
  editProblem: PropTypes.func.isRequired,
  selectedProblem: PropTypes.number,
  show: PropTypes.bool,
  problems: PropTypes.array,
  type: PropTypes.string,
  roomId: PropTypes.number
};

function mapStateToProps(state) {
  return {
    roomId: state.roomsStates.room.id,
    problems: state.problemStates.problems
  };
}

export default connect(mapStateToProps, {editProblem})(EditProblemModal);
