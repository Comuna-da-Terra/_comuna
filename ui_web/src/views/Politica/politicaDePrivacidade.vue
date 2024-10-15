<template>
     <div class="all-container">
         <p v-html="contentHtml"></p>
     </div>
</template>

<script>

import apiPolicyService from '../../services/policy/apiPolicyService';

export default{
    data(){
        return {
            contentHtml: '',
        }
    },
    methods: {
        async load_data(){
            await apiPolicyService.getListPolicies("privacidade")
                .then(response => {
                    this.contentHtml = response.data.content
                })
        },

    },
    mounted(){ 
        this.load_data()
    }
}
</script>

<style>
    .all-container{
        height: 100%;
        margin: 1rem 1rem 1rem 1rem;
    }
</style>

