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
        background-color: blue;
        color: white;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        box-sizing: border-box;
    }
</style>