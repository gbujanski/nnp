<template>
    <div class="header">
        <p>NNP</p>
    </div>
    <div class="channel-container">
        <div class="channel-list">
            <span class="channel-name channel-name-active">sidebar</span>
            <span class="channel-name">sidebar</span>
            <span class="channel-name">sidebar</span>
            <span class="channel-name">sidebar</span>
            <span class="channel-name">sidebar</span>
            <span class="channel-name">sidebar</span>
            <span class="channel-name">sidebar</span>
            <span class="channel-name">sidebar</span>
            <span class="channel-name">sidebar</span>
            <span class="channel-name">sidebar</span>
            <span class="channel-name channel-name-add">new channel</span>
        </div>
        <div class="channel-content">
            <slot />
        </div>
    </div>
</template>