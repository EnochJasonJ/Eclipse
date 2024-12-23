<script setup>

</script>

<template>
    <div class="flex flex-col mr-auto">
        <div class="flex  flex-row gap-5 mr-20 ml-auto items-center justify-center">
            <div class="bg-white w-20 rounded-2xl p-3 flex items-center justify-center">
                <h1>Design</h1>
            </div>
            <div class="bg-white w-20 rounded-2xl p-3 flex items-center justify-center">
                <h1>Color</h1>
            </div>
            <div class="bg-white w-20 rounded-2xl p-3 flex items-center justify-center">
                <h1>Text</h1>
            </div>
            <div class="bg-white w-20 rounded-2xl p-3 flex items-center justify-center">
                <h1>Upload</h1>
            </div>
        </div>
        <div class="bg-white h-72 mt-10 rounded-xl">
            <button class="mt-5 bg-blue-300 px-3 py-1 rounded-2xl border border-gray-300">Upload your image</button>
        </div>
        <div class="flex flex-row items-center justify-center  gap-28 mt-5">
            <i class="pi pi-save bg-white text-lg p-2 rounded-md w-20"><p class="text-sm">drag</p></i>
            <i class="pi pi-check bg-white text-lg p-2 rounded-md w-auto"><p class="text-sm">Design Check</p></i>
            <i class="pi pi-share-alt bg-white text-lg p-2 rounded-md w-20"><p class="text-sm">Share</p></i>
        </div>
        <div class="mt-5 flex flex-row items-center justify-center gap-1">
            <h2 class="text-2xl">Amount: 899rs</h2><p class="text-sm">(inc tax)</p>
        </div>
    </div>
</template>