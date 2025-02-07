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
        background-color: #0D47A1;
        height: 40px;
        border-bottom: 1px solid #BDBDBD;
        align-items: center;
        display: flex;
    }
</style>