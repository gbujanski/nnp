<script setup lang="ts">
</script>

<template>
    <div class="header">
        <p>NNP</p>
    </div>
    <slot />
</template>
<style>
    .header {
        padding: 0.5rem 1rem;
        height: 40px;
        border-bottom: var(--main-border);
        align-items: center;
        display: flex;
    }
</style>