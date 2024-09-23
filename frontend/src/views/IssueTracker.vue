<template>
    <div class="container mt-5">
      <h1 class="mb-4">Issue Tracker</h1>
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
            axios.put(apiEndpoints.updateIssue(issue.id), issue)
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
/* Add your styles here */
</style>
