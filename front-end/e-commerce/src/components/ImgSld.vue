<script setup>
    import back from '../assets/back.png'
    import b1 from '../assets/b1.png'
    import g1 from '../assets/g1.png'
    import g2 from '../assets/g2.png'
</script>

<template>
    <div class="flex flex-col">
        <div id="singleimg" class="mt-20 flex justify-center items-center relative ">
            <img :src="back" alt="" class="object-cover rounded-3xl z-0 ">
            <h1 class="z-10 top-32 absolute text-4xl text-center ml-14">Your one-step Fashion<br>Destination</h1>
            <h2 class="text-center mt-5 text-lg">Find Your Fashion with us. click here to explore our customizable wears</h2>
            <h1 class="text-center text-5xl font-light mt-3">#TRENDY</h1>
        </div>
        <div  class="image flex flex-row gap-10 items-center justify-center mt-5">
            <div>
                <img :src="b1" alt="boy">
                <h1 class="text-center mt-3 text-lg">Vintage Coat suits</h1>
            </div>
            <div>
                <img :src="g1" alt="girl1">
                <h1 class="text-center mt-3 text-lg">Boho-chic</h1>
            </div>
            <div>
                <img :src="g2" alt="girl2">
                <h1 class="text-center mt-3 text-lg">Casual Elegance</h1>
            </div>
        </div>
    </div>
</template>


<style scoped>
    #singleimg{
        display: inline-block;
    }
    img {
        max-width: 100%; /* Responsive sizing */
        height: auto;
        box-shadow: 0 0 15px rgb(183, 182, 182);
    }

    .image img{
        box-shadow: 0 0 15px rgb(183, 182, 182);
        border-radius: 15px;
    }
</style>