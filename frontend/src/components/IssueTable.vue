<template>
  <div class="table-responsive">
    <table class="table table-striped table-bordered" style="width: 100%;">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Description</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="issue in issues" :key="issue.id">
          <td>{{ issue.issue_id }}</td>
          <td>{{ issue.title }}</td>
          <td>{{ issue.description }}</td>
          <td>{{ issue.status }}</td>
          <td class="button-container">
            <div class="button-wrapper">
              <button class="btn btn-warning btn-sm" @click="$emit('editIssue', issue)">Edit</button>
            </div>
            <div class="button-wrapper">
              <button class="btn btn-danger btn-sm" @click="$emit('deleteIssue', issue)">Delete</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    issues: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
.table-responsive {
  overflow-x: auto;
  width: 100%;
}

.table {
  width: 100%;
}

.table-bordered {
  border: 1px solid #dee2e6;
}

/* Button Container Styling */
.button-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

/* Wrapper around each button */
.button-wrapper {
  margin-bottom: 0;
}

/* Button Styling */
.btn-warning {
  background-color: #9da0a3 !important;
  border-color: #9da0a3 !important;
  color: #000000 !important;
  padding: 5px 10px;
  margin: 0;
}

.btn-danger {
  background-color: #9da0a3 !important;
  border-color: #9da0a3 !important;
  color: #000000 !important;
  padding: 5px 10px;
  margin: 0;
}

/* Responsive Adjustments for Smaller Screens */
@media (max-width: 576px) {
  .button-container {
    flex-direction: column;
    align-items: flex-start;
  }

  .button-wrapper {
    width: 100%;
    margin-bottom: 10px;
  }

  .btn-warning, .btn-danger {
    width: 100%;
  }

  .button-wrapper:last-child {
    margin-bottom: 0;
  }
}
</style>
