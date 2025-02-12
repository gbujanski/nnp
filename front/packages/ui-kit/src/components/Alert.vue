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
<style lang="scss" scoped>
    .alert {
        position: absolute;
        display: flex;
        align-items: center;
        top: 1rem;
        right: 1rem;
        min-width: 250px;
        min-height: 60px;
        padding: 15px;
        border-radius: var(--border-radius);
        border: var(--border);
        box-sizing: border-box;
    }
</style>