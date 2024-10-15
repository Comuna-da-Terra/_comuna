<template>

<form style="height: 100%;" id="container" @submit.prevent="sendPolicy">
    <div>
        <div ref="editorContainer" class="quill-editor" ></div>
    </div>
    <div>
        <label for="policyType">Selecione o tipo de política:</label>
        <select v-model="selectedOption" id="policyType" required>
            <option disabled value="">Escolha uma opção</option>
            <option value="privacidade">Política de Privacidade</option>
            <option value="termos">Termos de Uso</option>
        </select>

        <span v-if="errors.selectedOption" style="color: red;">Selecione uma opção válida!</span>

        <button type="submit"  >Enviar Política</button>
        <p v-html="contentHtml"></p>
    </div>
    
</form>

</template>

<script>

import Quill from 'quill';
import "quill/dist/quill.snow.css";
import apiPolicyService from '../../services/policy/apiPolicyService';

export default {
    data(){
        return{
            quill: '',
            contentHtml: '',
            typePolicy: ["termos","privacidade"],

            selectedOption: '',
            errors: {
                selectedOption: false,
            },
        }
    },
    methods:{
        async load_data(){
        },

        async sendPolicy() {
            if (!this.selectedOption) {
                this.errors.selectedOption = true;
            } else {
                this.errors.selectedOption = false;
                const conteudo = {
                    type: this.selectedOption,
                    content: "2",
                }
                if (conteudo) {
                    await apiPolicyService.createPolicy(conteudo)
                    .then(response => {
                        console.log('Política enviada com sucesso:', response);
                    })
                    .catch(error => {
                        console.error('Erro ao enviar a política:', error);
                    });
                } else {
                    console.log('Nenhum conteúdo para enviar');
                }
                    console.log('Formulário enviado com sucesso! Seleção:', this.selectedOption);
                }
            }
        },
    
    mounted(){
        this.load_data()
        const editorContainer = this.$refs.editorContainer;
        const options = {
            debug: 'info',
            modules: {
                toolbar: [
                [{ header: [1, 2, 3, 4, 5, 6, false] }],
                [{ font: [] }],
                [{ size: ['small', false, 'large', 'huge'] }],
                ['bold', 'italic', 'underline', 'strike'],
                [{ color: [] }, { background: [] }],
                [{ script: 'sub' }, { script: 'super' }],
                [{ list: 'ordered' }, { list: 'bullet' }],
                [{ indent: '-1' }, { indent: '+1' }],
                [{ direction: 'rtl' }],
                [{ align: [] }],
                ['link', 'image', 'video', 'formula'],
                ['clean']
                ]
            },
            placeholder: 'Compose an epic...',
            theme: 'snow',
            height: '200px' 
        };

        this.$nextTick(async () => {
            // await apiPolicyService.getListPolicies()
            // .then(response => {
            //         this.contentHtml = response.data.content
            // })

            this.quill = new Quill(editorContainer, options);
            // this.quill.root.innerHTML = this.contentHtml;

            this.quill.on('text-change', () => {
                this.contentHtml = this.quill.root.innerHTML;
                this.$emit('content-changed', this.contentHtml);
            });
        });
    },
    
}
</script>

<style>
    .quill-editor{
        height: 90%;
    }
   #container{
    max-height: 90%;
    margin: 5px;
    display: flex;
    gap: 5vw;
   }
   .ql-editor strong { 
        font-weight: bold !important; 
    }
</style>