import cv2
from skimage.metrics import structural_similarity as ssim

def detect_and_compare(original_image_path, uploaded_image_path):
    # Load images
    original = cv2.imread(str(original_image_path), 0)  # Read as grayscale
    uploaded = cv2.imread(str(uploaded_image_path), 0)

    # Resize uploaded image to match original dimensions
    height, width = original.shape
    uploaded_resized = cv2.resize(uploaded, (width, height), interpolation=cv2.INTER_AREA)

    # Preprocess (denoising and thresholding)
    original_denoised = cv2.fastNlMeansDenoising(original, None, 30, 7, 21)
    uploaded_denoised = cv2.fastNlMeansDenoising(uploaded_resized, None, 30, 7, 21)

    _, original_thresh = cv2.threshold(original_denoised, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    _, uploaded_thresh = cv2.threshold(uploaded_denoised, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # Calculate structural similarity
    score, _ = ssim(original_thresh, uploaded_thresh, full=True)

    return round(score * 100, 2)  # Return similarity percentage
