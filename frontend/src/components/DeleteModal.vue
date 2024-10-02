<template>
    <div class="modal fade show" style="display: block;" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Delete Issue</h5>
            <button type="button" class="close" @click="$emit('close')">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>Are you sure you want to delete the issue with ID <strong>{{ issue.issue_id }}</strong>?</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="$emit('close')">Cancel</button>
            <button type="button" class="btn btn-danger" @click="$emit('delete', issue.issue_id)">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      issue: {
        type: Object,
        required: true
      }
    }
  };
  </script>
  