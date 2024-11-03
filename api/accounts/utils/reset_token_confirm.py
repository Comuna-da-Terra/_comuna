from django.shortcuts import render

def reset_token_confirm(request):
    return render(request, "token/reset-token-confirm.html", {"message": "O token de confirmação expirou. Por favor, solicite um novo."})
