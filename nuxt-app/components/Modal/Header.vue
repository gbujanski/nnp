<template>
    <div class="modal-header">
        <slot />
        <button class="btn-close" @click="$emit('close-modal')">X</button>
    </div>
</template>