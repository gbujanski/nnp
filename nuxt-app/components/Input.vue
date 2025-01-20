<script setup>
    defineProps({
        label: {
            type: String,
            required: true
        },
        id: {
            type: String,
            required: true
        },
        modelValue: {
            type: String,
            default: '',
        },
    });
    const notchMiddleRef = ref();
    const labelRef = ref();

    onMounted(() => {
        notchMiddleRef.value.style.width = `${labelRef.value.offsetWidth + 10}px`;
    })

</script>
<template>
    <div class="input-wrapper">
        <label ref="labelRef" :for="id" class="label">{{ label }}</label>
        <input :id="id" :name="id" class="input" type="text" :value="modelValue" :aria-labelledby="id" @input="$emit('update:modelValue', $event.target.value)"/>
        <div class="notch">
            <div class="notch-start"></div>
            <div ref="notchMiddleRef" class="notch-middle"></div>
            <div class="notch-end"></div>
        </div>
    </div>


</template>