<template>
    <div class="modal">
        <div class="modal-overlay">
            <slot />
        </div>
    </div>
</template>
<style lang="scss" scoped>
    .modal {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: var(--main-backdrop-bg);
        display: flex;
        flex-direction: column;
    }

    .modal-overlay {
        border-radius: var(--main-border-radius);
        border: var(--main-border);
        background-color: var(--main-bg);
    }
</style>