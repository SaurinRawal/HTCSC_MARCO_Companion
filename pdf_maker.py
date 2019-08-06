from fpdf import FPDF
import os
import csv

def get_images(image_dir):
    '''
    Given a directory, returns all filepaths for images of allowed type.
    Current allowed types are jpeg, jpg png and gif.
    '''
    allowed_file_types = {'jpg', 'jpeg', 'png', 'gif'}
    try:
        images = os.listdir(image_dir)
        images = [image for image in images if image.split('.')[-1] in allowed_file_types]
        images = [os.path.join(image_dir, image) for image in images]
        return images
    except FileNotFoundError as e:
        return e

def make_cocktail_dict(results_csv):
    '''
    makes a dictionary of the image to cocktail information
    '''
    well_dict = {}
    with open(results_csv, 'r') as results_csv:
        results_reader = csv.reader(results_csv)

        for line in results_reader:

            well_dict[line[6]] = line[7]  # well number = key cocktail info = va;ue

    return well_dict

def format_cocktail(cocktail):
    print(cocktail)
    removal_items = ['[', ']', '"', "'", ',']
    for item in removal_items:
        cocktail = cocktail.replace(item, '')

    cocktail = str(cocktail).replace('    ', '\n')

    return cocktail

# [cock for cock in c.split(' ') if cock != '']

def write_entry(pdf, cocktail_info):
    '''
    writes the well and cocktail information corresponding to an image
    into a pdf
    '''
    # need to unpack the tuple
    pdf.multi_cell(w=200, h=100, align='R', txt=format_cocktail(cocktail_info))

    '''
    tuple = format_cocktail(cocktail_info)
    for item in tuple:
        pdf.ln(1)
        pdf.multi_cell(200, 10, txt=str(item), align='R')
        pdf.ln(1)
    '''


def make_results_pdf(image_dir, results_csv, output='results.pdf', pdf_title='Image Results'):
    # known bug with writing the seconf page has to do with mod operation
    height = 85
    width = 85
    x = 15
    y = 10
    space_between_text = 40

    cocktail_dict = make_cocktail_dict(results_csv)
    # PDF set up
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    images = get_images(image_dir)
    pdf.add_page()
    pdf.cell(200, 10, txt=pdf_title, align='C')

    j = 1
    for image in images:
        basename = os.path.basename(image).split('.')[0]
        pdf.image(image, h=height, w=width, x=x, y=y)
        y += 100
        #write_entry(pdf, cocktail_dict[basename])
        pdf.cell(200, 10, txt=os.path.basename(image), align='R')
        j += 1
        if j % 3 == 0:  # three images per page
            pdf.add_page()
            y = 10
        else:
            pdf.ln(space_between_text)

    pdf.output(output)
