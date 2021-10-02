import axios from 'axios';
import store from '@/store';

const API_URL = 'http://localhost:8000';

export default {
  getAll(params) {
    const url = `${API_URL}/api/v1/certificates/`;
    const headers = { Authorization: `Token ${store.getters['auth/accessToken']}` };
    return axios.get(url, { params, headers: headers }).then(response => response.data);
  },
  get(id) {
    const url = `${API_URL}/api/v1/certificates/${id}`;
    const headers = { Authorization: `Token ${store.getters['auth/accessToken']}` };
    return axios.get(url, { headers: headers }).then(response => response.data);
  },
  getInfo(id) {
    const url = `${API_URL}/api/v1/certificates/${id}/info`;
    const headers = { Authorization: `Token ${store.getters['auth/accessToken']}` };
    return axios.get(url, { headers: headers }).then(response => response.data);
  },
  download(id, callback, callbackError) {
    const url = `${API_URL}/api/v1/certificates/${id}/download`;
    const headers = { Authorization: `Token ${store.getters['auth/accessToken']}` };
    axios.get(url, { headers: headers, responseType: 'blob' }).then((response) => {
      const fileURL = window.URL.createObjectURL(new Blob([response.data]));
      const suggestedFileName = response.headers['content-disposition'];
      const effectiveFileName =
          (suggestedFileName === undefined ? 'download' : suggestedFileName.split(';')
            .find(n => n.includes('filename='))
            .replace('filename=', '')
            .trim());
      const fileLink = document.createElement('a');
      fileLink.href = fileURL;
      fileLink.setAttribute('download', effectiveFileName);
      document.body.appendChild(fileLink);
      fileLink.click();
      callback();
    }).catch((e) => {
      callbackError(e);
    });
  },
  revoke(id, data) {
    const url = `${API_URL}/api/v1/certificates/${id}`;
    const headers = { Authorization: `Token ${store.getters['auth/accessToken']}` };
    return axios.delete(url, { data: data, headers: headers }).then(response => response.data);
  },
  create(data) {
    const url = `${API_URL}/api/v1/certificates/`;
    const headers = { Authorization: `Token ${store.getters['auth/accessToken']}` };
    return axios.post(url, data, { headers: headers });
  },
};