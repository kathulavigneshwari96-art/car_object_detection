import pandas as pd
import cv2
import matplotlib.pyplot as plt
import os

# -------------------------------
# LOAD CSV FILE
# -------------------------------
df = pd.read_csv("data/cars.csv")

# -------------------------------
# CREATE OUTPUT FOLDER
# -------------------------------
output_folder = "outputs"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# -------------------------------
# GROUP ALL DETECTIONS BY IMAGE
# -------------------------------
grouped = df.groupby("image")

# -------------------------------
# PROCESS EACH IMAGE
# -------------------------------
for image_name, group in grouped:

    # Image path
    image_path = "data/training_images/" + image_name

    # Read image
    image = cv2.imread(image_path)

    # Skip if image not found
    if image is None:
        print(f"image not found: {image_name}")
        continue

    # Car counter
    car_count = 0

    # Draw all bounding boxes
    for _, row in group.iterrows():

        xmin = int(row['xmin'])
        ymin = int(row['ymin'])
        xmax = int(row['xmax'])
        ymax = int(row['ymax'])

        # Draw rectangle
        cv2.rectangle(image,
                      (xmin, ymin),
                      (xmax, ymax),
                      (0, 255, 0),
                      2)

        # Add label
        cv2.putText(image,
                    "Car",
                    (xmin, ymin - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 0, 0),
                    2)

        # Count cars
        car_count += 1

    # Display total cars
    cv2.putText(image,
                f"Total Cars: {car_count}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3)

    # Save output image
    output_path = output_folder + "/" + image_name
    cv2.imwrite(output_path, image)

    # Convert for matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Show image
    plt.figure(figsize=(10,8))
    plt.imshow(image_rgb)
    plt.title(f"{image_name} - Cars Detected: {car_count}")
    plt.axis("off")
    plt.show()

    # Process only first 5 images
    # Remove this break later if needed
    

print("Detection completed successfully!")