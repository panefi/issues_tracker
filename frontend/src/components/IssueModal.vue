<template>
    <div class="modal fade show" style="display: block;" tabindex="-1" aria-labelledby="issueModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? 'Edit Issue' : 'Create Issue' }}</h5>
            <button type="button" class="close" @click="$emit('close')">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm">
              <div class="form-group">
                <label for="title">Title</label>
                <input type="text" class="form-control" id="title" v-model="formData.title" required>
              </div>
              <div class="form-group">
                <label for="description">Description</label>
                <textarea class="form-control" id="description" v-model="formData.description" required></textarea>
              </div>
              <!-- Show status only when editing -->
              <div class="form-group" v-if="isEditing">
                <label for="status">Status</label>
                <select class="form-control" id="status" v-model="formData.status">
                  <option value="open">Open</option>
                  <option value="in progress">In Progress</option>
                  <option value="closed">Closed</option>
                </select>
              </div>
              <button type="submit" class="btn btn-primary">{{ isEditing ? 'Update' : 'Create' }}</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      isEditing: {
        type: Boolean,
        required: true
      },
      issue: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        formData: { ...this.issue }
      };
    },
    methods: {
      submitForm() {
        this.$emit('save', this.formData);
      }
    },
    watch: {
      issue: {
        handler(newValue) {
          this.formData = { ...newValue };
        },
        deep: true
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  