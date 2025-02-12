<template>
    <div class="modal-content">
        <slot />
    </div>
</template>
<style lang="scss" scoped>
    .modal-content {
        border-bottom: var(--main-border);
        border-top: var(--main-border);
        padding: 0 1rem;
    }
</style>