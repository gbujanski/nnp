<script setup lang="ts">
    defineProps({
        message: {
            type: String,
            required: true
        },
        status: {
            type: String,
            required: false
        },
        isVisible: {
            type: Boolean,
            required: false
        }
    });
</script>
<template>
    <div class="alert">
        <span>{{ message }}</span>
    </div>
</template>