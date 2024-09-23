<template>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Description</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="issue in issues" :key="issue.id">
          <td>{{ issue.id }}</td>
          <td>{{ issue.title }}</td>
          <td>{{ issue.description }}</td>
          <td>{{ issue.status }}</td>
          <td>
            <button class="btn btn-warning btn-sm" @click="$emit('editIssue', issue)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="$emit('deleteIssue', issue)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
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
  