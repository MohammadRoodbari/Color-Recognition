from sklearn.cluster import KMeans
import numpy as np
from collections import Counter

# __version__ = "0.1.0"

# BASE_DIR = Path(__file__).resolve(strict=True).parent

# with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as f:
#     model = pickle.load(f)




import warnings
warnings.filterwarnings("ignore")


def crop_image(image):
    width, height = image.size
    crop_width = int(width * 0.10)
    crop_height = int(height * 0.10)

    # Calculate the coordinates for cropping
    left = crop_width
    top = crop_height
    right = width - crop_width
    bottom = height - crop_height

    # Crop the image
    cropped_image = image.crop((left, top, right, bottom))
    return cropped_image

def RGBtoHEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def check_color(given_rgb):

    # Main colors in RGB
    main_colors = {
        'Red': np.array([255, 0, 0]),
        'Green': np.array([0, 255, 0]),
        'Blue': np.array([0, 0, 255]),
        'Yellow': np.array([255, 255, 0]),
        # 'Cyan': np.array([0, 255, 255]),
        # 'Magenta': np.array([255, 0, 255]),
        'White': np.array([255, 255, 255]),
        'Black': np.array([0, 0, 0]),
        # 'Gray': np.array([128, 128, 128]),
    }

    # Calculate the Euclidean distance between the given RGB and each main color
    distances = {color: np.linalg.norm(given_rgb - rgb) for color, rgb in main_colors.items()}

    # Find the closest main color
    closest_color = min(distances, key=distances.get)

    return closest_color

def final_gray_check(final_color, given_rgb):
    if final_color == "Black":
        main_colors = {
            'Black': np.array([40, 40, 40]),
            'Gray': np.array([128, 128, 128]),
        }

        # Calculate the Euclidean distance between the given RGB and each main color
        distances = {color: np.linalg.norm(given_rgb - rgb) for color, rgb in main_colors.items()}

        # Find the closest main color
        closest_color = min(distances, key=distances.get)

        return closest_color


    else:
        return final_color


def get_colors(image):
    # image = Image.fromarray(image)
    image = crop_image(image)
    image = np.array(list(image.getdata()))

    clf = KMeans(n_clusters = 1, random_state=42)
    labels = clf.fit_predict(image)

    counts = Counter(labels)
    counts = dict(sorted(counts.items()))

    center_colors = clf.cluster_centers_
    ordered_colors = [center_colors[i] for i in counts.keys()]
    final_color = check_color(ordered_colors[0])
    final_color = final_gray_check(final_color, ordered_colors[0])


    return final_color