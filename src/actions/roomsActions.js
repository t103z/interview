import * as types from '../constants/actionTypes';
import axios from 'axios';
import {displayNotification} from './notificationActions';
import {loadAllProblems, loadAllProblemsSuccess} from './problemActions';
import {loadAllRoomCandidates} from './candidateManagerActions';
import {push} from 'react-router-redux';
import {logout} from './userActions';


export function beginDeleteRoom() {
  return {
    type: types.DELETE_ROOM
  };
}

export function deleteRoomSuccess(roomId) {
  return {
    type: types.DELETE_ROOM_SUCCESS,
    roomId
  };
}

export function deleteRoomError(error) {
  return {
    type: types.DELETE_ROOM_ERROR,
    error
  };
}

export function beginLoadAllRooms() {
  return {
    type: types.LOAD_ALL_ROOMS
  };
}

export function loadAllRoomsSuccess(rooms) {
  return {
    type: types.LOAD_ALL_ROOMS_SUCCESS,
    rooms
  };
}

export function loadAllRoomsError(error) {
  return {
    type: types.LOAD_ALL_ROOMS_ERROR,
    error
  };
}

export function loadRoomSuccess(room) {
  return {
    type: types.LOAD_ROOM_SUCCESS,
    room
  };
}

export function loadRoomError(error) {
  return {
    type: types.LOAD_ROOM_ERROR,
    error
  };
}

export function beginLoadRoom() {
  return {
    type: types.LOAD_ROOM
  };
}

export function beginAddRoom() {
  return {
    type: types.ADD_ROOM
  };
}

export function addRoomSuccess(data) {
  return {
    type: types.ADD_ROOM_SUCCESS,
    data
  };
}

export function addRoomError(error) {
  return {
    type: types.ADD_ROOM_ERROR,
    error
  };
}

export function beginModifyRoom() {
  return {
    type: types.MODIFY_ROOM
  };
}

export function modifyRoomSuccess() {
  return {
    type: types.MODIFY_ROOM_SUCCESS
  };
}

export function modifyRoomError(error) {
  return {
    type: types.MODIFY_ROOM_ERROR,
    error
  };
}

export function beginUploadImage() {
  return {
    type: types.UPLOAD_IMAGE
  };
}

export function uploadImageSuccess() {
  return {
    type: types.UPLOAD_IMAGE_SUCCESS
  };
}

export function uploadImageError(error) {
  return {
    type: types.UPLOAD_IMAGE_ERROR,
    error
  };
}

export function deleteRoom(roomId) {
  return (dispatch, getState) => {
    dispatch(beginDeleteRoom());
    const token = getState().user.token;
    return axios.delete('/room/' + roomId + '?token=' + token)
      .then(response => {
        if (response.status === 200) {
          dispatch(deleteRoomSuccess(roomId));
          dispatch(displayNotification('success', '操作成功', '删除房间成功'));
        }
        else {
          dispatch(displayNotification('error', '错误', toString(response.data.error)));
        }
      })
      .catch(error => {
        if (error.response.status === 403) {
          dispatch(displayNotification('error', '错误', '您已下线'));
          dispatch(logout());
          dispatch(push('/login'));
        }
        else {
          dispatch(displayNotification('error', '错误', error.message));
        }
      });
  };
}

export function loadAllRooms() {
  return (dispatch, getState) => {
    dispatch(beginLoadAllRooms());
    const token = getState().user.token;
    return axios.get('/room', {
      params:{
        token,
        offset: 0,
        limit: 20
      }
    })
      .then(response => {
        if (response.status === 200) {
          dispatch(loadAllRoomsSuccess(response.data.rooms));
        }
        else {
          dispatch(displayNotification('error', '错误', response.data.error));
        }
      })
      .catch(error => {
        if (error.response.status === 403) {
          dispatch(displayNotification('error', '错误', '您已下线'));
          dispatch(logout());
          dispatch(push('/login'));
        }
        else {
          dispatch(displayNotification('error', '错误', error.message));
        }
      });
  };
}

export function loadInterviewerRoom() {
  return (dispatch, getState) => {
    const token = getState().user.token;
    let roomId;
    // get roomId by token
    return axios.get('/interviewer' + '?token=' + token)
      .then(res => {
        if (res.status === 200) {
          // get room info by roomId
          roomId = res.data.roomId;
          return axios.get('/room/' + roomId + '?token=' + token);
        }
        else if (res.status === 400) {
          throw '获取房间信息失败';
        }
        else {
          throw res.data;
        }
      })
      .then(res => {
        if (res.status === 200) {
          dispatch(loadRoomSuccess(res.data));
          dispatch(loadAllProblems(roomId));
          dispatch(loadAllRoomCandidates(roomId));
        }
        else if (res.status === 404) {
          throw '房间不存在';
        }
        else {
          throw res.data;
        }
      })
      .catch(error => {
        if (error.response.status === 403) {
          dispatch(displayNotification('error', '错误', '您已下线'));
          dispatch(logout());
          dispatch(push('/login'));
        }
        else {
          dispatch(displayNotification('error', '错误', error.message));
        }
      });
  };
}

export function modifyRoom(data) {
  return (dispatch, getState) => {
    dispatch(beginModifyRoom());
    const room_id = data.room_id;
    const room = data.newRoom;
    let image = data.image;
    let logoOrNot = data.logoOrNot;
    const token = getState().user.token;

    if(logoOrNot === 1) {
      return axios.put('/room/' + room_id + '?token=' + token, room)
        .then(response => {
          if (response.status === 200) {
            dispatch(beginUploadImage());
            return axios.put('/room/' + room_id + '/logo' + '?token=' + token, image);
          }
          else {
            throw (response.data);
          }
        })
        .then(response => {
          if (response.status === 200) {
            dispatch(displayNotification('success', '操作成功', '修改房间信息成功'));
            dispatch(uploadImageSuccess());
            dispatch(loadAllRooms());
          }
          else {
            throw (response.data);
          }
        })
        .catch(error => {
          if (error.response.status === 403) {
            dispatch(displayNotification('error', '错误', '您已下线'));
            dispatch(logout());
            dispatch(push('/login'));
          }
          else {
            dispatch(displayNotification('error', '错误', error.message));
          }
        });
    }
    else {
      return axios.put('/room/' + room_id +'?token=' + token, room)
        .then(response => {
          if(response.status === 200) {
            dispatch(displayNotification('success', '操作成功', '修改房间信息成功'));
            dispatch(loadAllRooms());
          }
          else {
            dispatch(displayNotification('error', '错误', response.data.error));
          }
        })
        .catch(error => {
          if (error.response.status === 403) {
            dispatch(displayNotification('error', '错误', '您已下线'));
            dispatch(logout());
            dispatch(push('/login'));
          }
          else {
            dispatch(displayNotification('error', '错误', error.message));
          }
        });
    }
  };
}

export function addRoom(data) {
  return (dispatch, getState) => {
    dispatch(beginAddRoom());
    const room = data.newRoom;
    let image = data.image;
    let logoOrNot = data.logoOrNot;
    const token = getState().user.token;

    if(logoOrNot === 0) {
      return axios.post('/room' + '?token=' + token, room)
        .then(response => {
          if(response.status === 200) {
            dispatch(displayNotification('success', '操作成功', '添加房间成功'));
            dispatch(loadAllRooms());
          }
          else {
            dispatch(displayNotification('error', '错误', response.data.error));
          }
        })
        .catch(error => {
          if (error.response.status === 403) {
            dispatch(displayNotification('error', '错误', '您已下线'));
            dispatch(logout());
            dispatch(push('/login'));
          }
          else {
            dispatch(displayNotification('error', '错误', error.message));
          }
        });
    }
    else {
      return axios.post('/room' + '?token=' + token, room)
        .then(response => {
          if (response.status === 200) {
            const room_id = response.data.id;
            dispatch(beginUploadImage());
            return axios.put('/room/' + room_id + '/logo' + '?token=' + token, image);
          }
          else {
            throw (response.data);
          }
        })
        .then(response => {
          if (response.status === 200) {
            dispatch(displayNotification('success', '操作成功', '添加房间成功'));
            dispatch(uploadImageSuccess());
            dispatch(loadAllRooms());
          }
          else {
            throw (response.data);
          }
        })
        .catch(error => {
          if (error.response.status === 403) {
            dispatch(displayNotification('error', '错误', '您已下线'));
            dispatch(logout());
            dispatch(push('/login'));
          }
          else {
            dispatch(displayNotification('error', '错误', error.message));
          }
        });
    }
  };
}

export function sendEmail(roomId) {
  return (dispatch, getState) => {
    const token = getState().user.token;
    return axios.get('/room/' + roomId + '/invitation?token=' + token)
      .then(response => {
        if (response.status === 200) {
          dispatch(displayNotification('success', '操作成功', '已发送邮件'));
        }
        else {
          dispatch(displayNotification('error', '操作失败', '邮件发送失败'));
        }
      })
      .catch(error => {
        if (error.response.status === 403) {
          dispatch(displayNotification('error', '错误', '您已下线'));
          dispatch(logout());
          dispatch(push('/login'));
        }
        else {
          dispatch(displayNotification('error', '错误', error.message));
        }
      });
  }
}
