const BASE_URL = import.meta.env.VITE_BASE_URL;

const apiEndpoints = {
    getIssues: `${BASE_URL}/issues`,
    createIssue: `${BASE_URL}/issue`,
    updateIssue: (issueId) => `${BASE_URL}/issue/${issueId}`,
    deleteIssue: (issueId) => `${BASE_URL}/issue/${issueId}`
  };
export default apiEndpoints;
