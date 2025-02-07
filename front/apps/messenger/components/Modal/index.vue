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
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        flex-direction: column;
    }

    .modal-overlay {
        background-color: rgb(31, 9, 226);
        border-radius: 6px;
    }
</style>