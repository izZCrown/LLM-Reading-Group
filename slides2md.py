from pptx import Presentation
import os

def mkdir(path):
    if not os.path.exists(path):
            os.makedirs(path)

slides_dir = './Slides'
slides_list = os.listdir(slides_dir)
markdown_dir = './Markdown'
markdown_list = os.listdir(markdown_dir)
image_dir = './Markdown/Images'
mkdir(image_dir)

for slides_name in slides_list:
    base_name = slides_name.split('.')[0]
    if base_name not in markdown_list:
        slides_path = os.path.join(slides_dir, slides_name)
        markdown_name = base_name + '.md'
        markdown_path = os.path.join(markdown_dir, markdown_name)

        images_path = os.path.join(image_dir, base_name)
        mkdir(images_path)

        presentation = Presentation(slides_path)

        content = []

        for slide_number, slide in enumerate(presentation.slides):
            index = 1
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    content.append(shape.text)
                    content.append(('\n'))
                elif shape.shape_type == 13:
                    image = shape.image
                    image_bytes = image.blob
                    local_image_path = os.path.join(images_path, f'img_{slide_number}_{index}.png')
                    # image_path = 'https://github.com/izZCrown/LLM-Reading-Group/tree/main/Markdown/Images/' + 'base_name/' + f'img_{slide_number}_{index}.png'
                    index += 1
                    with open(local_image_path, 'wb') as f:
                        f.write(image_bytes)

                    width_px = int(shape.width * 96 / 914400)
                    height_px = int(shape.height * 96 / 914400)
                    # img_tag = f'<img src="{image_path}" width="{width_px}" height="{height_px}"/>'
                    img_tag = f'![img]({local_image_path})'
                    content.append(img_tag)
                    content.append('\n')

        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))

        print(base_name)
