<template>
    <div class="modal-header">
        <slot />
        <button class="btn-close" @click="$emit('close-modal')">X</button>
    </div>
</template>
<style lang="scss" scoped>
    .modal-header {
        padding: 1rem;
        display: flex;
        justify-content: space-between;
        font-weight: bold;
    }
</style>