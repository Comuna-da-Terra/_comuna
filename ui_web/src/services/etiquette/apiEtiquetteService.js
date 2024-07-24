import api from '@/services/api';

export default {
    async emitEtiquette(data) {
        await api.post("/emitEtiquette/", data)
            .then(response => {

                const iframe            = document.createElement('iframe');
                iframe.srcdoc           = response.data; 
                const novaJanela        = window.open();
                iframe.style.border     = 'none'
                iframe.style.width      = '100%';
                iframe.style.height     = '100%';
                
                novaJanela.document.body.appendChild(iframe);
            })
            .catch(error => {
                console.error(error);
            });
    }
};