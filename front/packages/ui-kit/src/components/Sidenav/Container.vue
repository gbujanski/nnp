<template>
    <div class="sidenav-container">
        <slot />
    </div>
</template>
<style lang="scss" scoped>
    .sidenav-container {
        display: flex;
        height: calc(100% - 57px); // 40px height + 1px border + 8px padding top + 8px padding bottom
    }
</style>