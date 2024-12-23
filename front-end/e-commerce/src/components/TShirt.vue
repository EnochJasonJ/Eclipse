<script setup>
    import tshirt from '../assets/CustomT/tshirt.png'
    import { defineProps } from 'vue';
    defineProps({
        imgURL: {
            type: String,
            Required: true
        }
    })
</script>

<template>
    <img :src="imgURL" alt="Product Image">
</template>