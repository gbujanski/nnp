<script setup lang="ts">
    import { defineProps, ref, onMounted } from 'vue';

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
        type: {
            type: String,
            default: 'text',
        }
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
        <input :id="id" :name="id" class="input" :type="type" :value="modelValue" :aria-labelledby="id" @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"/>
        <div class="notch">
            <div class="notch-start"></div>
            <div ref="notchMiddleRef" class="notch-middle"></div>
            <div class="notch-end"></div>
        </div>
    </div>


</template>

<style lang="scss" scoped>
    .input-wrapper {
        position: relative;
        display: flex;
        flex-direction: column;
        margin: 0.5rem;

        .input {
            font-size: 1rem;
            border: none;
            background-color: transparent;
            padding: 0.5rem 0.7rem;
            caret-color: white;
            &:focus {
                outline: none;
            }
        }
        
        .label {
            position: absolute;
            font-size: 0.8rem;
            top: -7px;
            left: 12px;
            color: white;
        }
    }

    .notch {
        position: absolute;
        display: flex;
        flex-direction: row;
        width: 100%;
        height: 100%;
        pointer-events: none;
        &-start {
            border: 1px solid white;
            border-right: none;
            border-radius: 0.2rem 0 0 0.2rem;
            width: 0.4rem;
            height: 100%;
        }
        &-middle {
            border: 1px solid white;
            border-right: none;
            border-left: none;
            border-top: 1px solid transparent;
            height: 100%;
        }
        &-end {
            border: 1px solid white;
            border-left: none;
            flex-grow: 1;
            height: 100%;
            border-radius: 0 0.2rem 0.2rem 0;
        }
    }

    .input-wrapper input:focus + .notch {
        .notch-start {
            box-shadow: -1px 0 0 0 white, 0 -1px 0 0 white, 0 1px 0 0 white;
        }
        .notch-middle {
            box-shadow: 0 1px 0 0 white;
        }
        .notch-end {
            box-shadow: 1px 0 0 0 white, 0 -1px 0 0 white, 0 1px 0 0 white;
        }
    }
</style>