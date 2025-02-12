<script lang="ts" setup>
    import { defineProps } from 'vue';

    defineProps({
        key: {
            type: String,
            required: false
        },
        id: {
            type: String,
            required: false
        }
    });
</script>
<template>
    <li :key="key" :id="id" class="sidenav-item">
        <slot />
    </li>
</template>
<style lang="scss" scoped>
    .sidenav-item {
        padding-right: 1rem;
        padding-left: 1rem;
        padding-top: 0.25rem;
        padding-bottom: 0.25rem;
        list-style: none;
        cursor: pointer;

        &-active {
            border-radius: var(--border-radius);
            font-weight: bold;
        }
    }
</style>