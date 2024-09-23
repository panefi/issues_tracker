<template>
  <div class="table-responsive"> <!-- Ensure table is in a responsive container -->
    <table class="table table-striped table-bordered" style="width: 100%;"> <!-- Ensure table is 100% width -->
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
          <td>{{ issue.id }}</td>
          <td>{{ issue.title }}</td>
          <td>{{ issue.description }}</td>
          <td>{{ issue.status }}</td> <!-- Match the number of columns in tbody -->
          <td>
            <button class="btn btn-warning btn-sm" @click="$emit('editIssue', issue)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="$emit('deleteIssue', issue)">Delete</button>
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
  overflow-x: auto; /* Enable horizontal scrolling if needed */
  width: 100%; /* Full width of its parent container */
}

.table {
  width: 100%; /* Ensure the table spans the full width */
}


.table-bordered {
  border: 1px solid #dee2e6; /* Add a border around the table */
}

.btn-warning {
  background-color: #9da0a3 !important; /* Change to a custom yellow color */
  border-color: #9da0a3 !important;
  color: #000000 !important; /* Black text color */
  margin-right: 15px;
}

.btn-danger {
  background-color: #9da0a3 !important; /* Change to a custom red color */
  border-color: #9da0a3 !important;
  color: #000000 !important; /* White text color */
}


</style>
