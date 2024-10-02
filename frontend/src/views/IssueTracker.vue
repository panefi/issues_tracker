<template>
    <div class="container mt-5">
      <h1 class="issue-tracker-title">Issues Tracker</h1> 
      <button class="btn btn-primary mb-3" @click="openCreateModal">Create Issue</button>
      <IssueTable 
        :issues="issues" 
        @editIssue="openEditModal" 
        @deleteIssue="openDeleteModal" 
      />
      <IssueModal 
        v-if="showIssueModal" 
        :is-editing="isEditing" 
        :issue="selectedIssue" 
        @close="closeModal" 
        @save="saveIssue" 
      />
      <DeleteModal 
        v-if="showDeleteModal" 
        :issue="selectedIssue" 
        @close="closeModal" 
        @delete="confirmDeleteIssue" 
      />
    </div>
</template>
  
<script>
import axios from 'axios';
import IssueTable from '../components/IssueTable.vue';
import IssueModal from '../components/IssueModal.vue';
import DeleteModal from '../components/DeleteModal.vue';
import apiEndpoints from '../api/apiEndpoints';

export default {
components: {
    IssueTable,
    IssueModal,
    DeleteModal,
},
data() {
    return {
    issues: [],
    showIssueModal: false,
    showDeleteModal: false,
    isEditing: false,
    selectedIssue: null,
    };
},
methods: {
    fetchIssues() {
        axios.get(apiEndpoints.getIssues).then(response => {
            this.issues = response.data;
        });
    },
    openCreateModal() {
        this.isEditing = false;
        this.selectedIssue = { title: '', description: '', status: 'open' };
        this.showIssueModal = true;
    },
    openEditModal(issue) {
        this.isEditing = true;
        this.selectedIssue = { ...issue };
        this.showIssueModal = true;
    },
    openDeleteModal(issue) {
        this.selectedIssue = { ...issue };
        this.showDeleteModal = true;
    },
    closeModal() {
        this.showIssueModal = false;
        this.showDeleteModal = false;
    },
    saveIssue(issue) {
        if (this.isEditing) {
            axios.put(apiEndpoints.updateIssue(issue.issue_id), issue)
                .then(() => {
                this.fetchIssues();
                this.closeModal();
                });
        } else {
            axios.post(apiEndpoints.createIssue, issue)
            .then(() => {
                this.fetchIssues();
                this.closeModal();
            });
        }
    },
    confirmDeleteIssue(issueId) {
        axios.delete(apiEndpoints.deleteIssue(issueId)).then(() => {
            this.fetchIssues();
            this.closeModal();
        });
    }
},
created() {
    this.fetchIssues();
}
};
</script>



<style scoped>
.issue-tracker-title {
  font-family: 'Poppins', sans-serif; /* Use a modern sans-serif font */
  font-size: 2.5rem; /* Large font size */
  font-weight: 700; /* Bold font weight */
  text-align: center; /* Center the title */
  background: linear-gradient(135deg, #343A40, #343A40); /* Gradient background */
  background-clip: text; /* Make the gradient apply to text only */
  -webkit-text-fill-color: transparent; /* Make the text itself transparent */
  margin-bottom: 1.5rem; /* Space below the title */
  padding: 10px 20px; /* Padding around the text */
  border-radius: 8px; /* Slightly rounded corners */
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Light shadow for depth */
}

.btn-primary {
  font-weight: 600; /* Bold text */
  padding: 10px 20px; /* Padding around the button */
  border-radius: 5px; /* Rounded corners */
  background-color: #343A40;
  margin-left: auto; /* Push the button to the right side */
}

</style>
