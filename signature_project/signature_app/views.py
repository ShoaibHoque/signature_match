from django.shortcuts import render, redirect
from .forms import SignatureForm
from .utils import detect_and_compare

def upload_signature(request):
    if request.method == 'POST':
        form = SignatureForm(request.POST, request.FILES)
        if form.is_valid():
            signature = form.save()
            similarity = detect_and_compare(
                signature.original_image.path,
                signature.uploaded_image.path
            )
            return render(request, 'signature_app/result.html', {
                'similarity': similarity,
                'signature': signature
            })
    else:
        form = SignatureForm()

    return render(request, 'signature_app/upload.html', {'form': form})
